import streamlit as st
from api.conecction import connection

class ChatInterface:
    def __init__(self, titulo="", llamada_id=None):
        if 'chat_history' not in st.session_state:
            st.session_state.chat_history = []
        self.connection = connection()
        self.llamada_id = llamada_id
        self.titulo = titulo

    def display_chat(self):
        st.title("UCaldas Bot: " + self.titulo)
        st.markdown(
            """
            <style>
            .chat-bubble {
            padding: 10px;
            margin: 5px;
            border-radius: 10px;
            max-width: 70%;
            color: black;
            }
            .user-message {
            background-color: #DCF8C6;
            align-self: flex-end;
            }
            .bot-message {
            background-color: #ECECEC;
            align-self: flex-start;
            }
            .chat-container {
            display: flex;
            flex-direction: column;
            }
            </style>
            """, unsafe_allow_html=True
        )
        chat_display = st.empty()
        message = st.text_input("Enter your message:")
        if st.button("Send"):
            self.send_message(message)
        chat_html = "<div class='chat-container'>"
        for msg in st.session_state.chat_history:
            if msg.startswith("You:"):
                chat_html += f"<div class='chat-bubble user-message'>{msg}</div>"
            else:
                chat_html += f"<div class='chat-bubble bot-message'>{msg}</div>"
        chat_html += "</div>"
        chat_display.markdown(chat_html, unsafe_allow_html=True)

    def send_message(self, message):
        if message:
            st.session_state.chat_history.append(f"You: {message}")
            response = self.connection.make_put_call("mensage",{"id": self.llamada_id, "mensaje": message})
            st.session_state.chat_history.append(f"Bot: {response}")

if __name__ == "__main__":
    chat_interface = ChatInterface()
    chat_interface.display_chat()
