from capaLogicaNegocio.nProducto import nProducto
import streamlit as st


class PProducto:
    def __init__(self):
        self.__nProducto = nProducto()

        # Variables de sesión
        if 'formularioKey' not in st.session_state:
            st.session_state.formularioKey = 0

        if 'productoSeleccionado' not in st.session_state:
            st.session_state.productoSeleccionado = None

        if 'id_sesion' not in st.session_state:
            st.session_state.id_sesion = ''

        if 'nombre_sesion' not in st.session_state:
            st.session_state.nombre_sesion = ''

        if 'precio_sesion' not in st.session_state:
            st.session_state.precio_sesion = 0.0

        if 'stock_sesion' not in st.session_state:
            st.session_state.stock_sesion = 0

        self.__construirInterfaz()

    # ---------------- INTERFAZ ----------------
    def __construirInterfaz(self):
        st.title("Sistema de Ventas e Inventario - TAYTA SHANTI")

        # Si hay producto seleccionado (editar)
        if st.session_state.productoSeleccionado:
            st.session_state.id_sesion = st.session_state.productoSeleccionado["id"]
            st.session_state.nombre_sesion = st.session_state.productoSeleccionado["nombre"]
            st.session_state.precio_sesion = st.session_state.productoSeleccionado["precio"]
            st.session_state.stock_sesion = st.session_state.productoSeleccionado["stock"]

        with st.form(f"Formulario{st.session_state.formularioKey}"):

            txtNombre = st.text_input(
                "Nombre del producto",
                value=st.session_state.nombre_sesion
            )

            txtPrecio = st.number_input(
                "Precio",
                min_value=0.0,
                value=st.session_state.precio_sesion
            )

            txtStock = st.number_input(
                "Stock",
                min_value=0,
                value=st.session_state.stock_sesion
            )

            # ----- BOTONES -----
            if st.session_state.productoSeleccionado:
                btnActualizar = st.form_submit_button("Actualizar", type="primary")

                if btnActualizar:
                    producto = {
                        "nombre": txtNombre,
                        "precio": txtPrecio,
                        "stock": txtStock
                    }
                    self.actualizarProducto(producto, st.session_state.id_sesion)

            else:
                btnGuardar = st.form_submit_button("Guardar", type="primary")

                if btnGuardar:
                    producto = {
                        "nombre": txtNombre,
                        "precio": txtPrecio,
                        "stock": txtStock
                    }
                    self.nuevoProducto(producto)

        self.mostrarProductos()

    # ---------------- TABLA ----------------
    def mostrarProductos(self):
        listaProductos = self.__nProducto.mostrarProductos()

        col1, col2 = st.columns([10, 2])

        with col1:
            seleccion = st.dataframe(
                listaProductos,
                selection_mode="single-row",
                on_select="rerun"
            )

        with col2:
            if seleccion.selection.rows:
                index = seleccion.selection.rows[0]
                producto = listaProductos[index]

                btnEditar = st.button("Editar")
                btnEliminar = st.button("Eliminar")

                if btnEditar:
                    st.session_state.productoSeleccionado = producto
                    st.rerun()

                if btnEliminar:
                    self.eliminarProducto(producto["id"])

    # ---------------- CRUD ----------------
    def nuevoProducto(self, producto):
        try:
            self.__nProducto.nuevoProducto(producto)
            st.toast("Producto registrado correctamente")
            self.limpiar()
        except Exception as e:
            st.error(e)

    def actualizarProducto(self, producto, id_producto):
        try:
            self.__nProducto.actualizarProducto(producto, id_producto)
            st.toast("Producto actualizado correctamente")
            self.limpiar()
        except Exception as e:
            st.error(e)

    def eliminarProducto(self, id_producto):
        try:
            self.__nProducto.eliminarProducto(id_producto)
            st.toast("Producto eliminado correctamente")
            self.limpiar()
        except Exception as e:
            st.error(e)

    # ---------------- LIMPIAR ----------------
    def limpiar(self):
        st.session_state.formularioKey += 1
        st.session_state.productoSeleccionado = None
        st.session_state.id_sesion = ''
        st.session_state.nombre_sesion = ''
        st.session_state.precio_sesion = 0.0
        st.session_state.stock_sesion = 0
        st.rerun()

