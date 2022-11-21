$picpath=@WorkingDir&"\3.jpg"
;上传附件1
ControlClick("网证通", "","MacromediaFlashPlayerActiveX1");
;ControlFocus("title","text",controlID) Edit1=Edit instance 1
ControlFocus("选择要上载的文件", "","Edit1")


; Wait 10 seconds for the Upload window to appear
  WinWait("[CLASS:#32770]","",10)


; Set the File name text on the Edit field

  ControlSetText("选择要上载的文件", "", "Edit1", $picpath)

  Sleep(2000)

; Click on the Open button

  ControlClick("选择要上载的文件", "","Button2");
