#!/usr/bin/env python
# -*- coding=utf-8 -*-

from config import VIDEO_ID, USER_ID, NUM_WINNERS
from helper import get_commenters, get_followers, draw

if __name__ == '__main__':
    with open("cookies.txt", "r") as f:
        raw = f.read().strip()
        cookies = dict(cookies_are=raw)
    commenters = get_commenters(VIDEO_ID)
    del commenters[USER_ID]
    followers = get_followers(USER_ID, cookies)
    pool = set(commenters.keys()) & set(followers.keys())
    winners = draw(pool, NUM_WINNERS)
    print("*************************************")
    print("抽奖结果: ")
    for i in range(len(winners)):
        print("第{}位获奖观众: {} - https://space.bilibili.com/{}".format(i +
                                                                    1, followers[winners[i]], winners[i]))
