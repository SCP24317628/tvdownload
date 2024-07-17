# JableTVDownload


### 1.搭建环境
本人使用了anaconda创建虚拟环境，所以还要安装anaconda

```
conda create --name jabletv 

conda activate jabletv

pip install -r requirements.txt
```

ps:安装 [FFmpeg] 用于视频编码 (不安装也能看，不过视频会有拖拉卡帧的情况)


### 2.运行程序
```
python main.py
```
### 3.输入视频网址

`https://jable.tv/videos/ipx-486/`    


### 4.等待下载 
要编码输入`y`，不要输入`n`   
要用GPU加速(Nvidia)输入`y`，用CPU输入`n`   

### 5.等待轉檔(Wait Encode) 

### 6.完成(Finish)


### 如果覺得好用 再麻煩給個星星好評 謝謝!!
---


[FFmpeg]:<https://www.ffmpeg.org/>  

### 参数帮助
```
python main.py -h
```
可以直接下载热门视频
```
python main.py --random True
```


---
### Windows 懒狗一键部署

1. 安装 ffmpeg，安装后运行 INIT.bat 将会自动执行环境搭建。
2. 若收到可以运行 RUN.bat 的信息，运行 RUN.bat 即可使用。