
"""
/**
 * @author [Lee-Yoon-Sang]
 * @email [22012081@yu.ac.kr]
 * @create date 2023-06-04 14:59:13
 * @modify date 2023-06-04 14:59:13
 * @desc [Download Icons from TheNounProjects]
 * @url : https://thenounproject.com/
 */
"""
import requests
from requests_oauthlib import OAuth1
import json
import urllib.request
import matplotlib.pyplot as plt
import cv2
from PIL import Image

# Image 정제 후 저장 ()
def getImageData(json_File , strNum):
    if 'icon' in json_File and 'thumbnail_url' in json_File['icon']:
        thumbnail_url = json_File['icon']['thumbnail_url']
        term = json_File['icon']['term']
        fileName = f"{term}.png"
    else:
        thumbnail_url = None
        fileName = None
        pass
    
    
    
    try:
        if thumbnail_url != None and fileName != None:
            urllib.request.urlretrieve(thumbnail_url, "./ImageFolder/" + fileName)
            print(strNum + "번째 이미지 다운 성공")
    except urllib.error.URLError:
        print(strNum + "번째 이미지를 다운로드할 수 없습니다.")
        pass
    if thumbnail_url != None and fileName != None:
        image = Image.open("./ImageFolder/" + fileName)
        image = image.convert("RGBA")
        background = Image.new("RGBA", image.size, (255, 255, 255))
        image = Image.alpha_composite(background, image)
        image.save("./ImageFolder/" + fileName)
        pass




auth = OAuth1("10baf80743224b4d9c99efac2cf5e750",
              "93e81703890449c3a6d5e3d65a912c25")

#endPoint 에서 icon/ 뒤의 숫자를 1부터 증가시켜서 다운하는 것 같음.

original = "https://api.thenounproject.com/v2/icon/"

"""
for i in range(1,5):
    sentence = original + str(i)
    print(sentence)
    pass
"""



for i in range(4000, 4500):
    endPoint = original + str(i)
    response = requests.get(endPoint, auth=auth)
    getImageData(json.loads(response.content), str(i))
    pass
