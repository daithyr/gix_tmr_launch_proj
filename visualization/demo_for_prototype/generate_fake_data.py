import json
import random
import numpy as np

data = []

# 生成主要区域数据 (信号强度以dBm为单位)
interval = 5  # 控制点的间隔
offset_rand = 3

for x in np.arange(5, 95, interval):  # 在X轴均匀取点
    for y in np.arange(5, 95, interval):  # 在Y轴均匀取点
        # 检查是否在左下角弱信号区域
        if x < (10 + random.uniform(-5, 5)) and y < (10 + random.uniform(-5, 5)):
            point = {
                "x": x + random.uniform(-offset_rand, offset_rand),
                "y": y + random.uniform(-offset_rand, offset_rand),
                "signal_strength": random.uniform(-110, -90)  # 非常弱信号范围
            }
        elif x < (40 + random.uniform(-5, 5)) and y < (30 + random.uniform(-5, 5)):
            point = {
                "x": x + random.uniform(-offset_rand, offset_rand),
                "y": y + random.uniform(-offset_rand, offset_rand),
                "signal_strength": random.uniform(-90, -70)  # 中等信号范围
            }
        else:
            point = {
                "x": x + random.uniform(-offset_rand, offset_rand),  # 缩小随机偏移以保持点的密集性
                "y": y + random.uniform(-offset_rand, offset_rand),
                "signal_strength": random.uniform(-70, -60)  # 非常强信号范围
            }
        data.append(point)

# 将数据保存为JSON文件
with open('../data/raw_fake_prototype.json', 'w') as f:
    json.dump(data, f, indent=4)
