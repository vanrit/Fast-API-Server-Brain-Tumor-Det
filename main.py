from fastapi_app import create_fastapi_app
from gradio_app import create_gradio_app
import uvicorn
import threading

if __name__ == "__main__":
    # Создание приложений
    fastapi_app = create_fastapi_app()
    gradio_app = create_gradio_app()

    # Запуск Gradio в отдельном потоке
    threading.Thread(target=gradio_app.launch, kwargs={"server_name": "0.0.0.0", "server_port": 7860},
                     daemon=True).start()

    # Запуск FastAPI на другом порту
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
