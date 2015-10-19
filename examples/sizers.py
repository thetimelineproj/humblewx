import humblewx
import wx


class SizersExampleDialog(humblewx.Dialog):

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
    dialog = SizersExampleDialog(None)
    dialog.ShowModal()
    dialog.Destroy()
