Using Sizers
============

Sizers is the technique used in wxPython to control the layout of components.
However, using sizers directly requires writing code that is difficult to
understand.  Here is a simple example:

.. literalinclude:: ../examples/sizers.py
    :language: python
    :pyobject: SizersWxExampleDialog

We have two buttons that are laid out vertically. It looks like this:

.. image:: /images/sizers_wx.png

The problem is that this is not obvious to figure out by taking a quick look at
the code. That is because the structure of the components is not reflected in
the structure of the code. This problem grows larger the more components we
have in our dialogs.

``humblewx`` allow us to define everything about a component in one place. The
hierarchical structure of XML also makes it easier to see how the components
are laid out.  Let's see what the above example looks like rewritten using
``humblewx``:

.. literalinclude:: ../examples/sizers.py
    :language: python
    :pyobject: SizersHumbleWxExampleDialog

Quickly we can see that this dialog has two buttons and that they are laid out
vertically.

Here is a larger example demonstrating what we can do with sizers.

.. literalinclude:: ../examples/sizers.py
    :language: python
    :pyobject: SizersFullExampleDialog

The dialog looks like this:

.. image:: /images/sizers.png
