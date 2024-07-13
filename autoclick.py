import win32api
import win32con
import time

# 等待2秒以便切换到需要点击的窗口
time.sleep(2)

# 定义需要点击的四个位置 (x, y)


# 每次点击之间的时间间隔（总共8秒，间隔应为8秒除以3，因为是四次点击）
interval = 4

while True:
    # 移动到指定位置
    time.sleep(0.1)  # 等待一下确保位置已移动
    # 模拟鼠标点击
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    # 等待指定的时间间隔
    time.sleep(interval)
