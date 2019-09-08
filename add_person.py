#add_person.py
from face_authentic import config
import cognitive_face as CF
import glob
KEY = setup.APIKEY
CF.Key.set(KEY)
BASE_URL = setup.BASE_URL
CF.BaseUrl.set(BASE_URL)

def add_person(name,pictures_path):

	add_person = CF.person.create(setup.PERSON_GROUPID,name)
	personId = add_person["personId"]
	if pictures_path[-1:] == "/":			#pathの最後が"/*"となるようにする
		pictures_path = pictures_path + "*"
	else:
		pictures_path = pictures_path + "/*"
	print("path{}".format(pictures_path))
	picture_list = glob.glob(pictures_path)
	print("picture_list{}".format(picture_list))
	for picture in picture_list:
		result = CF.person.add_face(picture,setup.PERSON_GROUPID,personId)
		print(result)
	CF.person_group.train(setup.PERSON_GROUPID) #学習させる

if __name__ == '__main__':
	name:str = input("Name: ")
	pictures_path:str = input("Pictures directly path: ")
	add_person(name,pictures_path)


