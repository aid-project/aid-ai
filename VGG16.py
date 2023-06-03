import tensorflow as tf
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from sklearn.metrics.pairwise import cosine_similarity

# VGG16 모델 불러오기
model = VGG16(weights='imagenet', include_top=False)
