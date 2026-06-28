import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="ORION Dashboard",
    page_icon="🧠",
    layout="wide"
)

st.title(
    "🧠📦 ORION Dashboard de Observabilidad"
)

try:

    df = pd.read_csv(
        "logs/orion_logs.csv"
    )

    total = len(df)

    errores = (
        df["error"]
        .astype(str)
        .str.lower()
        .eq("true")
        .sum()
    )

    exitos = total - errores

    porcentaje = round(
        (exitos / total) * 100,
        2
    ) if total else 0

    st.subheader(
        "Métricas generales"
    )

    c1, c2, c3, c4, c5 = st.columns(5)

    c1.metric(
        "Consultas",
        total
    )

    c2.metric(
        "Éxitos",
        exitos
    )

    c3.metric(
        "Errores",
        errores
    )

    c4.metric(
        "Tasa éxito",
        f"{porcentaje}%"
    )

    c5.metric(
        "Latencia",
        round(
            df["latencia"]
            .astype(float)
            .mean(),
            2
        )
    )

    st.divider()

    st.subheader(
        "Herramientas utilizadas"
    )

    st.bar_chart(
        df["herramienta"]
        .value_counts()
    )

    st.subheader(
        "Latencia"
    )

    st.line_chart(
        df["latencia"]
        .astype(float)
    )

    st.subheader(
        "Precisión"
    )

    st.line_chart(
        df["precision"]
        .astype(float)
    )

    st.subheader(
        "Consumo CPU"
    )

    st.line_chart(
        df["cpu"]
        .astype(float)
    )

    st.subheader(
        "Consumo RAM"
    )

    st.line_chart(
        df["ram"]
        .astype(float)
    )

    st.subheader(
        "Trazabilidad"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

except Exception as e:

    st.error(
        f"Error: {e}"
    )