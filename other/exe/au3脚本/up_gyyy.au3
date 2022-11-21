ControlFocus("选择要加载的文件", "", "Edit1")
WinWait("[CLASS:#32770]", "", 5)
; @WorkingDir 当前工作目录
Sleep(2000)
If $CmdLine[1] == '208' Then
	ControlSetText("选择要加载的文件", "", "Edit1", @WorkingDir &"\gyyy208.xls")
ENDIF
If $CmdLine[1] == '59' Then
	ControlSetText("选择要加载的文件", "", "Edit1", @WorkingDir &"\gyyy59.xls")
ENDIF
If $CmdLine[1] == '67' Then
	ControlSetText("选择要加载的文件", "", "Edit1", @WorkingDir &"\gyyy67.xls")
ENDIF
Sleep(2000)
ControlClick("选择要加载的文件", "", "Button1")