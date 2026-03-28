# Delareyville Service Reporter

A Django-based web application for citizens of Delareyville to report service delivery issues and track their reports in real-time.

## 🎯 Features

- **User Authentication**: Simple login and signup system with session management
- **Service Issue Reporting**: Submit reports for water leaks, electricity faults, potholes, and waste collection problems
- **Success Notifications**: Toast notifications confirming successful report submission
- **Report Tracking**: Track submitted reports by Report ID with real-time status updates
- **Responsive Design**: Professional UI with municipality branding
- **Navigation System**: Intuitive navbar across all pages
- **Logout Functionality**: Secure session termination

## 🏗️ Project Structure

```
Django Project/
│
├── delareyville/              # Main Django project folder
│   ├── manage.py
│   ├── delareyville/          # Project settings
│   │   ├── settings.py        # Django configuration
│   │   ├── urls.py            # Main URL routing
│   │   ├── wsgi.py
│   │   └── asgi.py
│   │
│   ├── reports/               # Reports app
│   │   ├── views.py           # View functions (logic)
│   │   ├── urls.py            # App URL routing
│   │   ├── models.py          # Database models
│   │   └── migrations/        # Database migration files
│   │
│   ├── users/                 # Users app (for future expansion)
│   │
│   ├── static/                # Static files
│   │   └── images/
│   │       └── P9-Tswaing-local-municipality.jpg
│   │
│   └── templates/             # HTML templates
│       ├── home.html          # Home page
│       ├── report.html        # Report issue form
│       ├── track_report.html  # Track report page
│       ├── login.html         # Login page
│       ├── signup.html        # Sign up page
│       ├── about.html         # About us page
│       └── contact.html       # Contact page
│
└── env/                       # Python virtual environment
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Sieve303/HCI-assignment.git
   cd "Django Project"
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv env
   # On Windows:
   env\Scripts\Activate.ps1
   # On macOS/Linux:
   source env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install django
   ```

4. **Navigate to project directory**
   ```bash
   cd delareyville
   ```

5. **Run migrations** (optional)
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## 📖 How to Use

### 1. **Home Page**
   - Visit `http://127.0.0.1:8000/`
   - View information about the service reporter system
   - Navigate using the top navbar

### 2. **Sign Up**
   - Click "Sign Up" in the navbar
   - Fill in username, email, and password
   - Click "Register" → Automatically redirected to Report Issue page

### 3. **Login**
   - Click "Sign In" in the navbar
   - Enter any username and password
   - Click "Login" → Automatically redirected to Report Issue page

### 4. **Report an Issue**
   - Select issue type:
     - Water Leaks
     - Electricity Faults
     - Potholes
     - Waste Collection Problems
   - Describe the issue in detail
   - Click "Submit Report"
   - Success toast notification appears
   - Click "Track Report" to monitor your submission

### 5. **Track Report**
   - Click "Track Report" button or navbar link
   - Enter a Report ID (use demo IDs for testing)
   - View report status, dates, and team notes

### 6. **Demo Report IDs for Testing**
   ```
   RPT-001234 - Water Leak (In Progress)
   RPT-001235 - Pothole (Completed)
   RPT-001236 - Electricity Fault (Pending)
   ```

### 7. **Logout**
   - Click "Logout" in the navbar to end session
   - Returns to home page
   - Session cleared

## 🔧 Technology Stack

- **Backend**: Django 6.0.3
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3 (default Django database)
- **Server**: Django Development Server
- **Version Control**: Git & GitHub

## 📝 Key Views & Routes

| URL | View | Description |
|-----|------|-------------|
| `/` | home | Home page |
| `/login/` | login | Login page with POST handling |
| `/signup/` | signup | Signup page with POST handling |
| `/report/` | report | Report issue form (requires login) |
| `/track-report/` | track_report | Track report by ID |
| `/about/` | about | About us page |
| `/contact/` | contact | Contact information |
| `/check-login/` | check_login | Login verification (redirects) |
| `/logout/` | logout | Logout & session flush |

## 🔐 Authentication System

- **Type**: Session-based authentication
- **Session Storage**: Django sessions middleware
- **CSRF Protection**: Django CSRF tokens on POST forms
- **Logout**: Flushes entire session on logout

## 🎨 Styling Features

- Professional dark navbar with hover effects
- Semi-transparent form containers
- Blue accent color (#007BFF) for buttons
- Municipality background image branding
- Responsive padding and spacing
- Green success toast notifications
- Status badges (Pending, In Progress, Completed)

## 📧 Form Submissions

All forms include:
- CSRF token protection
- Required field validation
- POST method handling
- Success feedback (toast notifications)
- Form reset after submission

## 🔮 Future Enhancements

- [ ] Database integration for persistent report storage
- [ ] User profile management
- [ ] Email notifications for report updates
- [ ] SMS alerts for urgent issues
- [ ] Real-time report status updates
- [ ] Report comments/notes system
- [ ] Admin dashboard for municipal staff
- [ ] Map integration to show issue locations
- [ ] Image upload for issue evidence
- [ ] Rate limiting and security improvements

## 🐛 Testing

The application has been tested with:
- Chrome browser
- Mozilla Firefox
- Edge browser
- Mobile responsiveness (tested at 1024px+)

## 📞 Contact & Support

**Project**: Delareyville Service Reporter
**GitHub Repository**: https://github.com/Sieve303/HCI-assignment
**Author**: Sieve303

## 📄 License

This project is open source and available for educational purposes.

## 🙏 Acknowledgments

- Tswaing Municipality for inspiring the project
- Django framework for the robust backend
- Bootstrap concepts for responsive design

---

**Last Updated**: March 28, 2026
**Version**: 1.0.0
