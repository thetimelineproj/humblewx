API
===

.. py:module:: humblewx

Classes
-------

.. py:class:: Dialog

    .. py:method:: __init__(controller_class, parent, variables={}, \*\*kwargs)

        This constructs a ``wx.Dialog`` and fills it with content according to
        the :ref:`GUI description <gui-description-language-label>` found in
        this class' docstring.

        :param controller_class:

            The class that should be used as a controller in this dialog. It
            will be initialized automatically.

        :param parent:

            The parent window to this dialog. Passed as first argument to the
            ``__init__`` method of the ``wx.Dialog``.

        :param variables:

            Variables that can be accessed by name from the XML definition.
            Should be a mapping from strings to Python values.

        :param \*\*kwargs:

            Additional parameters that are passed to the ``__init__`` method of
            the ``wx.Dialog``.

.. py:class:: Controller

    .. py:method:: __init__(view)

Configuration
-------------

.. py:data:: COMPONENT_MODULES

    :default: ``[wx]``

    This is a list of modules where ``humblewx`` will search for components.

    By default, only ``wx`` components can be found. Extend or change this list
    to allow ``humblewx`` to find components defined in other modules.

.. _gui-description-language-label:

GUI Description Language
------------------------

GUI descriptions are defined in XML.

Nodes in the XML correspond to either components or sizers. Attributes
correspond to arguments passed to the constructors. For example::

    <Button label="Hello World" />

Will result in the following Python code::

    wx.Button(..., label="Hello World")

Attribute values
~~~~~~~~~~~~~~~~

Often components need arguments that are not strings. Attribute values in the
XML are interpreted in the following order:

.. describe:: Variable

    Example::

        <Button label="$(name)" />

    If the attribute value matches the variable pattern ``$(..)``, the Python
    value will be fetched from the variables dictionary passed to
    :py:meth:`Dialog <humblewx.Dialog.__init__>`.

.. describe:: Boolean

    Example::

        <Button label="True" />
        <Button label="False" />

    If the attribute value matches eihter ``True`` or ``False``, the Python
    value will be the corresponding boolean.

.. describe:: String

    Example::

        <Button label="Hello World" />

    All other attribute values will be returned as Python strings.

Special nodes
~~~~~~~~~~~~~

.. describe:: BoxSizerVertical

    This is the quivalent of the following Python code::

        wx.BoxSizer(wx.VERTICAL)

.. describe:: BoxSizerHorizontal

    This is the quivalent of the following Python code::

        wx.BoxSizer(wx.HORIZONTAL)

.. describe:: FlexGridSizer

    This creates a ``wx.FlexGridSizer``. It supports the following attributes:

    .. describe:: rows

        :default: ``0``

        The number of rows this sizer should have.

    .. describe:: columns

        :default: ``0``

        The number of columns this sizer should have.

    .. describe:: growableColumns

        A comma separated list of integers saying which columns should be
        growable. (Argument to ``AddGrowableCol``.)

    .. describe:: growableRows

        A comma separated list of integers saying which row should be growable.
        (Argument to ``AddGrowableRow``.)

.. describe:: StaticBoxSizerVertical

    This creates a static box and a corresponding sizer used to lay out child
    components. All attributes are passed to the ``wx.StaticBox``. The sizer is
    created like this::

        wx.StaticBoxSizer(..., wx.VERTICAL)

.. describe:: Spacer

    This can only be used within a sizer.

.. describe:: StretchSpacer

    This can only be used within a sizer.

Special attributes
~~~~~~~~~~~~~~~~~~

.. describe:: name

.. describe:: event_*

.. describe:: border

.. describe:: borderType

.. describe:: proportion

.. describe:: align
