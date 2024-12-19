# 퍼스널컬러 분류 및 메이크업 적용 프로젝트 (v1)

## 📂 프로젝트 구조

📁 personal-color-v1 <br/>
├── 📁 data # 데이터셋 (이미지, 레이블 등)<br/>
├── 📁 models # 학습된 모델 파일 (.h5, .pt 등)<br/>
├── 📁 notebooks # 데이터 분석 및 학습 노트북 파일 (.ipynb)<br/>
├── 📁 src # 소스 코드 (모델 학습, 평가, 예측 코드)<br/>
├── 📁 results # 결과 이미지, 테스트 결과 등<br/>
├── README.md # 프로젝트 개요 및 설명<br/>
└── requirements.txt # 필수 라이브러리 목록

## 📝 프로젝트 설명

퍼스널컬러 분류 모델과 BeautyGAN을 이용해 사용자의 퍼스널컬러를 예측하고, 기본적인 메이크업을 적용하는 AI 시스템입니다.

### 주요 기능:

- 얼굴 이미지 입력 → 퍼스널컬러 분류 (봄/여름/가을/겨울)

- 분류 결과에 따른 메이크업 자동 적용

- 90%의 분류 정확도 달성

## ⚙️ 설치 및 실행 방법

1. 가상환경 설정 및 라이브러리 설치:
   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

## 📊 모델 성능

- 퍼스널컬러 분류 정확도: 90%

- BeautyGAN 메이크업 적용 결과: 기본적인 메이크업 적용 (퍼스널컬러 반영 X)

## 🏆 개선 계획 (v2)

- 퍼스널컬러 기반 메이크업 스타일 적용

- 데이터셋 확장 및 새로운 모델 학습

- 사용자 선택형 메이크업 기능 추가
