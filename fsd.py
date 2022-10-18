# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 22:30:45 2022

@author: vinayak
"""

import wx


class Electronics(wx.Frame):

    def __init__(self, parent, title):
        super(Electronics, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        home = fileMenu.Append(wx.ID_ANY, 'Home')
        ph = fileMenu.Append(wx.ID_ANY, 'Phones')
        tab = fileMenu.Append(wx.ID_ANY, 'Tablets')
        con = fileMenu.Append(wx.ID_ANY, 'Consoles')
        lap = fileMenu.Append(wx.ID_ANY, 'Laptops')
        menubar.Append(fileMenu, 'Categories')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.home, home)
        self.Bind(wx.EVT_MENU, self.phone, ph)
        self.Bind(wx.EVT_MENU, self.tablet, tab)
        self.Bind(wx.EVT_MENU, self.console, con)
        self.Bind(wx.EVT_MENU, self.laptop, lap)
        welcome = wx.StaticBitmap(self, wx.ID_ANY, wx.Bitmap("Images/welcome.jpg", wx.BITMAP_TYPE_ANY))
        welcome.SetSize(1920,1080)
        
    
    def home(self, e):
        self.Close()
        H = Electronics(None, title = 'HKVNPS SHOP')
        H.Show()
    def phone(self, e):
        self.Close()
        P = phoneUI(None, title = 'Phones')
        P.Show()
    def tablet(self, e):
        self.Close()
        T = tabletUI(None, title = 'Tablets')
        T.Show()
    def console(self, e):
        self.Close()
        C = consoleUI(None, title = 'Consoles')
        C.Show()
    def laptop(self, e):
        self.Close()
        L = laptopUI(None, title = 'Laptop')
        L.Show()

class phoneUI(wx.Frame):
    def __init__(self, parent, title):
        super(phoneUI, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
        self.SetBackgroundColour(wx.WHITE)
        
    def InitUI(self):
        
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        home = fileMenu.Append(wx.ID_ANY, 'Home')
        ph = fileMenu.Append(wx.ID_ANY, 'Phones')
        tab = fileMenu.Append(wx.ID_ANY, 'Tablets')
        con = fileMenu.Append(wx.ID_ANY, 'Consoles')
        lap = fileMenu.Append(wx.ID_ANY, 'Laptops')
        menubar.Append(fileMenu, 'Categories')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.home, home)
        self.Bind(wx.EVT_MENU, self.phone, ph)
        self.Bind(wx.EVT_MENU, self.tablet, tab)
        self.Bind(wx.EVT_MENU, self.console, con)
        self.Bind(wx.EVT_MENU, self.laptop, lap)
        
        image1 = wx.Image("Images/iPhone.jpg", wx.BITMAP_TYPE_ANY)
        W = image1.GetWidth()
        H = image1.GetHeight()
        if W > H:
            NewW = 600
            NewH = 600 * H / W
        else:
            NewH = 600
            NewW = 600 * W / H
        image1 = image1.Scale(NewW,NewH)
        image1=image1.ConvertToBitmap()
        image1.SetSize((400,250))
        bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, image1, pos=(50,50))
        
        image2 = wx.Image("Images/Samsung.jpg", wx.BITMAP_TYPE_ANY)
        W = image2.GetWidth()
        H = image2.GetHeight()
        if W > H:
            NewW = 400
            NewH = 400 * H / W
        else:
            NewH = 400
            NewW = 400 * W / H
        image2 = image2.Scale(NewW,NewH)
        image2 = image2.ConvertToBitmap()
        image2.SetSize((400, 250))
        bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, image2, pos=(800, 50))
        
        image3 = wx.Image("Images/ROG.jpg", wx.BITMAP_TYPE_ANY)
        W = image3.GetWidth()
        H = image3.GetHeight()
        if W > H:
            NewW = 350
            NewH = 350 * H / W
        else:
            NewH = 350
            NewW = 350 * W / H
        image3 = image3.Scale(NewW,NewH)
        image3 = image3.ConvertToBitmap()
        image3.SetSize((400, 250))
        bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, image3, pos=(50, 450))
        
        image4 = wx.Image("Images/Pixel.jpg", wx.BITMAP_TYPE_ANY)
        W = image4.GetWidth()
        H = image4.GetHeight()
        if W > H:
            NewW = 350
            NewH = 350 * H / W
        else:
            NewH = 350
            NewW = 350 * W / H
        image4 = image4.Scale(NewW,NewH)
        image4 = image4.ConvertToBitmap()
        image4.SetSize((400, 250))
        bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, image4, pos=(800,450))
            
        st1 = wx.StaticText(self, label = "APPLE IPHONE 14 PRO MAX\nSCREEN: 6.7\nRAM: 6GB\nBATTERY: 4323 mAh\nPRICE: RS. 1,29,999", pos = (500,50))
        st2 = wx.StaticText(self, label = "SAMSUNG ZFOLD 3 5G\nSCREEN: 7.8\nRAM: 12GB\nBATTERY: 4400 mAh\nPRICE: RS. 1,09,999", pos = (1250,50))
        st3 = wx.StaticText(self, label = "ROG PHONE 6 PRO\nSCREEN: 6.78\nRAM: 18GB\nBATTERY: 6000 mAh\nPRICE: RS. 89,999", pos = (500,450))
        st4 = wx.StaticText(self, label = "PIXEL 7 PRO\nSCREEN: 6.7\nRAM: 8GB\nBATTERY: 5000 mAh\nPRICE: RS. 85,999", pos = (1250, 450))
        
    def home(self, e):
        self.Close()
        H = Electronics(None, title = 'HKVNPS SHOP')
        H.Show()
    def phone(self, e):
        self.Close()
        P = phoneUI(None, title = 'Phones')
        P.Show()
    def tablet(self, e):
        self.Close()
        T = tabletUI(None, title = 'Tablets')
        T.Show()
    def console(self, e):
        self.Close()
        C = consoleUI(None, title = 'Consoles') 
        C.Show()
    def laptop(self, e):
        self.Close()
        L = laptopUI(None, title = 'Laptop')
        L.Show()
    
    
class tabletUI(wx.Frame):
    def __init__(self, parent, title):
        super(tabletUI, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
        self.SetBackgroundColour(wx.WHITE)
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        home = fileMenu.Append(wx.ID_ANY, 'Home')
        ph = fileMenu.Append(wx.ID_ANY, 'Phones')
        tab = fileMenu.Append(wx.ID_ANY, 'Tablets')
        con = fileMenu.Append(wx.ID_ANY, 'Consoles')
        lap = fileMenu.Append(wx.ID_ANY, 'Laptops')
        menubar.Append(fileMenu, 'Categories')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.home, home)
        self.Bind(wx.EVT_MENU, self.phone, ph)
        self.Bind(wx.EVT_MENU, self.tablet, tab)
        self.Bind(wx.EVT_MENU, self.console, con)
        self.Bind(wx.EVT_MENU, self.laptop, lap)
    
        image1 = wx.Image("Images/iPad.jpg", wx.BITMAP_TYPE_ANY)
        W = image1.GetWidth()
        H = image1.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image1 = image1.Scale(NewW,NewH)
        image1 = image1.ConvertToBitmap()
        image1.SetSize((400, 250))
        bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, image1, pos=(50,50))
        
        image2 = wx.Image("Images/PixelTab.jpg", wx.BITMAP_TYPE_ANY)
        W = image2.GetWidth()
        H = image2.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image2 = image2.Scale(NewW,NewH)
        image2 = image2.ConvertToBitmap()
        image2.SetSize((400, 250))
        bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, image2, pos=(800, 50))
        
        image3 = wx.Image("Images/SamTab.jpg", wx.BITMAP_TYPE_ANY)
        W = image3.GetWidth()
        H = image3.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image3 = image3.Scale(NewW,NewH)
        image3 = image3.ConvertToBitmap()
        image3.SetSize((400, 250))
        bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, image3, pos=(50, 450))
        
        image4 = wx.Image("Images/LenTab.jpg", wx.BITMAP_TYPE_ANY)
        W = image4.GetWidth()
        H = image4.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image4 = image4.Scale(NewW,NewH)
        image4 = image4.ConvertToBitmap()
        image4.SetSize((400, 250))
        bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, image4, pos=(800,450))
        
        st1 = wx.StaticText(self, label = "APPLE IPAD 10.2\nSCREEN: 10.2\nRAM: 3GB\nBATTERY: 8827 mAh\nPRICE: RS. 29,999", pos = (500,50))
        st2 = wx.StaticText(self, label = "GOOGLE PIXEL TAB\nSCREEN: 10.95\nRAM: 6GB\nBATTERY: 9000 mAh\nPRICE: RS. 34,999", pos = (1250,50))
        st3 = wx.StaticText(self, label = "SAMSUNG GALAXY TAB S8\nSCREEN: 10.1\nRAM: 8GB\nBATTERY: 8000 mAh\nPRICE: RS. 49,999", pos = (500,450))
        st4 = wx.StaticText(self, label = "LENOVO TAB 4 10\nSCREEN: 11\nRAM: 3GB\nBATTERY: 7000 mAh\nPRICE: RS. 14,999", pos = (1250, 450))
        
    def home(self, e):
        self.Close()
        H = Electronics(None, title = 'HKVNPS SHOP')
        H.Show()
    def phone(self, e):
        self.Close()
        P = phoneUI(None, title = 'Phones')
        P.Show()
    def tablet(self, e):
        self.Close()
        T = tabletUI(None, title = 'Tablets')
        T.Show()
    def console(self, e):
        self.Close()
        C = consoleUI(None, title = 'Consoles')
        C.Show()
    def laptop(self, e):
        self.Close()
        L = laptopUI(None, title = 'Laptop')
        L.Show()
        
class consoleUI(wx.Frame):
    def __init__(self, parent, title):
        super(consoleUI, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
        self.SetBackgroundColour(wx.WHITE)
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        home = fileMenu.Append(wx.ID_ANY, 'Home')
        ph = fileMenu.Append(wx.ID_ANY, 'Phones')
        tab = fileMenu.Append(wx.ID_ANY, 'Tablets')
        con = fileMenu.Append(wx.ID_ANY, 'Consoles')
        lap = fileMenu.Append(wx.ID_ANY, 'Laptops')
        menubar.Append(fileMenu, 'Categories')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.home, home)
        self.Bind(wx.EVT_MENU, self.phone, ph)
        self.Bind(wx.EVT_MENU, self.tablet, tab)
        self.Bind(wx.EVT_MENU, self.console, con)
        self.Bind(wx.EVT_MENU, self.laptop, lap)
        
        image1 = wx.Image("Images/PS5.jpg", wx.BITMAP_TYPE_ANY)
        W = image1.GetWidth()
        H = image1.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image1 = image1.Scale(NewW,NewH)
        image1 = image1.ConvertToBitmap()
        image1.SetSize((400, 250))
        bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, image1, pos=(50,50))
        
        image2 = wx.Image("Images/Xbox.jpg", wx.BITMAP_TYPE_ANY)
        W = image2.GetWidth()
        H = image2.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image2 = image2.Scale(NewW,NewH)
        image2 = image2.ConvertToBitmap()
        image2.SetSize((400, 250))
        bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, image2, pos=(800, 50))
        
        image3 = wx.Image("Images/Wii.jpg", wx.BITMAP_TYPE_ANY)
        W = image3.GetWidth()
        H = image3.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image3 = image3.Scale(NewW,NewH)
        image3 = image3.ConvertToBitmap()
        image3.SetSize((400, 250))
        bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, image3, pos=(50, 450))
        
        image4 = wx.Image("Images/Switch.jpg", wx.BITMAP_TYPE_ANY)
        W = image4.GetWidth()
        H = image4.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image4 = image4.Scale(NewW,NewH)
        image4 = image4.ConvertToBitmap()
        image4.SetSize((400, 250))
        bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, image4, pos=(800,450))
        
        st1 = wx.StaticText(self, label = "PS5\nSTORAGE: 512GB\nRAM: 16GB\nGPU: CUSTOM AMD GPU 10.3 TFLOPs\nPRICE: RS. 89,999", pos = (500,50))
        st2 = wx.StaticText(self, label = "XBOX SERIES X\nSTORAGE: 1TB\nRAM: 16GB\nGPU: CUSTOM AMD GPU 12.1 TFLOPs\nPRICE: RS. 99,999", pos = (1250,50))
        st3 = wx.StaticText(self, label = "WII\nSTORAGE: 32GB\nRAM: 1GB\nGPU: CUSTOM ATI GPU 12 GFLOPs\nPRICE: RS. 7,999", pos = (500,450))
        st4 = wx.StaticText(self, label = "NINTENDO SWITCH\nSTORAGE: 64GB\nRAM: 4GB\nGPU: CUSTOM TEGRA GPU\nBATTERY: 4310mAh\nPRICE: RS. 39,999", pos = (1250, 450))
        
    def home(self, e):
        self.Close()
        H = Electronics(None, title = 'HKVNPS SHOP')
        H.Show()
    def phone(self, e):
        self.Close()
        P = phoneUI(None, title = 'Phones')
        P.Show()
    def tablet(self, e):
        self.Close()
        T = tabletUI(None, title = 'Tablets')
        T.Show()
    def console(self, e):
        self.Close()
        C = consoleUI(None, title = 'Consoles')
        C.Show()
    def laptop(self, e):
        self.Close()
        L = laptopUI(None, title = 'Laptop')
        L.Show()
        
class laptopUI(wx.Frame):
    def __init__(self, parent, title):
        super(laptopUI, self).__init__(parent, title=title)
        self.InitUI()
        self.Centre()
        self.Maximize(True)
        self.SetBackgroundColour(wx.WHITE)
        
    def InitUI(self):
        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        home = fileMenu.Append(wx.ID_ANY, 'Home')
        ph = fileMenu.Append(wx.ID_ANY, 'Phones')
        tab = fileMenu.Append(wx.ID_ANY, 'Tablets')
        con = fileMenu.Append(wx.ID_ANY, 'Consoles')
        lap = fileMenu.Append(wx.ID_ANY, 'Laptops')
        menubar.Append(fileMenu, 'Categories')
        self.SetMenuBar(menubar)
        
        self.Bind(wx.EVT_MENU, self.home, home)
        self.Bind(wx.EVT_MENU, self.phone, ph)
        self.Bind(wx.EVT_MENU, self.tablet, tab)
        self.Bind(wx.EVT_MENU, self.console, con)
        self.Bind(wx.EVT_MENU, self.laptop, lap)
        
        image1 = wx.Image("Images/Mac.jpg", wx.BITMAP_TYPE_ANY)
        W = image1.GetWidth()
        H = image1.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image1 = image1.Scale(NewW,NewH)
        image1 = image1.ConvertToBitmap()
        image1.SetSize((400, 250))
        bitmap1 = wx.StaticBitmap(self, wx.ID_ANY, image1, pos=(50,50))
        
        image2 = wx.Image("Images/HP.jpg", wx.BITMAP_TYPE_ANY)
        W = image2.GetWidth()
        H = image2.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image2 = image2.Scale(NewW,NewH)
        image2 = image2.ConvertToBitmap()
        image2.SetSize((400, 250))
        bitmap2 = wx.StaticBitmap(self, wx.ID_ANY, image2, pos=(800, 50))
        
        image3 = wx.Image("Images/Lenovo.jpg", wx.BITMAP_TYPE_ANY)
        W = image3.GetWidth()
        H = image3.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image3 = image3.Scale(NewW,NewH)
        image3 = image3.ConvertToBitmap()
        image3.SetSize((400, 250))
        bitmap3 = wx.StaticBitmap(self, wx.ID_ANY, image3, pos=(50, 450))
        
        image4 = wx.Image("Images/Dell.jpg", wx.BITMAP_TYPE_ANY)
        W = image4.GetWidth()
        H = image4.GetHeight()
        if W > H:
            NewW = 300
            NewH = 300 * H / W
        else:
            NewH = 300
            NewW = 300 * W / H
        image4 = image4.Scale(NewW,NewH)
        image4 = image4.ConvertToBitmap()
        image4.SetSize((400, 250))
        bitmap4 = wx.StaticBitmap(self, wx.ID_ANY, image4, pos=(800,450))
        
        st1 = wx.StaticText(self, label = "MACBOOK PRO 16\nSCREEN: 16\nRAM: 16GB\nBATTERY: 80.9 Whr\nPRICE: RS. 99,999", pos = (500,50))
        st2 = wx.StaticText(self, label = "PAVILION 15\nSCREEN: 15.6\nRAM: 8GB\nBATTERY: 70 Whr\nPRICE: RS. 59,999", pos = (1250,50))
        st3 = wx.StaticText(self, label = "LENOVO THINKPAD\nSCREEN: 15.6\nRAM: 8GB\nBATTERY: 48 Whr\nPRICE: RS. 49,999", pos = (500,450))
        st4 = wx.StaticText(self, label = "DELL INSPIRON 15\nSCREEN: 15.6\nRAM: 16GB\nBATTERY: 56 Whr\nPRICE: RS. 79,999", pos = (1250, 450))
        
    
    def home(self, e):
        self.Close()
        H = Electronics(None, title = 'HKVNPS SHOP')
        H.Show()
    def phone(self, e):
        self.Close()
        P = phoneUI(None, title = 'Phones')
        P.Show()
    def tablet(self, e):
        self.Close()
        T = tabletUI(None, title = 'Tablets')
        T.Show()
    def console(self, e):
        self.Close()
        C = consoleUI(None, title = 'Consoles')
        C.Show()
    def laptop(self, e):
        self.Close()
        L = laptopUI(None, title = 'Laptop')
        L.Show()

def main():

    app = wx.App()
    E = Electronics(None, title='HKVNPS SHOP')
    E.Show()
    app.MainLoop()


if __name__ == '__main__':
    main()