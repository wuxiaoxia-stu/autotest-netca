
;���ܣ�ɾ��֤��
;˵��������̶���12345678

ControlFocus("ɾ��֤��Ի���", "","Button3")
WinWait("[CLASS:#32770]","",10)
Sleep(1000)
ControlClick("ɾ��֤��Ի���", "","Button3")
ControlClick("ɾ��֤��Ի���", "","Button1")
Sleep(1000)
ControlFocus("ɾ��֤��", "","Button1")
WinWait("[CLASS:#32770]","",10)
ControlClick("ɾ��֤��", "","Button1")

Sleep(1000)
ControlFocus("��������Ի���", "","Edit2")
WinWait("[CLASS:#32770]","",10)
ControlSetText("��������Ի���", "", "Edit2", "12345678");��������ǩ��
Sleep(1000)
ControlClick("��������Ի���", "","Button1");
Sleep(1000)
ControlFocus("ɾ��֤��", "","Button1")
WinWait ( "ɾ��֤��","ɾ���ɹ�",10)
ControlClick("ɾ��֤��", "","Button1")
Sleep(1000)
ControlClick("ɾ��֤��Ի���", "","Button2")

