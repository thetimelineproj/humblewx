import humblewx
import wx


class VariablesExampleDialog(humblewx.Dialog):

    """
    <BoxSizerVertical>
        <StaticText
            label="$(translated_label)"
        />
    </BoxSizerVertical>
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, humblewx.Controller, parent, {
            "translated_label": "Gutent tag",
        })


if __name__ == "__main__":
    app = wx.App()
    dialog = VariablesExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
