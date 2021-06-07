import cv2
import dropbox
import time
import random
import dropbox
import keyboard


class TransferData:
	def __init__(self, token):
		self.token = token

	def upload_file(self, file_from, file_name):
		dbx = dropbox.Dropbox(self.token)

		with open(file_from, 'rb') as f:
			dbx.files_upload(f.read(), file_name)

def take_snapshot(file_name):
	camera_object = cv2.VideoCapture(0)
	result = True

	while result:
		ret, frame = camera_object.read()
		print(frame)
		cv2.imwrite(file_name, frame)
		result = False

	camera_object.release()
	cv2.destroyAllWindows()

token = 'sl.AyRNXXBMACGINGr3WUGZwkKs_oVTy8FeNx4gap5eyXYLGkCeVA5q1vMZHzS1zJBWT-xgB15Uq8yFRwOeLYJ4fpCSWh3iPBulmL2tCbpG7FNN5CEH72t3Epdqobb-CBq3Nolbyq0jxoo'
transfer_data = TransferData(token)


while True:
	if(keyboard.is_pressed('q')):
		break
	else:
		file_name = file_name = dropbox_file_name = str(random.randint(0, 100))+'.png'
		dropbox_file_name = '/images/'+file_name
		take_snapshot(file_name)
		transfer_data.upload_file(file_name, dropbox_file_name)
		time.sleep(10)