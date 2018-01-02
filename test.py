# -*- coding:utf-8 -*-

import orm
from models import User, Blog, Comment
import asyncio, logging
import aiomysql
logging.basicConfig(level=logging.INFO)

def test():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(orm.create_pool(host='127.0.0.1', port=3306, user="root", password="", db="awesome", loop=loop))
    u = User(name='test1', email='test@example', passwd='12345', image='about:blank',id="001514872645462fbf6c845b6ab4ade861573c15267afc9000")
    rs = loop.run_until_complete(u.update())

test()