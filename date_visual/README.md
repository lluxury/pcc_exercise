[toc]



pip install --user matplotlib

## 数据可视化　
### 生成数据　

 安装Matplotlib　

####  绘制简单的折线图　

```python
import matplotlib.pyplot as plt
plt.plot(list)

# 详细设置
squares = [1,4,9,16,25]
plt.plot(squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.show()
```

#### 矫正图形

注意！，上图数据不准，刻度默认从零开始，矫正如下，推荐

```python
input_value = [1,2,3,4,5]
squares = [1,4,9,16,25]
plt.plot(input_value,squares, linewidth=5)
```

#### 散点图

```python
plt.scatter(2,4)
plt.show()

plt.scatter(x_values, y_values, edgecolor='none', s=40)
```



 随机漫步　
 使用Plotly模拟掷骰子　
 小结　
下载数据　
 CSV文件格式　
 制作全球地震散点图：JSON格式　
 小结　
使用API　
 使用WebAPI　
 使用Plotly可视化仓库　
 HackerNewsAPI　
 小结　