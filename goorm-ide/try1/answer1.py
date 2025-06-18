# 출력을 원할 경우 print() 함수 활용
# 예시) print(df.head())

# getcwd(), chdir() 등 작업 폴더 설정 불필요
# 파일 경로 상 내부 드라이브 경로(C: 등) 접근 불가

import pandas as pd

df = pd.read_csv("data/employee_performance.csv")

# 사용자 코딩

# print(df)
# 1. 고객만족도가 없는 직원의 경우, 평균 고객 만족도로 결측치를 채운다.
df['고객만족도'] = df['고객만족도'].fillna(df['고객만족도'].mean())
# print(df.isna().sum())

# 2. 근속연수가 없는 직원의 경우, 해당직원을 삭제한다.
df = df.dropna(subset='근속연수')
# print(df.isna().sum())

# 3. 직원의 고객만족도의 4분위 중 3사분위수 값을 계산한다.
# 3-1
# print(df.describe()) # 고객만족도의 75% 값
# 3-2
print(df['고객만족도'].quantile(0.75))
# 3-3
# print(df.count()) # 952 * 0.75 = 714
# print(df.sort_values('고객만족도').iloc[713])

# 4. 부서별로 평균연봉을 구하고, 두번째로 평균연봉이 높은 부서의 평균연봉을 계산한다.
# (X) sorted_df = df.groupby('부서').mean('연봉').sort_values('연봉', ascending=False)
sorted_df = df.groupby('부서')['연봉'].mean().sort_values('연봉', ascending=False)
print(sorted_df)
