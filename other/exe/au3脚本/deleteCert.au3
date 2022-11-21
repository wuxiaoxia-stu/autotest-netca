
;功能：删除证书
;说明：密码固定是12345678

ControlFocus("删除证书对话框", "","Button3")
WinWait("[CLASS:#32770]","",10)
Sleep(1000)
ControlClick("删除证书对话框", "","Button3")
ControlClick("删除证书对话框", "","Button1")
Sleep(1000)
ControlFocus("删除证书", "","Button1")
WinWait("[CLASS:#32770]","",10)
ControlClick("删除证书", "","Button1")

Sleep(1000)
ControlFocus("密码输入对话框", "","Edit2")
WinWait("[CLASS:#32770]","",10)
ControlSetText("密码输入对话框", "", "Edit2", "12345678");输入密码签名
Sleep(1000)
ControlClick("密码输入对话框", "","Button1");
Sleep(1000)
ControlFocus("删除证书", "","Button1")
WinWait ( "删除证书","删除成功",10)
ControlClick("删除证书", "","Button1")
Sleep(1000)
ControlClick("删除证书对话框", "","Button2")

