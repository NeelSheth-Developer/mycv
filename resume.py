import streamlit as st
import smtplib
import requests
from streamlit_option_menu import option_menu
import plotly.graph_objects as go

st.set_page_config(page_icon="📑",
                   page_title="Digital CV | Neel Sheth",
                   )

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
col2.download_button(label="📄Download Resume",
                     data=file_content,
                     file_name="Sheth Neel Resume.pdf",
                     mime="application/octet-stream")

# Function to get IP address and location
def get_ip_location():
    ip_data = requests.get("https://api.ipify.org?format=json").json()
    ip_address = ip_data["ip"]
    
    location_data = requests.get(f"https://ipinfo.io/{ip_address}/json").json()
    location = location_data.get("city", "Unknown City") + ", " + location_data.get("region", "Unknown Region") + ", " + location_data.get("country", "Unknown Country")
    
    return ip_address, location

# Get IP and location when the page is visited
ip_address, location = get_ip_location()
visit_message = f"Visitor IP: {ip_address}\nLocation: {location}"

# Send email notification for the visit
sender_email = "neeldemo2050@gmail.com"
receiver_email = "shethneel2022@gmail.com"
subject = f"Website Visit Notification"

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, "bmby ttlr ampu dilj")
    email_message = f"Subject: {subject}\n\n{visit_message}"
    server.sendmail(sender_email, receiver_email, email_message)
    server.quit()
except Exception as e:
    st.warning(f"Email notification failed: {e}")

#--------------------------------menu---------------------------------
st.write("--------------------")
with st.container():
    contain = option_menu(
        menu_title=None,
        options=["MySelf", "My Projects", "Contact Me"],
        icons=["person", "code-slash", "chat-left-text-fill"],
        orientation="horizontal"
    )
#------------------------------------myself-------------------------
    if contain == "MySelf":
        # Add the rest of your 'MySelf' content here
        pass

#--------------------contact me------------------------------------------     
    elif contain == "Contact Me":   
        st.markdown("## Contact me 📨")
        name = st.text_input("Enter your name:")
        email = st.text_input("Enter your Email-id")
        notes = st.text_area("Enter your Message:")
        combine = name + "--" + email + "--" + notes

        if st.button("Send"):
            try:
                # Send the email
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(sender_email, "bmby ttlr ampu dilj")
                email_message = f"Subject: {subject}\n\n{combine}"
                server.sendmail(sender_email, receiver_email, email_message)
                server.quit()
                st.success("Your Message is Sent Successfully")
            except Exception as e:
                st.warning(f"Oops, there was an error: {e}")

