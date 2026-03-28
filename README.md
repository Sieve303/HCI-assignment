#  Delareyville Municipality Service Reporter

##  Project Overview
Delareyville Service Reporter is a basic Django web application designed to help residents report and track service delivery issues such as water leaks, electricity outages, and waste collection problems.

The system aims to improve communication between residents and the municipality by providing a simple and user-friendly platform.

---

## Features
- Report service delivery issues
- Select issue categories (Water, Electricity, Roads, Waste)
- Upload image (UI placeholder)
- Sign In / Sign Up functionality (basic session-based)
- Navigation between pages
- Simple and clean user interface
- Track submitted reports by Report ID
- Success notifications for form submissions

---

## Project Structure
The project is built using Django and includes:

### Apps:
- `reports` → Handles reporting functionality
- `users` → Handles user-related pages (login/signup)

### Templates:
- Home Page (`home.html`)
- Report Page (`report.html`)
- About Page (`about.html`)
- Contact Page (`contact.html`)
- Login Page (`login.html`)
- Signup Page (`signup.html`)
- Track Report Page (`track_report.html`)

---

## Navigation
The system includes a navigation bar that allows users to:
- Access the home page
- Report issues
- View About Us and Contact pages
- Sign In or Sign Up
- Logout

Users must sign in before accessing the report feature, ensuring better user control and system security.

---

## Design Considerations
The system was designed using Interaction Design principles:

- **Visibility** → Clear buttons and navigation bar  
- **Consistency** → Same layout across all pages  
- **Feedback** → Users are guided through actions (success toasts)
- **Learnability** → Simple and easy-to-use interface  
- **Control** → Users have clear logout and navigation options

The design also supports inclusiveness by using simple language and clear layouts for users with different levels of technical experience.

---

## Technologies Used
- Python
- Django 6.0.3
- HTML & CSS
- JavaScript (for toast notifications and tracking functionality)

---

## How to Run the Project

1. Clone the repository:
```bash
git clone https://github.com/Sieve303/HCI-assignment.git
cd "Django Project"
```

2. Create and activate virtual environment:
```bash
python -m venv env
env\Scripts\Activate.ps1
```

3. Install Django:
```bash
pip install django
```

4. Navigate to project and run server:
```bash
cd delareyville
python manage.py runserver
```

5. Open browser and visit:
```
http://127.0.0.1:8000/
```

---

## Author
**Lopang Kolberg**

---

## Repository
GitHub: https://github.com/Sieve303/HCI-assignment

---

## License
Open source for educational purposes

---

**Last Updated**: March 29, 2026
**Version**: 1.0.0
