

;功能：上传附件
;参数：1、操作系统-7或者10，2、附件名称，3、是否需要输密码签名--1用或者0不用
;说明：该窗口类型为【选择上传文件】类型的，比如上传业务附件

Sleep(2000)
If $CmdLine[1] == '7' Then ;win7
   ControlClick("网证通", "","MacromediaFlashPlayerActiveX1");点击-选择上传文件
   Sleep(2000)
   ControlFocus("选择要上载的文件", "", "Edit1")
   WinWait("[CLASS:#32770]", "", 5)
   ControlClick("选择要上载的文件", "","ComboBox3");点击下拉框-防止无法输入图片地址
   ControlSetText("选择要上载的文件", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] ) ;输入文件名称
   Sleep(2000)
   ControlClick("选择要上载的文件", "", "Button2");点击打开
   if $CmdLine[3] == '1' Then ;需要输密码
	  ControlFocus("密码输入对话框", "","Edit2")
	  WinWait("[CLASS:#32770]","",10)
	  Sleep(2000)
	  ControlSetText("密码输入对话框", "", "Edit2", "12345678")
	  Sleep(1000)
	  ControlClick("密码输入对话框", "","Button1");
	  Sleep(2000)
   EndIf
Else ;win10
   ControlFocus("打开", "", "Edit1")
   WinWait("[CLASS:#32770]", "", 5)
   ControlSetText("打开", "", "Edit1", @WorkingDir &"\" &$CmdLine[2] );输入文件名称
   Sleep(2000)
   ControlClick("打开", "", "Button1");点击打开
   if $CmdLine[3] == '1' Then ;需要输密码
	  ControlFocus("密码输入对话框", "","Edit2")
	  WinWait("[CLASS:#32770]","",10)
	  Sleep(2000)
	  ControlSetText("密码输入对话框", "", "Edit2", "12345678")
	  Sleep(1000)
	  ControlClick("密码输入对话框", "","Button1");
	  Sleep(2000)
   EndIf
EndIf
