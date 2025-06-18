from ultralytics import YOLO

# Инициализация модели и классов
model = YOLO("model.onnx")
class_names = ['Glioma', 'Meningioma', 'Pituitary', 'No Tumor']
