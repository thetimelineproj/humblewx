import humblewx
import wx


class SizersWxExampleDialog(wx.Dialog):

    def __init__(self, parent):
        wx.Dialog.__init__(self, parent)
        button1 = wx.Button(self, label="button 1")
        button2 = wx.Button(self, label="button 2")
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(button1, flag=wx.EXPAND|wx.ALL, border=5)
        sizer.Add(button2, flag=wx.EXPAND)
        self.SetSizerAndFit(sizer)


class SizersHumbleWxExampleDialog(humblewx.Dialog):

    """
    <BoxSizerVertical>
        <Button label="button 1" border="ALL" />
        <Button label="button 2" />
    </BoxSizerVertical>
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, humblewx.Controller, parent)



class SizersFullExampleDialog(humblewx.Dialog):

    """
    <BoxSizerVertical>

        <StaticText border="TOP" label="Demonstrating proportion:" />
        <BoxSizerHorizontal>
            <Button label="button 1" proportion="1" />
            <Button label="button 2" proportion="1" />
            <Button label="button 3" proportion="2" />
        </BoxSizerHorizontal>

        <StaticText border="TOP" label="Demonstrating stretch spacer:" />
        <BoxSizerHorizontal>
            <Button label="button 1" />
            <StretchSpacer />
            <Button label="button 2" />
        </BoxSizerHorizontal>

        <StaticText border="TOP" label="Demonstrating spacer:" />
        <BoxSizerHorizontal>
            <Button label="button 1" />
            <Spacer />
            <Button label="button 2" proportion="1" />
        </BoxSizerHorizontal>

        <StaticText border="TOP" label="Demonstrating grid:" />
        <FlexGridSizer columns="2" align="ALIGN_CENTER">
            <Button label="button 1" />
            <Button label="button 2" />
            <Button label="button 3" />
            <Button label="button 4" />
        </FlexGridSizer>

    </BoxSizerVertical>
    """

    def __init__(self, parent):
        humblewx.Dialog.__init__(self, humblewx.Controller, parent)


if __name__ == "__main__":
    app = wx.App()
    dialog = SizersWxExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
    dialog = SizersHumbleWxExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
    dialog = SizersFullExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
