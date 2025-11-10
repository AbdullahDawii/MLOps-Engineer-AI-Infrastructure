# 🌸 Iris Classifier Service - MLOps Deployment (MLflow & Docker)

---

## 🏷️ Project Title
**Iris Classifier Service – Complete MLOps Workflow using MLflow & Docker**

---

## 📘 Project Overview

This project demonstrates a **complete MLOps solution** for training, packaging, and deploying a machine learning model to classify *Iris flowers*.  
The model is tracked and managed using **MLflow**, then containerized using **Docker** to ensure consistent and reproducible deployments.

---

## 🎯 Objectives

1. **Packaging:** Log and export the ML model using MLflow.  
2. **Secure Deployment:** Build a hardened and stable Docker image.  
3. **Path Resolution:** Fix MLflow absolute path issues inside Docker containers.  
4. **Integration:** Expose an API endpoint (`/invocations`) to serve predictions.

---

## ⚙️ Tech Stack

| Technology | Role |
| :--- | :--- |
| **Python 3.10** | Main programming language |
| **Scikit-learn** | Model training and classification |
| **MLflow** | Model tracking, versioning, and management |
| **Docker** | Application containerization and portability |
| **Curl** | API testing |
| **Image Name:** | `thabetabdullah73/mlflow-iris-service` |

---

## 🧩 Project Structure


# 🌸 Iris Classifier Service - MLOps Deployment (MLflow & Docker)

## Project Title
خدمة تصنيف زهرة السوسن (Iris Classifier Service) - نشر MLOps باستخدام MLflow و Docker.

---

## Overview
هذا المشروع يجسد حلاً كاملاً لـ **MLOps** بهدف تغليف ونشر نموذج تعلم آلي لتصنيف زهرة السوسن (Iris). تم استخدام مكتبة **MLflow** لتسجيل النموذج وإدارة ملفاته، وتم تغليف الخدمة بأكملها باستخدام **Docker** لضمان بيئة تشغيل مستقلة وقابلة للتكرار.

---

## 🎯 Objectives
1.  **التغليف (Packaging):** استخدام MLflow لتسجيل النموذج مع اعتماداته وتصديره.
2.  **النشر الآمن (Secure Deployment):** بناء صورة Docker متينة (Hardened Docker Image) لنشر الخدمة.
3.  **التجاوز التلقائي (Automated Resolution):** حل مشكلة المسارات المطلقة لـ MLflow داخل الحاوية لضمان التشغيل المستقر.
4.  **التكامل (Integration):** توفير نقطة نهاية (Endpoint) جاهزة لاستقبال التنبؤات عبر HTTP.

---

## ⚙️ Tech Used
| التقنية | الدور |
| :--- | :--- |
| **Python 3.10** | البيئة الأساسية لتشغيل النموذج والخادم. |
| **Scikit-learn** | مكتبة التدريب والتصنيف. |
| **MLflow** | تسجيل النموذج وإدارته (Tracking & Registry). |
| **Docker** | تغليف التطبيق وبيئة التشغيل (Containerization). |
| **Image Name** | `thabetabdullah73/mlflow-iris-service` |

---

## 🧩 Project Structure
يجب أن يحتوي المجلد الجذر للمشروع على الملفات والمجلدات التالية لضمان نجاح عملية البناء والنشر:

iris-classifier-service/ ├── .gitignore ├── README.md ├── Dockerfile ├── input.json # ملف لاختبار API ├── requirements.txt # قائمة الاعتماديات (Packages) └── mlruns/ # مجلد MLflow Artifacts ├── mlflow.db # قاعدة بيانات MLflow (SQLite) └── 0/ └── models/ └── <RUN_ID>/ └── artifacts/ # الملفات الثنائية للنموذج


---

## 🛠️ Setup Config كامل
تعتمد عملية النشر على وجود ملفات `Dockerfile` و `mlflow.db` ومجلد `mlruns` في المسار الجذر للمشروع.

### 1. بناء صورة Docker (Build Image)

```bash
docker build -t thabetabdullah73/mlflow-iris-service:latest ...

### 2. تشغيل الحاوية (Run Container)

يتم تعيين المنفذ الداخلي 5001 على المنفذ الخارجي 5002 للمضيف.
---

## 🖼️ متطلبات لقطات الشاشة (Screenshots)

للإيفاء بمتطلبات قسم `Screenshots and Commands`، ستحتاج إلى **لقطتي شاشة أساسيتين** (بالإضافة إلى إمكانية إضافة لقطات أخرى اختيارية):

| عدد اللقطات المطلوبة | عنوان لقطة الشاشة | الغرض |
| :--- | :--- | :--- |
## 🖼️ Image Screen (Run App)

![MLflow Screenshot](https://i.ibb.co/0pMNXgpW/mlflow.png)






| **1** | **لقطة شاشة لـ Docker PS** | تُظهر حالة الحاوية وهي تعمل بنجاح (`Status: Up`) وتأكيد تعيين المنفذ `0.0.0.0:5002->5001/tcp`. |
| **2** | **لقطة شاشة لأمر Curl** | تُظهر أمر `curl` والرد الناجح من خدمة API (مثل: `{"predictions": [2]}`)، مما يؤكد أن الخدمة تعمل. |

**العناوين المقترحة في الملف:**

1.  لقطة شاشة لـ **Docker PS** (تأكيد تشغيل الحاوية).
2.  لقطة شاشة لأمر **Curl** (تأكيد نجاح الاختبار والاستجابة).
3.  لقطة شاشة للواجهة الويب (اختياري).
  -p 5002:5001 \
  thabetabdullah73/mlflow-iris-service:latest
