# Use the full official Python image.
FROM python:3.8

# Explicitly install all possible system dependencies for OpenCV and refresh the linker cache.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && ldconfig

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application's code
COPY . .

# Run the command that was previously failing
RUN python model_config.py

# Expose ports
EXPOSE 8000
EXPOSE 7860

# Set the final command to run the application
CMD ["python", "-u", "main.py"]
