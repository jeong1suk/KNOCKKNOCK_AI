import streamlit as st
import cv2
import numpy as np
import personal_color_analysis.personal_color as personal_color

st.title("Personal Color & Makeup Analyzer")

st.sidebar.title("Upload Image")
image_file = st.sidebar.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

if image_file is not None:
    try:
        # 이미지 파일을 numpy 배열로 변환
        image_data = np.frombuffer(image_file.read(), np.uint8)
        image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

        # Personal Color Analysis 수행
        tone = personal_color.analysis(image)
        st.success(f"Detected Personal Color: {tone}")

        # 결과 이미지 출력
        st.image(image, channels="BGR", caption=f"Uploaded Image - Detected Tone: {tone}")

    except Exception as e:
        st.error(f"Error: {str(e)}")
else:
    st.info("Please upload an image file.")
