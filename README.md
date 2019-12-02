# bilibili_lottery

B站UP主抽奖脚本，从评论+关注的用户中抽取若干名幸运观众

## 使用说明

1. 打开`config.py`修改相关参数

|参数名|说明|
|:-:|:-:|
|VIDEO_ID|视频代码，例如av76438397，取数字部分76438397|
|USER_ID|UP主用户代码|
|NUM_WINNERS|计划抽取的获奖人数|
|COOKIE|B站cookie，必须正确设置才能获取完整粉丝列表|

2. 安装依赖

`$ pip install -r requirements`

3. 运行抽奖脚本

`$ python draw.py`

## 测试说明

1. （可选）打开`config.py`修改相关参数

|参数名|说明|
|:-:|:-:|
|TEST_POOL_SIZE|测试奖池人数|
|TEST_WINNERS|测试获奖人数|
|TEST_EXPERIMENTS|测试实验次数|

2. 运行测试

`$ python test.py`
