# **Track Tone - Gym Management System**

---

### Overview
Track Tone is a web-based gym management application that facilitates workout and diet management for trainees and trainers. It also includes an integrated e-commerce platform for gym-related products. The application offers separate logins for **Trainees, Trainers, and Super Users** to provide tailored features for each role.  
🚫 **Note:** Payment integration is not yet included in this version.

---

### Features
✅ **Browse Workout Plans:** Trainees can explore available workout and diet plans.

🛒 **E-commerce:** Users can browse and purchase gym products like supplements and equipment. The product list is loaded dynamically using a JavaScript array, meaning the **Super User cannot directly manage the products**.

🏋️‍♂️ **Trainer Management:** Trainers can create and manage workout plans for trainees.

📊 **Progress Tracking:** Trainees can track their progress in workouts and diet.

⚙️ **Admin Dashboard:** Super Users can manage users and plans and access the Django admin dashboard.

---

### Tech Stack
- **Frontend:** HTML, CSS, JavaScript (React.js)
- **Backend:** Django
- **Database:** MySQL (using XAMPP)
- **E-commerce:** JavaScript array for dynamic product loading

---

### Installation
#### Clone the repository:
```bash
git clone https://github.com/Tejas2913/Track-Tone.git
```
#### Navigate to the project folder:
```bash
cd Track-Tone
```
#### Install dependencies:
```bash
pip install Django
```

#### Set up MySQL database:
1. Open **XAMPP** and start the MySQL server.
2. Create a new database in **phpMyAdmin** (e.g., `tracktone_db`).
3. Update the database connection settings in your Django `settings.py` file with the MySQL database credentials.

#### Run database migrations:
```bash
python manage.py migrate
```
#### Create a Super User:
To create a superuser and access the admin dashboard, run:
```bash
python manage.py createsuperuser
```
You'll be prompted to enter a **username, email, and password** for the superuser account.

#### Run the server:
```bash
python manage.py runserver
```
#### Open the app in your browser:
```bash
http://127.0.0.1:8000/
```

#### Access the Admin Dashboard:
Go to: 
```bash
http://127.0.0.1:8000/admin/
```
and log in with the **superuser credentials** you just created.

---

### License
This project is **open-source** and can be modified as needed.

---

### Contributors
👨‍💻 **Tejas R M** - Backend Developer, Database Integration  
🎨 **Sree Dharan C** - Frontend Developer

