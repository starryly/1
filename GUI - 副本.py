import torch

# 加载模型
w=torch.load('E:/91019/bishe/ruanjian/modelll/yolov5-1/runs/train/exp5/weights/best.pt')

#打印所有name
print(w.get('model').names)

# 定义一个将英文单词映射到中文单词的字典
word_map = {
    'crosswalk': 'c',
    'limit-speed': 'l',
    'STOP': 'S',
    'NO Parking': 'NP',
    'Prohibition sign': 'P',
    'Warning sign': 'W',
    'Descriptive sign': 'D1',
    'Directional sign': 'D2',
    'Traffic light': 'T'
    # 根据需要添加更多映射
}

# 遍历列表，将每个英文单词替换为其中文对应词
for i in range(len(w.get('model').names)):
    if w.get('model').names[i] in word_map:
        w.get('model').names[i] = word_map[w.get('model').names[i]]

# 打印替换后的列表
print('替换后')
print(w.get('model').names)
#保存替换后的模型
torch.save(w,'E:/91019/bishe/ruanjian/modelll/yolov5-1/runs/train/exp5/weights/t.pt')

