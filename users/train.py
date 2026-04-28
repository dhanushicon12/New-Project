import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

csv_path = "D:\modifying main proejct\media\online_course_ml_ready_-1_0_1_NO_CLICKS.csv"

df = pd.read_csv(csv_path)

FEATURES = [
    "daysOfTraining",
    "refToMaterials",
    "averageScore",
    "numOfIntermediateClasses"
]

X = df[FEATURES]
TARGET = "final_result_-1_0_1"
y = df[TARGET]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
from sklearn.metrics import accuracy_score, classification_report
accuracy = round(accuracy_score(y_test, y_pred), 4)
print(f"✅ Model training completed")
print(f"Model Accuracy: {accuracy}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
joblib.dump(model, "media/RandomForest_model.joblib")
joblib.dump(scaler, "media/scaler.joblib")
