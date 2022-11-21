
import configparser

#读取配置
def read_config(section, key):
	config = configparser.ConfigParser()
	config.read("./input/config/config.ini")
	return config.get(section, key) #获取指定节点下key的值

