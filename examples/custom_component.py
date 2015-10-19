import humblewx
import wx
import sys


humblewx.COMPONENT_MODULES.append(sys.modules[__name__])


class CustomComponent(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        label = wx.StaticText(self, label="this is a custom component")
        button = wx.Button(self, label="click me")
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        sizer.Add(label)
        sizer.Add(button)
        self.SetSizer(sizer)


class CustomComponentExampleDialog(humblewx.Dialog):

    """
    <BoxSizerVertical>
        <StaticText label="before custom component" />
        <CustomComponent />
        <StaticText label="after custom component" />
    </BoxSizerVertical>
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, humblewx.Controller, parent)


if __name__ == "__main__":
    app = wx.App()
    dialog = CustomComponentExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
