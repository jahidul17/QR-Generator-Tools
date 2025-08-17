# QR Generator App

A web application built with **Python**, **Django**, and **Bootstrap** that allows users to generate QR codes for any text or URL. The app provides a simple interface to input data, instantly creates a QR code, and lets users download the generated image.

## Features

- Generate QR codes for text, URLs, or any input
- Responsive design using Bootstrap
- Download QR codes as image files
- User-friendly interface

## Technologies Used

- Python
- Django
- Bootstrap
- qrcode (Python library)

## Usage

1. Enter the text or URL you want to encode.
2. Click the "Generate" button.
3. View and download your QR code.



# How to Install a Django Project 
1. **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

6. **Access the project:**
    Open your browser and go to `http://127.0.0.1:8000/qr`<br>
