
;功能：保存文件
;参数：参数1为运行系统--7表示win7、10表示win10，参数2为另存的文件名称

Sleep(1000)
WinActivate ("网证通-业务运营平台(证书业务系统) - Internet Explorer", "")
Send("{F6}")
sleep(500)
Send("{TAB}")
sleep(500)
Send("{DOWN}")
sleep(500)
Send("A")

Sleep(2000)
ControlFocus("另存为", "", "Edit1")
WinWait("[CLASS:#32770]", "", 5)

If $CmdLine[1] == '10' Then
   ControlSetText("另存为", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] )
   Sleep(2000)
   ControlClick("另存为", "", "Button2")
Else
   ControlClick("另存为", "", "Edit1")
   Send("{7}")
   ControlSetText("另存为", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] )
   Sleep(2000)
   ControlClick("另存为", "", "Button1")
EndIf

Sleep(2000)
ControlFocus("确认另存为", "", "Button1")
ControlClick("确认另存为", "", "Button1")