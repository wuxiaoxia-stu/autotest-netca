$picpath=@WorkingDir&"\1.png"
ControlFocus("ѡ��Ҫ���ص��ļ�", "","Edit1")
; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
; Set the File name text on the Edit field �ȵ�������� ��ֹ�޷�����ͼƬ��ַ
Sleep(1000)
ControlClick("ѡ��Ҫ���ص��ļ�", "","ComboBox3")
Sleep(1000)
ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", $picpath)
Sleep(2000)
; Click on the Open button
ControlClick("ѡ��Ҫ���ص��ļ�", "","Button2");
;��������ǩ��
ControlFocus("��������Ի���", "","Edit2")
WinWait("[CLASS:#32770]","",10)
Sleep(2000)
ControlSetText("��������Ի���", "", "Edit2", "12345678")
Sleep(1000)
ControlClick("��������Ի���", "","Button1");
Sleep(2000)