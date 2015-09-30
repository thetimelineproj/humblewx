# Copyright (C) 2009-2015 Contributors as noted in the AUTHORS file
#
# This file is part of humblewx.
#
# humblewx is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# humblewx is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with humblewx.  If not, see <http://www.gnu.org/licenses/>.


import platform
import xml.etree.ElementTree

import wx


COMPONENT_MODULES = [wx]


if platform.system() == "Windows":
    BORDER = 10
    SMALL_BORDER = 6
else:
    BORDER = 12
    SMALL_BORDER = 6


class GuiCreator(object):

    def _create(self, controller_class, variables):
        self._variables = variables
        self.controller = controller_class(self)
        return self._create_from_node(self, xml.etree.ElementTree.fromstring(self.__doc__))

    def _create_from_node(self, parent, node):
        try:
            if node.get("use"):
                if self._variables[node.get("use")[2:-1]] is False:
                    return None
            creator = getattr(self, "_create_%s" % node.tag)
        except AttributeError:
            creator = self._create_generic_component
        component = creator(parent, node)
        self._bind_events(node, component)
        if node.get("name", None):
            setattr(self, node.get("name"), component)
        return component

    def _create_BoxSizerVertical(self, parent, node):
        return self._populate_sizer(parent, node, wx.BoxSizer(wx.VERTICAL))

    def _create_BoxSizerHorizontal(self, parent, node):
        return self._populate_sizer(parent, node, wx.BoxSizer(wx.HORIZONTAL))

    def _create_FlexGridSizer(self, parent, node):
        rows = int(node.get("rows", "0"))
        columns = int(node.get("columns", "0"))
        sizer = wx.FlexGridSizer(rows, columns, SMALL_BORDER, SMALL_BORDER)
        for column_string in self._get_comma_int_list(node.get("growableColumns")):
            sizer.AddGrowableCol(int(column_string))
        for row_string in self._get_comma_int_list(node.get("growableRows")):
            sizer.AddGrowableRow(int(row_string))
        return self._populate_sizer(parent, node, sizer)

    def _create_StaticBoxSizerVertical(self, parent, node):
        box = wx.StaticBox(parent, **self._get_attributes(node))
        return self._populate_sizer(parent, node, wx.StaticBoxSizer(box, wx.VERTICAL))

    def _create_Notebook(self, parent, node):
        notebook = self._get_component_constructor(node)(parent, **self._get_attributes(node))
        for child_node in node.getchildren():
            child_component = self._create_from_node(notebook, child_node)
            label = self._get_variable_or_value(child_node.get("notebookLabel", ""))
            notebook.AddPage(child_component, label)
        return notebook

    def _create_Panel(self, parent, node):
        component = self._get_component_constructor(node)(parent, **self._get_attributes(node))
        for child_node in node.getchildren():
            child_component = self._create_from_node(component, child_node)
            if isinstance(child_component, wx.Sizer):
                component.SetSizer(child_component)
        return component

    def _populate_sizer(self, parent, node, sizer):
        for child_node in node.getchildren():
            if child_node.tag == "Spacer":
                sizer.AddSpacer(int(child_node.get("size", SMALL_BORDER)))
            elif child_node.tag == "StretchSpacer":
                sizer.AddStretchSpacer()
            else:
                component = self._create_from_node(parent, child_node)
                if component:
                    border = self._get_or_value(child_node.get("border", ""))
                    if child_node.get("align"):
                        align = self._get_or_value(child_node.get("align", ""))
                    else:
                        align = wx.EXPAND
                    if child_node.get("borderType") == "SMALL":
                        borderType = SMALL_BORDER
                    else:
                        borderType = BORDER
                    sizer.Add(component,
                              flag=border|align,
                              border=borderType,
                              proportion=int(child_node.get("proportion", "0")))
        return sizer

    def _create_generic_component(self, parent, node):
        component = self._get_component_constructor(node)(parent, **self._get_attributes(node))
        for child_node in node.getchildren():
            self._create_from_node(component, child_node)
        return component

    def _get_component_constructor(self, node):
        for module in COMPONENT_MODULES:
            try:
                return getattr(module, node.tag)
            except AttributeError:
                pass # Try the next
        raise ValueError("Component %s not found." % node.tag)

    def _get_attributes(self, node):
        SPECIAL_ATTRIBUTES = [
            "use",
            "notebookLabel",
            # Standard wx
            "width", "height",
            "style",
            # Spacer attributes
            "border",
            "borderType",
            "proportion",
            "align",
        ]
        attributes = {}
        if node.get("width") or node.get("height"):
            attributes["size"] = (int(node.get("width", "-1")),
                                  int(node.get("height", "-1")))
        if node.get("style"):
            attributes["style"] = self._get_or_value(node.get("style", None))
        for attribute in node.keys():
            if (attribute not in SPECIAL_ATTRIBUTES) and not attribute.startswith("event_"):
                attributes[attribute] = self._get_variable_or_value(node.get(attribute))
        return attributes

    def _get_variable_or_value(self, text):
        if text.startswith("$(") and text.endswith(")"):
            return self._variables[text[2:-1]]
        else:
            return self._get_value(text)

    def _get_value(self, text):
        if text == "True":
            return True
        elif text == "False":
            return False
        else:
            return text

    def _get_comma_int_list(self, text):
        if text:
            return [int(x) for x in text.split(",")]
        else:
            return []

    def _get_or_value(self, wx_constant_names):
        value = 0
        if wx_constant_names:
            for wx_constant_name in wx_constant_names.split("|"):
                value |= getattr(wx, wx_constant_name)
        return value

    def _bind_events(self, node, component):
        for key in node.keys():
            if key.startswith("event_"):
                self._bind_event(key[6:], node.get(key), component)

    def _bind_event(self, event_name, target_name, component):
        wxid = None
        if "__" in event_name:
            (event_name, wxid) = event_name.split("__")
        target = getattr(self.controller, target_name)
        if wxid:
            self.Bind(getattr(wx, event_name), target, id=getattr(wx, wxid))
        else:
            try:
                component.Bind(getattr(component, event_name), target)
            except AttributeError:
                self.Bind(getattr(wx, event_name), target, component)


class Dialog(wx.Dialog, GuiCreator):

    def __init__(self, controller_class, parent, variables={}, **kwargs):
        wx.Dialog.__init__(self, parent, **kwargs)
        component = self._create(controller_class, variables)
        if isinstance(component, wx.Sizer):
            self.SetSizerAndFit(component)


class Controller(object):

    def __init__(self, view):
        self.view = view
