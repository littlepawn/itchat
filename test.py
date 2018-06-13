import itchat, time
import os
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # msg.user.send('%s: %s' % (msg.type, msg.text))
    list=os.popen('php /var/www/html/index.php').readlines() #这个返回值是一个list
    msg.user.send('%s: ' % ("".join(list)))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):
    # msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
    list=os.popen('php /var/www/html/index.php').readlines()
    if msg['IsAt']:
        # itchat.send(u'@%s\u2005I received: %s '%(msg['ActualNickName'],msg['Content']),msg['FromUserName'])
        itchat.send(u'@%s\u2005I received: %s '%(msg['ActualNickName'],"".join(list)),msg['FromUserName'])

def loginCallback():
    print("***登录成功***")


def exitCallback():
    print("***已退出***")

itchat.auto_login(enableCmdQR=2,hotReload=True,loginCallback=loginCallback,exitCallback=exitCallback)
itchat.run(True)

