function music(){
     var music = $("audio")[0];
     music.play();
}

$(function(){
    var musiclink = $(".music-stop");
    var music = $("audio")[0];
    music.play();
    musiclink.click(function(){
        if(music.paused){
            music.play();
            //TODO:音乐开始的图标
            musiclink.attr("src","/static/images/音乐播放11.png");
        }else{
            music.pause();
            //TODO:音乐暂停的图标
            musiclink.attr("src","/static/images/音乐暂停11.png");
        }
    });
});