
;���ܣ���ӡ
;����������1Ϊ���еĲ���ϵͳ--7��ʾwin7��10��ʾwin10������2Ϊ��ӡ�����ļ�����

ControlFocus("��ӡ", "", "Edit1")

WinWait("[CLASS:#32770]", "", 5)

ControlCommand("��ӡ","", "ComboBox1","SelectString", 'Microsoft XPS Document Writer')
Sleep(2000)

ControlClick("��ӡ", "", "Button10");
Sleep(2000)

If $CmdLine[1] == '7' Then
   ; win7
   ControlFocus("�ļ����Ϊ", "", "Edit1")
   ControlSetText("�ļ����Ϊ", "", "Edit1", @WorkingDir &"\" &$CmdLine[2])
   Sleep(1000)
   ControlClick("�ļ����Ϊ", "", "Button1")
Else
; win10
   ControlFocus("����ӡ������Ϊ", "", "Edit1")
   ControlSetText("����ӡ������Ϊ", "", "Edit1", @WorkingDir &"\" &$CmdLine[2])
   Sleep(1000)
   ControlClick("����ӡ������Ϊ", "", "Button2")
EndIf

Sleep(2000)
ControlFocus("ȷ�����Ϊ", "", "Button1")
ControlClick("ȷ�����Ϊ", "", "Button1")

