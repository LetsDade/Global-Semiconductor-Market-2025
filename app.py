import streamlit as st
import plotly.express as px
import pandas as pd

# Configurazione pagina
st.set_page_config(
    page_title="Semiconductor Market 2025",
    page_icon="💻",
    layout="wide"
)

# Header minimale
st.title("Global Semiconductor Market 2025")

# Sidebar compatta
with st.sidebar:
    st.subheader("Filters")
    
    sectors = ['All Sectors', 'Logic & AI Chips', 'Memory', 'Foundry', 'Equipment & IP']
    selected_sector = st.selectbox("Sector:", sectors)
    
    show_values = st.checkbox("Show values on chart", value=True)
    
    st.divider()
    st.caption("**Data Sources:** WSTS, Deloitte 2025, Company Reports Q4 2025")

# Dati
data = {
    'Sector': [
        'Logic & AI Chips', 'Logic & AI Chips', 'Logic & AI Chips', 'Logic & AI Chips', 'Logic & AI Chips',
        'Memory', 'Memory', 'Memory',
        'Foundry', 'Foundry',
        'Equipment & IP'
    ],
    'Company': [
        'NVIDIA', 'Broadcom', 'Intel', 'Qualcomm', 'AMD',
        'Samsung (Memory)', 'SK Hynix', 'Micron',
        'TSMC', 'Others (Foundry)',
        'ASML'
    ],
    'Revenue_B': [
        180.0, 56.0, 54.0, 38.0, 28.0,
        75.0, 50.0, 35.0,
        114.0, 33.0,
        36.0
    ]
}

df = pd.DataFrame(data)

# Applica filtro
if selected_sector != 'All Sectors':
    df_filtered = df[df['Sector'] == selected_sector].copy()
    chart_title = f"<b>{selected_sector}</b><br><span style='font-size:16px'>Revenue by Company</span>"
else:
    df_filtered = df.copy()
    chart_title = "<b>Global Semiconductor Market 2025</b><br><span style='font-size:16px'>Revenue by Sector and Company</span>"

# Color map
color_map = {
    'Logic & AI Chips': '#084594',
    'Memory': '#4292c6',
    'Foundry': '#9ebcda',
    'Equipment & IP': '#737373'
}

# Treemap
fig = px.treemap(
    df_filtered,
    path=['Sector', 'Company'] if selected_sector == 'All Sectors' else ['Company'],
    values='Revenue_B',
    color='Sector',
    color_discrete_map=color_map
)

# Layout
fig.update_layout(
    title={
        'text': chart_title,
        'font': {'size': 22, 'color': '#1a1a1a'},
        'x': 0.5,
        'xanchor': 'center',
        'y': 0.98
    },
    margin=dict(t=100, l=10, r=10, b=10),
    template="plotly_white",
    font=dict(family="Arial, sans-serif"),
    showlegend=True if selected_sector == 'All Sectors' else False,
    legend=dict(
        title=dict(text="<b>Sector</b>", font=dict(size=13)),
        orientation="v",
        yanchor="top",
        y=0.95,
        xanchor="right",
        x=0.99,
        bgcolor="rgba(255,255,255,0.95)",
        bordercolor="#cccccc",
        borderwidth=1,
        font=dict(size=12)
    ),
    height=750
)

# Etichette
text_template = "<b>%{label}</b><br>$%{value:.0f}B" if show_values else "<b>%{label}</b>"

fig.update_traces(
    textposition="middle center",
    texttemplate=text_template,
    textfont=dict(size=14, color='white'),
    hovertemplate='<b>%{label}</b><br>Sector: %{parent}<br>Revenue: $%{value:.1f}B<extra></extra>',
    marker=dict(
        line=dict(width=3, color='white'),
        pad=dict(t=3, l=3, r=3, b=3)
    )
)

# Display grafico
st.plotly_chart(fig, use_container_width=True)

# Footer minimale
st.divider()
st.caption("Financial Data Analytics 2025 - Interactive Portfolio Visualization")
