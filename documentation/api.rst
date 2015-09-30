API
===

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
