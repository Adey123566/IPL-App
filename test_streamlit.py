import streamlit as st
import streamlit.web.server.server as server

# Configure the server to use port 8080
server.Server.port = 8080

st.title("Test Page")
st.write("If you can see this, Streamlit is working!") 