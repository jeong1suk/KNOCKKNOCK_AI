# 퍼스널컬러 분류 및 메이크업 적용 프로젝트 (v2)

## 📝 프로젝트 설명

퍼스널컬러 분류 모델과 BeautyGAN을 이용해 사용자의 퍼스널컬러를 예측하고, 메이크업을 적용하는 AI 시스템입니다.

### 주요 기능:

- 얼굴 이미지 입력 → 퍼스널컬러 분류 (봄/여름/가을/겨울)
- 분류 결과에 따른 메이크업 자동 적용
- 90%의 분류 정확도 달성

---

## ⚙️ 설치 및 실행 방법

1. **레포지토리 클론:**

   ```bash
   git clone https://github.com/your-repo/personal-color-v1.git
   cd personal-color-v1
   ```

2. **가상환경 설정 및 라이브러리 설치:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **face detector 모델 다운로드**

   프로젝트 실행 전에 다음 경로에서 `shape_predictor_68_face_landmarks.dat` 파일을 다운로드하고 `res/` 폴더에 넣어 주세요:

   [다운로드 링크](https://example.com/shape_predictor_68_face_landmarks.dat)

4. **실행**
   ```
   streamlit run app.py
   ```

---

## 📊 모델 성능

- **퍼스널컬러 분류 정확도:** 90%
- **BeautyGAN 메이크업 적용 결과:** 기본적인 메이크업 적용 (퍼스널컬러 반영 X)

---

## 📚 주요 기술 스택

- Python (3.10)
- PyTorch
- OpenCV (이미지 전처리)
- Dlib (얼굴 감지)
- Streamlit
- AWS EC2, S3

---
