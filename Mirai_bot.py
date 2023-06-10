# -*- coding : utf-8-*-
from os import getcwd
from PIL import Image
from cnocr import CnOcr
from xpinyin import Pinyin
from random import randint
from threading import Thread
from json import loads, dumps
from re import compile, search
from requests import get, post
from rich.console import Console
from unicodedata import normalize
from time import localtime, strftime, time, sleep
from websocket import WebSocket, send, recv
from psutil import cpu_percent, virtual_memory

print('初始化中.....')

拼音对象 = Pinyin()

console = Console(color_system='auto', highlighter=None, style=None)
文字识别对象 = CnOcr(model_name='densenet_lite_136-gru')
服务器对象 = WebSocket()
post('http://localhost:23323/verify')
服务器对象.connect('ws://localhost:23423/all?verifyKey=INITKEYsV4Mnulq&qq=2303798671')

初始地址 = '{}/附属/'.format(getcwd().replace('\\', '/'))
工具箱地址 = 初始地址 + 'hwid.txt'
小号地址 = 初始地址 + 'Accounts.txt'
违禁词地址 = 初始地址 + 'bw.txt'
pixiv地址 = 初始地址 + 'pixiv.png'
消息存储地址 = 初始地址 + 'msg_pull.txt'
水影地址 = 初始地址 + 'liquid_hwid.txt'
配置地址 = 初始地址 + 'Robot.config'
卡密地址 = 初始地址 + 'card_pwd.txt'
cancir卡密地址 = 初始地址 + 'cancir_cards.txt'
cancir记录地址 = 初始地址 + 'cancir_log.txt'
卡密存储地址 = 初始地址 + 'cards.txt'
轰炸授权地址 = 初始地址 + 'boom.txt'
商店收款码地址 = 初始地址 + '商店付款码.jpg'
商店内容地址 = 初始地址 + '商店内容.txt'
http接口 = 'http://localhost:23323/'
云黑接口 = 'http://106.126.15.217:83'
云黑信息接口 = 'yh.qdqlenard.cn/CloudList/Robot/{}.html'
二次元接口 = ['https://api.mtyqx.cn/tapi/random.php', 'https://api.ixiaowai.cn/api/api.php',
         'https://tenapi.cn/acg', 'https://api.dujin.org/pic/yuanshen/']
pixiv接口 = 'https://api.lolicon.app/setu/v2?size=regular&proxy=pixiv.leaveold.xyz&r18='
轰炸密钥 = ['ec9429dc5f3cf1d9951b1747935294a9', '03a6d383e306017677d71c80099b5ebe', 'ab21aab25a1abb6bedd550828ab8a0d2']
轰炸接口 = 'http://hz.1aya.cn/api/index/submit?key={}&time={}&phone={}'
真人接口 = ['https://bak.yantuz.cn:8000/mmPic/index.php']
头像接口 = ['https://api.sunweihu.com/api/sjtx/api.php?lx=']
小号接口 = 'http://106.126.15.217:81/xh?key=7Vm0xMFlWbFdXWGhXV0doVVltdHdUMVp0ZUhkWFZteFZVVlJHVmxac1dubFhhMlIzVkd4S2MxTnVhRlpXTTJob1ZsWmFWMVpWTVVWaGVqQTk='
花雨庭接口1 = 'http://mc-api.16163.com/search/{}.html?uid={}'
花雨庭接口2 = 'https://mc-api.16163.com/search/info.html?key={}'
花雨庭模式 = ['bedwars', 'skywars', 'kitbattle', 'bedwarsxp', 'uhc', 'pubgsolo', 'pubgdouble', 'werewolf']
接口1查询 = ['bedwars', 'skywars', 'kitbattle']
接口2查询 = list(set(花雨庭模式) - set(接口1查询))
群消息配色 = ['rgb(238,238,0)','rgb(0,215,0)', 'rgb(0,135,255)', 'rgb(95,0,255)', 'rgb(95,175,215)', "rgb(255,95,215)", 'rgb(255,255,255)']
好友消息配色 = ['rgb(238,238,0)','rgb(95,175,215)', "rgb(255,95,215)",'rgb(255,255,255)']
临时会话消息配色 = ['rgb(238,238,0)', 'rgb(0,215,0)', 'rgb(0,135,255)', 'rgb(95,0,255)', 'rgb(95,175,215)', "rgb(255,95,215)",'rgb(255,255,255)']
接口1返回数据 = ''
接口2返回数据 = ''
总数据 = '[1]: {}\n[2]: {}\n[3]: {}'
第一条消息 = 0
小号限制 = time()
小号间隔 = 5
上一次消息 = ''
上一次发送者 = 0
上一次群号 = 0
消息重复次数 = 0
发送者重复次数 = 0
qq号 = 0
手机号 = 0
地区 = ''
LOL名 = ''
LOL大区 = ''
消息标签 = 0
云黑列表 = get(云黑接口).text
云黑列表 = 云黑列表.split('\r\n')

with open(卡密存储地址, 'r', encoding='gbk') as 文件对象:
    现有卡密 = 文件对象.read().split('\n')

with open(cancir卡密地址, 'r', encoding='gbk') as 文件对象:
    现有cancir卡密 = 文件对象.read().split('\n')

with open(违禁词地址, 'r', encoding='gbk') as 文件对象:
    违禁词列表 = 文件对象.read().split('\n')

with open(配置地址, 'r', encoding='gbk') as 文件对象:
    配置_json格式 = 文件对象.read()

with open(商店内容地址, 'r', encoding='gbk') as 文件对象:
    商店内容 = 文件对象.read()

with open(小号地址, 'r') as 文件对象:
    小号列表 = 文件对象.read().split('\n')

with open(轰炸授权地址, 'r') as 文件对象:
    轰炸授权 = 文件对象.read().split('\n')

配置 = loads(配置_json格式)
白名单列表 = 配置['名单']['白名单']
黑名单 = 配置['名单']['黑名单']
超管名单 = 配置['名单']['超管']
总开关 = 配置['总开关']
验证开关 = 配置['验证']
功能开关 = 配置['功能']
格式 = 配置['格式']


def 压缩图片(图片地址, 宽, 高, 保存地址):
    图片对象 = Image.open(图片地址)
    处理后图片 = 图片对象.resize((宽, 高), Image.ANTIALIAS)
    处理后图片.save(保存地址)


def 查找(主体='str', 组别=1, 表达式=''):
    正则表达式 = compile(u'%s' % 表达式)
    return 正则表达式.search(主体).group(组别)


def 添加违禁词(违禁词):
    with open(违禁词地址, 'a', encoding='gbk') as 文件对象:
        文件对象.write('\n' + 违禁词)


def 删除违禁词(违禁词):
    with open(违禁词地址, 'r', encoding='gbk') as 文件对象:
        已有违禁词 = 文件对象.read()
    新违禁词 = 已有违禁词.replace('\n' + 违禁词, '')
    with open(违禁词地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(新违禁词)


def 日志输出(消息配色, 消息日志):
    for 循环对象 in range(len(消息配色)):
        配色 = 消息配色[循环对象]
        日志项 = 消息日志[循环对象]
        if 消息日志[循环对象] != 消息日志[-1]:
            日志项 = '[%s]' % 日志项
            console.print(日志项, style=配色, end='')
        else:
            console.print(日志项, style=配色)


def 消息推送(群列表,消息):
    推送群数 = 0
    消息链 = [{'type': 'Plain', 'text': '[影子]消息推送\n%s' % 消息}]
    for 循环对象 in 群列表:
        发送消息('sendGroupMessage', 循环对象['id'], 消息链)
        推送群数 += 1
        sleep(2)
    消息链 = [{'type': 'Plain', 'text': '推送成功!\n总共{}个群聊,已推送至{}个群聊'.format(len(群列表), 推送群数)}]


def 接受进群邀请(事件编号, 邀请人qq, 进群号):
    请求内容 = {
        "syncId": -1,
        "command": 'resp_botInvitedJoinGroupRequestEvent',
        "content": {
            "eventId": 事件编号,
            "fromId": 邀请人qq,
            "groupId": 进群号,
            "operate": 0,
            "message": "已接受"
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 接受好友申请(事件编号, 申请人qq, 来源群号):
    请求内容 = {
        "syncId": -1,
        "command": 'resp_newFriendRequestEvent',
        "content": {
            "eventId": 事件编号,
            "fromId": 申请人qq,
            "groupId": 来源群号,
            "operate": 0,
            "message": "已接受"
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 发送消息(消息关键字, 发送目标, 消息链):
    global 消息标签
    请求内容 = {
        "syncId": -1,
        "command": 消息关键字,
        "content": {
            "target": 发送目标,
            "messageChain": 消息链
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)
    消息标签 = 发送目标


def 发送群临时消息(qq号, 群号, 消息链):
    请求内容 = {
        "syncId": -1,
        "command": 'sendTempMessage',
        "content": {
            "qq": qq号,
            "group": 群号,
            "messageChain": 消息链
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)
    消息标签 = 群号


def 获取群列表():
    链接 = http接口 + 'groupList'
    请求对象 = get(链接)
    请求结果 = loads(请求对象.text)['data']
    请求结果 = list(set(请求结果))
    return 请求结果


def 获取群成员(群号):
    链接 = http接口 + 'memberList?target=%s' % 群号
    请求对象 = get(链接)
    请求结果 = loads(请求对象.text)['data']
    return 请求结果


def 禁言群员(群号, 群员号, 时长=360):
    请求内容 = {
        "syncId": -1,
        "command": 'mute',
        "content": {
            "target": 群号,
            "memberId": 群员号,
            'time': 时长
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 踢出群员(群号, 群员号, 理由):
    请求内容 = {
        "syncId": -1,
        "command": 'kick',
        "content": {
            "target": 群号,
            "memberId": 群员号,
            "msg": 理由
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 解除禁言(群号, 群员号):
    请求内容 = {
        "syncId": -1,
        "command": 'unmute',
        "content": {
            "target": 群号,
            "memberId": 群员号,
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 撤回消息(消息编号):
    请求内容 = {
        "syncId": -1,
        "command": 'recall',
        "content": {
            "target": 消息编号
        }
    }
    请求内容_json格式 = dumps(请求内容, indent=5, ensure_ascii=False)
    服务器对象.send(请求内容_json格式)


def 花雨庭查询(ID, 模式, 群号):
    print(ID, 模式)
    模板 = 格式[模式]
    if 模式 in 接口1查询:
        请求对象 = get(花雨庭接口1.format(模式, ID))
        结果 = 请求对象.text
        if 'Not Found' in 结果:
            消息链 = [{'type': 'Plain', 'text': '未找到结果'}]
        else:
            结果 = loads(结果)
            if 模式 == 'bedwars':
                渲染 = 模板.format(结果['name'], 结果['duanwei'], 结果['winRate'],
                               结果['killDead'], 结果['rank'], 结果['playNum'], 结果['beddesNum'],
                               结果['rowNum'], 结果['rowRate'], 结果['lastkillNum'], 结果['mvpNum'])
            elif 模式 == 'skywars':
                渲染 = 模板.format(结果['name'], 结果['duanwei'], 结果['winRate'],
                               结果['killDead'], 结果['rank'], 结果['playNum'], 结果['killNum'])
            elif 模式 == 'kitbattle':
                # 职业战争
                渲染 = 模板.format(结果['name'], 结果['duanwei'], 结果['rank'],
                               结果['exp'], 结果['killDead'], 结果['deadNum'], 结果['killNum'])
            消息链 = [{'type': 'Plain', 'text': 渲染}]
    elif 模式 in 接口2查询:
        请求对象 = get(花雨庭接口2.format(模式))
        结果 = loads(请求对象.text)
        渲染 = ''
        for 循环对象 in 结果:
            if 循环对象['name'] == ID:
                if 模式 == 'bedwarsxp':
                    渲染 = 模板.format(循环对象['name'], 循环对象['duanwei'], 循环对象['winRate'],
                                   循环对象['killDead'], 循环对象['rank'], 循环对象['games'], 循环对象['dbed'],
                                   循环对象['deadNum'], 循环对象['killNum'])
                elif 模式 == 'uhc':
                    渲染 = 模板.format(循环对象['name'], 循环对象['duanwei'], 循环对象['winRate'],
                                   循环对象['killDead'], 循环对象['rank'], 循环对象['gamePlayed'], 循环对象['win'],
                                   循环对象['killNum'], 循环对象['deadNum'])
                # 吃鸡系列
                elif 模式 == 'pubgsolo' or 模式 == 'pubgdouble':
                    渲染 = 模板.format(循环对象['name'], 循环对象['duanwei'], 循环对象['killDead'],
                                   循环对象['rank'], 循环对象['play'], 循环对象['person']['wins'], 循环对象['killNum'],
                                   循环对象['DeadNum'])
                # 狼人杀
                else:
                    渲染 = 模板.format(循环对象['name'], 循环对象['duanwei'], 循环对象['winRate'],
                                   循环对象['rank'], 循环对象['play'], 循环对象['win'], 循环对象['kills'],
                                   循环对象['name'], 循环对象['name'], 循环对象['name'], 循环对象['name'])
        if 渲染 == '':
            消息链 = [{'type': 'Plain', 'text': '未找到结果'}]
        else:
            消息链 = [{'type': 'Plain', 'text': 渲染}]
    else:
        消息链 = [{'type': 'Plain', 'text': '没有此模式'}]
    发送消息('sendGroupMessage', 群号, 消息链)


def 轰炸(手机号, 时间, 好友qq):
    def 请求轰炸接口(批次, 卡密, 时间, 手机号):
        global 接口1返回数据, 接口2返回数据, 接口3返回数据
        请求对象 = get(轰炸接口.format(卡密, 时间, 手机号))
        轰炸结果 = loads(请求对象.text)
        if 批次 == 1:
            接口1返回数据 = 轰炸结果['msg']
        elif 批次 == 2:
            接口2返回数据 = 轰炸结果['msg']
        else:
            接口3返回数据 = 轰炸结果['msg']

    线程_轰炸1 = Thread(target=请求轰炸接口, args=(1, 轰炸密钥[0], 时间, 手机号,))
    线程_轰炸2 = Thread(target=请求轰炸接口, args=(2, 轰炸密钥[1], 时间, 手机号,))
    线程_轰炸3 = Thread(target=请求轰炸接口, args=(3, 轰炸密钥[2], 时间, 手机号,))
    线程_轰炸1.start()
    线程_轰炸2.start()
    线程_轰炸3.start()
    线程_轰炸1.join()
    线程_轰炸2.join()
    线程_轰炸3.join()

    渲染 = 总数据.format(接口1返回数据, 接口2返回数据, 接口3返回数据)
    消息链 = [{'type': 'Plain', 'text': 渲染}]
    发送消息('sendFriendMessage', 好友qq, 消息链)


def 恶俗(模式, 目标, 群号):
    global qq号, 手机号, 地区, LOL大区, LOL名

    def qq查手机(目标qq):
        global qq号, 手机号, 地区
        请求对象 = get('https://zy.xywlapi.cc/qqapi?qq=%s' % 目标qq)
        恶俗结果 = loads(请求对象.text)
        if 恶俗结果['message'] != '没有找到':
            qq号 = 目标qq
            手机号 = 恶俗结果['phone']
            地区 = 恶俗结果['phonediqu']
        else:
            qq号 = 目标qq
            手机号 = 'None'
            地区 = '地球村'

    def 手机查qq(目标手机号):
        global qq号, 手机号, 地区
        请求对象 = get('https://zy.xywlapi.cc/qqphone?phone=%s' % 目标手机号)
        恶俗结果 = loads(请求对象.text)
        if 恶俗结果['message'] != '没有找到':
            qq号 = 恶俗结果['qq']
            手机号 = 目标手机号
            地区 = 恶俗结果['phonediqu']
        else:
            qq号 = 'None'
            手机号 = 目标手机号
            地区 = '地球村'

    def qq_查LOL(目标qq号):
        global LOL大区, LOL名
        请求对象 = get('https://zy.xywlapi.cc/qqlol?qq=%s' % 目标qq号)
        恶俗结果 = loads(请求对象.text)
        if 恶俗结果['message'] != '没有找到':
            LOL名 = 恶俗结果['name']
            LOL大区 = 恶俗结果['daqu']
        else:
            LOL名 = 'None'
            LOL大区 = 'None'

    if 模式 == '查询':
        线程_恶俗1 = Thread(target=qq查手机, args=(目标,))
        线程_恶俗2 = Thread(target=qq_查LOL, args=(目标,))
        线程_恶俗1.start()
        线程_恶俗2.start()
        线程_恶俗1.join()
        线程_恶俗2.join()
        if 手机号 == 'None' and LOL名 == 'None':
            恶俗消息 = '无此QQ信息'
        else:
            恶俗消息 = '''QQ: {}
手机号: {}
地区: {}
LOL名: {}
LOL区: {}'''.format(qq号, 手机号, 地区, LOL名, LOL大区)
        消息链 = [{'type': 'Image', 'url': 'https://tenapi.cn/qqimg/?qq=%s' % 目标}, {'type': 'Plain', 'text': 恶俗消息}]
    else:
        线程_恶俗3 = Thread(target=手机查qq, args=(目标,))
        线程_恶俗3.start()
        线程_恶俗3.join()
        if qq号 == 'None' and 地区 == '地球村':
            恶俗消息 = '无此手机号信息'
        else:
            恶俗消息 = '''QQ: {}
手机号: {}
地区: {}'''.format(qq号, 手机号, 地区)
        消息链 = [{'type': 'Image', 'url': 'https://tenapi.cn/qqimg/?qq=%s' % 目标}, {'type': 'Plain', 'text': 恶俗消息}]
    发送消息('sendGroupMessage', 群号, 消息链)


def 获取头像(模式, 关键字, 发送目标):
    链接 = 头像接口[randint(0, len(头像接口) - 1)] + 模式
    消息链 = [{'type': 'Image', 'url': 链接}]
    发送消息(关键字, 发送目标, 消息链)


def 色色(模式, 关键字, 发送目标, 群号):
    if 模式 == 'acg':
        链接 = 二次元接口[randint(0, len(二次元接口) - 1)]
    else:
        链接 = 真人接口[randint(0, len(真人接口) - 1)]
    消息链 = [{'type': 'Image', 'url': 链接}]
    if 关键字 == 'sendTempMessage':
        发送群临时消息(发送目标, 群号, 消息链)
    else:
        发送消息(关键字, 发送目标, 消息链)


def pixiv(关键字, 发送目标, 群号):
    global pixiv接口
    if 总开关['r18']:
        pixiv接口_ = pixiv接口 + '2'
    else:
        pixiv接口_ = pixiv接口 + '0'
    原始数据 = get(pixiv接口_)
    数据文本 = loads(原始数据.text)['data'][0]
    图像链接 = 数据文本['urls']['regular']
    图像名称 = 数据文本['title']
    图像作者 = 数据文本['author']
    图像级别 = 数据文本['r18']
    图像编号 = 数据文本['pid']
    图像标签 = 数据文本['tags']

    图像标签数据 = ''
    标签个数 = ''
    for 循环对象 in 图像标签:
        标签个数 += 循环对象
        if len(标签个数) >= 27:
            图像标签数据 += '\n'
            标签个数 = ''
        图像标签数据 += '[%s]' % 循环对象

    if 图像级别:
        图像级别 = 'True'
    else:
        图像级别 = 'False'

    图像头部 = '''标题: {}
作者: {}'''.format(图像名称, 图像作者)

    图像尾部 = '''r18: {}
图像编号: {}
标签: {}'''.format(图像级别, 图像编号, 图像标签数据)

    下载图像 = get(图像链接)
    with open(pixiv地址, 'wb') as 文件对象:
        文件对象.write(下载图像.content)
    消息链 = [{'type': 'Plain', 'text': 图像头部}, {'type': 'Image', 'path': pixiv地址}, {'type': 'Plain', 'text': 图像尾部}]
    if 关键字 == 'sendTempMessage':
        发送群临时消息(发送目标, 群号, 消息链)
    else:
        发送消息(关键字, 发送目标, 消息链)


def 保存小号(小号列表):
    小号文本 = ''
    for 循环对象 in 小号列表:
        小号文本 += 循环对象 + '\n'
    with open(小号地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(小号文本.strip())


def 保存配置(配置):
    配置_json = dumps(配置, ensure_ascii=False, indent=5)
    with open(配置地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(配置_json)


def 保存授权(授权列表):
    授权文本 = ''
    for 循环对象 in 授权列表:
        授权文本 += 循环对象 + '\n'
    with open(轰炸授权地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(授权文本.strip())


def 保存卡密配置(卡密, 类别):
    if 类别 == 'leave':
        地址 = 卡密地址
    elif 类别 == 'cancir':
        地址 = cancir记录地址
    卡密_json = dumps(卡密, ensure_ascii=False, indent=5)
    with open(地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(卡密_json)


print('初始化完成')

while True:
    第一条消息 += 1
    # 接收
    try:
        返回数据 = 服务器对象.recv()
        返回数据 = normalize('NFKC', 返回数据)  # 中文标点转英文标点
    except:
        服务器对象.connect('ws://localhost:23423/all?verifyKey=INITKEYsV4Mnulq&qq=2303798671')
        返回数据 = 服务器对象.recv()
    if 第一条消息 == 1:
        continue

    try:
        消息处理 = loads(返回数据)
        数据信息 = 消息处理['data']['type']
    except:
        数据信息 = ''

    if 数据信息 == 'GroupMessage':
        # 定义基本信息
        返回数据 = loads(返回数据)['data']
        主要消息 = 返回数据['messageChain']
        发送者 = 返回数据['sender']['id']
        群号 = 返回数据['sender']['group']['id']
        群昵称 = 返回数据['sender']['group']['name']
        消息来源 = 返回数据['type']
        消息编号 = 主要消息[0]['id']
        发送者昵称 = 返回数据['sender']['memberName']
        管理员 = 返回数据['sender']['permission']
        机器人管理员 = 返回数据['sender']['group']['permission']
        消息文本 = ''

        # 遍历,获取消息纯文本形式
        for 循环对象 in 主要消息:
            消息类型_取文本 = 循环对象['type']

            if 消息类型_取文本 == 'Plain':
                消息文本 += 循环对象['text']

            elif 消息类型_取文本 == 'At':
                消息文本 += '{@%d}' % 循环对象['target']

            elif 消息类型_取文本 == 'AtAll':
                消息文本 += '[@All]'

            elif 消息类型_取文本 == 'Face':
                消息文本 += '[表情:%s]' % 循环对象['name']

            elif 消息类型_取文本 == 'Image':
                图片识别信息 = 文字识别对象.ocr('运行时图片.png')
                文字识别结果 = ''
                for 循环对象甲 in 图片识别信息:
                    for 循环对象乙 in 循环对象甲[0]:
                        文字识别结果 += 循环对象乙
                文字识别结果 = 文字识别结果.lower().replace(' ', '')  # 去除空格,转小写
                消息文本 += '[文字识别:%s]' % 文字识别结果

            elif 消息类型_取文本 == 'File':
                消息文本 += '[文件名称: {} , 文件大小: {}]'.format(循环对象['name'], 循环对象['size'])

            elif 消息类型_取文本 == 'MiraiCode':
                消息文本 += 'MiraiCode: %s' % 循环对象['code']
        消息文本 = 消息文本.strip().replace(' ', '')

        群消息日志 = [数据信息, 群昵称, str(群号), 管理员, 发送者昵称, str(发送者), 消息文本]
        日志输出(群消息配色, 群消息日志)

        # 云黑检测
        if 发送者 in 黑名单:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                踢出群员(群号, 发送者, '检测到您在云黑系统中,可找3055843259申诉')
                消息链 = [{'type': 'Plain', 'text': '发现已被本地云黑收录的目标%s,\n已进行踢出' % 发送者}]
                发送消息('sendGroupMessage', 群号, 消息链)
        elif str(发送者) in 云黑列表:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                踢出群员(群号, 发送者, '检测到您在落樱云黑系统中')
                消息链 = [{'type': 'Plain', 'text': '发现已被落樱云黑收录的目标%s,\n已进行踢出' % 发送者}]
                发送消息('sendGroupMessage', 群号, 消息链)
            else:
                消息链 = [{'type': 'Plain', 'text': '[{}]已被落樱云黑收录,请谨慎判别.\n详细信息: {}'.format(发送者,云黑信息接口.format(发送者))}]
                发送消息('sendGroupMessage', 群号, 消息链)

        # 频率验证
        if 上一次消息 == 消息文本 and 上一次发送者 == 发送者 and 上一次群号 == 群号:
            消息重复次数 += 1
            发送者重复次数 += 1
        elif 上一次发送者 == 发送者 and 上一次群号 == 群号:
            发送者重复次数 += 1
            消息重复次数 = 0
        else:
            消息重复次数 = 0
            发送者重复次数 = 0

        # 检测次数
        if 消息重复次数 >= 4 or 发送者重复次数 >= 8:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                if 发送者 not in 白名单列表 and 群号 in 配置['功能']['群管'] and 总开关['群管']:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发频率检测'}]
                    禁言群员(群号, 发送者)
                    撤回消息(消息编号)
                    发送消息('sendGroupMessage', 群号, 消息链)
                    消息重复次数 = 0
                    发送者重复次数 = 0
                    continue

        上一次群号 = 群号
        上一次消息 = 消息文本
        上一次发送者 = 发送者

        # 字数验证
        消息长度 = len(消息文本)
        消息长度 -= 消息文本.count('[文字识别:') * 60
        if 群号 not in 配置['功能']['群管'] and 消息长度 > 130 and 总开关['群管']:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                if 发送者 not in 白名单列表:
                    禁言群员(群号, 发送者)
                    撤回消息(消息编号)
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发字数检测'}]
                    发送消息('sendGroupMessage', 群号, 消息链)
                    continue

        elif 消息文本 == '#up':
            if 群号 in 配置['验证']['#up'] and 总开关['#up']:
                with open(工具箱地址, 'r', encoding='gbk') as 文件对象:
                    已验证名单 = 文件对象.read()
                if str(发送者) in 已验证名单:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您已验证过'}]
                else:
                    with open(工具箱地址, 'a', encoding='gbk') as 文件对象:
                        文件对象.write(str(发送者) + ',')
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '验证成功'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '#获取卡密':
            if 群号 in 配置['验证']['card_pwd'] and 总开关['card_pwd']:
                with open(卡密地址, 'r', encoding='gbk') as 文件对象:
                    卡密信息 = 文件对象.read()
                if str(发送者) not in 卡密信息:
                    卡密信息 = loads(卡密信息)
                    卡密信息[发送者] = 现有卡密[0]
                    消息链 = [{'type': 'Plain', 'text': '%s' % 现有卡密[0]}]
                    现有卡密.pop(0)
                    保存卡密配置(卡密信息, 'leave')
                    卡密库 = ''
                    for 循环对象 in 现有卡密:
                        卡密库 += 循环对象 + '\n'
                    with open(卡密存储地址, 'w', encoding='gbk') as 文件对象:
                        文件对象.write(卡密库.strip())
                else:
                    卡密信息 = loads(卡密信息)
                    消息链 = [{'type': 'Plain', 'text': '%s' % 卡密信息[str(发送者)]}]
                发送群临时消息(发送者, 群号, 消息链)
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '已私发,如未收到请添加机器人好友'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '.getcode':
            if 群号 in 配置['验证']['cancir_check'] and 总开关['cancir_check']:
                with open(cancir记录地址, 'r', encoding='gbk') as 文件对象:
                    卡密信息 = 文件对象.read()
                if str(发送者) not in 卡密信息:
                    卡密信息 = loads(卡密信息)
                    卡密信息[发送者] = 现有cancir卡密[0]
                    消息链 = [{'type': 'Plain', 'text': '%s' % 现有cancir卡密[0]}]
                    现有cancir卡密.pop(0)
                    保存卡密配置(卡密信息, 'cancir')
                    卡密库 = ''
                    for 循环对象 in 现有cancir卡密:
                        卡密库 += 循环对象 + '\n'
                    with open(cancir卡密地址, 'w', encoding='gbk') as 文件对象:
                        文件对象.write(卡密库.strip())
                else:
                    卡密信息 = loads(卡密信息)
                    消息链 = [{'type': 'Plain', 'text': '%s' % 卡密信息[str(发送者)]}]
                发送群临时消息(发送者, 群号, 消息链)
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '已私发,如未收到请添加机器人好友'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('#水影'):
            if 群号 in 配置['验证']['#水影'] and 总开关['#水影']:
                水影验证码 = 消息文本[3:]
                with open(水影地址, 'r', encoding='gbk') as 文件对象:
                    已验证名单 = 文件对象.read()
                if 水影验证码 in 已验证名单:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您已验证过'}]
                elif len(水影验证码) != 15:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '格式错误'}]
                else:
                    with open(水影地址, 'a', encoding='gbk') as 文件对象:
                        文件对象.write('[{}]{}\n'.format(发送者, 水影验证码))
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '验证成功'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '菜单':
            菜单文本 = '''请访问机器人文档: https://easydoc.net/s/54855991
By Edwad_过客[3055843259]
'''
            消息链 = [{'type': 'Plain', 'text': '%s' % 菜单文本}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '机器人状态':
            CPU占用 = cpu_percent(interval=1)
            内存占用 = virtual_memory().percent
            群列表 = 获取群列表()
            总群数 = len(群列表)
            管理群数=0
            for 循环对象 in 群列表:
                if 循环对象['permission'] != 'MEMBER':
                    管理群数+=1
            状态消息 = '''机器人名称: 影子、淺笑
QQ号: 2303798671
CPU占用 : {}%
内存占用: {}%
有管理位群数: {}/{}
By Edwad_过客[3055843259]'''.format(CPU占用, 内存占用,管理群数,总群数)
            消息链 = [{'type': 'Plain', 'text': 状态消息}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == 'acg' or 消息文本 == '真人' or 消息文本 == '获取pixiv':
            if 群号 not in 配置['功能']['acg'] or 群号 not in 配置['功能']['真人'] or 群号 not in 配置['功能']['pixiv']:
                if 发送者 in 超管名单:
                    if 消息文本 == 'acg' and 总开关['acg']:
                        线程_色色 = Thread(target=色色, args=('acg', 'sendGroupMessage', 群号, '',)).start()
                        continue
                    elif 消息文本 == '真人' and 总开关['真人']:
                        线程_色色 = Thread(target=色色, args=('真人', 'sendGroupMessage', 群号, '',)).start()
                        continue
                    elif 消息文本 == '获取pixiv' and 总开关['pixiv']:
                        线程_色色 = Thread(target=pixiv, args=('sendGroupMessage', 群号, '',)).start()
                        continue
                    else:
                        消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启'}]
                else:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '请私聊机器人'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('hyt查询|') and 消息文本.count('|') == 2:
            切割 = 消息文本.split('|')
            模式 = 切割[2]
            ID = 切割[1]
            线程_花雨庭 = Thread(target=花雨庭查询, args=(ID, 模式, 群号,)).start()

        elif 消息文本.startswith('获取头像|'):
            if 群号 not in 配置['功能']['获取头像'] and 总开关['获取头像']:
                模式 = 消息文本.split('|')[1]
                if 模式 == '男':
                    模式字符 = 'a1'
                elif 模式 == '女':
                    模式字符 = 'b1'
                elif 模式 == '动漫男':
                    模式字符 = 'c3'
                elif 模式 == '动漫女':
                    模式字符 = 'c2'
                elif 模式 == '动漫混合':
                    模式字符 = 'c1'
                线程_头像 = Thread(target=获取头像, args=(模式字符, 'sendGroupMessage', 群号,)).start()
            elif 总开关['获取头像']:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群'}]
                发送消息('sendGroupMessage', 群号, 消息链)
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启'}]
                发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('&总启用') or 消息文本.startswith('&总关闭'):
            if 发送者 in 超管名单:
                指令 = 消息文本[4:]
                if 指令 in 总开关 or 指令 == '全部':
                    if 指令 == '全部':
                        for 键 in 总开关:
                            if '启用' in 消息文本:
                                if 总开关[键] == False:
                                    总开关[键] = True
                            else:
                                if 总开关[键]:
                                    总开关[键] = False
                    else:
                        if '启用' in 消息文本:
                            if 总开关[指令] == False:
                                总开关[指令] = True
                        else:
                            if 总开关[指令]:
                                总开关[指令] = False
                    if '启用' in 消息文本:
                        反馈 = '启用成功'
                    else:
                        反馈 = '关闭成功'
                else:
                    反馈 = '没有此项'
            else:
                反馈 = '没有权限'
            配置['总开关'] = 总开关
            保存配置(配置)
            消息链 = [{'type': 'Plain', 'text': 反馈}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('&启用') or 消息文本.startswith('&关闭'):
            try:
                if 消息文本.endswith('功能'):
                    配置_ = 配置['功能']
                    标记 = '功能'
                elif 消息文本.endswith('验证'):
                    配置_ = 配置['验证']
                    标记 = '验证'
                if 发送者 in 超管名单:
                    指令 = 消息文本[3:-2]
                    if 指令 in 配置_ or 指令 == '全部':
                        if 指令 == '全部':
                            for 键 in 配置_:
                                if '启用' in 消息文本:
                                    if 群号 in 配置_[键]:
                                        配置_[键].remove(群号)
                                else:
                                    if 群号 not in 配置_[键]:
                                        配置_[键].append(群号)
                        else:
                            if '启用' in 消息文本:
                                if 群号 in 配置_[指令]:
                                    配置_[指令].remove(群号)
                            else:
                                if 群号 not in 配置_[指令]:
                                    配置_[指令].append(群号)
                        if '启用' in 消息文本:
                            反馈 = '启用成功'
                        else:
                            反馈 = '关闭成功'
                    else:
                        反馈 = '没有此项'
                else:
                    反馈 = '没有权限'
                保存配置(配置)
                消息链 = [{'type': 'Plain', 'text': 反馈}]
                发送消息('sendGroupMessage', 群号, 消息链)
            except:
                pass

        elif 消息文本 == '查看总开关':
            授权消息 = '[总开关]\n'
            for 键, 值 in 总开关.items():
                if 值:
                    授权消息 += 键 + ': 开\n'
                else:
                    授权消息 += 键 + ': 关\n'
            授权消息 += 'By Edwad_过客[3055843259]'
            消息链 = [{'type': 'Plain', 'text': 授权消息}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '查看授权':
            授权消息 = '[功能类]\n'
            for 键, 值 in 配置['功能'].items():
                if 群号 in 配置['功能'][键]:
                    授权消息 += 键 + ': 已授权\n'
                else:
                    授权消息 += 键 + ': 未授权\n'
            授权消息 += '[验证类]\n'
            for 键, 值 in 配置['验证'].items():
                if 群号 in 配置['验证'][键]:
                    授权消息 += 键 + ': 已授权\n'
                else:
                    授权消息 += 键 + ': 未授权\n'
            授权消息 += 'By Edwad_过客[3055843259]'
            消息链 = [{'type': 'Plain', 'text': 授权消息}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('查询') or 消息文本.startswith('反查'):
            if 群号 not in 配置['功能']['查询'] or 群号 not in 配置['功能']['反查']:
                if 总开关['q绑']:
                    目标 = 消息文本[2:]
                    if 消息文本.startswith('查询'):
                        线程_恶俗 = Thread(target=恶俗, args=('查询', 目标, 群号)).start()
                    else:
                        线程_恶俗 = Thread(target=恶俗, args=('反查', 目标, 群号)).start()
                else:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启'}]
                    发送消息('sendGroupMessage', 群号, 消息链)
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群'}]
                发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('解禁'):
            if 发送者 in 超管名单:
                if '@' in 消息文本:
                    被解禁者 = 查找(消息文本, 1, "{@([0-9]*)}")
                else:
                    被解禁者 = 查找(消息文本, 1, '禁言([0-9]*)')
                解除禁言(群号, 被解禁者)
                消息链 = [{'type': 'Plain', 'text': '解禁成功'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('禁言'):
            if 发送者 in 超管名单:
                if '@' in 消息文本:
                    被禁言者 = 查找(消息文本, 1, "{@([0-9]*)}")
                else:
                    被禁言者 = 查找(消息文本, 1, '禁言([0-9]*)|')
                时长 = 消息文本.split('|')[1]
                禁言群员(群号, 被禁言者, int(时长))
                消息链 = [{'type': 'Plain', 'text': '禁言已进行'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('踢出'):
            if 发送者 in 超管名单:
                if '@' in 消息文本:
                    被踢出者 = 查找(消息文本, 1, "{@([0-9]*)}")
                else:
                    被踢出者 = 查找(消息文本, 1, '踢出([0-9]*)|')
                if '|' in 消息文本:
                    理由 = 消息文本.split('|')[1]
                else:
                    理由 = ''
                踢出群员(群号, 被踢出者, 理由)
                消息链 = [{'type': 'Plain', 'text': '已进行踢出'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '私聊获取小号':
            if 群号 not in 配置['功能']['私聊获取小号'] and 总开关['私聊获取小号']:
                if 小号限制 + 小号间隔 <= time():
                    # 请求小号 = get(小号接口,timeout=3)
                    # 请求结果 = 请求小号.text
                    # if '----' in 请求结果:
                    #     账户分割 = 请求结果.split('----')
                    #     渲染 = 格式['小号格式'].format(账户分割[0], 账户分割[1], '接口获取,无信息').replace('\\n', '\n')
                    #     消息链 = [{'type': 'Plain', 'text': 渲染}]
                    #     发送群临时消息(发送者, 群号, 消息链)
                    #     消息链 = [{'type': 'Plain', 'text': '已私发,未收到请加机器人好友'}]
                    # else:
                    if len(小号列表) != 0 and 小号列表[0] != '':
                        小号 = 小号列表[0].split('----')
                        渲染 = 格式['小号格式'].format(小号[0], 小号[1], len(小号列表) - 1).replace('\\n', '\n')
                        小号限制 = time()
                        消息链 = [{'type': 'Plain', 'text': 渲染}]
                        发送群临时消息(发送者, 群号, 消息链)
                        小号列表.pop(0)
                        保存小号(小号列表)
                        消息链 = [{'type': 'Plain', 'text': '已私发,未收到请加机器人好友'}]
                    else:
                        消息链 = [{'type': 'Plain', 'text': '小号库存已空'}]
                    小号限制 = time()
                else:
                    消息链 = [{'type': 'Plain', 'text': '小号冷却中,还剩下%s秒' % str(小号限制 + 小号间隔 - time()).split('.')[0]}]
            else:
                消息链 = [{'type': 'Plain', 'text': '您不在授权群'}]
            发送消息('sendGroupMessage', 群号, 消息链)


        elif 消息文本 == '获取小号':
            if 群号 not in 配置['功能']['获取小号'] and 总开关['获取小号']:
                if 小号限制 + 小号间隔 <= time():
                    # 请求小号 = get(小号接口,timeout=3)
                    # 请求结果 = 请求小号.text
                    # if '----' in 请求结果:
                    #     账户分割 = 请求结果.split('----')
                    #     渲染 = 格式['小号格式'].format(账户分割[0], 账户分割[1], '接口获取,无信息').replace('\\n', '\n')
                    #     消息链 = [{'type': 'Plain', 'text': 渲染}]
                    # else:
                    if len(小号列表) != 0 and 小号列表[0] != '':
                        小号 = 小号列表[0].split('----')
                        渲染 = 格式['小号格式'].format(小号[0], 小号[1], len(小号列表) - 1).replace('\\n', '\n')
                        消息链 = [{'type': 'Plain', 'text': 渲染}]
                        小号限制 = time()
                        小号列表.pop(0)
                        保存小号(小号列表)
                    else:
                        消息链 = [{'type': 'Plain', 'text': '小号库存已空'}]
                    小号限制 = time()
                else:
                    消息链 = [{'type': 'Plain', 'text': '小号冷却中,还剩下%s秒' % str(小号限制 + 小号间隔 - time()).split('.')[0]}]
            else:
                消息链 = [{'type': 'Plain', 'text': '您不在授权群'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('添加违禁'):
            if 发送者 in 超管名单:
                违禁词 = 消息文本[5:]
                if 违禁词 in 违禁词列表:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '已有此违禁词'}]
                else:
                    违禁词列表.append(违禁词)
                    添加违禁词(违禁词)
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '添加成功'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '没有权限'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('删除违禁'):
            if 发送者 in 超管名单:
                违禁词 = 消息文本[5:]
                if 违禁词.strip() == '':
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '违禁词无效'}]
                else:
                    try:
                        违禁词列表.remove(违禁词)
                        删除违禁词(违禁词)
                        消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '删除成功'}]
                    except ValueError:
                        消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '没有此违禁词'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '没有权限'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '查看云黑':
            名单人数 = len(黑名单)
            消息链 = [{'type': 'Plain', 'text': '云黑系统已收容%s人' % 名单人数}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('云黑检测|'):
            qq号 = int(消息文本.split('|')[1])
            try:
                云黑列表 = get(云黑接口).text
                云黑列表 = 云黑列表.split('\r\n')
            except:
                云黑列表 = 'None'
            if qq号 in 黑名单:
                消息链 = [{'type': 'Plain', 'text': '此QQ已被本地云黑收录'}]
            elif str(qq号) in 云黑列表:
                消息链 = [{'type': 'Plain', 'text': '此QQ已被落樱云黑收录,具体信息见\n{}'.format(云黑信息接口.format(qq号))}]
            else:
                消息链 = [{'type': 'Plain', 'text': '此QQ未被云黑收录'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('&添加云黑|') or 消息文本.startswith('&添加白名单|') or 消息文本.startswith('&添加超管|'):
            if 发送者 in 超管名单 or 发送者 == 3055843259:
                if 消息文本.startswith('&添加云黑|'):
                    名单 = 黑名单
                elif 消息文本.startswith('&添加白名单|'):
                    名单 = 白名单列表
                else:
                    名单 = 超管名单
                    if 发送者 != 3055843259:
                        消息链 = [{'type': 'Plain', 'text': '权限不足'}]
                        发送消息('sendGroupMessage', 群号, 消息链)
                        continue
                qq号 = int(消息文本.split('|')[1])
                if qq号 in 名单:
                    消息链 = [{'type': 'Plain', 'text': '此QQ已在列表中'}]
                else:
                    名单.append(qq号)
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '添加成功'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('&删除云黑|') or 消息文本.startswith('&删除白名单|') or 消息文本.startswith('&删除超管|'):
            if 发送者 in 超管名单 or 发送者 == 3055843259:
                if 消息文本.startswith('&删除云黑|'):
                    名单 = 黑名单
                elif 消息文本.startswith('&删除白名单|'):
                    名单 = 白名单列表
                else:
                    名单 = 超管名单
                    if 发送者 != 3055843259:
                        消息链 = [{'type': 'Plain', 'text': '权限不足'}]
                        发送消息('sendGroupMessage', 群号, 消息链)
                        continue
                qq号 = int(消息文本.split('|')[1])
                if qq号 in 名单:
                    名单.remove(qq号)
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '删除成功'}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '此qq不在名单中'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        else:
            # 违禁词检测
            if 发送者 not in 白名单列表 and 群号 not in 配置['功能']['群管'] and 总开关['群管']:
                if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                    消息拼音 = 拼音对象.get_pinyin(消息文本, ' ')
                    ID拼音 = 拼音对象.get_pinyin(发送者昵称, ' ')
                    for 循环对象 in 违禁词列表:
                        违禁词拼音 = '{}'.format(拼音对象.get_pinyin(循环对象, ' '))
                        if 违禁词拼音 in 消息拼音 or 违禁词拼音 in ID拼音:
                            违禁时间 = strftime('%Y-%m-%d %H:%M:%S')
                            if 消息拼音.endswith(违禁词拼音.rstrip()) or ID拼音.endswith(违禁词拼音.rstrip()):
                                pass
                            else:
                                违禁词拼音 += ' '
                            if 违禁词拼音 in 消息拼音:
                                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发违禁词检测'}]
                                违禁消息 = '[消息违禁]\n违禁时间: {}\n违禁词: {}\n违禁人昵称: {}\n违禁人qq: {}\n群昵称: {}\n群号码: {}\n违禁消息: {}'
                                违禁渲染 = 违禁消息.format(违禁时间, 循环对象, 发送者昵称, 发送者, 群昵称, 群号, 消息文本)
                                检测类别 = '消息违禁'
                            elif 违禁词拼音 in ID拼音:
                                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发ID检测'}]
                                违禁消息 = '[ID违禁]\n违禁时间: {}\n违禁词: {}\n违禁人昵称: {}\n违禁人qq: {}\n群昵称: {}\n群号码: {}'
                                违禁渲染 = 违禁消息.format(违禁时间, 循环对象, 发送者昵称, 发送者, 群昵称, 群号)
                            禁言群员(群号, 发送者)
                            撤回消息(消息编号)
                            发送消息('sendGroupMessage', 群号, 消息链)
                            消息链 = [{'type': 'Plain', 'text': 违禁渲染}]
                            发送消息('sendFriendMessage', 3055843259, 消息链)
                            break

    elif 数据信息 == 'StrangerMessage' or 数据信息 == 'FriendMessage':
        返回数据 = loads(返回数据)['data']
        好友qq = 返回数据['sender']['id']
        好友昵称 = 返回数据['sender']['nickname']

        if 返回数据['messageChain'][1]['type'] == 'Plain':
            指令 = 返回数据['messageChain'][1]['text']
            好友消息日志 = [数据信息, 好友昵称, 好友qq, 指令]
            日志输出(好友消息配色,好友消息日志)

            if 指令 == 'acg' or 指令 == '真人' or 指令 == '获取pixiv':
                if 指令 == 'acg' and 总开关['acg']:
                    线程_色色 = Thread(target=色色, args=('acg', 'sendFriendMessage', 好友qq, '',)).start()
                elif 指令 == '真人' and 总开关['真人']:
                    线程_色色 = Thread(target=色色, args=('真人', 'sendFriendMessage', 好友qq, '',)).start()
                elif 指令 == '获取pixiv' and 总开关['pixiv']:
                    线程_色色 = Thread(target=pixiv, args=('sendFriendMessage', 好友qq, '',)).start()
                else:
                    消息链 = [{'type': 'Plain', 'text': '此功能未开启'}]
                    发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令.startswith('反馈'):
                if 好友qq == 3055843259 or 好友qq == 1502656934:
                    目标qq = 查找(指令, 表达式='反馈([0-9]*)|')
                    返回消息 = 指令.split('|')[1]
                    with open(消息存储地址, 'r', encoding='gbk') as 文件对象:
                        已有消息 = 文件对象.read()
                    if 目标qq in 已有消息:
                        for 循环对象 in 已有消息.split('\n'):
                            if 目标qq in 循环对象:
                                旧的消息 = 循环对象.split(']')[1]
                        新有消息 = 已有消息.replace('[{}]{}'.format(目标qq, 旧的消息), '[{}]{}'.format(目标qq, 返回消息))
                        with open(消息存储地址, 'w', encoding='gbk') as 文件对象:
                            文件对象.write(新有消息)
                    else:
                        with open(消息存储地址, 'a', encoding='gbk') as 文件对象:
                            文件对象.write('[{}]{}\n'.format(目标qq, 返回消息))
                    消息链 = [{'type': 'Plain', 'text': '反馈成功'}]
                    发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令 == '商店':
                消息链 = [{'type': 'Plain', 'text': 商店内容}]
                发送消息('sendFriendMessage', 好友qq, 消息链)
                消息链 = [{'type': 'Plain', 'text': '请按照商品价格缴费,缴费后请截图发给群主'}, {'type': 'Image', 'path': 商店收款码地址}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令.startswith('DIY小号格式'):
                if 好友qq in 超管名单:
                    小号格式 = 指令[6:]
                    配置['格式']['小号格式'] = 小号格式
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '定义格式成功'}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '权限不足'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令.startswith('轰炸'):
                if str(好友qq) in 轰炸授权:
                    try:
                        分割指令 = 指令.split('|')
                        电话 = 分割指令[0][2:]
                        时间 = 分割指令[1]
                    except IndexError:
                        消息链 = [{'type': 'Plain', 'text': '缺少参数'}]
                        发送消息('sendFriendMessage', 好友qq, 消息链)
                        continue
                    if int(时间) > 60 or int(时间) < 1:
                        消息链 = [{'type': 'Plain', 'text': '时间范围错误'}]
                    else:
                        轰炸(电话, 时间, 好友qq)
                        continue
                else:
                    消息链 = [{'type': 'Plain', 'text': '你没有被授权,请咨询3055843259'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

            elif '轰炸授权|' in 指令:
                if 好友qq == 3055843259 or 好友qq == 417800:
                    try:
                        被操作者 = 指令.split('|')[1]
                    except IndexError:
                        消息链 = [{'type': 'Plain', 'text': '参数缺失'}]
                        发送消息('sendFriendMessage', 好友qq, 消息链)
                        continue
                    if 指令.startswith('删除'):
                        if 被操作者 not in 轰炸授权:
                            消息链 = [{'type': 'Plain', 'text': '此qq号不在授权列表中'}]
                        else:
                            轰炸授权.remove(被操作者)
                            保存授权(轰炸授权)
                            消息链 = [{'type': 'Plain', 'text': '删除成功'}]
                    elif 指令.startswith('添加'):
                        if 被操作者 in 轰炸授权:
                            消息链 = [{'type': 'Plain', 'text': '此qq号已在授权列表中'}]
                        else:
                            轰炸授权.append(被操作者)
                            保存授权(轰炸授权)
                            消息链 = [{'type': 'Plain', 'text': '添加成功'}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '权限不足'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)


            elif 指令.startswith('消息推送'):
                if 好友qq in 超管名单:
                    消息 = 指令[5:]
                    群列表 = 获取群列表()
                    线程_推送 = Thread(target=消息推送, args=(群列表,消息,)).start()
                    所需时长 = len(群列表) * 2.3
                    消息链 = [{'type': 'Plain', 'text': '已经启动推送线程,大约需要%s秒推送完成'%所需时长}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '权限不足'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

    elif 数据信息 == 'TempMessage':
        返回数据 = loads(返回数据)['data']
        好友qq = 返回数据['sender']['id']
        好友昵称 = 返回数据['sender']['memberName']
        好友权限 = 返回数据['sender']['permission']
        群昵称 = 返回数据['sender']['group']['name']
        机器人权限 = 返回数据['sender']['group']['permission']
        群号 = 返回数据['sender']['group']['id']
        if 返回数据['messageChain'][1]['type'] == 'Plain':
            指令 = 返回数据['messageChain'][1]['text']
            临时会话消息日志 = [数据信息, 群昵称, str(群号), 好友权限, 好友昵称, str(好友qq), 指令]
            日志输出(临时会话消息配色, 临时会话消息日志)

            if 指令 == 'acg' or 指令 == '真人' or 指令 == '获取pixiv':
                if 群号 not in 配置['功能']['acg'] or 群号 not in 配置['功能']['真人'] or 群号 not in 配置['功能']['pixiv']:
                    if 指令 == 'acg' and 总开关['acg']:
                        线程_色色 = Thread(target=色色, args=('acg', 'sendTempMessage', 好友qq, 群号)).start()
                    elif 指令 == '真人' and 总开关['真人']:
                        线程_色色 = Thread(target=色色, args=('真人', 'sendTempMessage', 好友qq, 群号)).start()
                    elif 指令 == '获取pixiv' and 总开关['pixiv']:
                        线程_色色 = Thread(target=pixiv, args=('sendTempMessage', 好友qq, 群号)).start()
                    else:
                        消息链 = [{'type': 'Plain', 'text': '此功能未开启'}]
                        发送群临时消息(好友qq, 群号, 消息链)
                else:
                    消息链 = [{'type': 'Plain', 'text': '您不在授权群'}]
                    发送群临时消息(好友qq, 群号, 消息链)

            elif 指令 == '商店':
                消息链 = [{'type': 'Plain', 'text': 商店内容}]
                发送群临时消息(好友qq, 群号, 消息链)
                消息链 = [{'type': 'Plain', 'text': '请按照商品价格缴费,缴费后请截图发给群主'}, {'type': 'Image', 'path': 商店收款码地址}]
                发送群临时消息(好友qq, 群号, 消息链)
        else:
            continue

    elif 数据信息 == 'BotInvitedJoinGroupRequestEvent':
        返回数据 = loads(返回数据)['data']
        事件编号 = 返回数据['eventId']
        邀请人qq = 返回数据['fromId']
        邀请人昵称 = 返回数据['nick']
        进群号 = 返回数据['groupId']
        进群名 = 返回数据['groupName']
        接受进群邀请(事件编号, 邀请人qq, 进群号)

    elif 数据信息 == 'NewFriendRequestEvent':
        返回数据 = loads(返回数据)['data']
        事件编号 = 返回数据['eventId']
        申请人qq = 返回数据['fromId']
        来源群号 = 返回数据['groupId']
        申请人昵称 = 返回数据['nick']
        接受好友申请(事件编号, 申请人qq, 来源群号)

    elif 数据信息 == '' and 'data' in loads(返回数据) and 'messageId' in loads(返回数据)['data']:
        返回数据 = loads(返回数据)['data']
        print(返回数据)
        信息编号 = 返回数据['messageId']
        历史信息获取链接 = http接口 + 'messageFromId?id=%s'%信息编号
        返回历史信息 = loads(get(历史信息获取链接).text)['data']
        历史信息类型 = 返回历史信息['type']

        if 历史信息类型 == 'GroupMessage':
            历史消息文本 = ''
            消息文本 = ''
            历史主要信息 = 返回历史信息['messageChain']
            历史发送信息 = 返回历史信息['sender']
            for 循环对象 in 历史主要信息:
                消息类型_取文本 = 循环对象['type']
                if 消息类型_取文本 == 'Plain':
                    消息文本 += 循环对象['text']

                elif 消息类型_取文本 == 'At':
                    消息文本 += '{@%d}' % 循环对象['target']

                elif 消息类型_取文本 == 'AtAll':
                    消息文本 += '[@All]'

                elif 消息类型_取文本 == 'Face':
                    消息文本 += '[表情:%s]' % 循环对象['name']

                elif 消息类型_取文本 == 'Image':
                    图片识别信息 = 文字识别对象.ocr('运行时图片.png')
                    文字识别结果 = ''
                    for 循环对象甲 in 图片识别信息:
                        for 循环对象乙 in 循环对象甲[0]:
                            文字识别结果 += 循环对象乙
                    文字识别结果 = 文字识别结果.lower().replace(' ', '')  # 去除空格,转小写
                    消息文本 += '[文字识别:%s]' % 文字识别结果

                elif 消息类型_取文本 == 'File':
                    消息文本 += '[文件名称: {} , 文件大小: {}]'.format(循环对象['name'], 循环对象['size'])

                elif 消息类型_取文本 == 'MiraiCode':
                    消息文本 += 'MiraiCode: %s' % 循环对象['code']
            历史消息文本 = 消息文本.strip().replace(' ', '')

            历史群消息日志 = [历史信息类型, 历史发送信息['group']['name'], str(历史发送信息['group']['id']),
                       历史发送信息['permission'], 历史发送信息['memberName'], str(历史发送信息['id']), 历史消息文本]
            日志输出(群消息配色, 历史群消息日志)

        else:
            console.log(返回历史信息)

    else:
        # 输出剩余日志
        console.log(返回数据.replace('[/', '['))  # 规避rich语法
