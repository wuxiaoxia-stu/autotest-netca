$picpath=@WorkingDir&"\1.png"
ControlFocus("选择要上载的文件", "","Edit1")
; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
; Set the File name text on the Edit field 先点击下拉框 防止无法输入图片地址
Sleep(1000)
ControlClick("选择要上载的文件", "","ComboBox3")
Sleep(1000)
ControlSetText("选择要上载的文件", "", "Edit1", $picpath)
Sleep(2000)
; Click on the Open button
ControlClick("选择要上载的文件", "","Button2");
