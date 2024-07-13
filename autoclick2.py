import pyautogui
import time

# 等待2秒以便切换到需要点击的窗口
time.sleep(2)

# 定义需要点击的四个位置 (x, y)
positions = [
    (100, 200),
    (300, 400),
    (500, 600),
    (700, 800)
]

# 每次点击之间的时间间隔（总共8秒，间隔应为8秒除以3，因为是四次点击）
interval = 8 / (len(positions) - 1)

for position in positions:
    # 移动到指定位置并点击
    pyautogui.click(position)
    # 等待指定的时间间隔
    time.sleep(interval)
