
;���ܣ������ļ�
;����������1Ϊ����ϵͳ--7��ʾwin7��10��ʾwin10������2Ϊ�����ļ�����

Sleep(1000)
WinActivate ("��֤ͨ-ҵ����Ӫƽ̨(֤��ҵ��ϵͳ) - Internet Explorer", "")
Send("{F6}")
sleep(500)
Send("{TAB}")
sleep(500)
Send("{DOWN}")
sleep(500)
Send("A")

Sleep(2000)
ControlFocus("���Ϊ", "", "Edit1")
WinWait("[CLASS:#32770]", "", 5)

If $CmdLine[1] == '10' Then
   ControlSetText("���Ϊ", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] )
   Sleep(2000)
   ControlClick("���Ϊ", "", "Button2")
Else
   ControlClick("���Ϊ", "", "Edit1")
   Send("{7}")
   ControlSetText("���Ϊ", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] )
   Sleep(2000)
   ControlClick("���Ϊ", "", "Button1")
EndIf

Sleep(2000)
ControlFocus("ȷ�����Ϊ", "", "Button1")
ControlClick("ȷ�����Ϊ", "", "Button1")