import winreg

def ChangeRegedit(keynum,oper):
    #OpenKey中加上winreg.KEY_ALL_ACCESS用于获取注册表权限
    if keynum == 7:
        #文鼎创
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\NETCA\PKI\Devices\NETCAKeyMwES", 0,winreg.KEY_ALL_ACCESS)
    elif keynum == 47:
        #飞天3000GM
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Wow6432Node\NETCA\PKI\Devices\NETCAKeyFT3000GM", 0,winreg.KEY_ALL_ACCESS)
    else:
        #软设备
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\WOW6432Node\NETCA\PKI\Devices\NetcaKeySoftCert", 0,winreg.KEY_ALL_ACCESS)
    value,type = winreg.QueryValueEx(key,"dllpath")
    if oper is "put":
        winreg.SetValueEx(key,"dllpath", 0, 1, value.replace("dll1","dll"))
    if oper is "pull":
        winreg.SetValueEx(key,"dllpath",0,1,value.replace("dll", "dll1"))