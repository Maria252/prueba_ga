import streamlit as st

# --- Google Analytics (GA4) ---
st.markdown("""
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-P8FNDR77N5"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-P8FNDR77N5');
</script>
""", unsafe_allow_html=True)

# --- UI de prueba ---
st.title("🚀 App de prueba para despliegue en Streamlit Cloud")
st.write("Si ves esto, la app funciona correctamente.")

# Pequeño demo para mostrar que Streamlit corre bien
import pandas as pd
import numpy as np

df = pd.DataFrame({
    'x': range(1, 11),
    'y': np.random.randint(10, 50, 10)
})

st.line_chart(df.set_index("x"))
