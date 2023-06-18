import os
from PIL import Image

"""
/**
 * @author [:ee-Yoon-Sang]
 * @email [22012081.yu.ac.kr]
 * @create date 2023-06-18 21:10:35
 * @modify date 2023-06-18 21:10:35
 * @desc [resize image 200 to 224]
 */
"""




def resize_image(image_path, target_size):
    img = Image.open(image_path)
    img = img.resize(target_size)
    img.save(image_path)
    pass

image_directory = "./ImageFolder/"
i = 0


"""
for image_file in os.listdir(image_directory):
    image_path = os.path.join(image_directory, image_file)
    resize_image(image_path, (224,224))
    print(str(i) + "번째 이미지 변환 완료.")
    i = i + 1
    pass
"""

def convert_rgba_to_rgb(image_path):
    # RGBA 이미지 열기
    rgba_image = Image.open(image_path).convert("RGBA")
    
    # RGBA 이미지에서 RGB로 변환
    rgb_image = Image.new("RGB", rgba_image.size, (255, 255, 255))
    rgb_image.paste(rgba_image, mask=rgba_image.split()[3])  # 알파 채널을 마스크로 사용
    
    # 이미지 저장
    #print(image_path)
    #print(os.path.splitext(image_path)[0][14:])
    output_path = "./jpgImage(Transform)/" + os.path.splitext(image_path)[0][14:] + ".jpg"  # 원본 파일 이름에 "_rgb" 접미사 추가
    rgb_image.save(output_path)

    # 이미지 출력
    #rgb_image.show()
    pass

for image_file in os.listdir(image_directory):
    image_path = os.path.join(image_directory, image_file)
    convert_rgba_to_rgb(image_path)
    print(str(i) + "번째 이미지 rgb로 변환 완료")
    i = i + 1
    pass



"""
def get_image_channels(fileName):
    img = Image.open(fileName)
    channels = img.mode
    return channels

print("channel 수 : " + str(get_image_channels("./ImageFolder/Add Folder.png")))
"""



