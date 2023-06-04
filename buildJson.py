"""
5/25 : 22012081 이윤상 json파일에서 이미지 추출하는 코드 (파일명 : buildJson.py)
아래 코드는 thenounproject에서 제공하는 기본 request 코드임

https://thenounproject.com/ >> google (22012081)로 로그인하면 됨.

key = 10baf80743224b4d9c99efac2cf5e750
Secret Key = 93e81703890449c3a6d5e3d65a912c25


import requests
from requests_oauthlib import OAuth1

auth = OAuth1("your-api-key", "your-api-secret")
endpoint = "https://api.thenounproject.com/v2/icon/1"

response = requests.get(endpoint, auth=auth)
print(response.content)

"""

import requests
from requests_oauthlib import OAuth1
import json
import urllib.request
from PIL import Image
import matplotlib.pyplot as plt
import cv2

auth = OAuth1("10baf80743224b4d9c99efac2cf5e750",
              "93e81703890449c3a6d5e3d65a912c25")
endPoint = "https://api.thenounproject.com/v2/icon/351"

response = requests.get(endPoint, auth=auth)
# print(response.content)

json_data = json.loads(response.content)

print(json_data)


# thumbnail_url과 term 추출
thumbnail_url = json_data['icon']['thumbnail_url']
term = json_data['icon']['term']

print(f"thumbnail_url: {thumbnail_url}")
print(f"term: {term}")

filename = f"{term}.png"  # 파일 확장자는 이미지 종류에 맞게 설정해야함. 일단 png로. (alpha channel 존재하게끔)

try:
    urllib.request.urlretrieve(thumbnail_url, filename)
    print(f"이미지 다운로드 완료: {filename}")
except urllib.error.URLError:
    print("이미지를 다운로드할 수 없습니다.")
    pass


image = Image.open(filename)
image = image.convert("RGBA")
background = Image.new("RGBA", image.size, (255, 255, 255))
image = Image.alpha_composite(background, image)
image.save("./ImageFolder/" + filename)

"""
buildJson.py 코드에서는 파일을 이름으로 저장하는 역할만 수행함.
이를 반복문을 통해 데탑에서 저장해서 dataset 폴더에 저장하는 코드를
추가로 작성할 것. (3차 수행 내용)

tag관련해서는 response.content 내에서 tags={} 내의 데이터를 어떻게 관리하고 저장할진 생각해봐야됨

그리고 병민님에게 줄 tag 목록을 저장하기 위해서는 추가로 리스트 형식으로 저장해서 반복문 다 돈 다음 txt파일로 저장하든지 하자

5/25 오후 11시 2차 완료

"""



#plt.imshow(image, cmap=plt.cm.gray)
#plt.show()






"""
img = Image.open(filename)

alpha_channel = img[:, :, 3]
img[alpha_channel == 0] = [255, 255, 255, 255]


# 이미지를 함께 보여주기 위한 subplot 생성
fig, axes = plt.subplots(1, 2)

# 첫 번째 이미지 출력
axes[0].imshow(image1)
axes[0].set_title('Image 1')

# 두 번째 이미지 출력
axes[1].imshow(image2)
axes[1].set_title('Image 2')

# 이미지 사이 간격 조정
plt.tight_layout()

# 이미지 보여주기
plt.show()
"""