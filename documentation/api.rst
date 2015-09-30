API
===

.. py:module:: humblewx

Classes
-------

.. py:class:: Dialog

    .. py:method:: __init__(controller_class, parent)

        This constructs a ``wx.Dialog`` and fills it with content according to
        the :ref:`GUI description <gui-description-language-label>` found in the docstring for this
        class.

        :param class controller_class:

            The class that should be uses as a controller in this dialog. It
            will be initialized automatically.

        :param class parent:

            The parent window to this dialog. Passes as first argument to the
            ``__init__`` method of the ``wx.Dialog``.

        :param dictionary variables:

            Variables that can be accessed by name from the XML definition.

        :param kwargs kwargs:

            Parameters passed to the ``__init__`` method of the ``wx.Dialog``.

.. py:class:: Controller

    .. py:method:: __init__(view)

.. _gui-description-language-label:

Configuration
-------------

.. py:data:: COMPONENT_MODULES

    :default: ``[wx]``

    This is a list of modules where ``humblewx`` will search for components.

    By default, only ``wx`` components can be found. Extend or change this list
    to allow ``humblewx`` to find components defined in other modules.

GUI description language
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

.. describe:: BoxSizerHorizontal

.. describe:: FlexGridSizer

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
