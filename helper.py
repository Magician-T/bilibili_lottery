#!/usr/bin/env python
# -*- coding=utf-8 -*-

import requests
from random import sample


def get_commenters(video_id):
    print("获取评论用户...")
    url_template = "https://api.bilibili.com/x/v2/reply?type=1&oid={}&pn={}&nohot=1&sort=0"
    commenters = {}
    pn = 1
    while True:
        url = url_template.format(video_id, pn)
        r = requests.get(url)
        j = r.json()
        replies = j["data"]["replies"]
        if not replies:
            break
        for reply in replies:
            mid = reply["mid"]
            user_name = reply["member"]["uname"]
            commenters[mid] = user_name
        pn += 1
    print("获取评论用户...完成!")
    return commenters


def get_followers(user_id, cookies):
    print("获取粉丝列表...")
    url_template = "https://api.bilibili.com/x/relation/followers?vmid={}&pn={}&ps=20&order=desc"
    followers = {}
    pn = 1
    while True:
        url = url_template.format(user_id, pn)
        r = requests.get(url, cookies=cookies)
        j = r.json()
        if j["code"] > 0:
            print("警告: 由于cookie设置不正确, {}".format(j["message"]))
            break
        followers_list = j["data"]["list"]
        if not followers_list:
            break
        for follower in followers_list:
            mid = follower["mid"]
            user_name = follower["uname"]
            followers[mid] = user_name
        pn += 1
    print("获取粉丝列表...完成!")
    return followers


def draw(pool, num_winners):
    return sample(pool, num_winners)
