import platform
import sys
import ctypes
from ctypes import *

def _load_dll():
	dll=None
	sys_str=platform.system()
	if sys_str=="Windows" :
		dll=windll.LoadLibrary("NETCA_CRYPTO.dll")
	elif sys_str=="Linux" :
		dll=cdll.LoadLibrary("libnetca_crypto.so")
	else:
		pass

	if dll==None :
		sys.exit(-1)
	return dll

def GetDeviceNum():
	Devicenum = 0;
	handle = _load_dll()
	NETCA_PKI_DEVICE_TYPE_ANY = -1
	NETCA_PKI_DEVICE_FLAG_SILENT = 1
	handle.NetcaPKICryptoGetAllDevices.restype = ctypes.c_uint64
	hSet = handle.NetcaPKICryptoGetAllDevices(NETCA_PKI_DEVICE_TYPE_ANY, NETCA_PKI_DEVICE_FLAG_SILENT)
	if hSet==None :
		sys.exit(-1)
	handle.NetcaPKICryptoGetDeviceCount.argtypes = [ctypes.c_uint64]
	count = handle.NetcaPKICryptoGetDeviceCount(hSet)
	for i in range(0, count) :
		handle.NetcaPKICryptoGetDevice.argtypes = [ctypes.c_ulonglong,ctypes.c_uint]
		handle.NetcaPKICryptoGetDevice.restype = ctypes.c_ulonglong
		hDevice = handle.NetcaPKICryptoGetDevice(hSet, i)
		if hDevice==None :
			sys.exit(-1)
		handle.NetcaPKICryptoGetType.argtypes = [ctypes.c_ulonglong]
		type = handle.NetcaPKICryptoGetType(hDevice)
		if type == -1 :
			sys.exit(-1)
		handle.NetcaPKICryptoGetKeypairCount.argtypes = [ctypes.c_ulonglong]
		handle.NetcaPKICryptoGetKeypairCount.restype = ctypes.c_uint
		keypairCount = handle.NetcaPKICryptoGetKeypairCount(hDevice)
		if keypairCount == -1 :
			sys.exit(-1)
		AllCertCount = 0
		for j in range(0, keypairCount) :
			handle.NetcaPKICryptoGetKeypair.argtypes = [ctypes.c_ulonglong,ctypes.c_uint]
			handle.NetcaPKICryptoGetKeypair.restype = ctypes.c_ulonglong
			hKeypair = handle.NetcaPKICryptoGetKeypair(hDevice, j)
			if hKeypair == None:
				sys.exit(-1)
			handle.NetcaPKICryptoGetCertificateCount.argtypes = [ctypes.c_ulonglong]
			handle.NetcaPKICryptoGetCertificateCount.restype = ctypes.c_uint
			certCount = handle.NetcaPKICryptoGetCertificateCount(hKeypair)
			if certCount == -1 :
				sys.exit(-1)
			AllCertCount+=certCount
		if AllCertCount > 0 :
			Devicenum = type
	return 	Devicenum

