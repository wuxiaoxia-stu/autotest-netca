import requests


def cbbb2bpay(ip, orderNum, amount):
	'''
	企业银联支付（模拟功能）
	ip：如：https://192.168.0.59，
	orderNum：订单号，
	amount：金额
	'''
	data = {
		"MPOSID": "031778542",
		"ORDER_NUMBER": "20200413202536010000040140_1", #订单号
		"CUST_ID": "GD44000009233915201",
		"ACC_NO": "44050147100109172201",
		"ACC_NAME": "广州沐风信息科技有限公司",
		"AMOUNT": "400", #金额
		"STATUS": "2",
		"ORDER_STATUS": "1",
		"REMARK1": "remark1",
		"REMARK2": "remark2",
		"TRAN_FLAG": "N",
		"TRAN_TIME": "201908231623",
		"BRANCH_NAME": "广东省",
		"SIGNSTRING": "2cc606cf4df88b533ad2b8bee282a024a31bea93ae2862bec1217cafb3e714a3d7dc7791dfc3a91b28da4ad9ed530ed86f377aae8454753ebb3d4bd75a14f02ad487e86e1df771630810cda19f417df479e66a6eb27e7ea98ab27681e819c17df8d891e7a41911bd046d4acad46549279460df1e5939467d5c1f0b3dd6b15905",
		"CHECKOK": "1"
	}

	data["ORDER_NUMBER"] = orderNum
	data["AMOUNT"] = amount

	response = requests.post(ip+'/paySimulator/cbbb2bpay', data = data, verify = False)
	if "成功" in response.text:
		print("企业网银支付成功")

#cbbb2bpay("https://192.168.0.59", "20200526105628010000041686_1", "400") #企业银联支付
