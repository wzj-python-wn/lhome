# coding:utf-8

import os

from handlers import Passport, VerifyCode, Profile, House
from handlers.BaseHandler import StaticFileHandler

handlers = [
    (r"/api/imagecode", VerifyCode.ImageCodeHandler),
    (r"/api/smscode", VerifyCode.SMSCodeHandler),
    (r'^/api/register$', Passport.RegisterHandler),
    (r'^/api/login$', Passport.LoginHandler),
    (r'^/api/check_login$', Passport.CheckLoginHandler),
    (r'^/api/profile/avatar$', Profile.AvatarHandler),
    (r'^/api/profile/name$', Profile.NameHandler),
    (r'^/api/profile/auth$', Profile.AuthHandler),
    (r'^/api/house/area$', House.AreaInfoHandler),
    (r'^/api/house/my$', House.MyHousesHandler),
    (r'^/api/house/info$', House.HouseInfoHandler),
    (r'^/api/house/image$', House.HouseImageHandler),
    (r'^/api/house/index$', House.IndexHandler),
    (r'^/api/house/list$', House.HouseListHandler),
    (r'^/api/house/listv2$', House.HouseListHandlerV2),
    (r"/(.*)", StaticFileHandler, dict(path=os.path.join(os.path.dirname(__file__), "html"), default_filename="index.html"))
]