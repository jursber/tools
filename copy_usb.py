import os
import time
from datetime import datetime 
import shutil


usb_path1='G:/'
usb_path2='E:/'
usb_path3='F:/'
save_path='C:/USB/'

print('Monitoring...')
def mission(usb_path):
		try:
			print('Contacted with a target\nperform the mission...')
			shutil.copytree(usb_path,os.path.join(save_path,datetime.now().strftime("%Y%m%d_%H%M%S")))
			print('Mission accomplished！')
		except:
			print('Mission interruption！')

while(True):
	if os.path.exists(usb_path1):
		mission(usb_path1)
		break

	elif os.path.exists(usb_path2):
		mission(usb_path2)
		break

	elif os.path.exists(usb_path3):
		mission(usb_path3)
		break

	else:
		time.sleep(10)
