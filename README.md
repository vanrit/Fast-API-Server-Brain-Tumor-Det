# FAST-API-SERVER-BRAIN-TUMOR-DET

Transforming Brain Tumor Detection with Rapid Precision

[![Last Commit](https://img.shields.io/github/last-commit/vanrit/Fast-API-Server-Brain-Tumor-Det?label=last%20commit)](https://github.com/vanrit/Fast-API-Server-Brain-Tumor-Det/commits/main)
[![Python](https://img.shields.io/github/languages/top/vanrit/Fast-API-Server-Brain-Tumor-Det)](https://github.com/vanrit/Fast-API-Server-Brain-Tumor-Det)
[![Languages](https://img.shields.io/github/languages/count/vanrit/Fast-API-Server-Brain-Tumor-Det)](https://github.com/vanrit/Fast-API-Server-Brain-Tumor-Det)

### Built with the tools and technologies:
<img src="https://github.com/tqdm/tqdm/raw/master/images/logo.gif" alt="tqdm" height="30" />
<img src="https://fastapi.tiangolo.com/img/icon-white.svg" alt="FastAPI" height="30" />
<img src="https://numpy.org/images/logo.svg" alt="NumPy" height="30" />
<img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" alt="Python" height="30" />
<img src="https://onnx.ai/images/icon/icon-ONNX-logo.svg" alt="ONNX" height="30" />

## Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Overview

Fast-API-Server-Brain-Tumor-Det is an integrated platform that combines FastAPI and Gradio to deliver real-time brain MRI tumor detection with an intuitive web interface. It enables developers to deploy diagnostic models efficiently, providing both API endpoints and interactive visualizations for medical imaging workflows.

### Why Fast-API-Server-Brain-Tumor-Det?

This project simplifies deploying and interacting with machine learning models for medical diagnostics. The core features include:

- 🔌 **Dual-Interface Support:** Seamlessly access the system via REST API and interactive web UI for versatile workflows.
- 🚀 **Real-Time Detection:** Leverages a pre-trained YOLO model for fast, accurate tumor identification.
- 📸 **Visual Results:** Upload images and visualize detected tumors directly within the interface.
- ⚙️ **Easy Deployment:** Unified architecture streamlines integration into existing medical applications.
- 📦 **Environment Management:** Dependencies are managed for consistent setup and deployment.

## Getting Started

### Prerequisites

This project requires the following dependencies:

- Programming Language: Python
- Package Manager: Pip

### Installation

Build Fast-API-Server-Brain-Tumor-Det from the source and install dependencies:

1. Clone the repository:

   ```bash
   git clone https://github.com/vanrit/Fast-API-Server-Brain-Tumor-Det
   ```

2. Navigate to the project directory:

   ```bash
   cd Fast-API-Server-Brain-Tumor-Det
   ```

3. Install the dependencies:

   Using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

After completing the installation, you can run the application using Uvicorn (assuming the main FastAPI app is in `main.py`):

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

- Access the FastAPI documentation at `http://localhost:8000/docs`.
- The Gradio interface may be accessible at `http://localhost:8000/gradio` or integrated within the app (check the code for specifics).
- Upload brain MRI images via the API or UI to detect tumors using the YOLO model.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.