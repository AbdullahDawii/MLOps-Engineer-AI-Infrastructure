#!/usr/bin/env python3
# train.py
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris
import mlflow
import mlflow.sklearn
import sys

# --- 1. إعداد التجربة ---
# اسم النموذج الذي سيتم تسجيله في Model Registry
MODEL_NAME = "IrisClassifier" 

# الحصول على قيمة المعامل C من المدخلات (لتشغيل تجارب مختلفة)
# إذا لم يتم تمرير قيمة، استخدم 0.01 كافتراضي
try:
    alpha = float(sys.argv[1])
except:
    alpha = 0.01

# بدء تتبع تجربة جديدة
with mlflow.start_run():
    # --- 2. تجهيز البيانات ---
    data = load_iris(as_frame=True)
    X, y = data.data, data.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # --- 3. التدريب والتسجيل ---
    
    # تعريف النموذج بمعامل C متغير

    # السطر 34: تهيئة النموذج
    model = LogisticRegression(C=alpha, solver='lbfgs', random_state=42)
# السطر 35 (أو 34 إذا حذفت السطر المدموج بالكامل): تدريب النموذج
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    
    # تسجيل المعاملات والمقاييس والنموذج
    mlflow.log_param("C_parameter", alpha)
    mlflow.log_param("solver", 'liblinear')
    mlflow.log_metric("accuracy", accuracy)

    print(f"Model trained with C={alpha}, Accuracy: {accuracy:.4f}")

    # تسجيل النموذج في Model Registry تحت اسم محدد
    mlflow.sklearn.log_model(
        model, 
        "model", 
        registered_model_name=MODEL_NAME
    )
