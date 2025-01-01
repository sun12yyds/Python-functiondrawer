# Python functiondrawer
一个利用了tkinter库和matplotlib库的优秀函数图像生成器
# 使用方法
运行functiondrawe.py即可
# 欢迎贡献和升级其代码
这里提供源码

```python
import tkinter as tk
from tkinter import simpledialog
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# 创建主窗口
class FunctionPlotter:
    def __init__(self, root):
        self.root = root
        self.root.title("精美函数绘制器")
        
        # 创建输入框和按钮
        self.label = tk.Label(root, text="输入函数表达式 (例如: np.sin(x)):")
        self.label.pack(pady=10)
        
        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)
        
        self.plot_button = tk.Button(root, text="绘制函数", command=self.plot_function)
        self.plot_button.pack(pady=10)
        
        # 初始化图形区域
        self.figure = plt.Figure(figsize=(5, 4), dpi=100)
        self.ax = self.figure.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.figure, root)
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    
    def plot_function(self):
        # 获取用户输入的函数表达式
        func_str = self.entry.get()
        x = np.linspace(-10, 10, 400)
        try:
            # 计算y值
            y = eval(func_str)
            self.ax.clear()
            self.ax.plot(x, y, label=f"y = {func_str}")
            self.ax.legend()
            self.ax.set_title("函数绘制器")
            self.ax.set_xlabel("x")
            self.ax.set_ylabel("y")
            self.canvas.draw()
        except Exception as e:
            tk.messagebox.showerror("错误", f"无效的函数表达式: {e}")

# 创建主应用程序
if __name__ == "__main__":
    root = tk.Tk()
    app = FunctionPlotter(root)
    root.mainloop()
```
# 代码解释
导入库：

     tkinter库用于创建图形用户界面。
     numpy库用于生成数值数组。
     matplotlib库用于绘制图形。
     FigureCanvasTkAgg将matplotlib画布嵌入到tkinter窗口中。
创建主窗口和布局：

创建一个主窗口并设置标题。
添加一个标签、一个输入框和一个按钮，用于输入函数表达式和触发绘图操作。
绘制函数：

获取输入框中的函数表达式。
使用numpy生成x值数组。
使用eval函数计算y值数组。注意，这里使用eval函数需要特别小心，以确保安全。
清除之前的绘图，并绘制新的函数曲线。
设置图表标题和标签。
运行应用程序：

创建主应用程序实例，并进入主事件循环。
这个脚本创建了一个简单的函数绘制器GUI，用户可以输入函数表达式（例如np.sin(x)），点击“绘制函数”按钮后，绘制相应的函数图形。可以绘制更多复杂的函数，并对代码进行扩展和优化。
