# -*- coding: utf-8 -*-

from mp.config import Config
from .error import Error
from .mpmessage_model import MPMessageModel
from .wechat import WeChat
from .wechat_session import WeChatSession


error = Error()
wechat = WeChat(
        token=Config.WECHAT.get('token'),
        appid=Config.WECHAT.get('appid'),
        EncodingAESKey=Config.WECHAT.get('EncodingAESKey'))
session = WeChatSession()
