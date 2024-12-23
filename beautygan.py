# beautygan.py
import dlib
import tensorflow as tf
import numpy as np
import base64
from PIL import Image
import random

def align_faces(img):
    detector = dlib.get_frontal_face_detector()
    sp = dlib.shape_predictor("res/shape_predictor_68_face_landmarks.dat")
    dets = detector(img, 1)
    objs = dlib.full_object_detections()

    for detection in dets:
        s = sp(img, detection)
        objs.append(s)

    faces = dlib.get_face_chips(img, objs, size=256, padding=0.35)
    return faces

def preprocess(img):
    return img.astype(np.float32) / 127.5 - 1  # 0~255 -> -1 ~ 1

def postprocess(img):
    return ((img + 1.0) * 127.5).astype(np.uint8)  # -1 ~ 1 -> 0~255

def makeup(img):
    tf.compat.v1.disable_eager_execution()
    tf.compat.v1.reset_default_graph()  # 그래프 초기화

    with tf.compat.v1.Session() as sess:
        # 모델 로드
        saver = tf.compat.v1.train.import_meta_graph("res/model.meta")
        saver.restore(sess, tf.train.latest_checkpoint("res"))

        # 그래프 가져오기
        graph = tf.compat.v1.get_default_graph()
        X = graph.get_tensor_by_name("X:0")
        Y = graph.get_tensor_by_name("Y:0")
        Xs = graph.get_tensor_by_name("generator/xs:0")

        # 얼굴 정렬 및 전처리
        img1_faces = align_faces(img)
        img2 = dlib.load_rgb_image("res/makeup/vFG756.png")
        img2_faces = align_faces(img2)

        src_img = img1_faces[0]
        ref_img = img2_faces[0]

        X_img = preprocess(src_img)
        X_img = np.expand_dims(X_img, axis=0)
        Y_img = preprocess(ref_img)
        Y_img = np.expand_dims(Y_img, axis=0)

        # 메이크업 결과 생성
        output = sess.run(Xs, feed_dict={X: X_img, Y: Y_img})
        output_img = postprocess(output[0])

        # 결과 저장
        random_int = random.randint(1, 1000)
        image_path = f"output/output_image_{random_int}.png"
        Image.fromarray(output_img).save(image_path)

        # Base64 변환
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode("utf-8")

        return output_img, base64_image

