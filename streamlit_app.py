import streamlit as st

# Set the page layout
st.set_page_config(page_title="Matt Getigan's Autobiography", layout="centered")

# Title and Header with center alignment
st.markdown("""
    <h1 style='text-align: center;'>My Life Journey</h1>
    <h2 style='text-align: center;'>From Humble Beginnings to Professional Growth</h2>
    """, unsafe_allow_html=True)

# Introduction
st.subheader("Introduction")
st.image("portal.jpg", caption="A Glimpse of My Journey")
st.write("""
Hi there! I'm Matt Jude Augustine U. Getigan. I was born and raised in Cebu, 
and I've always been driven by a strong work ethic and a passion for learning. 
Through this autobiography, I want to share my story with you the experiences that shaped me 
and the path I've walked to become who I am today.
""")

# Early Life
st.subheader("Early Life")
st.image("bata.jpg", caption="My Hometown")
st.write("""
Growing up in Cebu City, I was surrounded by a supportive family that instilled in me 
the values of hard work and perseverance. My childhood was filled with both joys and challenges, 
all of which played a significant role in shaping my character.
I attended Zapatera Elementary School from 2006 to 2012, where I first discovered my love for learning 
and began building the foundation for my future.
""")

# Adolescence
st.subheader("Adolescence")
st.image("red.jpg", caption="Formative School Years")
st.write("""
My teenage years were a time of exploration and growth. During my time at Abellana National Highschool (2012-2016) 
and later at Cebu Institute of Technology – University for Senior High School (2016-2018), 
I began to develop a clearer sense of who I was and what I wanted to achieve in life.
These years were marked by my involvement in University Dance Troupe, as well as the ups and downs 
that come with growing up. Each experience contributed to my understanding of the world and my place in it.
""")

# Adulthood
st.subheader("Adulthood")
st.image("shs.jpg", caption="Embarking on My Professional Journey")
st.write("""
After graduating high school, I pursued a degree in Information Technology at Cebu Institute of Technology – University. 
My college years (2018-present) were transformative, as I balanced my studies with the beginning of my professional career.
I started working as a Lead Generation Specialist & Sales Representative at AVANT in 2020, where I learned the ropes 
of customer service and project management.
Later, I took on the role of a Prior-Auth Specialist/Medical Staff at Center for the Healthy Hearts (2021-2024), 
where I gained valuable experience in the medical field, handling patient interactions and mastering administrative tasks.
""")

# Achievements and Accomplishments
st.subheader("Achievements and Accomplishments")
st.image("tops.jpg", caption="Celebrating Milestones")
st.write("""
Throughout my career, I've been recognized for my ability to manage projects efficiently, lead teams with confidence, 
and deliver high-quality results. I've honed my skills in multitasking, medical terminology, and administrative support, 
all of which have been crucial to my success.
On a personal level, I've also achieved obtaining things i've been wishing for a long time, which have been just as rewarding as my professional accomplishments.
""")

# Reflections
st.subheader("Reflections")
st.image("bagyo.jpg", caption="Looking Back with Gratitude")
st.write("""
Looking back, due to Typhoon Odette I see how every challenge and achievement has played a part in my personal growth. 
I've learned the value of resilience, adaptability, and the importance of continuous living and learning.
These experiences have shaped my approach to life and work, and I'm grateful for the lessons they've taught me.
""")

# Future Aspirations
st.subheader("Future Aspirations")
st.image("fam.jpg", caption="Excited for the Future")
st.write("""
As I look to the future, I'm excited about the possibilities that lie ahead. 
I plan to continue growing both personally and professionally, taking on new challenges and expanding my skills.
My long-term goals include owning my own company, and I'm committed to making a positive impact in my field and in the lives of others.
""")

# Conclusion
st.subheader("Conclusion")
st.image("conclusion.jpg", caption="Grateful for the Journey")
st.write("""
In closing, my journey has been one of growth, perseverance, and continuous learning. 
I hope that by sharing my story, I can inspire others to chase their dreams and face challenges head-on. 
Thank you for taking the time to read my autobiography. Remember, no matter where you start, with determination and effort, you can achieve great things.
""")
