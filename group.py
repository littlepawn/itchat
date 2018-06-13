import itchat
import time

itchat.auto_login(enableCmdQR=2,hotReload=True)
group=itchat.search_chatrooms(name='马克老师你别傻了')
# print(group[0]['UserName'])

while True:
    time_now = time.strftime('%H%M',time.localtime(time.time()))
    if ( int(time_now) == 1130 or int(time_now) == 1625 ):
        msg_body='点饭了'
        itchat.send_msg(msg_body,toUserName=group[0]['UserName'])
        time.sleep(60)
