
import os

def generate_login_page():
    """
    Generate a login page with username and password fields.
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login</title>
    <style>
        body {
            margin: 0;
            padding: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
        }
        .login-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            width: 100%;
            max-width: 400px;
        }
        h1 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: #333;
        }
        .form-group {
            margin-bottom: 1rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #555;
        }
        input {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 0.75rem;
            background-color: #4a69bd;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 1rem;
        }
        button:hover {
            background-color: #3c55a5;
        }
        .error-message {
            color: #e74c3c;
            margin-top: 1rem;
            text-align: center;
            display: none;
        }
    </style>
</head>
<body>
    <div class="login-container">
        <h1>Login</h1>
        <form id="login-form" action="profile.html" method="get">
            <div class="form-group">
                <label for="username">Username</label>
                <input type="text" id="username" name="username" required>
            </div>
            <div class="form-group">
                <label for="password">Password</label>
                <input type="password" id="password" name="password" required>
            </div>
            <button type="submit">Login</button>
            <div id="error-message" class="error-message">Invalid username or password</div>
        </form>
    </div>

    <script>
        document.getElementById('login-form').addEventListener('submit', function(event) {
            event.preventDefault();
            
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // Simple validation - in a real app, this would be server-side
            if (username && password) {
                // Store username in localStorage to use in profile page
                localStorage.setItem('username', username);
                window.location.href = 'profile.html';
            } else {
                document.getElementById('error-message').style.display = 'block';
            }
        });
    </script>
</body>
</html>
"""
    
    with open('index.html', 'w') as f:
        f.write(html_content)
    
    print("Login page 'index.html' has been generated successfully!")

def generate_profile_page():
    """
    Generate a profile page where users can enter personal information.
    """
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Profile</title>
    <style>
        body {
            margin: 0;
            padding: 2rem;
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            color: #333;
        }
        .profile-container {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 800px;
            margin: 0 auto;
        }
        h1 {
            text-align: center;
            margin-bottom: 1.5rem;
            color: #333;
        }
        .form-group {
            margin-bottom: 1.5rem;
        }
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #555;
        }
        input, textarea, select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            box-sizing: border-box;
        }
        textarea {
            min-height: 100px;
            resize: vertical;
        }
        button {
            padding: 0.75rem 1.5rem;
            background-color: #4a69bd;
            color: white;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 1rem;
        }
        button:hover {
            background-color: #3c55a5;
        }
        .profile-header {
            display: flex;
            align-items: center;
            margin-bottom: 2rem;
        }
        .profile-picture-container {
            width: 150px;
            height: 150px;
            border-radius: 50%;
            overflow: hidden;
            margin-right: 2rem;
            background-color: #ddd;
            position: relative;
        }
        .profile-picture {
            width: 100%;
            height: 100%;
            object-fit: cover;
        }
        .profile-picture-placeholder {
            width: 100%;
            height: 100%;
            display: flex;
            justify-content: center;
            align-items: center;
            color: #888;
            font-size: 0.8rem;
            text-align: center;
            padding: 1rem;
            box-sizing: border-box;
        }
        .upload-btn {
            position: absolute;
            bottom: 0;
            left: 0;
            right: 0;
            background-color: rgba(0, 0, 0, 0.5);
            color: white;
            text-align: center;
            padding: 0.5rem;
            cursor: pointer;
            font-size: 0.8rem;
        }
        .upload-btn:hover {
            background-color: rgba(0, 0, 0, 0.7);
        }
        .profile-info {
            flex: 1;
        }
        .welcome-message {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        .success-message {
            background-color: #d4edda;
            color: #155724;
            padding: 1rem;
            border-radius: 4px;
            margin-bottom: 1rem;
            display: none;
        }
        .form-row {
            display: flex;
            gap: 1rem;
        }
        .form-col {
            flex: 1;
        }
        @media (max-width: 768px) {
            .profile-header {
                flex-direction: column;
                text-align: center;
            }
            .profile-picture-container {
                margin-right: 0;
                margin-bottom: 1rem;
            }
            .form-row {
                flex-direction: column;
                gap: 0;
            }
        }
    </style>
</head>
<body>
    <div class="profile-container">
        <div id="success-message" class="success-message">Profile updated successfully!</div>
        
        <div class="profile-header">
            <div class="profile-picture-container">
                <div id="profile-picture-placeholder" class="profile-picture-placeholder">
                    No profile picture selected
                </div>
                <img id="profile-picture" class="profile-picture" style="display: none;">
                <label for="profile-picture-upload" class="upload-btn">Upload Photo</label>
                <input type="file" id="profile-picture-upload" accept="image/jpeg, image/png" style="display: none;">
            </div>
            
            <div class="profile-info">
                <div id="welcome-message" class="welcome-message">Welcome!</div>
                <p>Please complete your profile information below.</p>
            </div>
        </div>
        
        <h1>Profile Information</h1>
        
        <form id="profile-form">
            <div class="form-row">
                <div class="form-col">
                    <div class="form-group">
                        <label for="first-name">First Name*</label>
                        <input type="text" id="first-name" name="first-name" required>
                    </div>
                </div>
                <div class="form-col">
                    <div class="form-group">
                        <label for="last-name">Last Name*</label>
                        <input type="text" id="last-name" name="last-name" required>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="dob">Date of Birth*</label>
                <input type="date" id="dob" name="dob" required>
            </div>
            
            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
            </div>
            
            <div class="form-group">
                <label for="address">Street Address*</label>
                <input type="text" id="address" name="address" required>
            </div>
            
            <div class="form-row">
                <div class="form-col">
                    <div class="form-group">
                        <label for="city">City*</label>
                        <input type="text" id="city" name="city" required>
                    </div>
                </div>
                <div class="form-col">
                    <div class="form-group">
                        <label for="state">State/Province*</label>
                        <input type="text" id="state" name="state" required>
                    </div>
                </div>
            </div>
            
            <div class="form-row">
                <div class="form-col">
                    <div class="form-group">
                        <label for="zip">Zip/Postal Code*</label>
                        <input type="text" id="zip" name="zip" required>
                    </div>
                </div>
                <div class="form-col">
                    <div class="form-group">
                        <label for="country">Country*</label>
                        <input type="text" id="country" name="country" required>
                    </div>
                </div>
            </div>
            
            <div class="form-group">
                <label for="bio">Bio/About Me</label>
                <textarea id="bio" name="bio"></textarea>
            </div>
            
            <button type="submit">Save Profile</button>
        </form>
    </div>

    <script>
        // Display username in welcome message
        document.addEventListener('DOMContentLoaded', function() {
            const username = localStorage.getItem('username');
            if (username) {
                document.getElementById('welcome-message').textContent = `Welcome, ${username}!`;
            }
        });

        // Handle profile picture upload
        document.getElementById('profile-picture-upload').addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const profilePicture = document.getElementById('profile-picture');
                    profilePicture.src = e.target.result;
                    profilePicture.style.display = 'block';
                    document.getElementById('profile-picture-placeholder').style.display = 'none';
                };
                reader.readAsDataURL(file);
            }
        });

        // Handle form submission
        document.getElementById('profile-form').addEventListener('submit', function(event) {
            event.preventDefault();
            
            // In a real app, this would send data to a server
            // For this demo, we'll just show a success message
            document.getElementById('success-message').style.display = 'block';
            
            // Scroll to top to show the message
            window.scrollTo(0, 0);
            
            // Hide the message after 3 seconds
            setTimeout(function() {
                document.getElementById('success-message').style.display = 'none';
            }, 3000);
        });
    </script>
</body>
</html>
"""
    
    with open('profile.html', 'w') as f:
        f.write(html_content)
    
    print("Profile page 'profile.html' has been generated successfully!")

def main():
    """
    Generate all HTML pages for the application.
    """
    generate_login_page()
    
    generate_profile_page()
    
    print("\nAll pages have been generated successfully!")
    print("Open 'index.html' in a web browser to start using the application.")

if __name__ == "__main__":
    main()
