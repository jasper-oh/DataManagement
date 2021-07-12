import numpy as np
import pandas as pd
import matplotlib.pylab as plt
# % matplotlib inline
# DataFrame
# List 로 DataFrame 만들기

df = pd.DataFrame([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

#  열 기준으로 추출하기

df.loc[:, 0]
np.mean(df.loc[:, 0])

#  행 기준으로 추출하기

df.loc[0, :]

# 아래 두개 동일
df.loc[:, 0:1]

df.loc[:, range(0, 2)]

df.loc[0:1, :]

# Dictionary 로 DataFrame 만들기

tb1 = pd.DataFrame({
    "weight": [80.0, 70.4, 65.5, 45.9, 51.2],
    "height": [170, 180, 155, 143, 154],
    "type": ["f", "n", "n", "t", "t"]
})

#  몸무게 col, 키 col 출력 하기

tb1.loc[:, ['weight', 'height']]

# 정렬의 오름차순과 내림차순

#  height 기준으로 오름 차순
tb1.sort_values(by="height")

#  height 기준으로 내림 차순
tb1.sort_values(by="height", ascending=False)


#  Pandas 와 MatplotLib 을 이용하여 시각화 하기
names = pd.read_csv("Baby_Names_1880-2014.csv")

# 앞에서 5개
names.head()

# 뒤에서 5개
names.tail()

# 전체갯수
names.count()

# pivot을 이용하여 각 이름의 count 를 연도별 합계로 그룹화 하여 집계하기

total_births = names.pivot_table(
    'births', index='year', columns='gender', aggfunc=sum)
total_births.head(10)

# matplotlib 을 이용하여 그래프 생성하기
total_births.plot()

# 그래프의 가로 세로 비율을 적용
plt.rcParams['figure.figsize'] = (14, 6)
total_births.plot(title="Total births by gender and year")
