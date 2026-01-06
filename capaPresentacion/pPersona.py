from capaLogicaNegocio.nPersona import nPersona
import streamlit as st

class PPersona:
    def __init__(self):
        self.__nPersona = nPersona()
        if 'formulariokey' not in st.session_state:
            st.session_state.formulariokey = 0 
        if 'persona_Selecionada' not in st.session_state:
            st.session_state.persona_Selecionada = ''
        if 'docIdentidad_sesion' not in st.session_state:
            st.session_state.docIdentidad_sesion = ''
        if 'nombre_sesion' not in st.session_state:
            st.session_state.nombre_sesion = ''
        if 'edad_sesion' not in st.session_state:
            st.session_state.edad_sesion = 0
        self.__construirInterfaz()
        
    def __construirInterfaz(self):
        st.title("tayta shanty")

        if st.session_state.persona_Selecionada != '':
            st.session_state.docIdentidad_sesion = st.session_state.persona_Selecionada['docIdentidad']
            st.session_state.nombre_sesion = st.session_state.persona_Selecionada['nombre']
            st.session_state.edad_sesion = st.session_state.persona_Selecionada['edad']

        with st.form(f'Formulario{st.session_state.formulariokey}'):
            textDocIdentidad = st.text_input('Documento de identidad',value=st.session_state.docIdentidad_sesion,disabled=st.session_state.persona_Selecionada != '')
            textNombre = st.text_input(
                'Nombre',
                value=st.session_state.nombre_sesion
            )
            textEdad = st.number_input(
                'Edad',
                min_value=0,
                max_value=150,
                value=st.session_state.edad_sesion
            )

            if st.session_state.persona_Selecionada != '':
                btnActualizar = st.form_submit_button('Actualizar', type='primary')
                if btnActualizar:
                    persona = {
                        'nombre': textNombre,
                        'edad': textEdad
                    }
                    self.actualizarPersona(persona, textDocIdentidad)
            else:
                btnGuardar = st.form_submit_button('Guardar', type='primary')
                if btnGuardar:
                    persona = {
                        'docIdentidad': textDocIdentidad,
                        'nombre': textNombre,
                        'edad': textEdad
                    }
                    self.nuevaPersona(persona)
            
        self.mostrarPersonas()
    
    def mostrarPersonas(self):
        listaPersonas = self.__nPersona.mostrarPersonas()
        col1, col2 = st.columns([10, 2])

        with col1:
            personaSelecionada = st.dataframe(
                listaPersonas,
                selection_mode='single-row',
                on_select='rerun'
            )
            
        with col2:
            if personaSelecionada.selection.rows:
                indice_persona = personaSelecionada.selection.rows[0]
                personaSelecionadaIndice = listaPersonas[indice_persona]
                btnEditar = st.button('Editar')
                btnEliminar = st.button('Eliminar')
                
                if btnEditar:
                    st.session_state.persona_Selecionada = personaSelecionadaIndice
                    st.rerun()
                    
                if btnEliminar:
                    self.eliminarPersona(personaSelecionadaIndice['docIdentidad'])
    def nuevaPersona(self, persona: dict):
        try:
            self.__nPersona.nuevaPersona(persona)
            st.toast('Registro insertado correctamente', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no insertado', duration='short')
            
    def actualizarPersona(self, persona: dict, docIdentidad: str):
        try:
            self.__nPersona.actualizasPersona(persona, docIdentidad)
            st.toast('Registro actualizado correctamente', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no actualizado', duration='short')
            
    def eliminarPersona(self, docIdentidad: str):
        try:
            self.__nPersona.eliminarPersona(docIdentidad)
            st.toast('Registro eliminado correctamente', duration='short')
            self.limpiar()
        except Exception as e:
            st.error(e)
            st.toast('Registro no eliminado', duration='short')

    def limpiar(self):
        st.session_state.formulariokey += 1
        st.session_state.persona_Selecionada = ''
        st.session_state.docIdentidad_sesion = ''
        st.session_state.nombre_sesion = ''
        st.session_state.edad_sesion = 0
        st.rerun()