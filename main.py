import time
import random
from flask import *
from getmusic import *
from getmovie import *
import logging
import os

struct = time.localtime()
year = str(struct[0])
month = str(struct[1])
day = str(struct[2])
week = str(struct[6])
hour = str(struct[4])
minute = str(struct[5])
seconds = str(struct[6])

if week == "0":
    week = "天"
elif week == "1":
    week = "一"
elif week == "2":
    week = "三"
elif week == "3":
    week = "四"
elif week == "4":
    week = "五"
elif week == "5":
    week = "六,周末快乐！"
else:
    week = "日,周末快乐！"

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(filename=year + month + day + 'myapp.log', level=logging.INFO)
logger.info("================================")
logger.info(time.strftime(time.strftime("Start!The time is %Y-%m-%d %H:%M:%S", struct)))
logger.info("================================")
logger.info('Classes initialization completed')


# "/favicon.ico"路由
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


logger.info('"favicon.ico"Route initialization completed')


# "/"路由
@app.route('/')
def index():
    try:
        with open("dress.txt", "r", encoding="UTF-8") as file:
            pic = file.read()
    except:
        pic = "/static/images/g25.gif"
    try:
        with open("music.txt", "r", encoding="UTF-8") as file:
            music = file.read()
    except:
        music = "https://static0.xesimg.com/talcode/webprotect/孤勇者.mp3"
    return render_template("index.html", x=pic, music=music, y=random.choice(
        ("作者不是神，所以网站当然有bug", "作者不止一个人",
         "真正的作者只有一个，其余的是挡箭牌", "作者的爱豆是刘电工", "作者喜欢玩Minecraft",
         "今天是" + year + "年" + month + "月" + day + "日，星期" + week)))


logger.info('Root route initialization completed')


# "/movie"路由
@app.route("/movie")
def movie():
    movie = get_movie()
    # TODO1:将movie数据赋值给movie_list进行传递
    return render_template("movie.html", movie_list=movie)


logger.info('"movie"Route initialization completed')


# "/music"路由
@app.route("/music")
def music():
    music = get_music()
    return render_template("music.html", music_list=music)


logger.info('"music"Route initialization completed')

"""
# "/gx"路由
@app.route("/gx")
def gx():
    return render_template("gx.html")


logger.info('"gx"Route initialization completed')
"""


# "/workroom"路由
@app.route("/workroom")
def workroom():
    return render_template("workroom.html")


logger.info('"workroom"Route initialization completed')


# "/me"路由
@app.route("/me")
def me():
    return render_template("me.html")


logger.info('"me"Route initialization completed')


# "/dress"路由
@app.route("/dress")
def dress():
    return render_template("dress.html")


logger.info('"dress"Route initialization completed')


# "/set_music"路由
@app.route("/set_music")
def set_music():
    global music
    index_music = request.values.get("music")
    with open("music.txt", "w", encoding="UTF-8") as file:
        file.write(index_music)
    return redirect("/")


logger.info('"set_music"Route initialization completed')


# "/show_img"路由
@app.route("/show_img")
def show_img():
    index_img = request.values.get("img")
    with open("dress.txt", "w", encoding="UTF-8") as file:
        file.write(index_img)
    return redirect("/")


logger.info('"show_img"Route initialization completed')


# "/recommend"路由
@app.route("/recommend")
def recommend():
    return render_template("recommend.html")


logger.info('"recommend"Route initialization completed')


# "/search_form"路由
@app.route("/search_form")
def search_form():
    """
    a = request.values.get("word")
    #作答区域39行：使用request.values.get()方法获取名为"A组"的数据
    search = request.values.get("A组")
    if search=="video":
        url="https://search.bilibili.com/all?keyword=" + a
    elif search=="shop":
        url="https://search.jd.com/Search?keyword=" + a
    elif search=="music":
        url="https://music.163.com/#/search/m/?s=" + a
    elif search=="image":
        url="https://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&dyTabStr=MCw2LDIsMyw1LDEsNCw3LDgsOQ%3D%3D&word=" + a
    elif search=="txt":
        url="https://wenku.baidu.com/search?ie=utf-8&word=" + a
    elif search=="word":
        url="https://baike.baidu.com/item/" + a
    elif search=="article":
        url="/article"
    elif search=="joke":
        url="/joke"
    elif search=="secret":
        #作答区域58行:设置输入框的1号密码
        if a=="输入密码才可查看":
            url="/secret"
        else:
            url="/wrong"
"""
    return '网页维护中，敬请期待！'  # redirect(url)


logger.info('"search_form"Route initialization completed')


# "/sectet"路由
@app.route("/secret")
def secret_form_form():
    return render_template("secret.html")


logger.info('"secret"Route initialization completed')


# "/mc"路由
@app.route("/mc")
def mc():
    return render_template("mc.html")


logger.info('"mc"Route initialization completed')


# "/hmcl"路由
@app.route("/hmcl")
def hmcl():
    return send_file('HMCL.exe', as_attachment=True)


logger.info('Hmcl initialization completed')


# "/pcl2"路由
@app.route("/pcl2")
def pcl2():
    return send_file('PCL2.exe', as_attachment=True)


logger.info('PCL2 initialization completed')


# "/minecraft"路由
@app.route("/minecraft")
def minecraft():
    return send_file('Minecraft.exe', as_attachment=True)


logger.info('Minecraft Route initialization completed')


# "/java8"路由
@app.route("/java8")
def java8():
    return send_file('java_8.exe', as_attachment=True)


logger.info('Java(8) initialization completed')


# "/java17"路由
@app.route("/java17")
def java17():
    return send_file('java_17.exe', as_attachment=True)


logger.info('Java(17) initialization completed')

app.run()
logger.info("================================")
logger.info(time.strftime(time.strftime("Finish!The time is %Y-%m-%d %H:%M:%S", struct)))
logger.info("================================")
