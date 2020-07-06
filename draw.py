#!/usr/bin/env python
# -*- coding=utf-8 -*-

import time
from config import VIDEO_ID, NUM_WINNERS
from helper import get_commenters, get_dm, draw, get_beijing_time


if __name__ == '__main__':
    print("北京时间: {}".format(get_beijing_time()))
    with open("cookies.txt", "r") as f:
        raw = f.read().strip()
        cookies = dict(cookies_are=raw)
    followed, not_followed = get_commenters(VIDEO_ID, cookies)
    dm_users = get_dm(VIDEO_ID, cookies)
    boosted_dm_users = set(followed.keys()) & dm_users
    print("其中{}名弹幕用户同时关注+评论".format(len(boosted_dm_users)))
    print("为弹幕用户提升中奖率...")
    time.sleep(3)  # 为了戏剧张力，等待3秒钟
    pool = sorted(list(followed.keys()) + list(boosted_dm_users))
    winners = draw(pool, NUM_WINNERS)
    print("*************************************")
    print("抽奖结果: ")
    for i in range(len(winners)):
        print("第{}位获奖观众({}发弹幕): {} - https://space.bilibili.com/{}".format(
            i + 1, "已" if winners[i] in boosted_dm_users else "未", followed[winners[i]], winners[i]))
