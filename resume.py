#Neel Sheth Digital Resume
import streamlit as st
import smtplib

from streamlit_option_menu import option_menu
import plotly.graph_objects as go

st.set_page_config(page_icon="📑",
                   page_title="Digital CV | Neel Sheth",
                   )


col1,col2=st.columns([1,1])
file_path = "Neel.K.Sheth_Resume.pdf"
file_content = open(file_path, "rb").read()


col1.image("my.png",width=300)
col2.title("NEEL SHETH")
email_address="shethneel2022@gmail.com"
col2.markdown(f"📧 <a style='color: white;' href='mailto:{email_address}'>{email_address}</a>", unsafe_allow_html=True)

phone_number = "(+91)7862861927"
col2.markdown(f"📞 [{phone_number}](tel:{phone_number})")
col2.download_button(label="📄Download Resume",
                     data=file_content,
                     file_name="Sheth Neel Resume.pdf",
                     mime="application/octet-stream")
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
      st.write("""Dedicated and highly motivated Electronics and Communication Engineering student with a strong foundation in programming and technical skills. Passionate about leveraging technology to solve real-world problems, particularly in the field of data science. Demonstrated proficiency in Python, NumPy, Pandas, OpenCV, plotly,  SkLearn, stramlit, SQL, and MySQL, with hands-on experience in data visualization, image processing, and microcontroller programming. Committed to delivering excellence in both individual and team-based projects. Seeking opportunities to apply my knowledge and skills to make a meaningful impact in the field of data science, where I can contribute to cutting-edge advancements and innovative solutions.""")
      st.write("------------------------------")
      #---------------------------education----------------------------------------
      st.subheader("Education")
      st.write("""
      **📕B.Tech in Electronics and Communication Engineering**
      
          Nirma University, Ahmedabad
      
          🗓️September 2021 – June 2025
      
          • CGPA: 7.87
      
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

      • Python (Opencv, sklearn, pandas, numpy)

      • SQL (Intermediate)

      • Shell Scripting

      • Perl

      🟨 **Data Visualization**:

      • MS Excel, Plotly

      • Machine Learning Modelling :
      
      Linear Regression, Logistic Regression,
      Decision Tree

      🟨 **Databases**:

      • MySQL""")
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
                        Jupyter Notebook ,
                        Google Colab""")
      st.write("---------------------------------------------")
      st.subheader("Experience")
      st.write("     **🚩 Nirma Funded - Multibot Coordinate System Project**")
      st.write("           🗓️ March 2023 - August 2023")
      st.write("            Worked with the image processing team, I contributed to the development of a cutting-edge program that leverages Python's OpenCV library. The system captures real-time data from a robotic car, employing ArUco markers for accurate localization. Using the acquired data, we implemented a graphical user interface (GUI) using Tkinter, allowing users to select specific shapes of interest. The program dynamically processes the chosen shape's attributes, creating a robust and intuitive interaction. Furthermore, the seamlessly integrated MQTT protocol facilitates the transmission of this processed real-time information to an ESP32 microcontroller, enabling efficient and low-latency control of the robotic car. This comprehensive solution demonstrates a fusion of computer vision, user interface design, and embedded systems for a versatile and responsive robotics application.""")
      st.write("----------------------------------------------")
      st.subheader("Achivements") 
      st.write("• Selected as a semifinalist in the Indian Automation Challenge 2023")
      st.write("[Certificate](https://github.com/DataMiiner/certificate/blob/main/FINAL%20CERTIFICATES-14.pdf)")
#----------------------projects-----------------------------
   
   elif contain=="My Projects":
# Links section
     st.markdown("## 🔗 Links")
     st.markdown("[Github Project Repository](https://github.com/DataMiiner)")
     st.markdown("[Code Forces](https://codeforces.com/profile/coder_1_neel)")
     #st.markdown("[My Website](https://your-website-url.com)")
     st.write("--------------------------------------------------")
     st.markdown("## 🗂️ Projects")
     st.subheader(" ")
     st.subheader("📈 Stock Market Dash Board using streamlit")
     st.write("""    • A web-based dashboard that helps to Analyse the historical data of anystocks.
                     
                     • Technology: Python, Pandas, Plotly, Streamlit""")
     co1,co2=st.columns([1,1])
     co1.write("[Github Repository](https://github.com/DataMiiner/stockanalysis/tree/main)")
     co2.write("[Dashboard](https://stockanalysis-1000.streamlit.app/)")
     st.write("--------------------------------------------")
     st.subheader("🏥 Hospital Management System")
     st.write("""    • A web-based graphical user interface (GUI) designed to facilitate the comprehensive management of patient data, including the efficient handling of appointment information.
                    
                     • Technology: Mysql, Python, Streamlit, Pandas""")
     col4,col5=st.columns([1,1])
     col4.write("[Github Repository](https://github.com/DataMiiner/Hospital_management_system/tree/main)")
     col5.write("[Hospital Management System Website](https://hospitalmanagementsystem-datamiiner.streamlit.app)")
     st.write("-----------------------------------------------------")
     st.subheader("📝 Student Marks Tracker")
     st.write("""    • A Python program designed to manage and organize students’ marks,utilizing Microsoft Excel for data storage and creating excel file.
                     
                     • Technology: MS Excel, Python, Pandas""")
     col6,col7=st.columns([1,1])
     col6.write("[Github Repository](https://github.com/DataMiiner/student_mark_tracker )")
     col7.write("[Student-Mark-tracker](https://student-mark-tracker-by-datamiiner.streamlit.app/)")

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
