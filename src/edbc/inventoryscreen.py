from edbc.textscreen import TextScreen
from edbc.data.cargo import Cargo

import pyperclip

class InventoryScreen(TextScreen):
    def __init__(self, data):
        super(InventoryScreen, self).__init__(data)
        self.selection = -1
        self.startitem = 0

    def select1(self):
        print("select1")
        self.selection = 0
        self.buildScreen()

    def select2(self):
        print("select2")
        self.selection = 1

    def select3(self):
        print("select3")
        self.selection = 2

    def select4(self):
        print("select4")
        self.selection = 3

    def select5(self):
        print("select5")
        self.selection = 4

    def copyEddbCommodityUrlFromPos(self, pos):
        itemIdx = self.startitem + pos - 1
        itemId = self.data.cargo.items[itemIdx][0]
        url = f"https://eddb.io/commodity/{itemId}"
        pyperclip.copy(url)

    def copy1(self):
        self.copyEddbCommodityUrlFromPos(1)

    def copy2(self):
        self.copyEddbCommodityUrlFromPos(2)

    def copy3(self):
        self.copyEddbCommodityUrlFromPos(3)

    def copy4(self):
        self.copyEddbCommodityUrlFromPos(4)

    def copy5(self):
        self.copyEddbCommodityUrlFromPos(5)

    def inventoryLine(self, cargoitem):
        empty = " . . . . . . . . . . . . . . . . . : "
        itemname = Cargo.getName(cargoitem[0])
        amount = cargoitem[1]
        out = itemname + empty[len(itemname):] + f"{amount:3}T"
        return out

    def buildInventoryScreen(self):
        self.setButton(19, "SEL")
        self.setButton(18, "SEL")
        self.setButton(17, "SEL")
        self.setButton(16, "SEL")
        self.setButton(15, "SEL")
        self.ui.click20 = self.select1
        self.ui.click19 = self.select2
        self.ui.click18 = self.select3
        self.ui.click17 = self.select4
        self.ui.click16 = self.select5
        self.setButton(5, "CPY")
        self.setButton(6, "CPY")
        self.setButton(7, "CPY")
        self.setButton(8, "CPY")
        self.setButton(9, "CPY")
        self.ui.click5 = self.copy1
        self.ui.click6 = self.copy2
        self.ui.click7 = self.copy3
        self.ui.click8 = self.copy4
        self.ui.click9 = self.copy5
        self.setButton(14, "A..G")
        self.setButton(13, "H..M")
        self.setButton(12, "N..S")
        self.setButton(11, "T..Z")
        self.setButton(10, "0..9-")

        numitem = len(self.data.cargo.items)
        if numitem > 5:
            numitem = 5

        for i in range(0, numitem):
            self.setText(1 + (3 * i), 0,
                         self.inventoryLine(self.data.cargo.items[i]))

    def buildDetailScreen(self):
        for i in range(15, 5):
            self.setButton(i, '')

        itemIdx = self.selection + self.startitem
        itemId = self.data.cargo.items[itemIdx][0]
        itemAmount = self.data.cargo.items[itemIdx][1]
        itemName = Cargo.getName(itemId)

        self.setText(1, 0, f"{itemName} ({itemAmount}T)")

    def buildScreen(self):
        super(InventoryScreen, self).buildScreen()
        if self.selection == -1:
            self.buildInventoryScreen()
        else:
            self.buildDetailScreen()

