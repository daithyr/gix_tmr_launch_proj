import json
import random
import numpy as np

data = []

# 生成主要区域数据 (信号强度0.8-1.0)
interval = 5 # 控制点的间隔
offset_rand = 3

for x in np.arange(5, 95, interval):  # 0到8均匀取点
    for y in np.arange(5, 95, interval):  # 0到6均匀取点
        # 检查是否在左下角区域
        if x < (20 + random.uniform(-5, 5)) and y < (60 + random.uniform(-5, 5)):
            point = {
                "x": x + random.uniform(-offset_rand, offset_rand),
                "y": y + random.uniform(-offset_rand, offset_rand),
                "signal_strength": random.uniform(0.2, 0.6)
            }
        else:
            point = {
                "x": x + random.uniform(-offset_rand, offset_rand),  # 缩小随机偏移以保持点的密集性
                "y": y + random.uniform(-offset_rand, offset_rand),
                "signal_strength": random.uniform(0.9, 1)
            }
        data.append(point)


with open('../data/raw_fake_prototype.json', 'w') as f:
    json.dump(data, f, indent=4)