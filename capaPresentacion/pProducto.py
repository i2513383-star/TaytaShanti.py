from capaLogicaNegocio.nProducto import nProducto
import streamlit as st

class PProducto:
    def __init__(self):
        self.__nProducto = nProducto()

        if 'producto_seleccionado' not in st.session_state:
            st.session_state.producto_seleccionado = None

        if 'form_key_producto' not in st.session_state:
            st.session_state.form_key_producto = 0

        self.construirInterfaz()

    def construirInterfaz(self):
        st.subheader("Gestión de Productos")

        producto = st.session_state.producto_seleccionado

        nombre = producto['nombre'] if producto else ''
        precio = producto['precio'] if producto else 0.0
        stock = producto['stock'] if producto else 0

        with st.form(f"formProducto{st.session_state.form_key_producto}"):
            txtNombre = st.text_input("Nombre", value=nombre)
            txtPrecio = st.number_input("Precio", min_value=0.0, step=0.1, value=float(precio))
            txtStock = st.number_input("Stock", min_value=0, step=1, value=int(stock))

            if producto:
                btnActualizar = st.form_submit_button("Actualizar", type="primary")
                if btnActualizar:
                    self.actualizarProducto(
                        {
                            "nombre": txtNombre,
                            "precio": txtPrecio,
                            "stock": txtStock
                        },
                        producto['id']
                    )
            else:
                btnGuardar = st.form_submit_button("Guardar", type="primary")
                if btnGuardar:
                    self.nuevoProducto(
                        {
                            "nombre": txtNombre,
                            "precio": txtPrecio,
                            "stock": txtStock
                        }
                    )

        self.mostrarProductos()

    def mostrarProductos(self):
        productos = self.__nProducto.mostrarProductos()

        col1, col2 = st.columns([8, 2])

        with col1:
            tabla = st.dataframe(productos, selection_mode="single-row", on_select="rerun")

        with col2:
            if tabla.selection.rows:
                indice = tabla.selection.rows[0]
                st.session_state.producto_seleccionado = productos[indice]

                if st.button("Editar"):
                    st.rerun()

                if st.button("Eliminar"):
                    self.eliminarProducto(productos[indice]['id'])

    def nuevoProducto(self, producto):
        self.__nProducto.nuevoProducto(producto)
        st.toast("Producto registrado correctamente")
        self.limpiar()

    def actualizarProducto(self, producto, id):
        self.__nProducto.actualizarProducto(producto, id)
        st.toast("Producto actualizado correctamente")
        self.limpiar()

    def eliminarProducto(self, id):
        self.__nProducto.eliminarProducto(id)
        st.toast("Producto eliminado correctamente")
        self.limpiar()

    def limpiar(self):
        st.session_state.producto_seleccionado = None
        st.session_state.form_key_producto += 1
        st.rerun()
