<img width="3188" height="1202" alt="frame (3)" src="https://github.com/user-attachments/assets/517ad8e9-ad22-457d-9538-a9e62d137cd7" />


Live demo : https://pathwave.onrender.com/
(It would take roughly 40 second to cold start as ot is hosted on free tier)

# PathWave

## Basic Details
### Team Name: Coconut

### Team Members
- Member 1: Adil KM - Farook College, Calicut
- Member 2: Shamil K - Farook College, Calicut

### Project Description
PathWave takes an image of a pothole and turns it into a unique 20 second of music. Because who said road damage can't sound beautiful?

### The Problem (that doesn't exist)
Path holes are everywhere - but no one has ever asked what they sound like. We have been looking at them all wrong. They're not ugly holes, they're hidden music waiting to be heard.

### The Solution (that nobody asked for)
Snap a photo of a path hole and upload it. Our system analyzes the image and turns it into a beat. It is completely unnecessary, but you have never heard anything like it. We didn’t solve a real problem. But we definitely made some noise😁.

## Technical Details
### Technologies/Components Used

### Backend
- Django
- PostgreSQL
- Gunicorn (WSGI Server)
- Whitenoise (Static File Management)
- dj-database-url & python-dotenv (Environment & DB config)

### Frontend
- Django Templates
- HTML5 & CSS3
- JavaScript
- Leaflet.js (Map and location tagging)

## 🔧 Features
- 🎼 Convert any path hole image into a playable melody
- 📍 Select the location of the path hole in the map
- 🎧 Audio preview
- 📂 Upload and preview images
- ✅ Responsive and interactive UI

## 📁 Project Structure

```
PathWave/
├── manage.py
├── requirements.txt
├── static/
├── templates/
├── UploadFile/
├── PathWave/
└── README.md
```

---

# Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Adil-km/PathWave.git
cd PathWave
```

### 2. Set Up Virtual Environment

#### On macOS/Linux:

```bash
python -m venv env
source env/bin/activate
```

#### On Windows:

```bash
python -m venv env
env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Configure Environment Variables

Create a `.env` file in the project root directory with the following content:

```env
DEBUG=True                 # Set to False in production
RENDER=True               # If True, connects to DATABASE_URL; otherwise uses SQLite
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url-here
```

> 🔒 Make sure `.env` is included in `.gitignore` to keep it out of version control.

### 6. Apply Migrations

```bash
python manage.py migrate
```


---

# Run

### 1. Start the Development Server

```bash
python manage.py runserver
```

### 2. Open in Browser

```
http://127.0.0.1:8000/
```

### Project Documentation

# Screenshots
![Screenshot1](https://github.com/user-attachments/assets/9a42aba1-e5a8-4372-a58c-563e886aa673)
*Landing page*
<br><br>

![Screenshot2](https://github.com/user-attachments/assets/7011ce5e-ebae-4ee6-aef7-cd3ec6c6c6bd)
*Page to upload image [fields: image file, description and location marking]*
<br><br>

![Screenshot3](https://github.com/user-attachments/assets/1c57d604-2062-4931-8b2a-72c42dc1ee2b)
*Upload file processing when submit*
<br><br>

![Screenshot4](https://github.com/user-attachments/assets/dd96f9d4-5a4e-4ddb-9316-84a8a5a84fc9)
*Gallery page*
<br><br>

![Screenshot5](https://github.com/user-attachments/assets/7bc12b2a-4ab0-4f16-a3e4-1ae711d595cd)
*View converted fie with it's image, audio, description and location(if marked)*
<br><br>

Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProjects--25-25?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)
