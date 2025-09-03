# 📚 ReadMate – your intelligent reading companion

This repository hosts a **Book Recommendation Web Application** built with **Django**, integrating **Natural Language Processing (NLP)** and **Pre-trained Machine Learning models** to deliver personalized reading suggestions.  

## 🚀 Features
- **Personalized Recommendations**: Suggests books to users based on NLP-driven similarity and embeddings.  
- **Pre-Trained ML Models**: Uses embedding models (e.g., word2vec, BERT-like) to understand semantic meaning of book metadata.  
- **Full-Stack Web App**: Django backend, SQLite database, responsive frontend (HTML, CSS, JavaScript).  
- **Dynamic Database Content**: Includes Programs, Courses, Departments, Announcements, and Hero-section modules.  
- **Scalable & Modular**: Easy to extend for larger datasets and production-ready deployment.  

## 🏗️ Tech Stack
- **Backend**: Django (Python)  
- **Database**: SQLite (with `djmoney` for handling fees in Programs module)  
- **Frontend**: HTML, CSS (MDBootstrap), JavaScript  
- **Machine Learning / NLP**: Pre-trained embedding models for text similarity  

## 📂 Project Structure
```
myApp/
 ├── APP1/                 # Main Django app
 │   ├── models.py         # Database models (Programs, Courses, Departments, Announcements, Heroes)
 │   ├── views.py          # Request handling and recommendation logic
 │   ├── forms.py          # Django forms for user input
 │   ├── admin.py          # Django admin integration
 │   ├── urls.py           # URL routes for APP1
 │   ├── templates/        # HTML templates
 │   └── static/           # CSS, JS, Images
 ├── myApp/                # Django project configuration
 │   ├── settings.py       # Project settings
 │   ├── urls.py           # Global URL routing
 │   ├── wsgi.py/asgi.py   # Deployment entry points
 ├── db.sqlite3            # Database
 └── manage.py             # Django management script
```

## ⚙️ Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Imswappy/NLP-Pre-Trained-ML-model-Book-Recommendation-System.git
   cd NLP-Pre-Trained-ML-model-Book-Recommendation-System/myApp
   ```

2. **Create & activate virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate    # Windows
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

5. **Start development server**:
   ```bash
   python manage.py runserver
   ```

6. **Access the app** at:  
   👉 http://127.0.0.1:8000/

---
<img width="1742" height="911" alt="image" src="https://github.com/user-attachments/assets/61906381-4d0c-4652-8e27-b2580769aa60" />
<img width="1763" height="912" alt="image" src="https://github.com/user-attachments/assets/08ea7a9d-254c-4f1f-908c-d9d55ec1ead2" />
<img width="1520" height="869" alt="image" src="https://github.com/user-attachments/assets/28efc858-8d10-4f19-ba5b-a53d71926019" />
<img width="1013" height="415" alt="image" src="https://github.com/user-attachments/assets/b9a94fef-03b7-4e24-8efd-af03f352b514" />
<img width="1000" height="483" alt="image" src="https://github.com/user-attachments/assets/b4b59e96-adfe-4875-a662-7a7638acdd03" />
<img width="1747" height="882" alt="image" src="https://github.com/user-attachments/assets/6466a7b4-accd-4917-8eb3-4c66688e81d7" />







## 🧠 Recommendation Engine Workflow
- Extracts features from book metadata (title, description, tags).  
- Applies **pre-trained NLP embeddings** to represent text in vector space.  
- Computes **cosine similarity** between books and user preferences.  
- Returns **ranked book recommendations** to the user interface.  

---

## 🔮 Future Enhancements
- Integration with real-world datasets (Goodreads, Kaggle book datasets).  
- Docker/Cloud deployment.  
- Hybrid recommendation models (content-based + collaborative filtering).  
- Real-time personalization based on user activity.  

---

## 📌 Author
Developed by [Imswappy](https://github.com/Imswappy)  
A full-stack ML application merging **Django web development** with **NLP-driven recommendation systems**.
