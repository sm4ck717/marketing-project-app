import streamlit as st

# App title and description
st.title("Pantomath Career Booster : Upskill with Wellness and Stay Competitive")
st.write("An all-in-one platform for college students, job seekers, and working professionals to prepare for job interviews and upgrade their skills.")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Go to", ["Home", "Practical Sessions", "Mentorship", "Certifications & Assessments", "Learning Resources", "Career Development"])

# Home page
if app_mode == "Home":
    st.header("Welcome to CareerPrep!")
    st.write("""
    Our Offerings:
    - Hands-on practical sessions
    - One-on-one mentorship
    - Certifications & assessments
    - Access to learning resources
    - Career development support
    Explore each section to boost your employability!
    """)

# Practical Sessions Section
elif app_mode == "Practical Sessions":
    st.header("Hands-On Practical Sessions")
    st.write("Participate in real-world projects and practical workshops designed to enhance your skills.")
    st.selectbox("Choose a session type", [
    "Web Development",
    "Cloud Computing",
    "Digital Marketing",
    "Business Analytics",
    "Graphic Designing",
    "Content Writing",
    "Public Speaking",
    "Data Science with Python",
    "Machine Learning",
    "Time Management",
    "Mindfulness & Wellness",
    "Leadership",
    "Language Learning",
    "Personal Finance"
])
    st.button("Join Session")

# Mentorship Section
elif app_mode == "Mentorship":
    st.header("One-on-One Mentorship")
    st.write("Get personalized guidance from experienced professionals to achieve your career goals.")
    st.button("Request a Mentor")

# Certifications & Assessments Section
elif app_mode == "Certifications & Assessments":
    st.header("Certifications & Assessments")
    st.write("Earn industry-recognized certifications by completing courses and assessments.")
    st.button("View Available Certifications")

# Learning Resources Section
elif app_mode == "Learning Resources":
    st.header("Access to Learning Resources")
    st.write("Explore a vast library of tutorials, video lectures, and self-paced courses.")
    st.button("Browse Resources")

# Career Development Section
elif app_mode == "Career Development":
    st.header("Career Development Support")
    st.write("Receive support for resume building, interview preparation, and job search strategies.")
    st.button("Get Career Support")

