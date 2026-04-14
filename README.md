# Flask Login Authentication System UI

A full-stack web application built with Flask that provides a complete user authentication system with login, signup, and password reset functionality. The application uses MySQL for data persistence and features a modern, responsive UI with glassmorphism design.

## 📋 Table of Contents

- [Features](#-features)
- [Project Structure](#-project-structure)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
- [Configuration](#-configuration)
- [Database Setup](#-database-setup)
- [Running the Application](#-running-the-application)
- [API Routes](#-api-routes)
- [Security Notes](#-security-notes)
- [License](#-license)

## ✨ Features

- **User Authentication**: Secure login system with email and password validation
- **User Registration**: Sign up functionality with email validation and duplicate account prevention
- **Password Reset**: Allow users to reset forgotten passwords
- **Session Management**: Secure session handling with user data persistence
- **Responsive Design**: Modern UI with glassmorphism effect and CSS styling
- **Form Validation**: Client and server-side validation for user inputs
- **User Dashboard**: Protected user page displaying logged-in user information

## 📁 Project Structure

```
fullstack-flaskloginUI/
├── app.py                 # Main Flask application
├── README.md             # Project documentation
├── readme.md             # Database setup guide
├── static/
│   └── styles.css        # CSS styling for UI
└── templates/
    ├── login.html        # Login page
    ├── signup.html       # User registration page
    ├── reset.html        # Password reset page
    └── user.html         # User dashboard page
```

## 🛠 Tech Stack

- **Backend**: Flask (Python)
- **Database**: MySQL
- **Frontend**: HTML5, CSS3
- **Database Driver**: MySQLdb, mysql-connector-python
- **Session Management**: Flask Sessions

## 📦 Prerequisites

- Python 3.x
- MySQL Server
- pip (Python Package Manager)

## 🚀 Installation & Setup

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd fullstack-flaskloginUI
   ```

2. **Create a virtual environment** (optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required dependencies**
   ```bash
   pip install Flask Flask-MySQLdb mysql-connector-python
   ```

## ⚙️ Configuration

Update the database configuration in `app.py`:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'python'
```

⚠️ **Important**: Change the secret key for production:
```python
app.secret_key = 'your-secure-secret-key'
```

## 🗄️ Database Setup

### Prerequisites

- MySQL Server installed and running
- MySQL command-line client or GUI tool (MySQL Workbench)

### Database Creation

Create a new database:

```sql
CREATE DATABASE python;
USE python;
```

### Table Creation

Create the `user` table to store user account information:

```sql
CREATE TABLE `user` (
  `userid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
```

**Table Schema Description**

| Column | Type | Constraints | Purpose |
|--------|------|-------------|---------|
| `userid` | INT(11) | PRIMARY KEY, AUTO_INCREMENT | Unique user identifier |
| `name` | VARCHAR(100) | NOT NULL | User's full name |
| `email` | VARCHAR(100) | NOT NULL | User's email address |
| `password` | VARCHAR(255) | NOT NULL | User's password |

### Inserting Sample Data

Insert test users into the database (optional):

```sql
INSERT INTO user (name, email, password) VALUES 
('John Doe', 'john@example.com', 'password123'),
('Jane Smith', 'jane@example.com', 'password456'),
('Test User', 'test@example.com', 'testpass');
```

### Database Configuration in Flask

Update `app.py` with your database credentials:

```python
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'harshit'
app.config['MYSQL_DB'] = 'python'
```

### Verification

To verify the table was created correctly:

```sql
USE python;
DESCRIBE user;
```

You should see the table structure with all four columns.

### Important Database Notes

- ⚠️ **Passwords are currently stored in plain text**. For production, implement password hashing using bcrypt or werkzeug.security
- Ensure MySQL user has appropriate permissions for CREATE, INSERT, SELECT, UPDATE operations
- Keep database credentials secure and never commit them to version control

### Troubleshooting Database Issues

- **Connection Error**: Ensure MySQL server is running and credentials are correct
- **Table Not Found**: Verify the database and table were created successfully
- **Permission Denied**: Check that MySQL user has proper privileges

## 🏃 Running the Application

1. **Start the Flask development server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Open your browser and navigate to: `http://localhost:5000`

The application will run in debug mode, which provides auto-reloading and detailed error messages.

## 🔗 API Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` or `/login` | GET, POST | Login page and authentication handler |
| `/signup` | GET, POST | User registration page and account creation |
| `/reset` | GET, POST | Password reset page and password update |
| `/logout` | GET | Logout and session termination |

### Route Details

**Login (`/login`)**
- **POST Parameters**: `email`, `password`
- **Response**: Redirects to user dashboard or login page with error message

**Sign Up (`/signup`)**
- **POST Parameters**: `name`, `email`, `password`
- **Validation**: Email format, duplicate account check
- **Response**: Success/error message with redirect to login

**Password Reset (`/reset`)**
- **POST Parameters**: `email`, `password`
- **Response**: Password update confirmation with redirect to login

**Logout (`/logout`)**
- Clears user session and redirects to login page

## 🔒 Security Notes

⚠️ **Current Implementation Limitations**:
- Passwords are stored in plain text (not hashed) - **NOT RECOMMENDED for production**
- No CSRF protection implemented
- No rate limiting on login attempts
- SQL queries use parameterized statements (SQL injection prevention)

**Recommendations for Production**:
- Implement password hashing using `werkzeug.security` or `bcrypt`
- Add CSRF protection using Flask-WTF
- Implement rate limiting using Flask-Limiter
- Use environment variables for sensitive configuration
- Add HTTPS/SSL encryption
- Implement proper input sanitization

## 📝 License

This project is open source and available under the MIT License.

---

**Author**: Harshit Gupta  
**Repository**: [fullstack-flaskloginUI](https://github.com/Harshitgupta5290/fullstack-flaskloginUI)  
**Last Updated**: April 2026