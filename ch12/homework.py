import matplotlib.pyplot as plt
import pandas as pd

file_name = '../ch11/data_raw.csv'
df_raw = pd.read_csv(file_name)

# 1. 나이 필터링 (35-44 years old)
target_age = '35-44 years old'
df_filtered = df_raw[df_raw['Age'] == target_age]

COL_LANG = 'LanguageHaveWorkedWith'
ds_data = df_filtered[COL_LANG]

# 결측치 제거
ds_data = ds_data.dropna()

print('-'*50)
print(f"Filtered Data ({target_age}):")
print(ds_data.head())

# 2. 데이터 분리 (split)
ds_data = ds_data.str.split(';')

print('-'*50)
print("Split Data:")
print(ds_data.head())

# 3. 리스트를 개별 행으로 변환
ds_data = ds_data.explode()

print('-'*50)
print("Exploded Data:")
print(ds_data.head())

# 4. 그룹화 및 카운트 (groupby size)
ds_data = ds_data.groupby(ds_data).size()

print('-'*50)
print("Grouped Data (Counts):")
print(ds_data.nlargest(5))

# 5. 상위 5개 언어 파이 차트 그리기 (nlargest(5))
# autopct로 퍼센트 표시, figsize로 크기
ds_data.nlargest(5).plot.pie(figsize=(10,10), autopct='%1.2f%%')

plt.title(f'Top 5 Languages for {target_age}')
plt.tight_layout()

plt.savefig('./lang_info_top5_35_44.png')