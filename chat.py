import streamlit as st
import threading
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialize Flask app and SocketIO
flask_app = Flask(__name__)
flask_app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(flask_app)

# Flask route
@flask_app.route('/')
def index():
    return render_template('chat.html')

@socketio.on('message')
def handle_message(msg):
    print(f"Message: {msg}")
    send(msg, broadcast=True)

# Function to run Flask app in a separate thread
def run_flask_app():
    socketio.run(flask_app, port=5000)

# Start Flask app in a separate thread
threading.Thread(target=run_flask_app).start()

# Streamlit code
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Person"])[0]

st.set_page_config(page_title="Welcome")

PERSON_NAME = get_person_name()
st.header(f"Welcome, {PERSON_NAME}!", anchor=False)
st.subheader("Use this link to access the live chat:")
st.markdown("[Open Live Chat](http://127.0.0.1:5000/)")



st.header("unblocker website")
st.subheader("use this link as a normal browser:")
st.markdown("https://4wt6q5-8080.csb.app/")
