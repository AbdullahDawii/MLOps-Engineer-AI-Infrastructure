import mlflow.pyfunc
import pandas as pd

# 1. تهيئة مسار تتبع MLflow 
# (مهم: يجب أن يتطابق مع المسار الذي استخدمته للتسجيل)
mlflow.set_tracking_uri("sqlite:///mlflow.db")

# 2. تحديد اسم وإصدار النموذج
MODEL_NAME = "IrisClassifier"
MODEL_VERSION = "2" # استخدم الإصدار الأخير الذي سجلته

# URI النموذج في سجل MLflow
model_uri = f"models:/{MODEL_NAME}/{MODEL_VERSION}"

print(f"Loading model: {model_uri}")

# 3. تحميل النموذج
try:
    loaded_model = mlflow.pyfunc.load_model(model_uri)
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# 4. إعداد بيانات الإدخال للتنبؤ
# البيانات التالية تمثل زهرة سوسن جديدة:
# (الطول البتلة، العرض البتلة، الطول التويجي، العرض التويجي)
#new_data = pd.DataFrame([[5.8, 2.7, 5.1, 1.9]], 
                        #columns=['sepal_length', 'sepal_width', 'petal_length', 'petal_width'])
new_data = pd.DataFrame([[5.8, 2.7, 5.1, 1.9]], 
                        columns=['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'])

print("\nNew data to predict:")
print(new_data)

# 5. إجراء التنبؤ
prediction = loaded_model.predict(new_data)

print("\n--- Prediction Result ---")
print(f"The model predicts the class index: {prediction[0]}")
print("-------------------------")
