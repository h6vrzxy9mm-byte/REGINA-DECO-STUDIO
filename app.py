
import streamlit as st

st.set_page_config(page_title="Regina Deco Studio", layout="wide")

st.title("🎈 Regina Deco Studio")
st.subheader("Armá tu decoración ideal")

st.sidebar.header("Paquetes")

paquete = st.sidebar.radio(
    "Elegí un paquete",
    ["Paquete Uno", "Paquete Dos", "Paquete Tres"]
)

st.sidebar.header("Elementos")

panel = st.sidebar.selectbox(
    "Tipo de panel",
    ["Panel pequeño", "Panel grande"]
)

forma = st.sidebar.selectbox(
    "Forma del panel",
    ["Redondeado", "Recto", "Inclinado"]
)

cilindros = st.sidebar.selectbox(
    "Cilindros",
    [
        "Transparentes",
        "Madera",
        "Blancos",
        "Fluorescentes"
    ]
)

neon = st.sidebar.selectbox(
    "Neón",
    [
        "Happy Birthday Grande",
        "Happy Birthday Pequeño"
    ]
)

globos = st.sidebar.slider(
    "Metros de globos",
    0, 10, 2
)

st.header("Vista previa")
st.info("Acá irá la decoración visual interactiva.")

precio = 0

if panel == "Panel pequeño":
    precio += 20000
else:
    precio += 25500

precio += 15000

if neon == "Happy Birthday Grande":
    precio += 25000
else:
    precio += 18000

precio += globos * 25000

traslado = 20000
armado = 50000

total = precio + traslado + armado

st.header("Cotización")

st.write(f"Panel: ${precio:,}")
st.write(f"Traslado: ${traslado:,}")
st.write(f"Armado y desarmado: ${armado:,}")

st.success(f"TOTAL: ${total:,}")

st.header("Consulta de disponibilidad")

fecha = st.date_input("Fecha del evento")
nombre = st.text_input("Nombre")
telefono = st.text_input("WhatsApp")

if st.button("Consultar disponibilidad"):
    st.success("Consulta enviada correctamente.")

st.header("Panel Administrador")

st.write("- Consultas")
st.write("- Calendario")
st.write("- Eventos")
st.write("- Estadísticas")
