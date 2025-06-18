from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse, StreamingResponse
import numpy as np
import cv2
from io import BytesIO
from model_config import model, class_names


def read_imagefile(file) -> np.ndarray:
    return cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)


def create_fastapi_app():
    app = FastAPI(root_path="/api", title="YOLO Detection API")

    @app.get("/", tags=["Main"])
    def root():
        return {"message": "Hello, World! It's tumor detection API"}

    @app.post("/detect/", tags=["Detection"])
    async def detect(file: UploadFile = File(...), conf: float = 0.3):
        image = read_imagefile(await file.read())
        results = model.predict(image, conf=conf, iou=0.5)
        detections = [
            {"x1": int(box.xyxy[0][0]), "y1": int(box.xyxy[0][1]),
             "x2": int(box.xyxy[0][2]), "y2": int(box.xyxy[0][3]),
             "score": float(box.conf), "class": class_names[int(box.cls)]}
            for box in results[0].boxes
        ]
        return JSONResponse(content={"detections": detections})

    @app.post("/detect/image/", tags=["Detection"])
    async def detect_image(file: UploadFile = File(...), conf: float = 0.3):
        image = read_imagefile(await file.read())
        results = model.predict(image, conf=conf, iou=0.5)
        annotated = results[0].plot()
        _, buffer = cv2.imencode(".png", annotated)
        return StreamingResponse(BytesIO(buffer), media_type="image/png")

    return app
