#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
from random import sample
from datetime import datetime, timedelta, timezone


def get_commenters(video_id, cookies):
    print("获取评论用户...")
    url_template = "https://member.bilibili.com/x/web/replies?order=ctime&filter=-1&is_hidden=0&type=1&bvid={}&pn={}&ps=10"
    followed = {}
    not_followed = {}
    pn = 1
    comment_cnt = 0
    while True:
        url = url_template.format(video_id, pn)
        r = requests.get(url, cookies=cookies)
        j = r.json()
        comments = j["data"]
        if not comments:
            break
        for comment in comments:
            mid = comment["mid"]
            user_name = comment["replier"]
            if comment["relation"] == 2:
                followed[mid] = user_name
            else:
                not_followed[mid] = user_name
            comment_cnt += 1
            if comment_cnt % 200 == 0:
                print("已读取{}条评论...".format(comment_cnt))
        pn += 1
    print("共读取{}条评论，包含{}名用户，{}人已关注".format(comment_cnt,
                                           len(followed) + len(not_followed), len(followed)))
    return followed, not_followed


def draw(pool, num_winners):
    return sample(pool, num_winners)


def get_beijing_time():
    utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
    bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
    return bj_dt.strftime("%Y-%m-%d, %H:%M:%S")
