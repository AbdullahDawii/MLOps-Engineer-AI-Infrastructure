# 🌸 Iris Classifier Service - MLOps Deployment (MLflow & Docker)

## 🏷️ Project Title
**Iris Classifier Service – Complete MLOps Workflow using MLflow & Docker**

---

## 📘 Project Overview

هذا المشروع يجسد حلاً كاملاً لـ **MLOps** بهدف تغليف ونشر نموذج تعلم آلي لتصنيف *Iris flowers*.
The model is tracked and managed using **MLflow**, then containerized using **Docker** to ensure consistent and reproducible deployments.

---

## 🎯 Objectives

1. **Packaging:** Log and export the ML model using MLflow. (التغليف)
2. **Secure Deployment:** Build a hardened and stable Docker image. (النشر الآمن)
3. **Path Resolution:** Fix MLflow absolute path issues inside Docker containers. (حل مشكلة المسارات)
4. **Integration:** Expose an API endpoint (`/invocations`) to serve predictions. (التكامل)

---

## ⚙️ Tech Stack

| Technology | Role |
| :--- | :--- |
| **Python 3.10** | Main programming language / البيئة الأساسية لتشغيل النموذج والخادم. |
| **Scikit-learn** | Model training and classification / مكتبة التدريب والتصنيف. |
| **MLflow** | Model tracking, versioning, and management / تسجيل النموذج وإدارته. |
| **Docker** | Application containerization and portability / تغليف التطبيق وبيئة التشغيل. |
| **Curl** | API testing |
| **Image Name:** | `thabetabdullah73/mlflow-iris-service` |

