from ultralytics import YOLO
import gdown, os

# Функция загрузки модели с Google Drive
def download_model():
    url = "https://drive.google.com/uc?id=1UXwcm_emlsQ7imt4Qjdd7rUaV1jqGxrx"
    output_path = "model.onnx"

    if not os.path.exists(output_path):
        print("Скачивание модели...")

        try:
            gdown.download(url, output_path, quiet=False)
        except Exception as e:
            # Если включен V2Ray
            print(f"Ошибка скачивания: {e}")
            print("Пробую через локальный прокси порт 10808")
            os.environ["HTTP_PROXY"] = "http://127.0.0.1:10808"   # если у тебя включён http-proxy
            os.environ["HTTPS_PROXY"] = "http://127.0.0.1:10808"

            gdown.download(url, output_path, quiet=False)

        print(f"Модель успешно скачана и сохранена как {output_path}")

download_model()

# Инициализация модели и классов
model = YOLO("model.onnx",  task="detect")
class_names = ['Glioma', 'Meningioma', 'Pituitary', 'No Tumor']
