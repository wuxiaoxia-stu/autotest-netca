$picpath=@WorkingDir&"\3.jpg"
;�ϴ�����1
ControlClick("��֤ͨ", "","MacromediaFlashPlayerActiveX1");
;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("ѡ��Ҫ���ص��ļ�", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("ѡ��Ҫ���ص��ļ�", "", "Edit1", $picpath)

  Sleep(2000)

; Click on the Open button

  ControlClick("ѡ��Ҫ���ص��ļ�", "","Button2");
