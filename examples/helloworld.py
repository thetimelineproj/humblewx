import humblewx
import wx


class HelloWorldDialog(humblewx.Dialog):

    """
    <StaticText label="Hello World" />
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, HelloWorldDialogController, parent)


class HelloWorldDialogController(humblewx.Controller):
    pass


if __name__ == "__main__":
    app = wx.App()
    dialog = HelloWorldDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
