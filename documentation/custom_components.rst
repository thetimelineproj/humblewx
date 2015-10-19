Using Custom Components
=======================

We have seen that we can refer to standard ``wx`` components such as buttons
and static text fields from the XML. What about custom components that are not
inside the ``wx`` namespace?

``humblewx`` can be configured to look for components anywhere. We just need to
modify the :py:data:`humblewx.COMPONENT_MODULES` configuration variable.

Say we have this custom component that we want to use in a dialog:

.. literalinclude:: ../examples/custom_component.py
    :language: python
    :pyobject: CustomComponent

In the XML we can just refer to this component by name as we do with any other
``wx`` component:

.. literalinclude:: ../examples/custom_component.py
    :language: python
    :pyobject: CustomComponentExampleDialog

It looks like this:

.. image:: /images/custom_component.png

In order for this to work, we have to tell ``humblewx`` that it should also
look for components in another module. In this example, we only have one module
where both the custom component and the dialog are defined. We can get a
reference to that module with the following code::

    sys.modules[__name__]

Next we need to modify :py:data:`humblewx.COMPONENT_MODULES` to include this
module:

.. literalinclude:: ../examples/custom_component.py
    :language: python
    :lines: 6

We need to run this code before we create our dialog.

We can add any module to this list::

    import foo.bar
    humblewx.COMPONENT_MODULES.append(foo.bar)
