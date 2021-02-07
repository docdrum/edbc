from util.dse.dseerror import DSEError

class DSEBase:
    def __init__(self, max_len):
        self.input = ''
        self.max_len = max_len
        self.wait_for_more = False
        self.current_count = 0
        self.current_button = -1

    def get(self):
        return self.input

    def currentChar(self):
        if self.current_button == -1:
            return None
        return self.keys[self.current_button][self.current_count]

    def pressButton(self, button_id):
        if button_id > len(self.keys):
            raise DSEError("invalid button id")
        if self.wait_for_more and self.current_button == button_id:
            self.current_count += 1
            if self.current_count >= len(self.keys[self.current_button]):
                self.current_count = 0
        elif self.wait_for_more:
            self.input = self.input + self.currentChar()
            self.current_count = 0
            self.current_button = button_id
        else:
            self.current_count = 0
            self.current_button = button_id
            self.wait_for_more = True

    def timeOut(self):
        self.wait_for_more = False
        self.input = self.input + self.currentChar()
        self.current_count = 0
        self.current_button = -1
