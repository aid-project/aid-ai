"""
/**
 * @author [:ee-Yoon-Sang]
 * @email [22012081.yu.ac.kr]
 * @create date 2023-06-18 21:49:08
 * @modify date 2023-06-18 21:49:08
 * @desc [VGG16모델을 사용하여 특징을 추출하고 .npz로 저장하는 코드]
 */
"""
import os
import numpy as np
import h5py
from tensorflow.keras.utils import load_img
from tensorflow.keras.utils import img_to_array
from keras.applications.vgg16 import VGG16, preprocess_input
from keras.models import Model
from scipy.spatial.distance import cosine

# 이미지 디렉토리 경로
image_directory = "./jpgImage(Transform)/"

# 이미지 파일 목록을 가져옴
image_files = os.listdir(image_directory)

# VGG16 모델 불러오기
vgg16 = VGG16(weights='imagenet', include_top=False)
model = Model(inputs=vgg16.input, outputs=vgg16.get_layer('block4_pool').output)  # 특성 추출할 레이어 설정

#model.save("VGG16_model.h5") # 저장 후 주석처리할 것.

# 이미지 특성 추출 함수
def extract_features(image_path):
    img = load_img(image_path)  # 이미지 로드
    img = img_to_array(img)  # 이미지를 배열로 변환
    img = np.expand_dims(img, axis=0)  # 배치 차원 추가
    img = preprocess_input(img)  # 이미지 전처리
    features = model.predict(img)  # 특성 추출
    print(type(features))
    return features.flatten()  # 1차원 벡터로 변환

# 이미지 특성 추출
# features_list = []
# for image_file in image_files:
#     image_path = os.path.join(image_directory, image_file)
#     features = extract_features(image_path)
#     features_list.append(features)

# # 특성 벡터를 Numpy 배열로 변환
# features_array = np.array(features_list)

#feature_file = "./features.npy"
#np.save(feature_file, feature_array)

new_image_path = "./Wine.jpg"

# new_features = extract_features(new_image_path)

# similarities = []
# for features in features_array:
#     similarity = 1 - cosine(features, new_features)  # 코사인 유사도 계산
#     similarities.append(similarity)

# # 유사도가 높은 순으로 정렬하여 상위 5개 인덱스 가져오기
# top_indices = np.argsort(similarities)[::-1][:5]

# # 유사도가 높은 이미지 파일명 출력
# for index in top_indices:
#     print(image_files[index])

fea_li = []
fe = extract_features(new_image_path)
fea_li.append(fe)
print(fea_li)
   
unique_elements, counts = np.unique(fea_li, return_counts=True)

# 개수 출력
for element, count in zip(unique_elements, counts):
    print(f"{element}: {count}")