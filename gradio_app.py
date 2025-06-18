import gradio as gr
import cv2
from model_config import model


# Gradio интерфейс
def gradio_detect(image, conf):
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    results = model.predict(image_bgr, conf=conf, iou=0.5)
    annotated = results[0].plot()
    return cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB)


def create_gradio_app():
    return gr.Interface(
        fn=gradio_detect,
        inputs=[
            gr.Image(type="numpy", label="Upload brain MRI"),
            gr.Slider(minimum=0.1, maximum=0.9, value=0.3, step=0.05, label="Confidence Threshold")
        ],
        outputs="image",
        title="Tumor Detection",
        description="Upload brain MRI and adjust confidence threshold to get detections."
    )
