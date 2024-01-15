import streamlit as st
from send_email import send_email

with st.form(key="send_email"):
    email_input=st.text_input("Enter email here")
    selector=st.selectbox('What topics you want to discuss?',('Job Inquires', 'Project Proposal', 'Other'))
    text=st.text_input("Enter text here")
    button=st.form_submit_button("Submit")
    message=f"""\
Subject: {selector}

From: {email_input}
{text}"""
    if button:
        send_email(message)
        st.info("Email sent successfully")