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
    # Filtro interattivo per settori
    st.subheader("🎯 Filter by Sector")
    sectors = ['All Sectors', 'Logic & AI Chips', 'Memory', 'Foundry', 'Equipment & IP']
    selected_sector = st.selectbox("Select a sector to highlight:", sectors)
    
    st.divider()
    
    # Opzione per mostrare/nascondere valori
    show_values = st.checkbox("Show revenue values on chart", value=True)
    color_scheme = st.radio(
        "Color Scheme:",
        ["Professional Blues",
        index=0


# Dati consolidati Semiconduttori (Revenue 2025 in Billions USD)
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

# Applica filtro se selezionato un settore specifico
if selected_sector != 'All Sectors':
    df_filtered = df[df['Sector'] == selected_sector].copy()
    chart_title = f"<b>{selected_sector}</b><br><span style='font-size:16px'>Revenue breakdown by Company</span>"
else:
    df_filtered = df.copy()
    chart_title = "<b>Global Semiconductor Market 2025</b><br><span style='font-size:16px'>Revenue breakdown by Sector and Key Players</span>"
    
if color_scheme == "Professional Blues":
    color_map = {
        'Logic & AI Chips': '#084594',
        'Memory': '#4292c6',
        'Foundry': '#9ebcda',
        'Equipment & IP': '#737373'
# Creazione della Treemap
fig = px.treemap(
    df_filtered,
    path=['Sector', 'Company'] if selected_sector == 'All Sectors' else ['Company'],
    values='Revenue_B',
    color='Sector',
)

# Layout responsive per Streamlit
fig.update_layout(
    title={
        'text': chart_title,
        'font': {'size': 22, 'color': '#1a1a1a'},
        'x': 0.5,
        'xanchor': 'center',
        'y': 0.98,
        'yanchor': 'top'
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
    height=700
)

# Etichette condizionali basate sulla scelta utente
if show_values:
    text_template = "<b>%{label}</b><br>$%{value:.0f}B"
else:
    text_template = "<b>%{label}</b>"

fig.update_traces(
    textposition="middle center",
    texttemplate=text_template,
    textfont=dict(size=14, color='white'),
    hovertemplate='<b>%{label}</b><br>Sector: %{parent}<br>Revenue: $%{value:.1f}B<br>Market Share: %{percentParent}<extra></extra>',
    marker=dict(
        line=dict(width=3, color='white'),
        pad=dict(t=3, l=3, r=3, b=3)
    )
)

# Mostra il grafico
st.plotly_chart(fig, use_container_width=True)


# Tabella dati interattiva
st.divider()
st.subheader("📋 Raw Data")

if selected_sector != 'All Sectors':
    display_df = df_filtered
else:
    display_df = df

# Aggiungi colonna percentuale
display_df_copy = display_df.copy()
display_df_copy['Market Share %'] = (display_df_copy['Revenue_B'] / df['Revenue_B'].sum() * 100).round(2)
display_df_copy['Revenue ($B)'] = display_df_copy['Revenue_B']
display_df_copy = display_df_copy[['Sector', 'Company', 'Revenue ($B)', 'Market Share %']]
display_df_copy = display_df_copy.sort_values('Revenue ($B)', ascending=False)

st.dataframe(
    display_df_copy,
    hide_index=True,
    use_container_width=True,
    column_config={
        "Revenue ($B)": st.column_config.NumberColumn(
            "Revenue ($B)",
            format="$%.1f B"
        ),
        "Market Share %": st.column_config.ProgressColumn(
            "Market Share %",
            format="%.2f%%",
            min_value=0,
            max_value=100,
        )
    }
)

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: #666; font-size: 12px;'>
    <p><b>Financial Data Analytics 2025 - Student Portfolio Project</b></p>
    <p>Data Sources: WSTS, Deloitte, Company Financial Reports | Last Updated: January 2026</p>
</div>
""", unsafe_allow_html=True)
