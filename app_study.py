import streamlit as st

# App title and description
st.title("Pantomath Exam Prep : Your One-Stop Destination for Exam Preparation")
st.write("Prepare for competitive exams, higher studies admissions, and skill development courses with us!")

# Sidebar for navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.selectbox("Go to", ["Home", "Study Materials", "Live Classes", "Doubt-Clearing", "Mock Tests"])

# Home page
if app_mode == "Home":
    st.header("Welcome to ExamPrep!")
    st.write("""
    We provide:
    - Comprehensive study materials
    - Live classes by expert faculty
    - Doubt-clearing sessions
    - Mock tests to track your progress
    Explore each section for more details!
    """)
    
# Study Materials Section
elif app_mode == "Study Materials":
    st.header("Study Materials")
    st.write("Find materials for various exams:")
    st.selectbox("Select your exam", [
    "CAT & OMETS",
    "IIT JEE",
    "NEET",
    "GATE",
    "UPSC",
    "Railways Exams",
    "Defence Exams",
    "CLAT & AILET",
    "CTET & NET",
    "Private Sector Exams",
    "Banking Exams",
    "SSC CGL",
    "JEE",
    "NEET",
    "GATE",
    "CAT",
    "UPSC"
])
    st.write("Download study materials and notes from this section.")
    st.button("Download PDF")

# Live Classes Section
elif app_mode == "Live Classes":
    st.header("Live Classes")
    st.write("Join live classes to enhance your preparation.")
    st.write("Check out the schedule and join the sessions.")
    st.button("Join Live Class")

# Doubt-Clearing Section
elif app_mode == "Doubt-Clearing":
    st.header("Doubt-Clearing Sessions")
    st.write("Submit your doubts here, and our experts will resolve them in live sessions.")
    doubt = st.text_area("Enter your doubt")
    if st.button("Submit"):
        st.write("Your doubt has been submitted.")

# Mock Tests Section
elif app_mode == "Mock Tests":
    st.header("Mock Tests")
    st.write("Take mock tests to evaluate your preparation.")
    st.button("Start Mock Test")
