import wx
from main_objects.frame import Frame
from matplotlib import rcParams

if __name__ == '__main__':
    rcParams.update({'figure.autolayout': True})
    app = wx.App()
    frame = Frame(None, -1)
    frame.Show()
    app.MainLoop()
