API
===

Classes
-------

.. py:module:: humblewx

.. py:class:: Dialog

    .. py:method:: __init__(controller_class, parent)

        This constructs a ``wx.Dialog`` where the components are created and
        laid out according to the XML definition found in the docstring for
        this class.

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

XML definition
--------------

Nodes in the XML definition correspond to a component or a sizer. Attributes
correspond to arguments to that component.

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

The following attributes can be put on any node that is a child of a sizer
node:

.. describe:: border

.. describe:: borderType

.. describe:: proportion

.. describe:: align

Attribute values
~~~~~~~~~~~~~~~~

Generic attribute values are interpreted in the following order:

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
