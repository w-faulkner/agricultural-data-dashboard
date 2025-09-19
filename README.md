# Agricultural Data Analysis Dashboard

An interactive Streamlit web application that visualizes comprehensive agricultural data including cropland values, commodity prices, and food price indices.

## 📊 Dashboard Features

### 1. Cropland Asset Value Analysis
- **Interactive line chart** showing cropland values by state (Indiana, Kentucky, Ohio, Tennessee) from 2013-2025
- **State comparison** with individual state metrics and growth percentages
- **Interactive legend** - click to hide/show states, double-click to isolate individual states
- **Professional hover tooltips** with vertical reference lines

### 2. Crop Prices Analysis  
- **Commodity price trends** for Corn, Soybeans, and Wheat across marketing years
- **Individual commodity tracking** with separate colored lines for each crop
- **Interactive legend** functionality for customizing chart views
- **Price comparison tools** and statistical summaries

### 3. Food Commodities Price Index
- **Price index tracking** with 2011 as base year (index = 100)
- **Historical trend analysis** showing price volatility and market cycles
- **Key performance metrics** including highest/lowest index values
- **Annual price received information** filtered for comprehensive analysis

## 🚀 Live Demo

The dashboard is deployed and accessible at: [Your Streamlit Cloud URL will go here]

## 📁 Repository Structure

```
├── streamlit_app.py          # Main Streamlit application
├── requirements.txt          # Python dependencies
├── README.md                # Project documentation
├── Faulkner,Will.jpg        # Profile image
├── Cropland Value.csv       # State cropland value data
├── Crop Prices.csv          # Commodity pricing data
└── Index Pricing.csv        # Food commodities price index data
```

## 🛠️ Installation & Setup

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/agricultural-data-dashboard.git
   cd agricultural-data-dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

4. **Open your browser** to `http://localhost:8501`

### Deployment on Streamlit Cloud

1. **Fork this repository** to your GitHub account
2. **Visit** [share.streamlit.io](https://share.streamlit.io)
3. **Deploy** by connecting your GitHub repository
4. **Main file path**: `streamlit_app.py`

## 📈 Data Sources

- **Cropland Values**: Agricultural land asset values measured in $/acre by state
- **Crop Prices**: National commodity prices for major crops ($/bushel)
- **Price Index**: Food commodities price index with 2011 baseline

## 🎯 Key Features

### Interactive Visualizations
- ✅ **Hover tooltips** with comprehensive data
- ✅ **Vertical reference lines** for precise year alignment
- ✅ **Legend interactivity** - hide/show individual data series
- ✅ **Professional styling** with consistent formatting

### User Experience
- ✅ **Responsive design** that works on desktop and mobile
- ✅ **Clear user guidance** with helpful instruction annotations
- ✅ **Statistical summaries** with key insights and trends
- ✅ **Professional appearance** with clean, modern styling

### Data Analysis Tools
- ✅ **Growth percentage calculations** since baseline years
- ✅ **Comparative analysis** across states and commodities
- ✅ **Historical trend visualization** with market context
- ✅ **Raw data exploration** with optional data tables

## 🔧 Technical Stack

- **Frontend**: Streamlit
- **Data Processing**: Pandas
- **Visualizations**: Plotly Express & Plotly Graph Objects
- **Deployment**: Streamlit Cloud
- **Version Control**: Git/GitHub

## 📱 Usage Instructions

### Chart Interactions
- **Single-click legend items** to hide/show data series
- **Double-click legend items** to isolate individual series
- **Hover over charts** for detailed data tooltips
- **Use checkboxes** to toggle raw data table views

### Navigation
- **Scroll through sections** for different analyses
- **Expand insights sections** for detailed observations
- **View statistics** in organized metric displays

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👤 Author

**Will Faulkner**

- Email: [Your email]
- LinkedIn: [Your LinkedIn profile]
- Portfolio: [Your portfolio URL]

## 🙏 Acknowledgments

- Data sources and agricultural statistics providers
- Streamlit community for excellent documentation
- Plotly for powerful visualization capabilities

---

*This dashboard provides comprehensive insights into agricultural economics, from land values to commodity pricing trends, helping stakeholders make informed decisions in the agricultural sector.*
