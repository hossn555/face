#face_authentic.py
from face_authentic.face_detec import Detection
from face_authentic import setup
import cognitive_face as CF
import cv2
RETURN_TIMES = 1
KEY = setup.APIKEY
CF.Key.set(KEY)
BASE_URL = setup.BASE_URL
CF.BaseUrl.set(BASE_URL)

def face_authentic():
	detec = Detection()
	detec.INTERVAL = 100
	count = 0
	faceIds = []
	while detec.end_flag == True:
		detec.main()
		imgUrl = "./face_authentic/trimImgs/out{}.jpg".format(str(count))
		cv2.imwrite(imgUrl, detec.face_img)
		faceDetec = CF.face.detect(imgUrl)
		faceId = faceDetec[0]['faceId']
		faceIds.append(faceId)
		count = count + 1
		if count == RETURN_TIMES:
			detec.end_flag = False
		print("count:{}".format(str(count)))
	result = CF.face.identify(faceIds,setup.PERSON_GROUPID)
	print("result:{}".format(result))
	personId:str = ""
	if result[0]['candidates'] == []:
		print("該当なし")
	else:
		personId = result[0]['candidates'][0]['personId']
	return personId
