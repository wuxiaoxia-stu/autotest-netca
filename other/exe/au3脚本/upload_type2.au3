

;���ܣ��ϴ�����
;������1������ϵͳ-7����10��2���������ƣ�3���Ƿ���Ҫ������ǩ��--1�û���0����
;˵�����ô�������Ϊ��ѡ���ϴ��ļ������͵ģ������ϴ�ҵ�񸽼�

Sleep(2000)
If $CmdLine[1] == '7' Then ;win7
   ControlClick("��֤ͨ", "","MacromediaFlashPlayerActiveX1");���-ѡ���ϴ��ļ�
   Sleep(2000)
   ControlFocus("ѡ��Ҫ���ص��ļ�", "", "Edit1")
   WinWait("[CLASS:#32770]", "", 5)
   ControlClick("ѡ��Ҫ���ص��ļ�", "","ComboBox3");���������-��ֹ�޷�����ͼƬ��ַ
   ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] ) ;�����ļ�����
   Sleep(2000)
   ControlClick("ѡ��Ҫ���ص��ļ�", "", "Button2");�����
   if $CmdLine[3] == '1' Then ;��Ҫ������
	  ControlFocus("��������Ի���", "","Edit2")
	  WinWait("[CLASS:#32770]","",10)
	  Sleep(2000)
	  ControlSetText("��������Ի���", "", "Edit2", "12345678")
	  Sleep(1000)
	  ControlClick("��������Ի���", "","Button1");
	  Sleep(2000)
   EndIf
Else ;win10
   ControlFocus("��", "", "Edit1")
   WinWait("[CLASS:#32770]", "", 5)
   ControlSetText("��", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] );�����ļ�����
   Sleep(2000)
   ControlClick("��", "", "Button1");�����
   if $CmdLine[3] == '1' Then ;��Ҫ������
	  ControlFocus("��������Ի���", "","Edit2")
	  WinWait("[CLASS:#32770]","",10)
	  Sleep(2000)
	  ControlSetText("��������Ի���", "", "Edit2", "12345678")
	  Sleep(1000)
	  ControlClick("��������Ի���", "","Button1");
	  Sleep(2000)
   EndIf
EndIf
