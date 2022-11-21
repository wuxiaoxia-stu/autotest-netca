
;功能：打印
;参数：参数1为运行的操作系统--7表示win7，10表示win10，参数2为打印出的文件名称

ControlFocus("打印", "", "Edit1")

WinWait("[CLASS:#32770]", "", 5)

ControlCommand("打印","", "ComboBox1","SelectString", 'Microsoft XPS Document Writer')
Sleep(2000)

ControlClick("打印", "", "Button10");
Sleep(2000)

If $CmdLine[1] == '7' Then
   ; win7
   ControlFocus("文件另存为", "", "Edit1")
   ControlSetText("文件另存为", "", "Edit1", @WorkingDir &"\" &$CmdLine[2])
   Sleep(1000)
   ControlClick("文件另存为", "", "Button1")
Else
; win10
   ControlFocus("将打印输出另存为", "", "Edit1")
   ControlSetText("将打印输出另存为", "", "Edit1", @WorkingDir &"\" &$CmdLine[2])
   Sleep(1000)
   ControlClick("将打印输出另存为", "", "Button2")
EndIf

Sleep(2000)
ControlFocus("确认另存为", "", "Button1")
ControlClick("确认另存为", "", "Button1")

