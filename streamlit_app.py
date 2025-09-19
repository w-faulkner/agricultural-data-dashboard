import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Set page config
st.set_page_config(page_title="Will Faulkner's Agricultural Data Analysis", layout="wide")

# Title
st.title("Agricultural Data Analysis Dashboard")

# Add your image with some styling
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("Faulkner,Will.jpg", caption="Will Faulkner", width=300)

# Load the Cropland Value data
@st.cache_data
def load_cropland_data():
    df = pd.read_csv("Cropland Value.csv")
    
    # Clean the Value column - remove commas and convert to numeric
    df['Value_Clean'] = df['Value'].str.replace(',', '').astype(float)
    
    # Convert Year to numeric
    df['Year'] = pd.to_numeric(df['Year'])
    
    return df

# Load the Crop Prices data
@st.cache_data
def load_crop_prices_data():
    df = pd.read_csv("Crop Prices.csv")
    
    # Clean the Value column and convert to numeric
    df['Value_Clean'] = pd.to_numeric(df['Value'], errors='coerce')
    
    # Convert Year to numeric
    df['Year'] = pd.to_numeric(df['Year'])
    
    return df

# Load the Index Pricing data
@st.cache_data
def load_index_pricing_data():
    df = pd.read_csv("Index Pricing.csv")
    
    # Clean the Value column and convert to numeric
    df['Value_Clean'] = pd.to_numeric(df['Value'], errors='coerce')
    
    # Convert Year to numeric
    df['Year'] = pd.to_numeric(df['Year'])
    
    # Filter for annual price received information only
    df = df[df['Period'] == 'YEAR'].copy()
    
    return df

# Load data
df_cropland = load_cropland_data()
df_crop_prices = load_crop_prices_data()
df_index_pricing = load_index_pricing_data()

# Add description
st.write("""
## Cropland Value Analysis by State
This analysis shows the agricultural land (cropland) asset values measured in dollars per acre 
across four states: Indiana, Kentucky, Ohio, and Tennessee from 2013 to 2025.
""")

# Create the main line chart
st.header("📈 Cropland Value Trends by State (2013-2025)")

# Create line plot with Plotly
fig = go.Figure()

# Get unique states and create a color palette
states = df_cropland['State'].unique()
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red

# Create a comprehensive hover data structure
years = sorted(df_cropland['Year'].unique())
hover_info = {}

# Pre-compute hover information for each year
for year in years:
    year_data = df_cropland[df_cropland['Year'] == year].copy()
    year_data = year_data.sort_values('Value_Clean', ascending=False)
    
    hover_lines = [f"<b>Year: {year}</b>"]
    for _, row in year_data.iterrows():
        hover_lines.append(f"{row['State']}: ${row['Value_Clean']:,.0f}/acre")
    
    hover_info[year] = "<br>".join(hover_lines)

# Add a line for each state with custom hover text
for i, state in enumerate(states):
    state_data = df_cropland[df_cropland['State'] == state].sort_values('Year')
    
    fig.add_trace(go.Scatter(
        x=state_data['Year'],
        y=state_data['Value_Clean'],
        mode='lines+markers',
        name=state,
        line=dict(width=3, color=colors[i]),
        marker=dict(size=8, color=colors[i]),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Year: %{x}<br>' +
                     'Value: $%{y:,.0f}/acre<br>' +
                     '<extra></extra>',
        showlegend=True
    ))

# Update layout for better appearance
fig.update_layout(
    title={
        'text': 'Cropland Asset Value by State (2013-2025)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    xaxis_title='Year',
    yaxis_title='Value ($ per Acre)',
    xaxis=dict(
        tickmode='linear',
        tick0=2013,
        dtick=1,
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    yaxis=dict(
        tickformat='$,.0f',
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02,
        font=dict(size=12),
        itemclick="toggle",  # Enables hide/show functionality
        itemdoubleclick="toggleothers"  # Double-click to show only that state
    ),
    width=800,
    height=500,
    hovermode='x',  # This gives the vertical line without the bottom summary
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="black",
        font_size=12,
        font_family="Arial"
    ),
    annotations=[
        dict(
            text="💡 Click legend to hide/show<br>Double-click to isolate",
            xref="paper", yref="paper",
            x=1.01, y=0.72,  # Adjusted position
            xanchor="left", yanchor="top",
            showarrow=False,
            font=dict(size=9, color="gray"),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="lightgray",
            borderwidth=1
        )
    ]
)

st.plotly_chart(fig, use_container_width=True)

# Display key statistics
st.header("📊 Key Statistics")

col1, col2, col3, col4 = st.columns(4)

for i, state in enumerate(states):
    state_data = df_cropland[df_cropland['State'] == state]
    latest_value = state_data[state_data['Year'] == state_data['Year'].max()]['Value_Clean'].iloc[0]
    earliest_value = state_data[state_data['Year'] == state_data['Year'].min()]['Value_Clean'].iloc[0]
    growth = ((latest_value - earliest_value) / earliest_value) * 100
    
    if i == 0:
        with col1:
            st.metric(
                label=f"{state}",
                value=f"${latest_value:,.0f}/acre",
                delta=f"{growth:.1f}% since 2013"
            )
    elif i == 1:
        with col2:
            st.metric(
                label=f"{state}",
                value=f"${latest_value:,.0f}/acre",
                delta=f"{growth:.1f}% since 2013"
            )
    elif i == 2:
        with col3:
            st.metric(
                label=f"{state}",
                value=f"${latest_value:,.0f}/acre",
                delta=f"{growth:.1f}% since 2013"
            )
    elif i == 3:
        with col4:
            st.metric(
                label=f"{state}",
                value=f"${latest_value:,.0f}/acre",
                delta=f"{growth:.1f}% since 2013"
            )

# Comparative analysis
st.header("🔍 Comparative Analysis")

# Bar chart for latest year comparison
latest_year = df_cropland['Year'].max()
latest_data = df_cropland[df_cropland['Year'] == latest_year]

fig_bar = px.bar(
    latest_data, 
    x='State', 
    y='Value_Clean',
    color='State',
    title=f'Cropland Values by State - {latest_year}',
    labels={'Value_Clean': 'Value ($ per Acre)', 'State': 'State'},
    color_discrete_sequence=colors
)

fig_bar.update_layout(
    showlegend=False,
    yaxis_tickformat='$,.0f',
    title_x=0.5
)

st.plotly_chart(fig_bar, use_container_width=True)

# Data table
st.header("📋 Raw Data")
if st.checkbox("Show Cropland Value Data"):
    # Display only relevant columns
    display_df = df_cropland[['Year', 'State', 'Value']].sort_values(['Year', 'State'])
    st.dataframe(display_df, use_container_width=True)

# Additional insights
st.header("💡 Key Insights")
st.write(f"""
**Observations from the Cropland Value Data:**

1. **Highest Values**: Ohio consistently shows the highest cropland values, reaching ${df_cropland[df_cropland['State'] == 'OHIO']['Value_Clean'].max():,.0f}/acre in {latest_year}.

2. **Growth Trends**: All states show general upward trends in cropland values over the period from 2013 to {latest_year}.

3. **State Rankings** (as of {latest_year}):
   - 1st: Ohio (${latest_data[latest_data['State'] == 'OHIO']['Value_Clean'].iloc[0]:,.0f}/acre)
   - 2nd: Indiana (${latest_data[latest_data['State'] == 'INDIANA']['Value_Clean'].iloc[0]:,.0f}/acre)
   - 3rd: Kentucky (${latest_data[latest_data['State'] == 'KENTUCKY']['Value_Clean'].iloc[0]:,.0f}/acre)
   - 4th: Tennessee (${latest_data[latest_data['State'] == 'TENNESSEE']['Value_Clean'].iloc[0]:,.0f}/acre)

4. **Market Dynamics**: The data reflects agricultural land appreciation trends across the Midwest and Southeast regions.
""")

# ================================
# CROP PRICES ANALYSIS
# ================================

st.markdown("---")  # Divider
st.title("🌾 Crop Prices Analysis")

st.write("""
## National Crop Prices by Commodity
This analysis shows the price trends for major agricultural commodities (Corn, Soybeans, and Wheat) 
across marketing years, measured in dollars per bushel.
""")

# Create the crop prices line chart
st.header("📈 Crop Price Trends by Commodity")

# Create line plot for crop prices
fig_crops = go.Figure()

# Get unique commodities and create a color palette
commodities = df_crop_prices['Commodity'].unique()
crop_colors = ['#FF6B6B', '#4ECDC4', '#45B7D1']  # Red, Teal, Blue

# Add a line for each commodity
for i, commodity in enumerate(commodities):
    commodity_data = df_crop_prices[df_crop_prices['Commodity'] == commodity].sort_values('Year')
    
    fig_crops.add_trace(go.Scatter(
        x=commodity_data['Year'],
        y=commodity_data['Value_Clean'],
        mode='lines+markers',
        name=commodity.title(),
        line=dict(width=3, color=crop_colors[i]),
        marker=dict(size=8, color=crop_colors[i]),
        hovertemplate='<b>%{fullData.name}</b><br>' +
                     'Year: %{x}<br>' +
                     'Price: $%{y:.2f}/bushel<br>' +
                     '<extra></extra>',
        showlegend=True
    ))

# Update layout for crop prices chart
fig_crops.update_layout(
    title={
        'text': 'Crop Prices by Commodity (Marketing Years)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    xaxis_title='Marketing Year',
    yaxis_title='Price ($ per Bushel)',
    xaxis=dict(
        tickmode='linear',
        tick0=df_crop_prices['Year'].min(),
        dtick=1,
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    yaxis=dict(
        tickformat='$,.2f',
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    legend=dict(
        orientation="v",
        yanchor="top",
        y=1,
        xanchor="left",
        x=1.02,
        font=dict(size=12),
        itemclick="toggle",  # Enables hide/show functionality
        itemdoubleclick="toggleothers"  # Double-click to show only that commodity
    ),
    width=800,
    height=500,
    hovermode='x',  # This gives the vertical line without summaries
    hoverlabel=dict(
        bgcolor="white",
        bordercolor="black",
        font_size=12,
        font_family="Arial"
    ),
    annotations=[
        dict(
            text="💡 Click legend to hide/show<br>Double-click to isolate",
            xref="paper", yref="paper",
            x=1.01, y=0.72,  # Adjusted position to prevent cutoff
            xanchor="left", yanchor="top",
            showarrow=False,
            font=dict(size=9, color="gray"),
            bgcolor="rgba(255,255,255,0.9)",
            bordercolor="lightgray",
            borderwidth=1
        )
    ]
)

st.plotly_chart(fig_crops, use_container_width=True)

# Display crop price statistics
st.header("📊 Crop Price Statistics")

col1, col2, col3 = st.columns(3)

for i, commodity in enumerate(commodities):
    commodity_data = df_crop_prices[df_crop_prices['Commodity'] == commodity]
    latest_price = commodity_data[commodity_data['Year'] == commodity_data['Year'].max()]['Value_Clean'].iloc[0]
    earliest_price = commodity_data[commodity_data['Year'] == commodity_data['Year'].min()]['Value_Clean'].iloc[0]
    price_change = ((latest_price - earliest_price) / earliest_price) * 100
    
    if i == 0:
        with col1:
            st.metric(
                label=f"{commodity.title()}",
                value=f"${latest_price:.2f}/bu",
                delta=f"{price_change:.1f}% since {commodity_data['Year'].min()}"
            )
    elif i == 1:
        with col2:
            st.metric(
                label=f"{commodity.title()}",
                value=f"${latest_price:.2f}/bu",
                delta=f"{price_change:.1f}% since {commodity_data['Year'].min()}"
            )
    elif i == 2:
        with col3:
            st.metric(
                label=f"{commodity.title()}",
                value=f"${latest_price:.2f}/bu",
                delta=f"{price_change:.1f}% since {commodity_data['Year'].min()}"
            )

# Comparative analysis for crop prices
st.header("🔍 Crop Price Comparison")

# Bar chart for latest year comparison
latest_crop_year = df_crop_prices['Year'].max()
latest_crop_data = df_crop_prices[df_crop_prices['Year'] == latest_crop_year]

fig_crop_bar = px.bar(
    latest_crop_data, 
    x='Commodity', 
    y='Value_Clean',
    color='Commodity',
    title=f'Crop Prices by Commodity - {latest_crop_year} Marketing Year',
    labels={'Value_Clean': 'Price ($ per Bushel)', 'Commodity': 'Commodity'},
    color_discrete_sequence=crop_colors
)

fig_crop_bar.update_layout(
    showlegend=False,
    yaxis_tickformat='$,.2f',
    title_x=0.5
)

# Update x-axis labels to be more readable
fig_crop_bar.update_xaxes(ticktext=[c.title() for c in latest_crop_data['Commodity']], 
                         tickvals=latest_crop_data['Commodity'])

st.plotly_chart(fig_crop_bar, use_container_width=True)

# Crop prices data table
st.header("📋 Crop Prices Raw Data")
if st.checkbox("Show Crop Prices Data"):
    # Display only relevant columns
    display_crop_df = df_crop_prices[['Year', 'Commodity', 'Value']].sort_values(['Year', 'Commodity'])
    st.dataframe(display_crop_df, use_container_width=True)

# Additional insights for crop prices
st.header("💡 Crop Price Insights")
st.write(f"""
**Observations from the Crop Prices Data:**

1. **Price Volatility**: {commodities[1].title()} shows the highest price volatility, reaching peaks during certain marketing years.

2. **Current Prices** (Marketing Year {latest_crop_year}):
   - {commodities[0].title()}: ${latest_crop_data[latest_crop_data['Commodity'] == commodities[0]]['Value_Clean'].iloc[0]:.2f}/bushel
   - {commodities[1].title()}: ${latest_crop_data[latest_crop_data['Commodity'] == commodities[1]]['Value_Clean'].iloc[0]:.2f}/bushel
   - {commodities[2].title()}: ${latest_crop_data[latest_crop_data['Commodity'] == commodities[2]]['Value_Clean'].iloc[0]:.2f}/bushel

3. **Market Trends**: The data reflects global commodity market dynamics, weather impacts, and supply/demand fluctuations.

4. **Price Rankings**: {commodities[1].title()} typically commands the highest price per bushel, followed by {commodities[2].title()} and {commodities[0].title()}.
""")

# ================================
# INDEX PRICING ANALYSIS
# ================================

st.markdown("---")  # Divider
st.title("📊 Food Commodities Price Index Analysis")

st.write("""
## Food Commodities Price Index (Base Year: 2011)
This analysis shows the annual Food Commodities Price Index, which tracks the overall price trends 
for food commodities with 2011 as the base year (index = 100).
""")

# Create the index pricing line chart
st.header("📈 Food Commodities Price Index Trend")

# Sort data by year for proper line plotting
index_data_sorted = df_index_pricing.sort_values('Year')

# Create single line plot for index pricing
fig_index = go.Figure()

fig_index.add_trace(go.Scatter(
    x=index_data_sorted['Year'],
    y=index_data_sorted['Value_Clean'],
    mode='lines+markers',
    name='Food Commodities Price Index',
    line=dict(width=4, color='#8B4513'),  # Brown color for food commodities
    marker=dict(size=10, color='#8B4513'),
    hovertemplate='<b>Food Commodities Price Index</b><br>' +
                 'Year: %{x}<br>' +
                 'Index Value: %{y:.1f}<br>' +
                 '(Base Year 2011 = 100)<br>' +
                 '<extra></extra>'
))

# Update layout for index pricing chart
fig_index.update_layout(
    title={
        'text': 'Food Commodities Price Index (Annual, Base Year 2011 = 100)',
        'x': 0.5,
        'xanchor': 'center',
        'font': {'size': 20}
    },
    xaxis_title='Year',
    yaxis_title='Price Index (Base Year 2011 = 100)',
    xaxis=dict(
        tickmode='linear',
        tick0=df_index_pricing['Year'].min(),
        dtick=2,  # Show every 2 years for better readability
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    yaxis=dict(
        tickformat='.1f',
        tickfont=dict(size=12),
        title_font=dict(size=14)
    ),
    showlegend=False,  # Single line doesn't need legend
    width=800,
    height=500,
    hovermode='x'
)

# Add a horizontal line at 100 to show the base year
fig_index.add_hline(y=100, line_dash="dash", line_color="gray", 
                   annotation_text="Base Year (2011) = 100", 
                   annotation_position="bottom right")

st.plotly_chart(fig_index, use_container_width=True)

# Display index pricing statistics
st.header("📊 Index Statistics")

# Calculate key statistics
current_index = index_data_sorted['Value_Clean'].iloc[-1]
base_year = 2011
current_year = index_data_sorted['Year'].iloc[-1]
max_index = index_data_sorted['Value_Clean'].max()
min_index = index_data_sorted['Value_Clean'].min()
max_year = index_data_sorted[index_data_sorted['Value_Clean'] == max_index]['Year'].iloc[0]
min_year = index_data_sorted[index_data_sorted['Value_Clean'] == min_index]['Year'].iloc[0]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label=f"Current Index ({current_year})",
        value=f"{current_index:.1f}",
        delta=f"{current_index - 100:.1f} from base year"
    )

with col2:
    st.metric(
        label="Highest Index",
        value=f"{max_index:.1f}",
        delta=f"in {max_year}"
    )

with col3:
    st.metric(
        label="Lowest Index",
        value=f"{min_index:.1f}",
        delta=f"in {min_year}"
    )

with col4:
    percent_change = ((current_index - 100) / 100) * 100
    st.metric(
        label="Total Change",
        value=f"{percent_change:+.1f}%",
        delta=f"since {base_year}"
    )

# Index pricing data table
st.header("📋 Index Pricing Raw Data")
if st.checkbox("Show Index Pricing Data"):
    # Display only relevant columns
    display_index_df = df_index_pricing[['Year', 'Value']].sort_values('Year')
    display_index_df.columns = ['Year', 'Price Index']
    st.dataframe(display_index_df, use_container_width=True)

# Additional insights for index pricing
st.header("💡 Price Index Insights")
st.write(f"""
**Observations from the Food Commodities Price Index:**

1. **Base Year Reference**: The index uses 2011 as the base year (index = 100), making it easy to compare relative price changes.

2. **Peak Performance**: The highest index value was {max_index:.1f} in {max_year}, representing a {((max_index - 100) / 100) * 100:.1f}% increase from the base year.

3. **Lowest Point**: The index reached its minimum of {min_index:.1f} in {min_year}, representing a {((min_index - 100) / 100) * 100:.1f}% change from the base year.

4. **Current Status**: As of {current_year}, the index stands at {current_index:.1f}, indicating that food commodity prices are {percent_change:+.1f}% {'higher' if percent_change > 0 else 'lower'} than the 2011 baseline.

5. **Long-term Trend**: The data shows the volatility and cyclical nature of agricultural commodity pricing, influenced by factors such as weather, global demand, and economic conditions.

6. **Market Context**: Values above 100 indicate prices higher than 2011 levels, while values below 100 indicate prices lower than the base year.
""")
