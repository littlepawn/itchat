import itchat
import time

itchat.auto_login(enableCmdQR=2,hotReload=True)
dahao=itchat.search_friends(name='dahao')
# print(dahao[0]['UserName'])
while True:
    time_now = time.strftime('%H%M',time.localtime(time.time()))
    if int(time_now) == 1130:
        msg_body='点饭了'
        itchat.send_msg(msg_body,toUserName=dahao[0]['UserName'])
        # itchat.send_msg(msg_body, toUserName='filehelper')
        time.sleep(60)
