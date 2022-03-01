# -*- coding : utf-8-*-
from os import getcwd
from cnocr import CnOcr
from PIL import Image
from random import randint
from threading import Thread
from json import loads, dumps
from re import compile, search
from requests import get, post
from time import localtime, strftime, time
from websocket import WebSocket, send, recv
from psutil import cpu_percent, virtual_memory

print('初始化中.....')

文字识别对象 = CnOcr(model_name='densenet_lite_136-gru')
服务器对象 = WebSocket()
post('http://localhost:23323/verify')
服务器对象.connect('ws://localhost:23423/all?verifyKey=INITKEYsV4Mnulq&qq=2303798671')

初始地址 = '{}/附属/'.format(getcwd().replace('\\', '/'))
工具箱地址 = 初始地址 + 'hwid.txt'
小号地址 = 初始地址 + 'Accounts.txt'
违禁词地址 = 初始地址 + 'bw.txt'
消息存储地址 = 初始地址 + 'msg_pull.txt'
图片存储地址 = 初始地址 + 'qq_image/'
水影地址 = 初始地址 + 'liquid_hwid.txt'
配置地址 = 初始地址 + 'Robot.config'
商店收款码地址 = 初始地址 + '商店付款码.jpg'
商店内容地址 = 初始地址 + '商店内容.txt'
http接口 = 'http://localhost:23323/'
二次元接口 = ['https://api.mtyqx.cn/tapi/random.php', 'https://api.ixiaowai.cn/api/api.php',
         'https://tenapi.cn/acg', 'https://api.mz-moe.cn/img.php', 'https://api.dujin.org/pic/yuanshen/']
真人接口 = ['https://api.nmb.show/xiaojiejie1.php', 'https://api.nmb.show/xiaojiejie2.php']
头像接口 = ['https://api.sunweihu.com/api/sjtx/api.php?lx=']
手机查询 = ['https://api.muxiaoguo.cn/api/chePhone?phoneNum=']
第一条消息 = 0
小号限制 = time()
上一次消息 = ''
上一次发送者 = 0
上一次群号 = 0
消息重复次数 = 0
发送者重复次数 = 0
qq号 = 0
手机号 = 0
地区 = ''


# LOL名 = ''
# LOL大区 = ''


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


def 发送消息(消息关键字, 发送目标, 消息链):
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


def 获取群列表():
    链接 = http接口 + 'groupList'
    请求对象 = get(链接)
    请求结果 = loads(请求对象.text)['data']
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


def 恶俗(模式, 目标, 群号):
    global qq号, 手机号, 地区

    def qq查手机(目标qq):
        global qq号, 手机号, 地区
        请求对象 = get('http://ww.you-api.icu/qb.php?mod=cha&qq=%s' % 目标qq)
        恶俗结果 = loads(请求对象.text)
        if 恶俗结果['msg'] != '没有找到':
            qq号 = 目标qq
            手机号 = 恶俗结果['data']['mobile']
            地区 = 恶俗结果['data']['mobile_area']
        else:
            qq号 = 目标qq
            手机号 = 'None'
            地区 = '地球村'

    def 手机查qq(目标手机号):
        global qq号, 手机号, 地区
        请求对象 = get('http://ww.you-api.icu/bq.php?mod=cha&qq=%s' % 目标手机号)
        恶俗结果 = loads(请求对象.text)
        if 恶俗结果['msg'] != '没有找到':
            qq号 = 恶俗结果['data']['qq']
            手机号 = 目标手机号
            地区 = 恶俗结果['data']['mobile_area']
        else:
            qq号 = 'None'
            手机号 = 目标手机号
            地区 = '地球村'

    # def qq_查LOL(目标qq号):
    #     global LOL大区, LOL名
    #     请求对象 = get('http://zy.xywlapi.cc/qqlol?qq=%s' % 目标qq号)
    #     恶俗结果 = loads(请求对象.text)
    #     if 恶俗结果['message'] != '没有找到':
    #         LOL名 = 恶俗结果['name']
    #         LOL大区 = 恶俗结果['daqu']
    #     else:
    #         LOL名 = 'None'
    #         LOL大区 = 'None'

    if 模式 == '查询':
        线程_恶俗1 = Thread(target=qq查手机, args=(目标,))
        线程_恶俗1.start()
        线程_恶俗1.join()
        # 线程_恶俗2 = Thread(target=qq_查LOL, args=(目标,))
        # 线程_恶俗2.start()
        # 线程_恶俗2.join()
        恶俗消息 = '''QQ: {}
手机号: {}
地区: {}'''.format(qq号, 手机号, 地区)
        消息链 = [{'type': 'Image', 'url': 'https://tenapi.cn/qqimg/?qq=%s' % 目标}, {'type': 'Plain', 'text': 恶俗消息}]
    else:
        线程_恶俗3 = Thread(target=手机查qq, args=(目标,))
        线程_恶俗3.start()
        线程_恶俗3.join()
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


def 保存小号(小号列表):
    小号文本 = ''
    for 循环对象 in 小号列表:
        小号文本 += 循环对象 + '\n'
    with open(小号地址, 'w', encoding='gbk') as f:
        f.write(小号文本.strip())


def 保存配置(配置):
    配置_json = dumps(配置, ensure_ascii=False, sort_keys=True, indent=5)
    with open(配置地址, 'w', encoding='gbk') as 文件对象:
        文件对象.write(配置_json)


with open(违禁词地址, 'r', encoding='gbk') as 文件对象:
    违禁词列表 = 文件对象.read().split('\n')

with open(配置地址, 'r', encoding='gbk') as 文件对象:
    配置_json格式 = 文件对象.read()

with open(商店内容地址, 'r', encoding='gbk') as 文件对象:
    商店内容 = 文件对象.read()

with open(小号地址, 'r') as 文件对象:
    小号列表 = 文件对象.read().split('\n')

配置 = loads(配置_json格式)
白名单列表 = 配置['名单']['白名单']
黑名单 = 配置['名单']['黑名单']
超管名单 = 配置['名单']['超管']
总开关 = 配置['总开关']
验证开关 = 配置['验证']
功能开关 = 配置['功能']

print('初始化完成!')

while True:
    第一条消息 += 1

    # 接收
    try:
        返回数据 = 服务器对象.recv()
    except:
        服务器对象.connect('ws://localhost:23423/all?verifyKey=INITKEYsV4Mnulq&qq=2303798671')
        返回数据 = 服务器对象.recv()
    if 第一条消息 == 1:
        continue

    # 输出日志
    print(返回数据)

    if '"type":"GroupMessage"' in 返回数据:
        # 定义基本信息
        返回数据 = loads(返回数据)['data']
        主要消息 = 返回数据['messageChain']
        发送者 = 返回数据['sender']['id']
        群号 = 返回数据['sender']['group']['id']
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
                # 图片存储
                消息链接 = 循环对象['url']
                图片 = get(消息链接)
                with open('运行时图片.png', 'wb') as 文件对象:
                    文件对象.write(图片.content)
                with open(图片存储地址 + strftime("%Y-%m-%d&%X", localtime()).replace(':', '-') + '.png',
                          'wb') as 文件对象:
                    文件对象.write(图片.content)

                # 图片下载
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
        消息文本 = 消息文本.lower().strip().replace(' ', '')
        print(消息文本)

        # 云黑检测
        if 发送者 in 黑名单:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                踢出群员(群号, 发送者, '检测到您在云黑系统中,可找3055843259申诉!')
                消息链 = 消息链 = [{'type': 'Plain', 'text': '发现已被云黑收录的目标%s,\n已进行踢出!' % 发送者}]
                发送消息('sendGroupMessage', 群号, 消息链)

        # 频率验证
        # 计算次数
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
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发频率检测!'}]
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
        消息长度 += 消息文本.count('[文字识别:') * 50
        if 群号 in 配置['功能']['群管'] and 消息长度 > 130 and 总开关['群管']:
            if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                if 发送者 not in 白名单列表:
                    禁言群员(群号, 发送者)
                    撤回消息(消息编号)
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发字数检测!'}]
                    发送消息('sendGroupMessage', 群号, 消息链)
                    continue

        elif 消息文本 == '#up':
            if 群号 in 配置['验证']['#up'] and 总开关['#up']:
                with open(工具箱地址, 'r', encoding='gbk') as 文件对象:
                    已验证名单 = 文件对象.read()
                if str(发送者) in 已验证名单:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您已验证过!'}]
                else:
                    with open(工具箱地址, 'a', encoding='gbk') as 文件对象:
                        文件对象.write(str(发送者) + ',')
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '验证成功!'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('#水影'):
            if 群号 in 配置['验证']['#水影'] and 总开关['#水影']:
                水影验证码 = 消息文本[3:]
                with open(水影地址, 'r', encoding='gbk') as 文件对象:
                    已验证名单 = 文件对象.read()
                if 水影验证码 in 已验证名单:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您已验证过!'}]
                elif len(水影验证码) != 15:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '格式错误!'}]
                else:
                    with open(水影地址, 'a', encoding='gbk') as 文件对象:
                        文件对象.write('[{}]{}\n'.format(发送者, 水影验证码))
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '验证成功!'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群!'}]
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
            状态消息 = '''机器人名称: 影子、淺笑
QQ号: 2303798671
CPU占用 : {}%
内存占用: {}%
By Edwad_过客[3055843259]'''.format(CPU占用, 内存占用)
            消息链 = [{'type': 'Plain', 'text': 状态消息}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == 'acg' or 消息文本 == '真人':
            if 群号 in 配置['功能']['acg'] or 群号 in 配置['功能']['真人']:
                if 总开关['acg'] or 总开关['真人']:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '请私聊机器人!'}]
                    if 发送者 == 3055843259:
                        线程_色色 = Thread(target=色色, args=('acg', 'sendGroupMessage', 群号, '',)).start()
                else:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启!'}]
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('获取头像|'):
            if 群号 in 配置['功能']['获取头像'] and 总开关['获取头像']:
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
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '您不在授权群!'}]
                发送消息('sendGroupMessage', 群号, 消息链)
            else:
                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启!'}]
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
                        反馈 = '启用成功!'
                    else:
                        反馈 = '关闭成功!'
                else:
                    反馈 = '没有此项!'
            else:
                反馈 = '没有权限!'
            保存配置(配置)
            消息链 = [{'type': 'Plain', 'text': 反馈}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('&启用') or 消息文本.startswith('&关闭'):
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
                                if 群号 not in 配置_[键]:
                                    配置_[键].append(群号)
                            else:
                                if 群号 in 配置_[键]:
                                    配置_[键] = 配置_[键].remove(群号)
                    else:
                        if '启用' in 消息文本:
                            if 群号 not in 配置_[指令]:
                                配置_[指令].append(群号)
                        else:
                            if 群号 in 配置_[指令]:
                                配置_[指令].remove(群号)
                    if '启用' in 消息文本:
                        反馈 = '启用成功!'
                    else:
                        反馈 = '关闭成功!'
                else:
                    反馈 = '没有此项!'
            else:
                反馈 = '没有权限!'
            保存配置(配置)
            消息链 = [{'type': 'Plain', 'text': 反馈}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '查看总开关':
            授权消息 = '[总开关]\n'
            for 键, 值 in 总开关.items():
                if 总开关:
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
            if 群号 in 配置['功能']['查询'] or 群号 in 配置['功能']['反查']:
                if 总开关['查询'] or 总开关['反查']:
                    目标 = 消息文本[2:]
                    if 消息文本.startswith('查询'):
                        线程_恶俗 = Thread(target=恶俗, args=('查询', 目标, 群号)).start()
                    else:
                        线程_恶俗 = Thread(target=恶俗, args=('反查', 目标, 群号)).start()
                else:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '此功能未开启!'}]
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
                消息链 = [{'type': 'Plain', 'text': '解禁成功!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('禁言'):
            if 发送者 in 超管名单:
                if '@' in 消息文本:
                    被禁言者 = 查找(消息文本, 1, "{@([0-9]*)}")
                else:
                    被禁言者 = 查找(消息文本, 1, '禁言([0-9]*)|')
                时长 = 消息文本.split('|')[1]
                禁言群员(群号, 被禁言者, int(时长))
                消息链 = [{'type': 'Plain', 'text': '禁言已进行!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
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
                消息链 = [{'type': 'Plain', 'text': '已进行踢出!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '私聊获取小号':
            if 群号 in 配置['功能']['私聊获取小号'] and 总开关['私聊获取小号']:
                if 小号限制 + 30 <= time() or 发送者 in 超管名单:
                    模板 = 配置['格式']['小号格式']
                    小号 = 小号列表[0].split('----')
                    渲染 = 模板.format(小号[0], 小号[1], len(小号列表) - 1).replace('\\n', '\n')
                    小号限制 = time()
                    消息链 = [{'type': 'Plain', 'text': '小号已私发!'}]
                    发送消息('sendGroupMessage', 群号, 消息链)
                    消息链 = [{'type': 'Plain', 'text': 渲染}]
                    发送群临时消息(发送者, 群号, 消息链)
                    小号列表.pop(0)
                    保存小号(小号列表)
                else:
                    消息链 = [{'type': 'Plain', 'text': '小号冷却中,还剩下%s秒!' % str(小号限制 + 30 - time()).split('.')[0]}]
                    发送消息('sendGroupMessage', 群号, 消息链)
            else:
                消息链 = [{'type': 'Plain', 'text': '您不在授权群!'}]
                发送消息('sendGroupMessage', 群号, 消息链)


        elif 消息文本 == '获取小号':
            if 群号 in 配置['功能']['获取小号'] and 总开关['获取小号']:
                if 小号限制 + 30 <= time() or 发送者 in 超管名单:
                    模板 = 配置['格式']['小号格式']
                    小号 = 小号列表[0].split('----')
                    渲染 = 模板.format(小号[0], 小号[1], len(小号列表) - 1).replace('\\n', '\n')
                    消息链 = [{'type': 'Plain', 'text': 渲染}]
                    小号限制 = time()
                    小号列表.pop(0)
                    保存小号(小号列表)
                else:
                    消息链 = [{'type': 'Plain', 'text': '小号冷却中,还剩下%s秒!' % str(小号限制 + 30 - time()).split('.')[0]}]
            else:
                消息链 = [{'type': 'Plain', 'text': '您不在授权群!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('添加违禁'):
            if 发送者 in 超管名单:
                违禁词 = 消息文本[5:]
                if 违禁词 in 违禁词列表:
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '已有此违禁词!'}]
                else:
                    违禁词列表.append(违禁词)
                    添加违禁词(违禁词)
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '添加成功!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '没有权限!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('删除违禁'):
            if 发送者 in 超管名单:
                违禁词 = 消息文本[5:]
                if 违禁词.strip() == '':
                    消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '违禁词无效!'}]
                else:
                    try:
                        违禁词列表.remove(违禁词)
                        删除违禁词(违禁词)
                        消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '删除成功!'}]
                    except ValueError:
                        消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '没有此违禁词!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '没有权限!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本 == '查看云黑':
            名单人数 = len(黑名单)
            消息链 = [{'type': 'Plain', 'text': '云黑系统已收容%s人!' % 名单人数}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('云黑检测|'):
            qq号 = int(消息文本.split('|')[1])
            if qq号 in 黑名单:
                消息链 = [{'type': 'Plain', 'text': '此QQ已被云黑收录!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '此QQ未被云黑收录!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('添加云黑|'):
            if 发送者 in 超管名单:
                qq号 = int(消息文本.split('|')[1])
                if qq号 in 黑名单:
                    消息链 = [{'type': 'Plain', 'text': '此QQ已被收录!'}]
                else:
                    黑名单.append(qq号)
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '收录成功!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        elif 消息文本.startswith('删除云黑|'):
            if 发送者 in 超管名单:
                qq号 = int(消息文本.split('|')[1])
                if qq号 in 黑名单:
                    黑名单.remove(qq号)
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '删除成功!'}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '此QQ未收录!'}]
            else:
                消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
            发送消息('sendGroupMessage', 群号, 消息链)

        else:
            # 违禁词检测
            if 发送者 not in 白名单列表 and 群号 in 配置['功能']['群管'] and 总开关['群管']:
                if 机器人管理员 != 'MEMBER' and 管理员 == 'MEMBER':
                    for 循环对象 in 违禁词列表:
                        if 循环对象 in 消息文本 or 循环对象 in 发送者昵称:
                            if 循环对象 in 消息文本:
                                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发违禁词检测!'}]
                            elif 循环对象 in 发送者昵称:
                                消息链 = [{'type': 'At', 'target': 发送者}, {'type': 'Plain', 'text': '触发ID检测!'}]
                            禁言群员(群号, 发送者)
                            撤回消息(消息编号)
                            发送消息('sendGroupMessage', 群号, 消息链)
                            break

    elif '"type":"FriendMessage"' in 返回数据 or '"type":"StrangerMessage"' in 返回数据:
        返回数据 = loads(返回数据)['data']
        好友qq = 返回数据['sender']['id']
        if 返回数据['messageChain'][1]['type'] == 'Plain':
            指令 = 返回数据['messageChain'][1]['text']
            if 指令 == 'acg' or 指令 == '真人':
                if 指令 == 'acg':
                    线程_色色 = Thread(target=色色, args=('acg', 'sendFriendMessage', 好友qq, '',)).start()
                else:
                    线程_色色 = Thread(target=色色, args=('真人', 'sendFriendMessage', 好友qq, '',)).start()
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
                    消息链 = [{'type': 'Plain', 'text': '反馈成功!'}]
                    发送消息('sendFriendMessage', 好友qq, 消息链)
            elif 指令 == '商店':
                消息链 = [{'type': 'Plain', 'text': 商店内容}]
                发送消息('sendFriendMessage', 好友qq, 消息链)
                消息链 = [{'type': 'Plain', 'text': '请按照商品价格缴费,缴费后请截图发给群主'}, {'type': 'Image', 'path': 商店收款码地址}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令.startswith('定义小号格式'):
                if 好友qq in 超管名单:
                    小号格式 = 指令[6:]
                    配置['格式']['小号格式'] = 小号格式
                    保存配置(配置)
                    消息链 = [{'type': 'Plain', 'text': '定义格式成功!'}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

            elif 指令.startswith('消息推送'):
                if 好友qq in 超管名单:
                    推送群数 = 0
                    消息 = 指令[5:]
                    群列表 = 获取群列表()
                    消息链 = [{'type': 'Plain', 'text': '[影子]消息推送\n%s' % 消息}]
                    for 循环对象 in 群列表:
                        if 循环对象['permission'] != 'MEMBER':
                            发送消息('sendGroupMessage', 循环对象['id'], 消息链)
                            推送群数 += 1
                    消息链 = [{'type': 'Plain', 'text': '推送成功!\n总共{}个群聊,已推送至{}个群聊'.format(len(群列表), 推送群数)}]
                else:
                    消息链 = [{'type': 'Plain', 'text': '权限不足!'}]
                发送消息('sendFriendMessage', 好友qq, 消息链)

    elif '"type":"TempMessage"' in 返回数据:
        返回数据 = loads(返回数据)['data']
        好友qq = 返回数据['sender']['id']
        群号 = 返回数据['sender']['group']['id']
        if 返回数据['messageChain'][1]['type'] == 'Plain':
            指令 = 返回数据['messageChain'][1]['text']
            if 指令 == 'acg' or 指令 == '真人':
                if 群号 in 配置['功能']['acg'] or 群号 in 配置['功能']['真人']:
                    if 指令 == 'acg':
                        线程_色色 = Thread(target=色色, args=('acg', 'sendTempMessage', 好友qq, 群号)).start()
                    else:
                        线程_色色 = Thread(target=色色, args=('真人', 'sendTempMessage', 好友qq, 群号)).start()
                else:
                    消息链 = [{'type': 'Plain', 'text': '您不在授权群!'}]
                    发送群临时消息(好友qq, 群号, 消息链)
            elif 指令 == '商店':
                消息链 = [{'type': 'Plain', 'text': 商店内容}]
                发送群临时消息(好友qq, 群号, 消息链)
                消息链 = [{'type': 'Plain', 'text': '请按照商品价格缴费,缴费后请截图发给群主'}, {'type': 'Image', 'path': 商店收款码地址}]
                发送群临时消息(好友qq, 群号, 消息链)
        else:
            continue