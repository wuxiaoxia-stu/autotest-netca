
;���ܣ�ѡ��֤��
;˵����Ŀǰ�̶���ѡ��2��֤��

ControlFocus("֤��ѡ��Ի���", "","SysListView32")
WinWait("[CLASS:#32770]","",10)

Sleep(1000)
Send("{DOWN}")

Sleep(1000)
ControlClick("֤��ѡ��Ի���", "","Button1")