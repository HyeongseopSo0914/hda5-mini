import pandas as pd
import matplotlib.pyplot as plt
import glob # pattern에 맞게 파일을 가져오기, SHS_*.csv

# data\SHS_2020.csv read data
# day by day    /   avg temp    /   avg rainfall    /   lowest temp /   highest temp

file_paths = glob.glob('data\SHS_*.csv')
df_combined = pd.DataFrame()

for file_path in file_paths:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(file_path, encoding='euc-kr')
        except UnicodeDecodeError:
            df = pd.read_csv(file_path, encoding='cp949')
    
    df.columns = df.columns.str.strip()
    #print(f"Columns in {file_path}: {df.columns}")  # 열 이름 출력
    selected_columns = ['일시','평균기온(°C)','최저기온(°C)','최고기온(°C)','강수 계속시간(hr)','일강수량(mm)']

    df_selected = df[selected_columns]
    df_selected = df_selected.fillna(0)
    #df_selected['일시'] = pd.to_datetime(df_selected['일시'], errors='coerce')
    df_combined = pd.concat([df_combined, df_selected], ignore_index=True)
df_combined = df_combined.sort_values(by='일시').reset_index(drop=True)

output_path = 'data/SHS.csv'
df_combined.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Data saved to {output_path}")

#import os
#print("Current working directory:", os.getcwd())