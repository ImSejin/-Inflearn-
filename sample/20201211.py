"""
22. pip로 외부 라이브러리 설치하여 데이터 시각화하기

pip install numpy pandas matplotlib

numpy:      데이터 분석 기초 패키지
pandas:     numpy 기반으로 series/dataframe 타입을 제공하며, 데이터 분석 고급 기능 제공 라이브러리
matplotlib: 데이터 시각화 라이브러리
series:     pandas 전용 열거형 데이터 타입
dataframe:  pandas 전용 테이블형 데이터 타입

pip install jupyter
jupyter notebook --notebook-dir=C:/Users/jupyter_notebook'
가상환경 실행: venv/Script/activate
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = np.random.rand(50)
series = pd.Series(data)
series.plot()
plt.show()
