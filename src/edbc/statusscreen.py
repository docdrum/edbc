from edbc.textscreen import TextScreen

class StatusScreen(TextScreen):
    def __init__(self, data):
        super(StatusScreen, self).__init__(data)

    def buildScreen(self):
        super(StatusScreen, self).buildScreen()
        self.setButton(19, "OVR")

        self.setButton(14, "A..G")
        self.setButton(13, "H..M")
        self.setButton(12, "N..S")
        self.setButton(11, "T..Z")
        self.setButton(10, "0..9-")

        self.setText(0, 0, f"CMDR: {self.data.pilot.name}")
        self.setText(1, 0, f"SHIP: {self.data.pilot.ship}")
        self.setText(2, 0, f"CRED: {self.data.pilot.credits}" )
        self.setText(3, 0, f"SYS:  {self.data.pilot.current_system}")
