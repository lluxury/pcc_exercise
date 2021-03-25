[toc]

### 初始化

各种变量

音乐

```python
music1= pygame.mixer.Sound("touch.wav")  # 音效
pygame.mixer.music.load("bkm.mp3") # 背景？
```



#### little_bird

little_bird(list)

- 种类，同样公共变量及3个参数



#### seteasy 难度

seteasy(list)

- 一些公共变量，相当于 设置模块
- 6个变量对就列表6个位置



### Bullet 子弹

update

image

mask

rect

visible



### Bird 

```python
class Bird(pygame.sprite.Sprite):
	def __init__(self,x,y,level,images):
		super(Bird,self).__init__()
        pass
- update 下一点坐标
- image	改变图像
- mask	改变图像
- rect	输出矩形
```



Bird(pygame.sprite.Sprite)

变量，初始化

- 



### Pipe

```python
class Pipe(pygame.sprite.Sprite):
	def __init__(self,pipe_head_image,pipe_body_image):
		super(Pipe, self).__init__()
        pass # 各种初始化
    	pipe_body_image 画管子
        pipe_body_image 画管子2？
- rect 矩形
- visible 可见
- update 更新率
- collides 碰撞？       
```





#### change_add_time



### Stone

```python
class Stone(pygame.sprite.Sprite):
	def __init__(self,image):
		super(Stone, self).__init__()
        pass
    
- rect 矩形？
- image 图像
- mask 阴影
- update 下一点？  frames_to_msec
- collides 碰撞？ collide_mask？ pygame自带
- visible 可见
```



 



#### level_goal



#### load_image



#### search_bk



#### load_images

- 读全部图片，返回对象



#### frames_to_msec

```python
def frames_to_msec(frames,fps=FPS):
	return 1000.0*frames/fps  # 图片出来时间？
```





#### msec_to_frames

```python
def msec_to_frames(milliseconds, fps=FPS):
    return fps * milliseconds / 1000.0#转化成对应的帧数
    #转化成每秒的相应的帧数？目前看不懂
```





#### **game_loop**

主循环

- 播放音乐

- 显示标题

- 时钟

- 图像字典 load_images

- 实例鸟

- 字体123？

- 管子

- 石头，子弹 新建精灵组

- 设停止标志

- 设帧数

- 循环

  ​	clock.tick(FPS) ？

  ​	没暂停或新柱子生成，实例柱子，加入队列

  ​	没暂停或新石头或鸟级比石头低，实例石头，加入组

  ​	事件判断，退出，按键弹起（暂停，射，快？），鼠标弹起（快）

  ​	是否暂停

  ​	

  ​	石头，子弹检测碰撞

  ​	管子检测碰撞

  ​	石头检测碰撞



​		管子碰撞处理

​		石头碰撞处理

​		鸟撞处理



​		绘图



​		队列不为空，管子0不可见，删石头，删子弹



​		画柱子，

​		画石头

​		画子弹

​		柱子超过鸟，柱子没计分？



​		级别

​		分

​		2种字体，渲染 （写的有点乱）

​		

​		计算一帧所需要的时间？

​		渲染

​		绘制屏幕



​		计算升级

​		增加时间

​		清理管子

​		清理石头

​		清理子弹

​		鸟升级

​		设置通关信息及画面

​		帧数增加？

音乐停止

初始化柱子速度

重新调用 main

​		

#### quit_but

调用exit 退出应用



#### buttons

按钮函数复用

- mouse_position 鼠标定位
- click 鼠标点击
- 判断位置，按钮变色
- 放音乐？
- 下面不太懂要试玩



#### setting

设置

- 显示背景

- 检测退出

  - 各种按钮 ：seteasy，main，little_bird

 ```python
, 'easy',seteasy,[0.19,2500,int(5 / 11 * BK_HEIGHT),0.97,5,6]
,little_bird,["f_u","f_m","f_w"]
 ```

​    按钮后半部分直接传6个参数过去，设置难度的方法

​    鸟同样，参数为3个图片

#### main

调用开始背景，维持显示

点关闭退出

显示3个按钮 game_loop，setting，quit_but

```python
buttons(x, y, w, h, color, color2, text,action,list=[]):
    pass
```



### 总结

使用了装饰器，pygame @property 用法？

调用了音乐，细节部分写的很随意

有相当程度的复用，所以代码量不是很大

