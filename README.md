# Object Detection System with YOLOv8 and MySQL Database

This project is a **real-time object detection application using YOLOv8**, featuring an interactive OpenCV interface and a **MySQL database** to store and describe detected objects.

---

<!-- ## 📸 Demonstração

> *Um exemplo visual pode ser adicionado aqui, como um GIF curto ou imagem da aplicação em execução.* -->

---

## 📸 Features

- Detects objects using the webcam and the YOLOv8 model (`ultralytics`).
- Displays a **clickable circle** on screen that opens an **interactive popup** showing:
  - Object name
  - Description
  - Clickable link for more information
- Saves detection data (object + date/time) to a database.
- Allows manually adding custom objects with descriptions and links.
- Visual interface with OpenCV and mouse interaction.

---

## 🛠️ Tecnologias utilizadas

- Python 3.11
- OpenCV
- YOLOv8 
- MySQL
- PIL (Pillow)
- dotenv


---

## 📂 Organização do projeto

- **main.py**: Main application logic
- **database/**: MySQL connection and data manipulation modules
- **utils/**: Auxiliary functions, graphical interactions, and mouse events
- **YOLOWeights/**: Trained models (YOLOv8 in `.pt` and `.onnx`)
- **font/**: Font used in the information popup
- **requirements.txt**: Required libraries
- **add_object_info.py**: File that adds more objects to the application

---

## ⚙️ How to execute the project


### 1. Clone the repository

```bash
git clone https://github.com/tenoriopedro/YOLO-Interactive-Detection.git
cd YOLO-Interactive-Detection
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the MySQL database

- Create the database_detect database with read and write permissions.

- Configure credentials in the data_database.py file.

- When starting the system, the necessary tables will be created automatically.

- Two objects are detected by default in the application. But you can add more with the add_object_info.py file.

### 5. Run the program

```bash
python main.py
```

### 🧠 Operating Logic

- The webcam is activated, and each frame is analyzed by a YOLOv8 model.

- If a predefined object is detected, a circle appears in the corner of the screen.

- Clicking the circle displays an animated pop-up displaying detailed information about the object.

- Informational links are clickable and open in the browser.

- All detections are recorded in a database with the date and time.

### 🛡️ Security and Best Practices

- Make sure to keep your database credentials outside of the repository (e.g., use .env).


### 👨‍💻 Author

Pedro Tenório
Python Developer | Computer Vision | Artificial Intelligence