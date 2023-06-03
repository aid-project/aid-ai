"""
외부 사이트에서 GAN 모델 혹은 icon generator model 가져와서 수정하는 python code

@author: 22012081 이윤상

작업 순서 및 우선순위
1. Find free model can generate icons or image.
2. Decide input, output shape of images.
3. Modify model(.h5)
4. Insert Test data and carry out additional-fine tuning.

"""

import coremltools
import tensorflow
import numpy

print("um")
mlmodel = coremltools.utils.load_spec('./upconv_7_photo_scale2.mlmodel')
print("umm")
tfmodel = coremltools.converters.convert(mlmodel, 'tensorflow')
print("u,mmm")
tfmodel.summary()
tfmodel.save('tfmodel')