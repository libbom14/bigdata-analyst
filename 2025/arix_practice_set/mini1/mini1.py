"""
✅ 문제 요약
목표: purchase_amt > 30000 여부 예측하는 이진 분류 모델을 학습하고
mini_test.csv에 대해 예측값을 pred.csv로 저장하라
출력 형식: pred.csv → pred 컬럼만 존재, 총 5개 행
📦 파일 목록
mini_train.csv
mini_test.csv
결과 저장 → pred.csv
"""
import pandas as pd

# 1. 데이터 불러오기
train = pd.read_csv('./data/mini_train.csv')
test = pd.read_csv('./data/mini_test.csv')

# - 데이터 파악
# - 전처리
# - 학습 데이터 / 예측 데이터 분리
# - 예측 및 평가
# - 결과 저장 및 확인

# print(train.info())
# print(test.info())

# 🎯 예측에 사용할 입력값(X), 정답값(y)
X_train = train.drop(columns=['target', 'purchase_amt'])
y = train['target']
X_test = test.copy()

# 🔄 문자 → 숫자 인코딩
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
o_columns = X_train.select_dtypes(include='object').columns
for col in o_columns:   # LabelEncoder는 1개씩 수행해야함
    X_train[col] = encoder.fit_transform(X_train[col])
    X_test[col] = encoder.transform(X_test[col])
print(X_train.head())
print(X_test.head())

# 데이터 분리
from sklearn.model_selection import train_test_split
X_train, X_val, y_train, y_val = train_test_split(X_train, y, test_size=0.2, random_state=42)

# 예측 및 평가
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)
y_val_pred = model.predict(X_val)

from sklearn.metrics import accuracy_score
acc = accuracy_score(y_val, y_val_pred)
print(acc)

y_pred = model.predict(X_test)
result = pd.DataFrame(y_pred, columns=['pred'])
result.to_csv('./data/mini_result.csv', index=False)

result = pd.read_csv('./data/mini_result.csv')
print(result)

# 답안 제출 참고
# 아래 코드는 예시이며 변수명 등 개인별로 변경하여 활용
# pd.DataFrame변수.to_csv("result.csv", index=False)