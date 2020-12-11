"""
22. pip로 외부 라이브러리 설치하여 데이터 시각화하기

pip install numpy pandas matplotlib
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.rand(50)
series = pd.Series(data)
series.plot()
plt.show()
