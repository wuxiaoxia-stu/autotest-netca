

;功能：上传文件
;参数：1、文件名称
;说明：该窗口类型为【浏览】类型的，比如批量导入和证书上传，且win7和win10窗口一样、不用细分

ControlFocus("选择要加载的文件", "", "Edit1")
WinWait("[CLASS:#32770]", "", 5)
ControlSetText("选择要加载的文件", "", "Edit1", @WorkingDir &"\" &$CmdLine[1] );输入文件名称
Sleep(2000)
ControlClick("选择要加载的文件", "", "Button1");点打开
