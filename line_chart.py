# line_chart.py

import matplotlib.pyplot as plt

# 建立資料
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# 建立折線圖
plt.plot(x, y)

# 顯示折線圖
plt.show()

# 儲存折線圖
plt.savefig("line_chart.png")
