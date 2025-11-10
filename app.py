import streamlit as st
import pandas as pd
import numpy as np
from streamlit_autorefresh import st_autorefresh
import streamlit.components.v1 as components   # ← ESTE es el nombre correcto
# =========================================================
# 1) Google Analytics (GA4) – DEBE IR AL INICIO
# =========================================================
components.html("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P8FNDR77N5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-P8FNDR77N5', { 'debug_mode': true });
</script>
""", height=0)


# =========================================================
# 2) Función para enviar eventos a GA4 desde Streamlit
# =========================================================
def send_ga_event(event_name: str, params: dict = None):
    if params is None:
        params = {}
    js = f"""
    <script>
      gtag('event', '{event_name}', {params});
    </script>
    """
    st.markdown(js, unsafe_allow_html=True)


# =========================================================
# 3) UI – Estructura de navegación
# =========================================================
st.sidebar.header("Navegación")
page = st.sidebar.radio("Ir a:", ["Inicio", "Indicadores", "Exportaciones"])

# Registrar vista de página en GA
send_ga_event("page_view_custom", {"page_name": page})


# =========================================================
# 4) CONTENIDOS POR PÁGINA
# =========================================================

# -------- Página: INICIO --------
if page == "Inicio":
    st.title("🚀 App de prueba con GA4 y Streamlit Cloud")
    st.write("Esta página demuestra el tracking completo (A–E).")

    df = pd.DataFrame({
        'x': range(1, 11),
        'y': np.random.randint(10, 50, 10)
    })
    st.line_chart(df.set_index("x"))

    if st.button("Procesar datos"):
        send_ga_event("button_click", {"button_name": "Procesar datos"})
        st.success("Datos procesados (simulado).")


# -------- Página: INDICADORES --------
elif page == "Indicadores":
    st.title("📊 Indicadores")

    df = pd.DataFrame({
        "Indicador": ["Exportaciones", "IED", "Turismo"],
        "Valor": np.random.randint(100, 900, 3)
    })
    st.table(df)

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Descargar indicadores",
        csv,
        "indicadores.csv",
        "text/csv",
        on_click=lambda: send_ga_event("file_download", {"file_name": "indicadores.csv"})
    )


# -------- Página: EXPORTACIONES --------
elif page == "Exportaciones":
    st.title("🌎 Exportaciones")

    df = pd.DataFrame({
        'País': ["EE.UU", "México", "Chile", "Perú"],
        'Exportaciones (M USD)': np.random.randint(50, 500, 4)
    })
    st.bar_chart(df.set_index("País"))

    st.write("Esta página también tiene tracking activo.")


# =========================================================
# 5) Engagement (Tiempo activo del usuario) - SIN LOOPS
# =========================================================

# Auto refresco cada 10s (10000 ms)
st_autorefresh(interval=10000, limit=100000, key="engagement_refresh")

# Contador de tiempo activo
if "engaged_seconds" not in st.session_state:
    st.session_state["engaged_seconds"] = 0

st.session_state["engaged_seconds"] += 10

send_ga_event("engagement_ping", {"engaged_seconds": st.session_state["engaged_seconds"]})
