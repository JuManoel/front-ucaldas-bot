import streamlit as st
from api.conecction import connection
from interface.chat import ChatInterface

class LoginApp:
    def __init__(self):
        self.option = None
        self.agree = False
        self.connection = connection()

    def run(self):
        # Título de la aplicación
        st.title('UCaldas Bot')

        # Select box con valores
        options = {
            'Matricula': 0,
            'Entrar a U': 1,
            'Convalidaciones': 2,
            'Cambio de carrera': 3,
            'Otro': 4
        }
        
        st.write(f'Cualquier duda sobre la Universidad de Caldas, puedes preguntar aquí.')

        self.option = st.selectbox(
            'Sobre que tienes dudas?',
            list(options.keys())
        )
        self.option_value = options[self.option]

        # Checkbox para aceptar términos y condiciones
        self.agree = st.checkbox('Acepto los términos y condiciones')

        # Botón para generar conversación
        if st.button('Generar conversación'):
            if self.agree:
                st.write(f'Has seleccionado: {self.option}')
                st.write('Generando conversación...')
                id = self.connection.make_post_call('llamada', {'law': self.option})
                st.experimental_rerun()
                ChatInterface(titulo=self.option, llamada_id=id).display_chat()
            else:
                st.write('Debes aceptar los términos y condiciones para continuar.')