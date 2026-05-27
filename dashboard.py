import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Page Configuration
st.set_page_config(page_title="SDG3: Mental Health & Development", layout="wide")

# Custom CSS
st.markdown("""
    <style>
        .stApp {
            background-color: #080c0d;
            color: #FAF3F0;
        }
        
        [data-testid="stSidebar"] {
            background-color: #080c0d;
            border-right: 1px solid #2E6073;
        }
        
        [data-testid="stSidebar"] .stMarkdown, 
        [data-testid="stSidebar"] .stSelectbox label,
        [data-testid="stSidebar"] .stMultiSelect label {
            color: #FAF3F0;
        }
        
        h1, h2, h3 {
            color: #DCA993;
            font-family: 'Georgia', serif;
        }
        
        h1 {
            border-bottom: 2px solid #2E6073;
            padding-bottom: 10px;
        }
        
        .stMetricValue {
            color: #DCA993 !important;
        }
        
        .stMetricLabel {
            color: #C2BBB4 !important;
        }
        
        .custom-card {
            background-color: #1a1a1a;
            padding: 20px;
            border-radius: 8px;
            border-left: 4px solid #DCA993;
            color: #FAF3F0;
        }
        
        .stDataFrame {
            background-color: #080c0d;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
        }
        
        .stTabs [data-baseweb="tab"] {
            background-color: #1a1a1a;
            border-radius: 8px;
            color: #FAF3F0;
            padding: 8px 24px;
            border: 1px solid #2E6073;
            transition: all 0.2s ease;
        }
        
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #2E6073;
            cursor: pointer;
        }
        
        .stTabs [aria-selected="true"] {
            background-color: #2E6073;
            color: #FAF3F0;
            border: none;
        }
        
        /* Remove the red underline under selected tab */
        .stTabs [data-baseweb="tab-highlight"] {
            background-color: #DCA993 !important;
        }
        
        hr {
            border-color: #2E6073;
        }
        
        .streamlit-expanderHeader {
            background-color: #1a1a1a;
            color: #DCA993;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .streamlit-expanderHeader:hover {
            background-color: #2E6073;
            color: #FAF3F0;
        }
        
        .stAlert {
            background-color: #1a1a1a;
            border-radius: 8px;
        }
        
        .stDownloadButton button {
            background-color: #2E6073;
            color: #FAF3F0;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .stDownloadButton button:hover {
            background-color: #DCA993;
            color: #080c0d;
            cursor: pointer;
        }
        
        /* Plotly text color override */
        .js-plotly-plot .main-svg text {
            fill: #FAF3F0 !important;
        }
        
        /* Metric cards */
        [data-testid="stMetric"] {
            background-color: #1a1a1a !important;
            padding: 16px;
            border-radius: 8px;
            transition: all 0.2s ease;
            border-left: 3px solid #DCA993;
        }
        
        [data-testid="stMetric"]:hover {
            transform: translateY(-3px);
            background-color: #252525 !important;
            cursor: pointer;
            border-left-color: #C1E6E5;
        }
        
        /* Custom metric card */
        .metric-card {
            background-color: #1a1a1a !important;
            padding: 16px;
            border-radius: 8px;
            transition: all 0.2s ease;
        }
        
        .metric-card:hover {
            transform: translateY(-3px);
            background-color: #252525 !important;
            cursor: pointer;
        }
        
        /* Slider fixes - remove red */
        div[data-baseweb="slider"] {
            color: #DCA993 !important;
        }
        
        div[data-baseweb="slider"] div[role="slider"] {
            background-color: #DCA993 !important;
            border-color: #DCA993 !important;
        }
        
        div[data-baseweb="slider"] div[data-testid="stThumbValue"] {
            background-color: #DCA993 !important;
        }
        
        div[data-baseweb="slider"] div[data-testid="stTickBar"] div:first-child {
            background-color: #DCA993 !important;
        }
        
        div[data-baseweb="slider"] div[data-testid="stTickBar"] {
            background-color: #2E6073 !important;
        }
        
        /* Range slider specific */
        div[data-baseweb="slider"] div[data-testid="stTickBar"] div {
            background-color: #2E6073 !important;
        }
        
        /* Number input for year range - remove red border */
        .stNumberInput input {
            border-color: #2E6073 !important;
        }
        
        .stNumberInput input:focus {
            border-color: #DCA993 !important;
            box-shadow: 0 0 0 1px #DCA993 !important;
        }
        
        /* Selectbox */
        div[data-baseweb="select"] {
            border-color: #2E6073 !important;
        }
        
        div[data-baseweb="select"]:hover {
            border-color: #DCA993 !important;
        }
        
        span[data-baseweb="tag"] {
            background-color: #2E6073 !important;
            color: #FAF3F0 !important;
        }
        
        div[role="listbox"] li:hover {
            background-color: #2E6073 !important;
        }
        
        div[data-baseweb="input"]:focus-within {
            border-color: #DCA993 !important;
            box-shadow: 0 0 0 1px #DCA993 !important;
        }
        
        /* Expander spacing */
        .streamlit-expanderHeader {
            margin-top: 12px;
        }
        
        .stColumn {
            padding: 0 8px;
        }
            
        /* The active connecting line between the years */
        div[data-testid="stSlider"] div[data-baseweb="slider"] > div > div > div {
            background-color: #DCA993 !important;
        }
        
        /* The drag handles (thumbs) */
        div[data-testid="stSlider"] div[data-baseweb="slider"] [role="slider"] {
            background-color: #080c0d !important;
            border: 3px solid #DCA993 !important;
            box-shadow: none !important;
        }
        
        /* Hover/Click effect on the handles */
        div[data-testid="stSlider"] div[data-baseweb="slider"] [role="slider"]:hover,
        div[data-testid="stSlider"] div[data-baseweb="slider"] [role="slider"]:focus {
            box-shadow: 0 0 0 0.3rem rgba(220, 169, 147, 0.2) !important;
        }
        
        /* The numbers above the slider handles */
        div[data-testid="stSlider"] div[data-baseweb="slider"] div[role="slider"] > div > div {
            color: #FAF3F0 !important;
            font-family: 'Segoe UI', sans-serif !important;
        }
            
        /* Kills the default red outline when selecting a country */
        div[data-baseweb="select"] > div:focus-within {
            border-color: #DCA993 !important;
            box-shadow: 0 0 0 1px #DCA993 !important;
        }
    
        /* Make tabs container full width and reduce gap to fit the frame */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px; /* Brought the tabs closer together */
            justify-content: center;
            width: 100%;
            margin-bottom: 30px;
        }
        
        /* Adjust padding and font size so all 5 tabs fit in one row */
        .stTabs [data-baseweb="tab"] {
            background-color: #1a1a1a !important;
            border-radius: 8px !important; 
            color: #C2BBB4 !important; /* Dimmed inactive text */
            padding: 12px 10px !important; /* REDUCED horizontal padding */
            border: 2px solid #2E6073 !important;
            transition: all 0.2s ease;
            font-size: 0.95rem !important; /* Scaled down the font slightly */
            font-weight: 900 !important;
            flex: 1; /* Forces tabs to share the available width equally */
            text-align: center;
            letter-spacing: 0.5px;
            text-transform: uppercase;
            white-space: nowrap; /* Prevents text from breaking into two lines */
        }
        
        /* Active tab styling - Fixed Text Contrast */
        .stTabs [aria-selected="true"] {
            background-color: #2E6073 !important;
            color: #FAF3F0 !important; /* Bright white/beige text so it is readable */
            border: 2px solid #DCA993 !important;
            box-shadow: 0 4px 12px rgba(220, 169, 147, 0.4) !important;
        }
        
        /* Tab hover effect */
        .stTabs [data-baseweb="tab"]:hover {
            background-color: #2E6073 !important;
            color: #FAF3F0 !important;
            cursor: pointer;
            border-color: #DCA993 !important;
            transform: translateY(-2px);
        }

        /* Kill Streamlit's native sliding red highlight line */
        .stTabs [data-baseweb="tab-highlight"] {
            display: none !important;
        }
        
        /* Kill the default gray divider line */
        .stTabs [data-baseweb="tab-border"] {
            display: none !important;
        }
     
    </style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    df = pd.read_excel("SDG3_Mental_Health_Dataset.xlsx")
    return df

df = load_data()
df['Year'] = df['Year'].astype(int)

# Sidebar Filters
st.sidebar.title("⚙️ Filters")
st.sidebar.markdown("---")

years = sorted(df['Year'].unique())
year_range = st.sidebar.slider(
    "Select Year Range",
    min_value=int(years[0]),
    max_value=int(years[-1]),
    value=(int(years[0]), int(years[-1]))
)

countries = df['Country'].unique()
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(countries),
    default=["World", "United States", "China", "India"] if "World" in countries else sorted(countries)[:5]
)

filtered_df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
if selected_countries:
    filtered_df = filtered_df[filtered_df['Country'].isin(selected_countries)]

# Main Title
st.markdown("""
    <div style='border: 1px solid #2E6073; border-top: 3px solid #9D825D; border-bottom: 3px solid #9D825D; border-radius: 4px; text-align: center; padding: 35px 20px 30px 20px; margin-bottom: 20px; position: relative;'>
        <div style='position: absolute; top: -12px; left: 20px; background-color: #080c0d; padding: 0 10px;'>
            <span style='color: #9D825D; font-size: 0.8rem;'>✦ ✦ ✦</span>
        </div>
        <div style='position: absolute; bottom: -12px; right: 20px; background-color: #080c0d; padding: 0 10px;'>
            <span style='color: #9D825D; font-size: 0.8rem;'>✦ ✦ ✦</span>
        </div>
        <h1 style='margin-bottom: 12px; letter-spacing: -1px;'>
            <span style='color: #2E6073;'>SDG3:</span>
            <span style='color: #F5f5dc;'> Mental Health & Global Development Drivers</span>
        </h1>
        <p style='color: #C1E6E5; font-size: 1.1rem; margin-bottom: 0; font-style: italic;'>
            Exploring relationships between development indicators and mental health outcomes
        </p>
    </div>
""", unsafe_allow_html=True)

# Dataset Overview
st.markdown("## <span style='color: #FAF3F0; margin-bottom: 15px; display: inline-block;'>Dataset Overview</span>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Row 1: Structural Metadata Metrics (3 Columns)
# ---------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    unique_countries = df['Country'].nunique() if 'Country' in df.columns else df['Country_Name'].nunique()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #DCA993;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Countries/Regions</p>
            <p style='color: #DCA993; margin: 0; font-size: 2rem; font-weight: 500;'>{unique_countries}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #2E6073;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Years Covered</p>
            <p style='color: #2E6073; margin: 0; font-size: 2rem; font-weight: 500;'>{int(df['Year'].min())} — {int(df['Year'].max())}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #98A6B5;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Total Records</p>
            <p style='color: #98A6B5; margin: 0; font-size: 2rem; font-weight: 500;'>{df.shape[0]:,}</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Row 2: Target Variable & Core Labor Metrics (3 Columns)
# ---------------------------------------------------------
col4, col5, col6 = st.columns(3)

with col4:
    avg_suicide = df['Suicide Rate'].mean()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #C1E6E5;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Avg Suicide Rate</p>
            <p style='color: #C1E6E5; margin: 0; font-size: 2rem; font-weight: 500;'>{avg_suicide:.1f} <span style='font-size: 1rem;'>/100k</span></p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col5:
    avg_unemp = df['Unemployment Rate'].mean()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #D4DFCD;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Avg Unemployment</p>
            <p style='color: #D4DFCD; margin: 0; font-size: 2rem; font-weight: 500;'>{avg_unemp:.1f}%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col6:
    avg_oop = df['Out-of-Pocket Health Expenditure'].mean()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #7B6B86;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Avg Out-of-Pocket Exp</p>
            <p style='color: #7B6B86; margin: 0; font-size: 2rem; font-weight: 500;'>{avg_oop:.1f}%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------------------------------------------
# Row 3: Infrastructure & Demographic Metrics (2 Columns)
# ---------------------------------------------------------
col7, col8 = st.columns(2)

with col7:
    avg_internet = df['Internet Usage'].mean()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #7B8C7A;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Avg Internet Usage</p>
            <p style='color: #7B8C7A; margin: 0; font-size: 2rem; font-weight: 500;'>{avg_internet:.1f}%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

with col8:
    avg_urban = df['Urban Population Percentage'].mean()
    st.markdown(
        f"""
        <div class='metric-card' style='background-color: #1a1a1a; padding: 16px; border-radius: 8px; border-left: 4px solid #A3B598;'>
            <p style='color: #C2BBB4; margin: 0 0 8px 0; font-size: 0.85rem;'>Avg Urban Population</p>
            <p style='color: #A3B598; margin: 0; font-size: 2rem; font-weight: 500;'>{avg_urban:.1f}%</p>
        </div>
        """, 
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

with st.expander("View Raw Data Sample"):
    st.dataframe(df.head(100), use_container_width=True)

st.markdown("---")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Time Series", 
    "Country Comparison", 
    "Correlation",
    "Predictions",
    "Data Explorer"
])

# ==================== TAB 1 ====================
with tab1:
    st.header("Time Series Analysis")
    
    metric = st.selectbox(
        "Select Indicator",
        options=['Suicide Rate', 'Internet Usage', 'Unemployment Rate', 'Out-of-Pocket Health Expenditure', 'Urban Population Percentage'],
        format_func=lambda x: x.replace('_', ' ').title()
    )
    
    if selected_countries and len(selected_countries) <= 10:
        fig = px.line(
            filtered_df[filtered_df['Country'].isin(selected_countries)],
            x='Year',
            y=metric,
            color='Country',
            title=f'{metric.replace("_", " ").title()} Trends',
            template='plotly_dark',
            color_discrete_sequence=['#DCA993', '#2E6073', '#C1E6E5', '#D4DFCD', '#C2BBB4']
        )
    else:
        world_data = filtered_df[filtered_df['Country'] == 'World']
        fig = px.line(
            world_data,
            x='Year',
            y=metric,
            title=f'Global {metric.replace("_", " ").title()} Trends',
            template='plotly_dark',
            color_discrete_sequence=['#DCA993']
        )
        if world_data.empty:
            yearly_avg = filtered_df.groupby('Year')[metric].mean().reset_index()
            fig = px.line(
                yearly_avg,
                x='Year',
                y=metric,
                title=f'Average {metric.replace("_", " ").title()} (All Countries)',
                template='plotly_dark',
                color_discrete_sequence=['#DCA993']
            )
    
    fig.update_layout(height=500, font_color='#FAF3F0', title_font_color='#DCA993')
    st.plotly_chart(fig, use_container_width=True)

# ==================== TAB 2 ====================
with tab2:
    st.header("Country Comparison")
    
    col1, col2 = st.columns(2)
    with col1:
        metric_compare = st.selectbox(
            "Select Metric",
            options=['Suicide Rate', 'Internet Usage', 'Unemployment Rate', 'Out-of-Pocket Health Expenditure', 'Urban Population Percentage'],
            index=0,
            key="compare_metric"
        )
    with col2:
        year_compare = st.selectbox("Select Year", sorted(df['Year'].unique()), index=len(sorted(df['Year'].unique()))-1)
    
    year_data = df[df['Year'] == year_compare].copy()
    year_data = year_data[~year_data['Country'].isin(['World', 'Not classified'])]
    year_data = year_data.dropna(subset=[metric_compare])
    
    top_countries = year_data.nlargest(20, metric_compare)[['Country', metric_compare]]
    fig = px.bar(
        top_countries,
        x=metric_compare,
        y='Country',
        orientation='h',
        title=f'Highest 20 — {metric_compare.replace("_", " ").title()} ({year_compare})',
        template='plotly_dark',
        color=metric_compare,
        color_continuous_scale=['#C1E6E5', '#2E6073', '#DCA993']
    )
    fig.update_layout(height=500, font_color='#FAF3F0', title_font_color='#DCA993')
    st.plotly_chart(fig, use_container_width=True)
    
    if metric_compare != 'Suicide Rate':
        st.subheader("Suicide Rate Rankings")
        suicide_data = year_data.nlargest(20, 'Suicide Rate')[['Country', 'Suicide Rate']]
        fig2 = px.bar(
            suicide_data,
            x='Suicide Rate',
            y='Country',
            orientation='h',
            title=f'Highest Suicide Rates ({year_compare})',
            template='plotly_dark',
            color='Suicide Rate',
            color_continuous_scale=['#C1E6E5', '#2E6073', '#DCA993']
        )
        fig2.update_layout(height=500, font_color='#FAF3F0', title_font_color='#DCA993')
        st.plotly_chart(fig2, use_container_width=True)

# ==================== TAB 3 ====================
with tab3:
    st.header("Correlation Analysis")
    
    corr_vars = ['Suicide Rate', 'Unemployment Rate', 'Internet Usage', 'Out-of-Pocket Health Expenditure', 'Urban Population Percentage']
    corr_data = df[corr_vars].dropna()
    
    if len(corr_data) > 0:
        corr_matrix = corr_data.corr()
        
        # Custom colormap using Blumine, Ivory Tower, and Fortune's Prize (exactly as in your notebook)
        from matplotlib.colors import LinearSegmentedColormap
        cmap_sands = LinearSegmentedColormap.from_list('sands', ['#2E6073', '#FAF3F0', '#DCA993'])
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        # Render heatmap exactly as in your notebook
        sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap=cmap_sands, 
                    linewidths=1, linecolor="#080c0d", cbar_kws={"shrink": 0.8}, ax=ax)
        
        ax.set_title("CORRELATION MATRIX: MENTAL HEALTH vs SOCIOECONOMICS", 
                     color="#FAF3F0", pad=20, fontsize=12)
        ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right', color='#FAF3F0')
        ax.set_yticklabels(ax.get_yticklabels(), color='#FAF3F0')
        
        # Colorbar styling
        cbar = ax.collections[0].colorbar
        cbar.ax.yaxis.set_tick_params(color='#FAF3F0')
        plt.setp(plt.getp(cbar.ax.axes, 'yticklabels'), color='#FAF3F0')
        
        # Set background
        fig.patch.set_facecolor('#080c0d')
        ax.set_facecolor('#080c0d')
        
        plt.tight_layout()
        st.pyplot(fig)
        
        st.subheader("Relationship Explorer")
        
        col1, col2 = st.columns(2)
        with col1:
            x_var = st.selectbox("X-axis Variable", corr_vars[1:], key="x_var")
        with col2:
            y_var = st.selectbox("Y-axis Variable", corr_vars, index=0, key="y_var")
        
        scatter_data = df[[x_var, y_var, 'Country', 'Year']].dropna()
        
        fig2 = px.scatter(
            scatter_data,
            x=x_var,
            y=y_var,
            color='Country',
            size='Year',
            hover_data=['Country', 'Year'],
            title=f'{y_var.replace("_", " ").title()} vs {x_var.replace("_", " ").title()}',
            template='plotly_dark',
            color_discrete_sequence=['#2E6073', '#DCA993', '#C1E6E5', '#D4DFCD', '#C2BBB4']
        )
        fig2.update_layout(
            height=500, 
            font_color='#FAF3F0', 
            title_font_color='#DCA993',
            plot_bgcolor='#080c0d',
            paper_bgcolor='#080c0d',
            xaxis=dict(showgrid=True, gridcolor='#2E6073', gridwidth=0.5),
            yaxis=dict(showgrid=True, gridcolor='#2E6073', gridwidth=0.5)
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        corr_value = corr_matrix.loc[y_var, x_var] if y_var in corr_matrix.index and x_var in corr_matrix.columns else 0
        st.info(f"**Correlation:** {corr_value:.3f} — {'Strong' if abs(corr_value) > 0.5 else 'Moderate' if abs(corr_value) > 0.3 else 'Weak'} relationship")

# ==================== TAB 4 ====================
with tab4:
    st.header("Predictive Analysis: Future Suicide Rates")
    
    selected_country_pred = st.selectbox(
        "Select a country to predict future suicide rates (2022-2030)",
        options=['World', 'United States', 'China', 'India', 'United Kingdom', 'Japan', 'Germany', 'Brazil', 'Russia']
    )
    
    country_data = df[df['Country'] == selected_country_pred].dropna(subset=['Suicide Rate', 'Year'])
    
    if len(country_data) >= 5:
        years_clean = country_data['Year'].values
        rates_clean = country_data['Suicide Rate'].values
        
        slope, intercept, r_value, p_value, std_err = stats.linregress(years_clean, rates_clean)
        
        # Forecast array covering 2022 through 2030 sequentially
        future_years = np.array([2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030])
        predictions = slope * future_years + intercept
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=country_data['Year'], y=country_data['Suicide Rate'],
                                 mode='lines+markers', name='Historical Data',
                                 line=dict(color='#DCA993', width=2),
                                 marker=dict(color='#2E6073', size=8)))
        fig.add_trace(go.Scatter(x=future_years, y=predictions,
                                 mode='lines+markers', name='Predicted Trend',
                                 line=dict(color='#2E6073', width=2, dash='dash'),
                                 marker=dict(color='#C1E6E5', size=8)))
        
        # Chart title
        fig.update_layout(title=f'{selected_country_pred} - Suicide Rate Trend & Forecast (2022-2030)',
                          xaxis_title='Year', yaxis_title='Suicide Rate (per 100,000)',
                          template='plotly_dark', height=500,
                          font_color='#FAF3F0', title_font_color='#DCA993')
        st.plotly_chart(fig, use_container_width=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            # Dynamically shows the final year available in your training data (2021)
            last_historical_year = int(country_data['Year'].max())
            current_rate = country_data[country_data['Year'] == last_historical_year]['Suicide Rate'].values
            if len(current_rate) > 0:
                st.metric(f"Current Rate ({last_historical_year})", f"{current_rate[0]:.1f}")
        with col2:
            st.metric("Predicted Rate (2030)", f"{predictions[-1]:.1f}")
        with col3:
            change = predictions[-1] - (current_rate[0] if len(current_rate) > 0 else 0)
            direction = "↑ Increase" if change > 0 else "↓ Decrease"
            st.metric("Change by 2030", f"{change:.1f}", delta=f"{direction}")
        
        st.caption(f"Model confidence (R²): {r_value**2:.3f} | P-value: {p_value:.4f}")
        
        if change > 0:
            st.warning(f"⚠︎ Warning: {selected_country_pred} is projected to see a {abs(change):.1f} point INCREASE in suicide rate by 2030.")
        else:
            st.success(f"✓ Good news: {selected_country_pred} is projected to see a {abs(change):.1f} point DECREASE in suicide rate by 2030.")
    else:
        st.warning(f"Not enough historical data for {selected_country_pred}. Need at least 5 years of data.")
    
    # ---------------------------------------------------------
    # Dynamic Bivariate Factor Analysis
    # ---------------------------------------------------------
    st.subheader("Bivariate Predictor Analysis vs Suicide Rate")
    st.markdown("Select a macro-environmental metric below to dynamically evaluate its cross-national linear alignment with global suicide mortality trends.")

    # Dropdown option box to choose the factor
    factor_options = {
        'Internet Usage': 'Internet Usage (%)',
        'Unemployment Rate': 'Unemployment Rate (% of Labor Force)',
        'Out-of-Pocket Health Expenditure': 'Out-of-Pocket Health Expenditure (% of Total Health Spend)',
        'Urban Population Percentage': 'Urban Population Percentage (% of Total)'
    }
    
    selected_factor_label = st.selectbox(
        "Select Independent Variable (X-Axis Variable):",
        options=list(factor_options.keys())
    )
    
    # Get the exact display label for axis mapping
    selected_axis_label = factor_options[selected_factor_label]

    # Use filtered_df so it respects sidebar country and year selections
    bivariate_data = filtered_df.dropna(subset=[selected_factor_label, 'Suicide Rate'])
    bivariate_data = bivariate_data[~bivariate_data['Country'].isin(['World', 'Not classified'])]

    # Pull dynamic min and max years based on the sidebar slider bounds
    current_min = int(bivariate_data['Year'].min()) if len(bivariate_data) > 0 else 2010
    current_max = int(bivariate_data['Year'].max()) if len(bivariate_data) > 0 else 2021

    # Generate the dynamic Plotly bubble chart
    fig2 = px.scatter(
        bivariate_data, 
        x=selected_factor_label, 
        y='Suicide Rate', 
        color='Country', 
        size='Year', 
        hover_name='Country',
        title=f'{selected_factor_label} vs Suicide Rate ({current_min}-{current_max})',
        template='plotly_dark',
        labels={selected_factor_label: selected_axis_label, 'Suicide Rate': 'Suicide Rate (per 100k)'}
    )
    fig2.update_layout(height=450, font_color='#FAF3F0', title_font_color='#DCA993', showlegend=False)
    st.plotly_chart(fig2, use_container_width=True)
    
    # Run the Pearson correlation coefficient live on the selected variable
    corr = bivariate_data[selected_factor_label].corr(bivariate_data['Suicide Rate'])
    
    if not np.isnan(corr):
        if corr > 0.3:
            st.warning(f"⚠︎ Positive Correlation: {corr:.2f} — Countries with higher {selected_factor_label.lower()} exhibit a strong baseline risk trajectory with higher suicide rates.")
        elif corr < -0.3:
            st.success(f"✓ Negative Correlation: {corr:.2f} — Countries with higher {selected_factor_label.lower()} exhibit an inverse baseline trajectory with lower suicide rates.")
        else:
            st.info(f"⟡ Weak/Isolated Alignment: {corr:.2f} — There is no strong standalone linear baseline relationship between {selected_factor_label.lower()} and suicide rates.")
    
    st.caption(f"Based on {len(bivariate_data):,} dynamic data points.")

    # ---------------------------------------------------------
    # Systemic Diagnostic Framework (OLS Global Model Results)
    # ---------------------------------------------------------
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.subheader("Global Multiple Linear Regression (OLS) Framework")
    st.markdown(
        """
        While simple correlation charts isolate one factor at a time, our system's 
        <b>Multiple Linear Regression (OLS) Engine</b> evaluates how these macro-environmental 
        factors collectively drive global suicide mortality rates simultaneously ($N = 2,464$).
        """, 
        unsafe_allow_html=True
    )

    # Summary Statistics Row
    m_col1, m_col2, m_col3 = st.columns(3)
    with m_col1:
        st.markdown(
            """
            <div class='metric-card' style='background-color: #1a1a1a; padding: 12px; border-radius: 6px; border-left: 3px solid #2E6073;'>
                <p style='color: #C2BBB4; margin: 0; font-size: 0.8rem;'>Model Fit (R-squared)</p>
                <p style='color: #2E6073; margin: 0; font-size: 1.5rem; font-weight: bold;'>0.113</p>
            </div>
            """, unsafe_allow_html=True
        )
    with m_col2:
        st.markdown(
            """
            <div class='metric-card' style='background-color: #1a1a1a; padding: 12px; border-radius: 6px; border-left: 3px solid #C1E6E5;'>
                <p style='color: #C2BBB4; margin: 0; font-size: 0.8rem;'>F-Statistic (Significance)</p>
                <p style='color: #C1E6E5; margin: 0; font-size: 1.5rem; font-weight: bold;'>78.07 <span style='font-size:0.8rem;'>(p < 0.001)</span></p>
            </div>
            """, unsafe_allow_html=True
        )
    with m_col3:
        st.markdown(
            """
            <div class='metric-card' style='background-color: #1a1a1a; padding: 12px; border-radius: 6px; border-left: 3px solid #DCA993;'>
                <p style='color: #C2BBB4; margin: 0; font-size: 0.8rem;'>Model Sample Size</p>
                <p style='color: #DCA993; margin: 0; font-size: 1.5rem; font-weight: bold;'>2,464 Obs</p>
            </div>
            """, unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Custom Table for Model Coefficients
    coefficients_table = """
    <div style="overflow-x: auto;">
        <table style="width:100%; border-collapse: collapse; background-color: #141414; color: #FAF3F0; font-family: sans-serif; font-size: 0.9rem;">
            <thead>
                <tr style="border-bottom: 2px solid #2E6073; text-align: left;">
                    <th style="padding: 10px; color: #DCA993;">Predictor Variable (X)</th>
                    <th style="padding: 10px;">Coefficient (β)</th>
                    <th style="padding: 10px;">t-Value</th>
                    <th style="padding: 10px;">p-Value</th>
                    <th style="padding: 10px; color: #C2BBB4;">Empirical Impact Direction</th>
                </tr>
            </thead>
            <tbody>
                <tr style="border-bottom: 1px solid #222;">
                    <td style="padding: 10px; font-weight: bold;">Unemployment Rate</td>
                    <td style="padding: 10px; color: #E5A1A1;">+0.0746</td>
                    <td style="padding: 10px;">5.14</td>
                    <td style="padding: 10px; font-weight: bold; color: #C1E6E5;">0.000</td>
                    <td style="padding: 10px; color: #E5A1A1;">⬤ Significant Positive Risk Factor</td>
                </tr>
                <tr style="border-bottom: 1px solid #222;">
                    <td style="padding: 10px; font-weight: bold;">Internet Usage</td>
                    <td style="padding: 10px; color: #E5A1A1;">+0.0634</td>
                    <td style="padding: 10px;">6.42</td>
                    <td style="padding: 10px; font-weight: bold; color: #C1E6E5;">0.000</td>
                    <td style="padding: 10px; color: #E5A1A1;">⬤ Significant Positive Risk Factor</td>
                </tr>
                <tr style="border-bottom: 1px solid #222;">
                    <td style="padding: 10px; font-weight: bold;">Out-of-Pocket Expenditure</td>
                    <td style="padding: 10px; color: #A1E5AB;">-0.0774</td>
                    <td style="padding: 10px;">-7.23</td>
                    <td style="padding: 10px; font-weight: bold; color: #C1E6E5;">0.000</td>
                    <td style="padding: 10px; color: #A1E5AB;">✓ Significant Protective / Inverse Baseline</td>
                </tr>
                <tr style="border-bottom: 2px solid #2E6073;">
                    <td style="padding: 10px; font-weight: bold;">Urban Population %</td>
                    <td style="padding: 10px; color: #A1E5AB;">-0.0606</td>
                    <td style="padding: 10px;">-7.05</td>
                    <td style="padding: 10px; font-weight: bold; color: #C1E6E5;">0.000</td>
                    <td style="padding: 10px; color: #A1E5AB;">✓ Significant Protective / Inverse Baseline</td>
                </tr>
            </tbody>
        </table>
    </div>
    """
    st.markdown(coefficients_table, unsafe_allow_html=True)
    
    # Quick Interpretative Insight for Presentation Guidance
    st.markdown("<br>", unsafe_allow_html=True)
    st.info(
        "𓂃🖊 **Insights:** All four predictors are highly statistically significant ($p = 0.000$). "
        "The model demonstrates that while rising economic distress (unemployment) and digital connectivity "
        "track alongside higher baseline risk metrics, localized infrastructure indicators like structural health spend insulation "
        "and urbanization exhibit prominent inverse stabilization patterns globally."
    )

# ==================== TAB 5 ====================
with tab5:
    st.header("Raw Data Explorer")
    
    cols_to_show = st.multiselect(
        "Select columns to display",
        options=df.columns.tolist(),
        default=['Country', 'Year', 'Suicide Rate', 'Internet Usage', 'Unemployment Rate']
    )
    
    if cols_to_show:
        country_filter = st.selectbox("Filter by Country", options=['All'] + sorted(df['Country'].unique()))
        
        if country_filter != 'All':
            display_df = filtered_df[filtered_df['Country'] == country_filter][cols_to_show]
        else:
            display_df = filtered_df[cols_to_show]
        
        st.dataframe(display_df, use_container_width=True)
        
        csv = display_df.to_csv(index=False)
        st.download_button(
            label="Download Data as CSV",
            data=csv,
            file_name="sdg3_filtered_data.csv",
            mime="text/csv"
        )
        
        with st.expander("Summary Statistics"):
            st.dataframe(display_df.describe(), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("""
<hr style="border: 0; border-top: 1px solid #2E6073; margin-top: 50px; margin-bottom: 30px; opacity: 0.3;">
<div style='text-align: center; background-color: #080c0d; border: 1px solid #2E6073; padding: 20px; border-radius: 8px; max-width: 700px; margin: 0 auto 30px auto;'>
    <p style='color: #FAF3F0; font-size: 0.95rem; margin: 0 0 8px 0; font-weight: 600; letter-spacing: 0.5px;'>
         DATA SOURCE 
    </p>
    <p style='color: #C2BBB4; font-size: 0.85rem; margin: 0 0 16px 0; line-height: 1.5;'>
        Suicide Mortality Rate Dataset sourced from the World Bank.<br>
        <span style='font-style: italic; color: #7a6a58;'>Indicator: SH.STA.SUIC.P5 | Original data: WHO Global Health Observatory (CC BY-4.0)</span>
    </p>
    <div style='border-top: 1px dashed #2E6073; margin: 12px 0;'></div>
    <p style='color: #DCA993; font-size: 0.8rem; margin: 8px 0 0 0; font-family: monospace; letter-spacing: 0.5px;'>
        ENGINES: Python • Streamlit • Pandas • NumPy • SciPy • Matplotlib • Seaborn • Plotly
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    """
    <div style='text-align: center; background-color: #080c0d; border: 1px solid #2E6073; padding: 15px; border-radius: 8px; max-width: 700px; margin: 10px auto 40px auto;'>
        <p style='color: #FAF3F0; font-size: 0.8rem; letter-spacing: 2px; text-transform: uppercase; margin: 0;'>
            DEVELOPED BY: <span style='color: #DCA993; font-weight: 700; border-bottom: 1px solid #2E6073; padding-bottom: 2px;'>ATASHA MARIE M. BALICTAR</span>
        </p>
        <p style='color: #7a6a58; font-size: 0.75rem; font-family: monospace; margin: 6px 0 0 0;'>
            ANALYTICS TECHNIQUES AND TOOLS • 2026
        </p>
    </div>
    """, 
    unsafe_allow_html=True
)