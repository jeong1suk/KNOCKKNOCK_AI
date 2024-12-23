import streamlit as st
import cv2
import numpy as np
import personal_color_analysis.personal_color as personal_color
from beautygan import makeup
# 타이틀 및 설명
st.title("Personal Color & Makeup Analyzer")
st.markdown(
    """
    Upload an image to analyze your personal color and get makeup suggestions 
    tailored to your tone. 🌟
    """
)

# 중앙에 이미지 업로드 섹션 추가
st.markdown("## Upload Your Image")
uploaded_file = st.file_uploader("Choose an image file (jpg, jpeg, png)", type=["jpg", "jpeg", "png"], label_visibility="collapsed")

# '메이크업' 버튼 초기 상태
makeup_applied = False

if uploaded_file is not None:
    try:
        # 이미지 파일을 numpy 배열로 변환
        image_data = np.frombuffer(uploaded_file.read(), np.uint8)
        image = cv2.imdecode(image_data, cv2.IMREAD_COLOR)

        # Personal Color Analysis 수행
        tone = personal_color.analysis(image)

        # 이미지 중앙 정렬
        col1, col2, col3 = st.columns([1, 2, 1])  # 가운데 정렬을 위한 빈 열 추가
        with col1:
            st.image(
                image,
                channels="BGR",
                caption="Uploaded Image",
                width=300  # 이미지 크기 조정
            )
        st.markdown(f"### Detected Personal Color: {tone}")

        # '메이크업' 버튼 추가
        if st.button("Apply Makeup"):
            try:
                # Perform makeup
                result_img, base64_image = makeup(image)

                # Display result
                st.image(result_img, caption="Makeup Applied Image", use_column_width=True)

                # Option to download
                st.markdown(
                    f'<a href="data:image/png;base64,{base64_image}" download="makeup_result.png">Download Makeup Image</a>',
                    unsafe_allow_html=True,
                )
            except Exception as e:
                st.error(f"Error applying makeup: {str(e)}")

    except Exception as e:
        st.error(f"Error applying makeup: {str(e)}")
else:
    st.info("Please upload an image file.")
