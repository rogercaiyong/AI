import pandas as pd

dataset = \
"""色泽 根蒂 敲声 纹理 脐部 触感 密度 含糖率 好瓜
青绿 蜷缩 浊响 清晰 凹陷 硬滑 0.697 0.460 是
乌黑 蜷缩 沉闷 清晰 凹陷 硬滑 0.774 0.376 是
乌黑 蜷缩 浊响 清晰 凹陷 硬滑 0.634 0.264 是
青绿 蜷缩 沉闷 清晰 凹陷 硬滑 0.608 0.318 是
浅白 蜷缩 浊响 清晰 凹陷 硬滑 0.556 0.215 是
青绿 稍蜷 浊响 清晰 稍凹 软粘 0.403 0.237 是
乌黑 稍蜷 浊响 稍糊 稍凹 软粘 0.481 0.149 是
乌黑 稍蜷 浊响 清晰 稍凹 硬滑 0.437 0.211 是
乌黑 稍蜷 沉闷 稍糊 稍凹 硬滑 0.666 0.091 否
青绿 硬挺 清脆 清晰 平坦 软粘 0.243 0.267 否
浅白 硬挺 清脆 模糊 平坦 硬滑 0.245 0.057 否
浅白 蜷缩 浊响 模糊 平坦 软粘 0.343 0.099 否
青绿 稍蜷 浊响 稍糊 凹陷 硬滑 0.639 0.161 否
浅白 稍蜷 沉闷 稍糊 凹陷 硬滑 0.657 0.198 否
乌黑 稍蜷 浊响 清晰 稍凹 软粘 0.360 0.370 否
浅白 蜷缩 浊响 模糊 平坦 硬滑 0.593 0.042 否
青绿 蜷缩 沉闷 稍糊 稍凹 硬滑 0.719 0.103 否"""

# 将数据写入csv文件
file = r'machine_learning.csv'

with open(file, 'w', encoding='utf-8-sig') as f:
    dataset = dataset.replace(' ',',').split('\n')
    #print(dataset)
    f.write('编号,' + dataset[0] + '\n')
    #print(dataset[0])
    for i in range(len(dataset)-1):
        f.write(str(i+1) + ',' + dataset[i+1] + '\n')

# 向csv文件中加入一条新的数据（数据已给出）
inser_data = '18 青绿 硬挺 浊响 稍糊 平坦 硬滑 0.666 0.111 是'

with open(file, 'a', encoding='utf-8-sig') as f:
    f.write(inser_data.replace(' ',','))

# 查看全体数据
df = pd.read_csv(file)
print(df.head())

# 读取文件存储的数据
columns = []
datalist = []

with open(file, 'r', encoding='utf-8-sig') as f:
    dataset = f.readlines()
    columns = dataset[0].strip().split(',')
    for i in range(len(dataset)-1):
        datalist.append(dataset[i+1].strip().split(','))

# 验证数据信息是否相符
print(columns==['编号', '色泽', '根蒂', '敲声', '纹理', '脐部', '触感', '密度', '含糖率', '好瓜'])
print(datalist[-1]==['18', '青绿', '硬挺', '浊响', '稍糊', '平坦', '硬滑', '0.666', '0.111', '是'])

# 在所有数据中过滤出色泽='浅白'的数据
filter_colour = list(filter(lambda x: x[1] == '浅白' , datalist))
print(filter_colour)

# 在所有数据中过滤出密度大于0.5的数据
filter_density = list(filter(lambda x: float(x[-3]) > 0.5 , datalist))
print(filter_density)
