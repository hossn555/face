# 顔認識
※macで作ったので、windowsで使うときにはちょっと変更しなくてはならないところがある。ファイルのパスとかの`/`を`¥`にしなきゃいけなかったり 
## できること
1. 人とその顔の登録
1. 登録した人を識別

実際に実装するときには、チュートリアルを参考にコードを組むと多分いい
## インストール
```
git clone https://github.com/hossn555/face
```
## 必要なモジュールのインストール
```
pip install opencv-python
pip install cognitive_face
```
##APIKEYの入力
APIKEYを取得、これを`face/setup.py`の`<APIKEY>`の部分に入力する
必要ならばBASE_URLも変更
## チュートリアル
#### 登録
`git clone`で取得した`face`フォルダと同じ階層で以下の`add_main.py`を作成
```
from face_authentic import add_person

name:str = input("Name: ")
pictures_path:str = input("Pictures directly path: ")
add_person(name,pictures_path)
```
同じ人物が一人だけ映った画像が何枚か入ったフォルダ(例：pictureフォルダ)を同じ階層に作成
写真は何枚でもいい
add_main.pyを実行
```
python3 add_main.py
```
最初に名前、そのあとに写真の入ったフォルダのパス(`./picture`)を入力

登録完了
####
`face`フォルダと同じ階層に以下の`main.py`を作成
```
from face_authentic import face_detec
from face_authentic import face_authentic as FA
from face_authentic import setup
import cognitive_face as CF

def main_roop():
	#１秒間顔が検出されるまで待機（実際はもうちょっとかかる）
	detec = face_detec.Detection()
	timeLimit:float = 1
	time:float = 0 #[s]
	while detec.end_flag == True:
		detec.main()
		if detec.detecFlag == True:
			time = time + detec.INTERVAL/1000
		else:
			time = 0
		if time > timeLimit:
			detec.end_flag = False

	#顔が検出されたら顔識別を行う
	personId = FA.face_authentic()
	print(personId)
	#識別した顔の情報を取得
	if personId is not "":
		person_data = CF.person.get(setup.PERSON_GROUPID,personId)
		print("person_data:{}".format(person_data))

if __name__ == '__main__':
	main_roop()
```
実行
```
python3 main.py
```
カメラが動いていることを確認したあと、そのカメラに顔が映るようにしばらく見つめる
登録している人なら顔を識別して名前とか返してくれるはず
