# استخدم صورة Python خفيفة كقاعدة
FROM python:3.10

# تعيين دليل العمل
WORKDIR /app

# تثبيت التبعيات المطلوبة لتشغيل الخادم
# بما في ذلك scikit-learn و pandas و gunicorn لـ MLflow serve
RUN pip install mlflow scikit-learn pandas gunicorn

# نسخ ملفات التتبع وقاعدة البيانات (ملفات الميتا والملفات الثنائية للنموذج)
COPY mlflow.db /app/mlflow.db
COPY mlruns /app/mlruns

RUN chmod -R 777 /app/mlruns
# تعيين متغير البيئة لمسار التتبع
ENV MLFLOW_TRACKING_URI=sqlite:///mlflow.db
ENV MLFLOW_ARTIFACT_LOCATION=/app

# كشف المنفذ الذي سيعمل عليه خادم النشر (كما استخدمنا 5001)
EXPOSE 5001

# الأمر الافتراضي لتشغيل خادم MLflow عند بدء الحاوية:
# دمج المعاملات الصحيحة وحذف الأمر المكرر
#CMD ["mlflow", "models", "serve", "-m", "models:/IrisClassifier/2", "--env-manager", "local", "--host", "0.0.0.0", "--port", "5001"]
CMD ["mlflow", "models", "serve", "-m", "/app/mlruns/0/models/m-49cc536524bb452682b2c785088d5fa7/artifacts", "--env-manager", "local", "--host", "0.0.0.0", "--port", "5001"]
