import matplotlib.pyplot as plt
import pandas as pd







plt.rcParams['font.family'] = 'Malgun Gothic'

# 폰트 설정 시 마이너스 기호 깨짐 방지
plt.rcParams['axes.unicode_minus'] = False

country_map = {
    'United States of America': '미국',
    'India': '인도',
    'Germany': '독일',
    'United Kingdom of Great Britain and Northern Ireland': '영국',
    'Canada': '캐나다',
    'France': '프랑스',
    'Brazil': '브라질',
    'Poland': '폴란드',
    'Netherlands': '네덜란드',
    'Australia': '호주',
    'Spain': '스페인',
    'Italy': '이탈리아',
    'Russian Federation': '러시아',
    'Sweden': '스웨덴',
    'Turkey': '터키',
    'Switzerland': '스위스',
    'Israel': '이스라엘',
    'Pakistan': '파키스탄',
    'Ukraine': '우크라이나',
    'Nigeria': '나이지리아',
    'Iran, Islamic Republic of...': '이란'
}


file_name = './data_raw.csv'
df_raw = pd.read_csv(file_name)

ds_data = df_raw.groupby(['Country']).size()

print('-'*100)
print(ds_data)


ds_top20 = ds_data.nlargest(20)

# 인덱스(국가명)를 한글로 변경
ds_top20_korean = ds_top20.rename(index=country_map)

# 한글로 변경된 데이터로 차트 그리기
ds_top20_korean.plot.pie(figsize=(10,10)) #인치단위

plt.tight_layout()

plt.show()
