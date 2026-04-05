import pandas as pd
import psycopg2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
import joblib 

conn = psycopg2.connect(
    host="localhost",
    database="churn_project",
    user="postgres",
    password="postgresql123"
)

df = pd.read_sql("SELECT * FROM churn_schema.fact_churn", conn)
print(df.head())
print(df.columns)

# drop customerid
df = df.drop(columns=['customerid'])

# preprocessing sederhana
df = pd.get_dummies(df, drop_first=True)
print(df.head())

X = df.drop(columns=['churn'])
y = df['churn']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# train
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)

# evaluasi
print("Accuracy:", model.score(X_test, y_test))

# save
joblib.dump(model, "ml/src/model.joblib")

# save fitur names
joblib.dump(X.columns.tolist(), "ml/src/features.joblib")

print("Model saved!")