import streamlit as st
import plotly.express as px
import pandas as pd

# Configurazione della pagina
st.set_page_config(
    page_title="Semiconductor Market 2025",
    page_icon="💻",
    layout="wide"
)

# Header con descrizione
st.title("🌐 Global Semiconductor Market 2025")
st.markdown("""
This interactive treemap visualizes the global semiconductor market revenue distribution across sectors and key players.
Hover over any rectangle to see detailed information. Click on sectors to zoom in.
""")

# Sidebar con informazioni e filtri
with st.sidebar:
    st.header("📊 About This Visualization")
    st.markdown("""
    **Data Source:**
    - WSTS Market Forecast 2025
    - Deloitte Semiconductor Outlook 2025
    - Company Financial Reports Q4 2025
    
    **Key Insights:**
    - NVIDIA dominates Logic & AI with $180B
    - TSMC leads foundry services at $114B
    - Memory sector: $160B total revenue
    - Total market: ~$700B
    """)
    
    st.divider()
    
    # Filtro interattivo per settori
    st.subheader(
