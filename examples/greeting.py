import humblewx
import wx


class GreetingDialog(humblewx.Dialog):

    """
    <BoxSizerVertical>
        <BoxSizerHorizontal>
            <StaticText label="What is your name?" />
            <TextCtrl name="name_text_ctrl" />
            <Button label="Greet" event_EVT_BUTTON="on_greet_clicked" />
        </BoxSizerHorizontal>
        <StaticText name="greeting" label="" />
    </BoxSizerVertical>
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, GreetingDialogController, parent)

    def GetName(self):
        return self.name_text_ctrl.GetValue()

    def SetGreeting(self, text):
        self.greeting.SetLabel(text)


class GreetingDialogController(humblewx.Controller):

    def on_greet_clicked(self, event):
        self.view.SetGreeting("Hello %s!" % self.view.GetName())


if __name__ == "__main__":
    app = wx.App()
    dialog = GreetingDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
