import wx

class Game(wx.Frame):
	def __init__(self,parent,id):
		wx.Frame.__init__(self,parent,id,"Jacob's Game Window", size=(400,400))

if __name__=='__main__':
	app=wx.PySimpleApp()
	frame=Game(parent=None,id=-1)
	frame.Show()
	app.MainLoop()