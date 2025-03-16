import streamlit as st
import base64
from streamlit_pdf_viewer import pdf_viewer

# Set page title and icon
st.set_page_config(page_title="Pradeeshkumar U\nPortfolio", page_icon="🚀")

# Home Section
st.title("👋 Welcome to My Portfolio")
st.write("Hello! I'm a passionate developer and data scientist. This is my portfolio where you can explore my work and get in touch with me.")
st.divider()

# Projects Section
st.header("🛠️ My Projects")
projects = [
    {"name": "1.BMI calci App🏋️‍♂️", "description": "A simple BMI (Body Mass Index) Calculator built using Flutter. Enter your height and weight to calculate your BMI instantly.", "link": "https://github.com/Pradeeshkumar-U/BMIcalciApp"},
    {"name": "2.Weather App ☀️🌧️", "description": "A simple Weather App built using Flutter, fetching real-time weather data from the open weather api website.", "link": "https://github.com/Pradeeshkumar-U/WeatherApp"},
    {"name": "3.Waste Classifier using CNN", "description": "A waste classifier using CNN automatically identifies and categorizes waste into types like plastic, metal, and organic from images. This helps in efficient waste management and promotes recycling.", "link": "https://github.com/Pradeeshkumar-U/EdunetCNNProject"},
]
for project in projects:
    st.subheader(project["name"])
    st.write(project["description"])
    st.markdown(f"[🔗 View Project]({project['link']})")
st.divider()

# Resume Section
st.header("📄 My Resume")
resume_path = "resume/Pradeeshkumar U - resume.pdf"  # Change this to your actual resume file
st.write("### Preview of My Resume")
# Resume Page

    # Display PDF using iframe
pdf_viewer(resume_path)
    
    # Provide download option
with open(resume_path, "rb") as file:
    base64_pdf = base64.b64encode(file.read()).decode("utf-8")
href = f'<a href="data:application/pdf;base64,{base64_pdf}" download="Pradeeshkumar U - resume.pdf">📥 Download Resume</a>'
st.markdown(href, unsafe_allow_html=True)
st.divider()

# Contact Page
st.header("📬 Contact Me")
st.write("Feel free to reach out!")
st.write("📧 [Email](pradeeshkumar6382@gmail.com)")
st.write("🔗 [LinkedIn](https://www.linkedin.com/in/pradeeshkumar-u/)")
st.write("🐦 [Github](https://github.com/Pradeeshkumar-U)")
