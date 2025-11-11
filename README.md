# 🎥 Movie Theater Website

An interactive **movie theater web application** built with Django.\
The website allows users to browse movies, view sessions, choose seats,
and manage their profile --- all within a clean, responsive UI.

This project focuses on simplicity, performance, and solid backend
architecture.

## ⭐ Features

-   🎬 **Movie catalog** with posters, descriptions, and genres\
-   🕒 **Showtimes & sessions** for each movie\
-   🪑 **Interactive seat booking** page with visual hall layout\
-   👤 **User authentication** (register/login/profile)\
-   ✅ **Order & ticket system**\
-   📱 **Online Store With Snaks**\
-   🔧 Admin dashboard for managing movies, halls, and sessions

## 🖼️ Screenshots

Homepage\
![homepage](/assets/images/home.png)

Movie Detail Page\
![movie_detail](/assets/images/movie_detail.png)

Shop Page\
![movie_detail](/assets/images/shop.png)

Seat Selection\
![seats](/assets/images/seats.png)

User Profile\
![seats](/assets/images/profile.png)

## 🛠️ Tech Stack

### **Backend**

-   **Python 3**
-   **Django**
-   **PostgreSQL**

### **Frontend**

-   **HTML5 / CSS3**
-   **JavaScript (vanilla)**

## 📁 Project Structure

    movie-theater-website/
    │
    ├── movies/           # Movies list, detail info about movies
    ├── movie_schedule/   # Choose sessions and buy tickets
    ├── orders/           # Models and other data about orders/orders items
    ├── shop/             # Shop with a snacks for you
    ├── accounts/         # Login, registration, profiles
    ├── static/           # CSS, JS, images
    ├── templates/        # HTML templates
    ├── media/            # Uploaded movie posters
    ├── core/             # Core application with settings
    ├── manage.py
    └── requirements.txt

## 🚀 Getting Started

### 1. Clone the repo

``` bash
git clone https://github.com/oleksandrmerkuloff/movie-theater-website
cd movie-theater-website
```

### 2. Create virtual environment

``` bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

``` bash
pip install -r requirements.txt
```

### 4. Apply migrations

``` bash
python manage.py migrate
```

### 5. Start the development server

``` bash
python manage.py runserver
```

Visit:

    http://127.0.0.1:8000

## 📄 License

MIT License --- feel free to use and modify.