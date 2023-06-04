import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

# VGG16 모델 불러오기
model = VGG16(weights='imagenet', include_top=False)

def extract_features(image_path):
    img = image.load_img(image_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = model.predict(x)
    features = features.flatten()
    return features


# Dataset 이미지 경로 리스트
dataset_images = ["dataset/image1.jpg", "dataset/image2.jpg", "dataset/image3.jpg"]

# 새로 입력한 이미지 경로
new_image_path = "1.jpg"

# Dataset 이미지의 특징 추출
dataset_features = []
for image_path in dataset_images:
    features = extract_features(image_path)
    dataset_features.append(features)

# 새로 입력한 이미지의 특징 추출
new_image_features = extract_features(new_image_path)

# 코사인 유사도 계산
#similarities = cosine_similarity([new_image_features], dataset_features)
similarities = []

for dataset_feature in dataset_features:
    similarity = cosine_similarity(new_image_features, dataset_feature)
    similarities.append(similarity)

top_similar_indices = np.argsort(similarities)[-2:]
top_similar_images = [dataset_images[i] for i in top_similar_indices]

# 2개 저장 완료.