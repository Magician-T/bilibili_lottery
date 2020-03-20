#!/usr/bin/env python
# -*- coding=utf-8 -*-


from config import VIDEO_ID, NUM_WINNERS
from helper import get_commenters, draw, get_beijing_time


if __name__ == '__main__':
    print("北京时间: {}".format(get_beijing_time()))
    with open("cookies.txt", "r") as f:
        raw = f.read().strip()
        cookies = dict(cookies_are=raw)
    followed, not_followed = get_commenters(VIDEO_ID, cookies)
    pool = set(followed.keys())
    winners = draw(pool, NUM_WINNERS)
    print("*************************************")
    print("抽奖结果: ")
    for i in range(len(winners)):
        print("第{}位获奖观众: {} - https://space.bilibili.com/{}".format(
            i + 1, followed[winners[i]], winners[i]))
