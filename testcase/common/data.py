
import csv

#读取数据
def read_data(filename):
    # 读取文数据放到data列表
    with open('./input/data/' + filename, 'r') as f:
        data = list(csv.reader(f))
    return data[1]

