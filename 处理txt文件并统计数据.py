import chardet
import re
import pandas as pd

#读取txt文件并进行简单的处理
def read_time_machine():
    with open(r"/workspaces/text-processing/统计作业数据1 (1).txt", 'rb') as f:
        data = f.read()
        encoding = chardet.detect(data)['encoding']

    with open(r"/workspaces/text-processing/统计作业数据1 (1).txt", 'r', encoding=encoding) as f:
        lines = f.readlines()
    return [re.sub('[^A-Za-z]+', ' ', line).strip().lower() for line in lines]

lines = read_time_machine()#返回读取后的数据

def tokenize(lines, token='word'):
    """将文本行拆分为单词或字符词元"""
    if token == 'word':
        return [line.split() for line in lines]
    elif token == 'char':
        return [list(line) for line in lines]
    else:
        print('错误：未知词元类型：' + token)

tokens = tokenize(lines)

# 使用列表推导式将嵌套的 tokens 列表展开成一个单一的列表
flattened_tokens = [token for line_tokens in tokens for token in line_tokens]

def tongji(step,my_list):
  data = {}
  num = 0
  for item in my_list:
    if len(item)<step:
      continue
    for i in range(0,len(item)-step):
      num+=1
      key = item[i:i+step]
      if key in data:
        data[key] += 1
      else:
        data[key] = 1
    data["num"] = num
  return data

#将数据储存在合适的数据结构中
Series_1 = pd.Series(tongji(1,flattened_tokens)).sort_values()
print(Series_1)

Series_2 = pd.Series(Series_1.values/Series_1["num"],Series_1.index)
print(Series_2)

data = pd.DataFrame({"pinshu":Series_1,"pinlv":Series_2})
print(data)
