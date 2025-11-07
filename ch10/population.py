





import pandas as pd



# --- 하와이 인구 ---
hawaii_pop = 1441553
print(f"하와이 인구: {hawaii_pop}")

# --- 2. 대한민국 인구 ---
# covid_kor.csv 파일을 바로 읽기
df_korea = pd.read_csv('../ch05/data/covid_kor.csv')

# 'population' 열의 첫 번째(0번째) 값을 가져옵니다.
korea_pop = df_korea['population'].iloc[0]
print(f"대한민국 인구: {korea_pop}")

print("\n-----------------------------")
print(f"하와이 인구: {hawaii_pop}")
print(f"대한민국 인구: {korea_pop}")

# sample02.py 비율 계산.
rate = korea_pop / hawaii_pop
print(f"\n대한민국 인구는 하와이 인구의 약 {rate:.2f} 배입니다.")
