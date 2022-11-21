
;功能：选择证书
;说明：目前固定是选第2张证书

ControlFocus("证书选择对话框", "","SysListView32")
WinWait("[CLASS:#32770]","",10)

Sleep(1000)
Send("{DOWN}")

Sleep(1000)
ControlClick("证书选择对话框", "","Button1")