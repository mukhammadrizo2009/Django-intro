from django.http import HttpResponse

def home_view(x):
    
    content = """"<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home | MySite</title>
    <style>
        body {
            margin: 0;
            font-family: "Poppins", sans-serif;
            background-color: #f9fafc;
        }
        header {
            background-color: #0072ff;
            color: white;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        nav a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-weight: 500;
        }
        nav a:hover {
            text-decoration: underline;
        }
        section {
            text-align: center;
            margin-top: 80px;
        }
        section h1 {
            font-size: 2.5em;
        }
        .cards {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            margin-top: 40px;
            gap: 25px;
        }
        .card {
            width: 250px;
            background-color: white;
            border-radius: 16px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            padding: 25px;
            transition: 0.3s;
        }
        .card:hover {
            transform: translateY(-10px);
        }
    </style>
</head>
<body>
    <header>
        <h2>🏠 Home</h2>
        <nav>
            <a href="/about/">About</a>
            <a href="/contact/">Contact</a>
            <a href="/profile/">Profile</a>
        </nav>
    </header>

    <section>
        <h1>Welcome Back!</h1>
        <p>Explore our latest updates below 👇</p>
        <div class="cards">
            <div class="card">
                <h3>🔥 New Courses</h3>
                <p>Discover the latest programming and design lessons.</p>
            </div>
            <div class="card">
                <h3>💬 Community</h3>
                <p>Join our growing developer and designer community.</p>
            </div>
            <div class="card">
                <h3>🎯 Your Goals</h3>
                <p>Track your progress and reach new milestones.</p>
            </div>
        </div>
    </section>
</body>
</html>

"""
    
    return HttpResponse(content=content)

def about_view(x):
    
    content = """{% extends 'base.html' %}
{% block title %}About | MySite{% endblock %}
{% block content %}
<h1>About Us</h1>
<p>
    We are a passionate digital team focused on helping learners grow their skills in programming,
    design, and technology. Our mission is to make high-quality education available for everyone.
</p>

<div class="cards">
    <div class="card">
        <h3>🌟 Our Mission</h3>
        <p>Empowering students worldwide with free and creative learning tools.</p>
    </div>
    <div class="card">
        <h3>🚀 Our Vision</h3>
        <p>We believe education is the key to innovation and global growth.</p>
    </div>
    <div class="card">
        <h3>💡 What We Do</h3>
        <p>We build simple, elegant, and effective platforms for self-learning.</p>
    </div>
</div>
{% endblock %}

"""
    
    return HttpResponse(content=content)

def contact_view(x):
    
    content = """<{% extends 'base.html' %}
{% block title %}Contact | MySite{% endblock %}
{% block content %}
<h1>Contact Us</h1>
<p>Got questions, ideas, or feedback? We'd love to hear from you 👇</p>

<form>
    <label for="name">Full Name</label>
    <input type="text" id="name" placeholder="Enter your full name" required>

    <label for="email">Email</label>
    <input type="email" id="email" placeholder="Enter your email" required>

    <label for="message">Message</label>
    <textarea id="message" rows="6" placeholder="Write your message..." required></textarea>

    <button type="submit">Send Message</button>
</form>

<div class="cards" style="margin-top: 50px;">
    <div class="card">
        <h3>📍 Our Office</h3>
        <p>Samarkand, Uzbekistan</p>
    </div>
    <div class="card">
        <h3>📧 Email</h3>
        <p>support@mysite.com</p>
    </div>
    <div class="card">
        <h3>📞 Phone</h3>
        <p>+998 90 123 45 67</p>
    </div>
</div>
{% endblock %}

"""
    
    return HttpResponse(content=content)

def login_view(x):
    
    content = """{% extends 'base.html' %}
{% block title %}Login | MySite{% endblock %}
{% block content %}
<h1>Welcome Back 👋</h1>
<p>Login to continue to your account.</p>

<form method="post">
    {% csrf_token %}
    <label for="username">Username</label>
    <input type="text" id="username" name="username" placeholder="Enter your username" required>

    <label for="password">Password</label>
    <input type="password" id="password" name="password" placeholder="Enter your password" required>

    <button type="submit">Login</button>
</form>

<p style="text-align:center; margin-top: 15px;">
    Don’t have an account? <a href="/register/">Register here</a>.
</p>
{% endblock %}

"""
    
    return HttpResponse(content=content)

def register_view(x):
    
    content = """{% extends 'base.html' %}
{% block title %}Register | MySite{% endblock %}
{% block content %}
<h1>Create an Account 📝</h1>
<p>Join our community and start your learning journey today!</p>

<form method="post">
    {% csrf_token %}
    <label for="username">Username</label>
    <input type="text" id="username" name="username" placeholder="Choose a username" required>

    <label for="email">Email</label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>

    <label for="password">Password</label>
    <input type="password" id="password" name="password" placeholder="Create a password" required>

    <label for="confirm">Confirm Password</label>
    <input type="password" id="confirm" name="confirm" placeholder="Re-enter password" required>

    <button type="submit">Register</button>
</form>

<p style="text-align:center; margin-top: 15px;">
    Already have an account? <a href="/login/">Login here</a>.
</p>
{% endblock %}

"""
    
    return HttpResponse(content=content)

def profile_view(x):
    
    content = """{% extends 'base.html' %}
{% block title %}Profile | MySite{% endblock %}
{% block content %}
<h1>Your Profile</h1>
<p>Hello, <strong>{{ username }}</strong> 🎉 Welcome to your dashboard.</p>

<div class="cards">
    <div class="card">
        <h3>📘 Your Courses</h3>
        <p>You are currently enrolled in 3 active courses.</p>
    </div>
    <div class="card">
        <h3>🏆 Achievements</h3>
        <p>You've earned 4 certificates and 2 badges so far!</p>
    </div>
    <div class="card">
        <h3>⚙️ Settings</h3>
        <p>Update your password, profile photo, and preferences.</p>
    </div>
</div>

<a href="/logout/" class="btn" style="margin-top:40px;">Logout</a>
{% endblock %}

"""
    
    return HttpResponse(content=content)

def welcome_view(x):
    
    content = """<<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Muhammad Rizo | Personal Website</title>
  <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap" rel="stylesheet">
  <style>
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: 'Poppins', sans-serif;
    }

    body {
      background-color: #0f172a;
      color: white;
    }

    header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 25px 80px;
      background: rgba(255, 255, 255, 0.05);
      backdrop-filter: blur(10px);
      position: sticky;
      top: 0;
      z-index: 1000;
    }

    header h1 {
      font-size: 24px;
      color: #38bdf8;
      letter-spacing: 2px;
    }

    nav a {
      color: white;
      margin: 0 15px;
      text-decoration: none;
      font-weight: 500;
      transition: color 0.3s ease;
    }

    nav a:hover {
      color: #38bdf8;
    }

    .hero {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 100px 80px;
      min-height: 90vh;
    }

    .hero-text {
      max-width: 50%;
    }

    .hero-text h2 {
      font-size: 40px;
      color: #38bdf8;
      margin-bottom: 15px;
    }

    .hero-text h3 {
      font-size: 24px;
      font-weight: 300;
      margin-bottom: 20px;
      color: #cbd5e1;
    }

    .hero-text p {
      line-height: 1.8;
      color: #94a3b8;
      margin-bottom: 30px;
    }

    .btn {
      display: inline-block;
      background: #38bdf8;
      color: #0f172a;
      padding: 12px 28px;
      border-radius: 30px;
      font-weight: 600;
      text-decoration: none;
      transition: all 0.3s ease;
    }

    .btn:hover {
      background: #0ea5e9;
      transform: translateY(-3px);
    }

    .hero-img img {
      width: 350px;
      border-radius: 50%;
      border: 5px solid #38bdf8;
      box-shadow: 0 0 30px rgba(56, 189, 248, 0.4);
    }

    footer {
      text-align: center;
      padding: 30px;
      background: rgba(255, 255, 255, 0.05);
      font-size: 14px;
      color: #94a3b8;
    }

    @media (max-width: 900px) {
      .hero {
        flex-direction: column;
        text-align: center;
      }

      .hero-text {
        max-width: 100%;
      }

      .hero-img img {
        margin-top: 40px;
        width: 250px;
      }

      header {
        padding: 20px 30px;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>Muhammad Rizo</h1>
    <nav>
      <a href="#">Home</a>
      <a href="#">About</a>
      <a href="#">Projects</a>
      <a href="#">Contact</a>
    </nav>
  </header>

  <section class="hero">
    <div class="hero-text">
      <h2>Salom, men Muhammad Rizo!</h2>
      <h3>Backend Developer & Learner 💻</h3>
      <p>Men dasturlash, texnologiya va innovatsiyalarni sevaman. Hozirda Najot Ta'limda Backend yo‘nalishida tahsil olyapman va o‘z shaxsiy loyihalarim ustida ishlayapman.</p>
      <a href="#projects" class="btn">Mening ishlarimni ko‘r</a>
    </div>
    <div class="hero-img">
      <img src="https://avatars.githubusercontent.com/u/9919?s=280&v=4" alt="Profile Photo">
    </div>
  </section>

  <footer>
    © 2025 Muhammad Rizo. All rights reserved.
  </footer>
</body>
</html>

 """
    
    return HttpResponse(content=content)