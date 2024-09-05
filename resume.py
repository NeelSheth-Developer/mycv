import streamlit as st
import requests
import smtplib
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

# Function to fetch IP address
def get_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        ip = response.json()["ip"]
        return ip
    except requests.RequestException as e:
        st.error(f"Error fetching IP: {e}")
        return None

# Function to fetch location details using IP address
def get_location(ip):
    try:
        response = requests.get(f"http://ipapi.co/{ip}/json/")
        location_data = response.json()
        return location_data
    except requests.RequestException as e:
        st.error(f"Error fetching location: {e}")
        return None

# Function to get exact address from latitude and longitude
def get_exact_address(lat, lon):
    try:
        response = requests.get(f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}")
        address_data = response.json()
        return address_data.get('display_name')
    except requests.RequestException as e:
        st.error(f"Error fetching address: {e}")
        return None

# Function to send email with the visitor's information
def send_email(visitor_info):
    sender_email = "neeldemo2050@gmail.com"
    receiver_email = "neeldemo2050@gmail.com"
    subject = "New Visitor on Digital CV"
    message = f"Subject: {subject}\n\n{visitor_info}"
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, "bmby ttlr ampu dilj")  # Use your app password
        server.sendmail(sender_email, receiver_email, message)
        server.quit()
    except Exception as e:
        st.error(f"Error sending email: {e}")

# Main app code
st.set_page_config(page_icon="📑", page_title="Digital CV | Neel Sheth")

linkedin_url = "https://www.linkedin.com/in/neel-sheth-91b362262/"
col1, col2 = st.columns([1, 1])
file_path = "Neel-Sheth.pdf"
file_content = open(file_path, "rb").read()

col1.image("my.png", width=300)
col2.title("NEEL SHETH")
email_address = "shethneel2022@gmail.com"
col2.markdown(f"📧 <a style='color: white;' href='mailto:{email_address}'>{email_address}</a>", unsafe_allow_html=True)
phone_number = "(+91)7862861927"
col2.markdown(f"📞 [{phone_number}](tel:{phone_number})")
col2.markdown(f"[🔗 LinkedIn]({linkedin_url})")
col2.download_button(label="📄Download Resume", data=file_content, file_name="Sheth Neel Resume.pdf", mime="application/octet-stream")

# IP and Location Info
user_ip = get_ip()
if user_ip:
    location = get_location(user_ip)
    if location:
        lat = location.get('latitude')
        lon = location.get('longitude')
        exact_address = get_exact_address(lat, lon) if lat and lon else None
        visitor_info = f"Visitor IP: {user_ip}\nLocation: {location.get('city')}, {location.get('region')}, {location.get('country_name')}\nExact Address: {exact_address}\nISP: {location.get('org')}\nTime Zone: {location.get('timezone')}"
        st.write(f"IP: {user_ip}")
        st.write(f"Location: {location.get('city')}, {location.get('region')}, {location.get('country_name')}")
        st.write(f"Exact Address: {exact_address}")
        st.write(f"ISP: {location.get('org')}")
        st.write(f"Time Zone: {location.get('timezone')}")
        send_email(visitor_info)  # Send visitor info via email

#--------------------------------menu---------------------------------
st.write("--------------------")
with st.container():
   contain=option_menu(
     menu_title=None,
     options=["MySelf","My Projects","Contact Me"],
     icons=["person","code-slash","chat-left-text-fill"],
     orientation="horizontal"
   )

   
#------------------------------------myself-------------------------
   if contain=="MySelf":
      #summary
      st.subheader("Summary")
      st.write("""Dedicated and highly motivated Electronics and Communication Engineering student with a strong foundation in programming and technical skills. Passionate about leveraging technology to solve real-world problems, particularly in the field of data science. Demonstrated proficiency in Python, NumPy, Pandas, OpenCV, plotly,  SkLearn, streamlit, SQL, and MySQL, with hands-on experience in data visualization, image processing, and microcontroller programming. Committed to delivering excellence in both individual and team-based projects. Seeking opportunities to apply my knowledge and skills to make a meaningful impact in the field of data science, where I can contribute to cutting-edge advancements and innovative solutions.""")
      st.write("------------------------------")
      #---------------------------education----------------------------------------
      st.subheader("Education")
      st.write("""
      **📕B.Tech in Electronics and Communication Engineering**
      
          Nirma University, Ahmedabad
      
          🗓️September 2021 – June 2025
      
          • CGPA: 7.97
      
      **📕CLASS XII**
      
          Narayan Vidhyalay, Vadodara
      
          🗓️June 2021
      
          • Secured 84%
      
      **📕CLASS X**
      
          Bright School, Vadodara

          🗓️June 2019
      
          • Secured 80%""")
      st.write("-----------------------------------")

      col1,col2=st.columns([1,1])
      col1.subheader("Technical Skills")
      col1.write(" ")
      col1.write("""
      🟨 **Programming**:

      • Python
        (Opencv, sklearn, pandas, numpy, streamlit, FastAPI)

      • SQL (Intermediate)

      • Shell Scripting

      • Git
       
      • Perl
      
      • WebScraping

      🟨 **Data Visualization**:

      • MS Excel, Plotly, Matplotlib, Seaborn,
        PowerBI, Tableau

      🟨 **Machine Learning Modelling** :
      
      • Linear Regression, Logistic Regression, Decision Tree,
        Kmeans Clustering, KNN, RandomForest, NLP

      🟨 **Databases**:

      •  PostgreSQL, MySQL, MongoDB, Firebase""")
      col2.subheader("Soft Skills")
      labels = ['Communication', 'Adaptability', 'Analytical Skills', 'Teamwork', 'Project Management']
      fig = go.Figure(data=[go.Pie(labels=labels, hole=0.5, hoverinfo="label", textinfo="none")])
      col2.write(fig)
      st.write("--------------------------------------------")
      #-------------------------Tools and software----------------------------------
      st.subheader("Tools and Software")
      st.write("""     🔺
                        VSCode ,
                        Linux (Intermediate) , 
                        GitHub ,
                        Jupyter Lab ,
                        Google Colab""")
      st.write("---------------------------------------------")
      st.subheader("Experience")
      st.write("     **🚩 Nirma Funded - Multibot Coordinate System Project**")
      st.write("           🗓️ March 2023 - August 2023")
      st.write("            Worked with the image processing team, I contributed to the development of a cutting-edge program that leverages Python's OpenCV library. The system captures real-time data from a robotic car, employing ArUco markers for accurate localization. Using the acquired data, we implemented a graphical user interface (GUI) using Tkinter, allowing users to select specific shapes of interest. The program dynamically processes the chosen shape's attributes, creating a robust and intuitive interaction. Furthermore, the seamlessly integrated MQTT protocol facilitates the transmission of this processed real-time information to an ESP32 microcontroller, enabling efficient and low-latency control of the robotic car. This comprehensive solution demonstrates a fusion of computer vision, user interface design, and embedded systems for a versatile and responsive robotics application.""")
      st.write(" ")
      st.write("      **🚩 Student Placement Coordinator**")
      st.write("           🗓️February 2024 - Present")
      st.write("The role of a Student Placement Coordinator (SPC) entails assisting students with internship and placement-related inquiries, serving as a liaison between students and the Industry Institute Interaction (III) Cell.")
      st.write(" ")
      st.write("     **🚩 Data Analyst Intern at Hyperlab**")
      st.write("        🗓️March 2024 -Present")
      st.write("• Analyzed IMU sensor data to calculate athletic performance metrics (reflex time, fatigue levels, overshoot) with advanced processing and mathematics, improving accuracy by 30%")
      st.write("• Developed Python algorithms for reflex, overshoot, and BLE connectivity, enhancing performance tracking by 70%. Created visualizations with Python libraries (Pandas, NumPy, Matplotlib, Plotly) and BI tools (Power BI, Tableau),and designed a Streamlit dashboard that increased stakeholder engagement by 50%")
      st.write("----------------------------------------------")
      st.subheader("Achivements") 
      st.write("• Selected as a semifinalist in the Indian Automation Challenge 2023")
      st.write("[Certificate](https://github.com/DataMiiner/certificate/blob/main/FINAL%20CERTIFICATES-14.pdf)")
      st.write("• 2nd Runner-up in the DAS INFOMEDIA Track at the CSI Hackathon")
      st.write("[Certificate](https://github.com/NeelSheth-Developer/HackNuthon/tree/main)")
      

#----------------------projects-----------------------------
   
   elif contain=="My Projects":
# Links section
     st.markdown("## 🔗 Links")
     st.markdown("[Github Project Repository](https://github.com/NeelSheth-Developer)")
     st.markdown("[Code Forces](https://codeforces.com/profile/coder_1_neel)")
     #st.markdown("[My Website](https://your-website-url.com)")
     st.write("--------------------------------------------------")
     st.markdown("## 🗂️ Projects")
     st.subheader(" ")
     st.subheader("📈 Stock Market Dash Board using streamlit")
     st.write("""    • A web-based dashboard that helps to Analyse the historical data of anystocks.
                     
                     • Technology: Python, Pandas, Plotly, Streamlit""")
     co1,co2=st.columns([1,1])
     co1.write("[Github Repository](https://github.com/NeelSheth-Developer/stockanalysis)")
     co2.write("[Dashboard](https://stockanalysis-1000.streamlit.app/)")
     st.write("--------------------------------------------")
     st.subheader("🏥 Hospital Management System")
     st.write("""    • A web-based graphical user interface (GUI) designed to facilitate the comprehensive management of patient data, including the efficient handling of appointment information.
                    
                     • Technology: Mysql, Python, Streamlit, Pandas""")
     col4,col5=st.columns([1,1])
     col4.write("[Github Repository](https://github.com/NeelSheth-Developer/Hospital_management_system)")
     col5.write("[Hospital Management System Website](https://hospitalmanagementsystem-datamiiner.streamlit.app)")
     st.write("-----------------------------------------------------")
     st.subheader("📝 Student Marks Tracker")
     st.write("""    • A Python program designed to manage and organize students’ marks,utilizing Microsoft Excel for data storage and creating excel file.
                     
                     • Technology: MS Excel, Python, Pandas""")
     col6,col7=st.columns([1,1])
     col6.write("[Github Repository](https://github.com/NeelSheth-Developer/student_mark_tracker)")
     col7.write("[Student-Mark-tracker](https://student-mark-tracker-by-datamiiner.streamlit.app)")
     st.write("--------------------------------------------")
     st.subheader("📂 Student Internship and Placement Record System")
     st.write("""    • Student Internship and Placement Record System (SIPRS) website specifically designed for Student Placement Coordinators (SPCs). This platform enables SPCs to perform CRUD (Create, Read, Update, Delete) operations, manage internship and placement data in a MongoDB database, and conduct comprehensive analyses. The system facilitates tracking of placement statuses (placed and unplaced) and provides insights into the number of students placed in each company.

                     • Technology: Python, Pandas, Plotly, Streamlit, MongoDB """)
     col7,col8=st.columns([1,1])
     col7.write("[Github Repository](https://github.com/NeelSheth-Developer/Student-Internship-and-Placement-Record-System/tree/main)")
     col8.write("[Student Internship and Placement Record System](https://spc-ece-record-web.streamlit.app/)")


     st.write("--------------------------------------------")
     st.subheader("🤖 Personal Voice Assistant")
     st.write("""    • This project automates tasks via voice commands, including tab control, app management, system operations, Google searches, image generation, news reading, media playback, email sending, and note-taking, enhancing user productivity.
     
                     • Technology: Python, Html, CSS, Javascript,  Gemini API, Hugging Face API""")

     st.write("[Github Repository](https://github.com/NeelSheth-Developer/Personal-Voice-Assistant/tree/main)")
     st.write("-----------------------------------------------")
     st.subheader("📊 Sentimental Analysis of Amazon Product Reviews")

     st.write("""
• Developed a sentimental analysis project focusing on analyzing Amazon product reviews to extract insights into customer opinions and sentiments.

• Utilized Natural Language Processing (NLP) techniques to preprocess and tokenize text data, including techniques like tokenization and stemming.

• Implemented a machine learning model using the Random Forest algorithm from the Scikit-Learn (sklearn) library to classify reviews into positive and negative  neutral sentiment.

• Conducted extensive data manipulation and analysis using Pandas for data preprocessing and transformation tasks.

• Created interactive visualizations using Plotly to illustrate sentiment trends and patterns in the review data.

• Deployed the sentiment analysis model using Streamlit, allowing for a user-friendly web interface to analyze new reviews in real-time.

  
    • Technology: Scikit-Learn (Random Forest), NLP, Pandas, Plotly, Streamlit, BeautifulSoup""")
     
     col9,col10=st.columns([1,1])

     col9.write("[Github Repository](https://github.com/NeelSheth-Developer/Sentimental-Analysis-of-Amazon-Product-Reviews)")
     col10.write("[Sentiment Analysis of Amazon Product Reviews](https://sentimental-analysis-of-amazon-reviews.streamlit.app/)")
     st.write("------------------------------------------------------")
#--------------------contact me------------------------------------------     
   elif contain=="Contact Me":   
     st.markdown("## Contact me 📨")
     name=st.text_input("Enter your name:")
     
     email=st.text_input("Enter your Email-id")
     notes=st.text_area("Enter your Message:")
     combine=name+"--"+email+"--"+notes

     st.session_state["button"]=st.button("Send")
     # Email configuration
     sender_email = "neeldemo2050@gmail.com"
     receiver_email = "shethneel2022@gmail.com"
     subject = f"Notification from {name}"
     server=smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()

      # Login to your Gmail account
     server.login(sender_email,"bmby ttlr ampu dilj") 
     if st.session_state["button"]:
          # Send the email
          try:
             server.sendmail(sender_email, receiver_email, combine)
             st.success("Your Message is Send Successfully")
          except:
             st.warning("OOPs there is error!")
          # Close the SMTP connection
          server.quit()
