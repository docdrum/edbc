'''
Created on 5 Feb 2021

@author: cstft
'''
ruler16 = '-------------------------------------------------------'
ruler = ruler16

bgcol = "#000000"
#fgcol = "#00ff00"
fgcol = "#a89322"

class TextScreen:
    def __init__(self, data):
        self.lines = [''] * 19
        self.button = [''] * 20
        self.screen = None
        self.display = ''
        self.ui = None
        self.data = data
            
    def setUI(self, edbc):
        self.ui = edbc
    
    def setButton(self, i, text):
        self.button[i] = text[:5]
        
    def clear(self, i=-1):
        if i<0:
            for i in range(0, len(self.lines)):
                self.clear(i)
        else:
            self.lines[i] = len(ruler) * ' '
    
    def replace(self, s, newstr, pos):
        return s[:pos] + newstr + s[pos + len(newstr):]

    def replaceStart(self, s, newstr):
        return newstr + s[len(newstr):]
    
    def replaceEnd(self, s, newstr):
        return s[:len(s) - len(newstr)] + newstr
        
    def center(self, line, pos, text):
        l = len(text)
        offset = int(l/2)
        rpos = pos-offset
        self.lines[line] = self.replace(self.lines[line], text, rpos)
        
    def setText(self, line, pos, text):
        self.display[line] = self.replace(self.display[line], text, pos)
        
    def buildButtons(self):
        self.center(0, 5, '[' + self.button[0] + ']')
        self.center(0, 16, '[' + self.button[1] + ']')
        self.center(0, 28, '[' + self.button[2] + ']')
        self.center(0, 39, '[' + self.button[3] + ']')
        self.center(0, 50, '[' + self.button[4] + ']')
        self.lines[3] = self.replaceStart(self.lines[3], '[' + self.button[19] + ']')
        self.lines[6] = self.replaceStart(self.lines[6], '[' + self.button[18] + ']')
        self.lines[9] = self.replaceStart(self.lines[9], '[' + self.button[17] + ']')
        self.lines[12] = self.replaceStart(self.lines[12], '[' + self.button[16] + ']')
        self.lines[15] = self.replaceStart(self.lines[15], '[' + self.button[15] + ']')
        self.lines[3] = self.replaceEnd(self.lines[3], '[' + self.button[5] + ']')
        self.lines[6] = self.replaceEnd(self.lines[6], '[' + self.button[6] + ']')
        self.lines[9] = self.replaceEnd(self.lines[9], '[' + self.button[7] + ']')
        self.lines[12] = self.replaceEnd(self.lines[12], '[' + self.button[8] + ']')
        self.lines[15] = self.replaceEnd(self.lines[15], '[' + self.button[9] + ']')
        self.center(18, 50, '[' + self.button[10] + ']')
        self.center(18, 39, '[' + self.button[11] + ']')
        self.center(18, 28, '[' + self.button[12] + ']')
        self.center(18, 16, '[' + self.button[13] + ']')
        self.center(18, 5, '[' + self.button[14] + ']')
        
    def buildScreen(self):
        self.setButton(0, "STAT")
        self.setButton(1, "INV")
        self.setButton(2, "sys")
        self.setButton(3, "miss")
        self.setButton(4, "find")
        for i in range(5, 19):
            self.setButton(i, '')

    def build(self):
        self.clear(-1)
        fakeline = '' * 40
        self.display = [fakeline] * 15
        
        self.buildScreen()
        self.buildButtons()
        for i in range(2, 17):
            self.lines[i] = self.replace(self.lines[i], self.display[i-2], 8)
        
    def get(self):
        if self.screen is None:
            self.build()
            self.screen = '\n'.join(self.lines)
        return self.screen
            
