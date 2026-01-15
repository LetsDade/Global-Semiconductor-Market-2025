import plotly.express as px
import pandas as pd

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
        180.0, 56.0, 54.0, 38.0, 28.0,  # Logic (AMD 28 + Qualcomm 38 = 66 in Others)
        75.0, 50.0, 35.0,             # Memory
        114.0, 33.0,                  # Foundry (Samsung 25 + GlobalFoundries 8 = 33 in Others)
        36.0                          # Equipment
    ]
}

df = pd.DataFrame(data)

# Creazione della Treemap con gerarchia ottimizzata
fig = px.treemap(
    df,
    path=['Sector', 'Company'],
    values='Revenue_B',
    color='Sector',
    color_discrete_map={
        'Logic & AI Chips': '#084594',
        'Memory': '#4292c6',
        'Foundry': '#9ebcda',
        'Equipment & IP': '#737373'
    }
)

# Layout pulito e professionale
fig.update_layout(
    title={
        'text': "<b>Global Semiconductor Market 2025</b><br><span style='font-size:19px'>Revenue breakdown by Sector and Key Players</span>",
        'font': {'size': 19, 'color': '#1a1a1a'},
        'x': 0.5,
        'xanchor': 'center'
    },
    margin=dict(t=70, l=5, r=5, b=5),
    template="plotly_white",
    font=dict(family="Arial, sans-serif"),
    showlegend=True,
    legend=dict(
        title="Sector",
        orientation="v",
        y=0.98,  # Top-right corner
        x=0.99,
        bgcolor="rgba(255,255,255,0.9)",  # Semi-trasparente
        bordercolor="#cccccc",
        borderwidth=1
    )
)

# Etichette chiare con formattazione ottimale
fig.update_traces(
    textposition="middle center",
    texttemplate="<b>%{label}</b><br>$%{value:.0f}B",
    textfont=dict(size=13, color='white'),
    hovertemplate='<b>%{label}</b><br>Sector: %{parent}<br>Revenue: $%{value:.1f}B<extra></extra>',
    marker=dict(
        line=dict(width=3, color='white'),  # Bordi bianchi più spessi per separazione
        pad=dict(t=2, l=2, r=2, b=2)
    )
)

fig.show()
