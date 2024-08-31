import streamlit as st

# Set the page layout
st.set_page_config(page_title="Matt Getigan's Autobiography", layout="centered")

# Custom CSS for aesthetics
st.markdown("""
    <style>
    body {
        background-color: #f5f5f5;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        font-family: 'Arial', sans-serif;
        color: #333333;
    }
    h2, h3 {
        font-family: 'Helvetica', sans-serif;
        color: #444444;
    }
    .header {
        text-align: center;
    }
    img {
        border-radius: 10px;
        margin: 10px 0;
    }
    .caption {
        font-style: italic;
        color: #555555;
        text-align: center;
        font-size: 0.9em;
    }
    .content {
        text-align: justify;
        line-height: 1.6;
        font-family: 'Georgia', serif;
        color: #666666;
    }
    </style>
""", unsafe_allow_html=True)

# Title and Header with center alignment
st.markdown("""
    <div class="header">
        <h1>My Life Journey</h1>
        <h2>From Humble Beginnings to Professional Growth</h2>
    </div>
    """, unsafe_allow_html=True)

# Introduction
st.markdown("<h3 style='text-align: center;'>Introduction</h3>", unsafe_allow_html=True)
st.image("portal.jpg", caption="A Glimpse of My Journey")
st.markdown("""
<div class="content">
    Hi there! I'm Matt Jude Augustine U. Getigan. I was born and raised in Cebu, 
    and I've always been driven by a strong work ethic and a passion for learning. 
    Through this autobiography, I want to share my story with you the experiences that shaped me 
    and the path I've walked to become who I am today.
</div>
""", unsafe_allow_html=True)

# Early Life
st.markdown("<h3 style='text-align: center;'>Early Life</h3>", unsafe_allow_html=True)
st.image("bata.jpg", caption="My Hometown")
st.markdown("""
<div class="content">
    Growing up in Cebu City, I was surrounded by a supportive family that instilled in me 
    the values of hard work and perseverance. My childhood was filled with both joys and challenges, 
    all of which played a significant role in shaping my character.
    I attended Zapatera Elementary School from 2006 to 2012, where I first discovered my love for learning 
    and began building the foundation for my future.
</div>
""", unsafe_allow_html=True)

# Adolescence
st.markdown("<h3 style='text-align: center;'>Adolescence</h3>", unsafe_allow_html=True)
st.image("red.jpg", caption="Formative School Years")
st.markdown("""
<div class="content">
    My teenage years were a time of exploration and growth. During my time at Abellana National Highschool (2012-2016) 
    and later at Cebu Institute of Technology – University for Senior High School (2016-2018), 
    I began to develop a clearer sense of who I was and what I wanted to achieve in life.
    These years were marked by my involvement in University Dance Troupe, as well as the ups and downs 
    that come with growing up. Each experience contributed to my understanding of the world and my place in it.
</div>
""", unsafe_allow_html=True)

# Adulthood
st.markdown("<h3 style='text-align: center;'>Adulthood</h3>", unsafe_allow_html=True)
st.image("shs.jpg", caption="Embarking on My Professional Journey")
st.markdown("""
<div class="content">
    After graduating high school, I pursued a degree in Information Technology at Cebu Institute of Technology – University. 
    My college years (2018-present) were transformative, as I balanced my studies with the beginning of my professional career.
    I started working as a Lead Generation Specialist & Sales Representative at AVANT in 2020, where I learned the ropes 
    of customer service and project management.
    Later, I took on the role of a Prior-Auth Specialist/Medical Staff at Center for the Healthy Hearts (2021-2024), 
    where I gained valuable experience in the medical field, handling patient interactions and mastering administrative tasks.
</div>
""", unsafe_allow_html=True)

# Achievements and Accomplishments
st.markdown("<h3 style='text-align: center;'>Achievements and Accomplishments</h3>", unsafe_allow_html=True)
st.image("tops.jpg", caption="Celebrating Milestones")
st.markdown("""
<div class="content">
    Throughout my career, I've been recognized for my ability to manage projects efficiently, lead teams with confidence, 
    and deliver high-quality results. I've honed my skills in multitasking, medical terminology, and administrative support, 
    all of which have been crucial to my success.
    On a personal level, I've also achieved obtaining things I've been wishing for a long time, which have been just as rewarding as my professional accomplishments.
</div>
""", unsafe_allow_html=True)

# Reflections
st.markdown("<h3 style='text-align: center;'>Reflections</h3>", unsafe_allow_html=True)
st.image("bagyo.jpg", caption="Looking Back with Gratitude")
st.markdown("""
<div class="content">
    Looking back, due to Typhoon Odette I see how every challenge and achievement has played a part in my personal growth. 
    I've learned the value of resilience, adaptability, and the importance of continuous living and learning.
    These experiences have shaped my approach to life and work, and I'm grateful for the lessons they've taught me.
</div>
""", unsafe_allow_html=True)

# Future Aspirations
st.markdown("<h3 style='text-align: center;'>Future Aspirations</h3>", unsafe_allow_html=True)
st.image("fam.jpg", caption="Excited for the Future")
st.markdown("""
<div class="content">
    As I look to the future, I'm excited about the possibilities that lie ahead. 
    I plan to continue growing both personally and professionally, taking on new challenges and expanding my skills.
    My long-term goals include owning my own company, and I'm committed to making a positive impact in my field and in the lives of others.
</div>
""", unsafe_allow_html=True)

# Conclusion
st.markdown("<h3 style='text-align: center;'>Conclusion</h3>", unsafe_allow_html=True)
st.image("conclusion.jpg", caption="Grateful for the Journey")
st.markdown("""
<div class="content">
    In closing, my journey has been one of growth, perseverance, and continuous learning. 
    I hope that by sharing my story, I can inspire others to chase their dreams and face challenges head-on. 
    Thank you for taking the time to read my autobiography. Remember, no matter where you start, with determination and effort, you can achieve great things.
</div>
""", unsafe_allow_html=True)
