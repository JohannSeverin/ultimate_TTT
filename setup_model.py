from lightgbm import LGBMClassifier
import dill


model = LGBMClassifier(device = 'gpu', max_depth = 5)

model.booster_.save_model('model.txt')
#load from model:
