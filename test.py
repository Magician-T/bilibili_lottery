#!/usr/bin/env python
# -*- coding=utf-8 -*-

from helper import draw
from config import TEST_POOL_SIZE, TEST_WINNERS, TEST_EXPERIMENTS, TEST_DM_RATIO
import sys


all_users = [i for i in range(TEST_POOL_SIZE)]
dm_users = set(draw(all_users, int(TEST_POOL_SIZE * TEST_DM_RATIO)))
pool = sorted(all_users + list(dm_users))


def test_config_params():
    if TEST_POOL_SIZE <= 0 or TEST_WINNERS <= 0 or TEST_EXPERIMENTS <= 0:
        print("测试参数设定错误，各项测试参数均应大于零")
        raise ValueError
    if TEST_POOL_SIZE < TEST_WINNERS:
        print("测试参数设定错误，抽奖人数应小于等于奖池人数")
        raise ValueError
    if TEST_DM_RATIO >= 1 or TEST_DM_RATIO <= 0:
        print("弹幕人数比例应大于0小于1")
        raise ValueError


if __name__ == '__main__':
    try:
        test_config_params()
    except ValueError:
        sys.exit(1)
    print("测试开始...")
    print("将进行{}次实验，每次抽取{}名获奖观众".format(TEST_EXPERIMENTS, TEST_WINNERS))
    mean = TEST_EXPERIMENTS * \
        TEST_WINNERS // (TEST_POOL_SIZE * (1 + TEST_DM_RATIO))
    print("理想状况下，未发弹幕用户被抽中次数应接近{}，弹幕用户被抽中次数应接近{}".format(int(mean), int(mean * 2)))
    results = {}
    for i in range(TEST_EXPERIMENTS):
        result = draw(pool, TEST_WINNERS)
        for key in result:
            results[key] = results.get(key, 0) + 1
    dm_results = []
    no_dm_results = []
    for i in results:
        if i in dm_users:
            dm_results.append(results[i])
        else:
            no_dm_results.append(results[i])
    print("实验结束，结果如下：")
    print("未发弹幕用户最少被抽中{}次，最多被抽中{}次".format(
        min(no_dm_results), max(no_dm_results)))
    print("弹幕用户最少被抽中{}次，最多被抽中{}次".format(min(dm_results), max(dm_results)))
