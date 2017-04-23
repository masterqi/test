import win32gui
import win32ui
import win32con
import win32api
import time

time.sleep(3)
hdesktop = win32gui.GetDesktopWindow()

width = win32api.GetSystemMetrics(win32con.SM_CXVIRTUALSCREEN)
hight = win32api.GetSystemMetrics(win32con.SM_CYVIRTUALSCREEN)
left = win32api.GetSystemMetrics(win32con.SM_XVIRTUALSCREEN)
top = win32api.GetSystemMetrics(win32con.SM_YVIRTUALSCREEN)

desktop_dc = win32gui.GetWindowDC(hdesktop)
img_dc = win32ui.CreateDCFromHandle(desktop_dc)

mem_dc = img_dc.CreateCompatibleDC()

screenshot = win32ui.CreateBitmap()
screenshot.CreateCompatibleBitmap(img_dc, width, hight)
mem_dc.SelectObject(screenshot)

mem_dc.BitBlt((0,0), (width, hight), img_dc, (left, top), win32con.SRCCOPY)

screenshot.SaveBitmapFile(mem_dc, 'a.png')

mem_dc.DeleteDC()
win32gui.DeleteObject(screenshot.GetHandle())