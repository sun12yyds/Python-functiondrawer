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