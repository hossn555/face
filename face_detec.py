import cv2
from operator import itemgetter
import time

class Detection:
	def __init__(self):
		#self.ESC_KEY = 27	 # Escキー
		self.INTERVAL= 33	 # 待ち時間　フレームレート下げるならここ大きくする
		self.count = 0
		self.FRAME_RATE = 30 # fps ここ使ってなくない？

		self.ORG_WINDOW_NAME = "org"
		self.GAUSSIAN_WINDOW_NAME = "gaussian"

		self.DEVICE_ID = 0

		self.detecFlag = False

		self.cascade_file = "./face_authentic/haarcascade_frontalface_alt2.xml"
		self.cascade = cv2.CascadeClassifier(self.cascade_file)
		self.cap = cv2.VideoCapture(self.DEVICE_ID)
		# 初期フレームの読込
		self.end_flag, self.c_frame = self.cap.read()
		self.height, self.width, self.channels = self.c_frame.shape
		# ウィンドウの準備
		cv2.namedWindow(self.ORG_WINDOW_NAME)
		cv2.namedWindow(self.GAUSSIAN_WINDOW_NAME)
		#cv2.namedWindow("face")

	# ループ用
	def main(self):
		self.face = self.detection()#顔認識（一番面積がでかいやつが帰ってくる）
		self.face_img = self.trim_face()#顔写真切り取り
		# Escキーで終了
		#key = cv2.waitKey(self.INTERVAL)
		time.sleep(self.INTERVAL/1000)
		(x,y,w,h) = self.face
		color = (0, 0, 225)
		pen_w = 3
		cv2.rectangle(self.img_gray, (x, y), (x+w, y+h), color, thickness = pen_w)
		# フレーム表示
		cv2.imshow(self.ORG_WINDOW_NAME, self.c_frame)
		cv2.imshow(self.GAUSSIAN_WINDOW_NAME, self.img_gray)
		#cv2.imshow("face", self.face_img)

	def get_face_img(self):
		self.face = self.detection()#顔認識（一番面積がでかいやつが帰ってくる）
		trim_face_img = self.trim_face()#顔写真切り取り
		return trim_face_img 

	#顔検出する時に使う
	def detection(self):
		self.img = self.c_frame
		self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		self.face_list = self.cascade.detectMultiScale(self.img_gray, minSize=(100, 100))
		face = [0,0,0,0]
		if len(self.face_list) is not 0:
			self.detecFlag = True
			face = self.most_big_face()
		else:
			self.detecFlag = False
		self.end_flag, self.c_frame = self.cap.read()
		return face

	#一番でかい顔を選択
	def most_big_face(self):
		self.big_face = 0
		self.big_face_area = 0
		list = []
		for i,(x,y,w,h) in enumerate(self.face_list):
			area = w*h
			list.append([i,area])
		list.sort(key=itemgetter(1))
		most_big_face_num = list[-1][0]
		face = self.face_list[most_big_face_num]
		return face

	def trim_face(self):
		(x,y,w,h) = self.face
		result_img = self.img[y:y+h, x:x+w]
		return result_img

if __name__ == '__main__':
	detec = Detection()
	while detec.end_flag == True:
		detec.main()
	#detec.face_img
	cv2.imwrite("out.jpg", detec.face_img)

		
