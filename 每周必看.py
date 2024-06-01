import urllib.request
import json
import pickle

a=input("请输入第几期（纯数字）：")
try:
    number = int(a)  # 每周必看第几期
except ValueError as e:
    input("解析失败，请输入纯数字："+str(e))
    raise
_list = []  # 保存列表


def false():
    return False
    # What is?


def null():
    return None
    # What is,too?


def write():
    # 写入方法2(pickle)
    pickle_file = open("./must_see_every_week.pkl", 'wb')
    pickle.dump(_list, pickle_file)
    pickle_file.close()


head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62'}
url = "https://api.bilibili.com/x/web-interface/popular/series/one?number=" + str(number)
# url与head(目标网站与头文件)
response = urllib.request.Request(url, headers=head)  # 爬取
try:
    f = urllib.request.urlopen(response)  # 获取api
except urllib.error.URLError as e:
    input("爬取异常，请连接互联网并检查网络设置："+str(e))
    raise
f = f.read().decode("utf-8")  # 解码
f = json.loads(f)  # 将字符串编码成字典
# print(type(f))
# print(f)
# print("================================")
# 测试代码，不必理会
try:
    f['data']
except KeyError:
    print("你访问的太频繁了，等一下再试啦")  # 访问过于频繁会没有"data"键
else:
    for i in range(len(f['data']['list'])):
        a = [i]
        print("编号", a[0])
        a.append(f['data']['list'][i]['title'])
        print("标题：", a[1])
        a.append(f['data']['list'][i]['pic'])
        print("封面图片：", a[2])
        a.append(f['data']['list'][i]['owner']['name'])
        print("up主：", a[3])
        a.append(f['data']['list'][i]['short_link_v2'])
        print("链接：", a[4])
        a.append(f['data']['list'][i]["desc"])
        print("简介：", a[5])
        a.append(f['data']['list'][i]['rcmd_reason'])
        print("热门评论：", a[6])
        # a = [编号,标题,封面图片,up主,链接,简介,热门评论]
        _list.append(a)  # 将a追加至_list列表
        print("================================")
    print("共记", len(f['data']['list']), "条")  # 统计
    input("end")
    write()
