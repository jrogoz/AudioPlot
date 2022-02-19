import wx
from main_objects.panel import Panel

class Frame(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'AudioPlot', size=(1000, 700))
        panel = Panel(self, -1)



    def close_window(self, event):
        self.Destroy()

    def close_button(self, event):
        self.Close(True)