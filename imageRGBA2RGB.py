"""
/**
 * @author [:ee-Yoon-Sang]
 * @email [22012081.yu.ac.kr]
 * @create date 2023-06-18 21:15:55
 * @modify date 2023-06-18 21:15:55
 * @desc [convert RGBA image to RGB]
 */
"""
from PIL import Image
import os

# imageModifyTo224.py의 func 그대로 가져옴
def get_image_channels(fileName): 
    img = Image.open(fileName)
    channels = img.mode
    return channels

def convert_rgba_to_rgb(image_path):
    # RGBA 이미지 열기
    rgba_image = Image.open(image_path).convert("RGBA")
    print("변환 전 channel 수 : " + str(get_image_channels(image_path)))
    
    # RGBA 이미지에서 RGB로 변환
    rgb_image = Image.new("RGB", rgba_image.size, (255, 255, 255))
    rgb_image.paste(rgba_image, mask=rgba_image.split()[3])  # 알파 채널을 마스크로 사용
    
    # 이미지 저장
    output_path = os.path.splitext(image_path)[0] + ".jpg"  # 원본 파일 이름에 "_rgb" 접미사 추가
    rgb_image.save(output_path)

    print("변환 후 channel 수 : " + str(get_image_channels(output_path)))

    # 이미지 출력
    rgb_image.show()

# 변환할 이미지 경로 지정
image_path = "./jpgImage(Transform)/3D Glasses.jpg"

print("rgb로 변환 후 이미지의 channel 수 : " + str(get_image_channels(image_path)))

# RGBA 이미지를 RGB로 변환하여 출력
#convert_rgba_to_rgb(image_path)
