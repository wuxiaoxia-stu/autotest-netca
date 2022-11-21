
;功能：登录
;参数：参数1为要选择登录的证书的序号，参数2为密码

ControlFocus("证书选择对话框", "","SysListView321")
WinWait("[CLASS:#32770]","",10)

Sleep(1000)
$num = $CmdLine[1]
If $num>1 Then
   Do
	  Send("{DOWN}")
	  $num=$num-1
   Until $num=1
EndIf

Sleep(1000)
ControlClick("证书选择对话框", "","Button1")

ControlFocus("密码输入对话框", "","Edit2")
WinWait("[CLASS:#32770]","",10)
Sleep(1000)
ControlSetText("密码输入对话框", "", "Edit2", $CmdLine[2])

ControlClick("密码输入对话框", "","Button1");

