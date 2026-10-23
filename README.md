# 📊 Programming Language Demand Trend Analysis in Job Postings

A complete web scraping and data analysis project that examines the demand trend for programming languages in job postings on [JobVision](https://jobvision.ir), one of Iran's largest job platforms.

##  Project Goal

Answering the question: **Which programming languages are most in demand in the Iranian job market?**

##  Features

- ✅ Automated collection of job postings from JobVision
- ✅ Extraction of 27 columns of information (title, company, skills, publication date, etc.)
- ✅ Identification of 15 programming languages from job descriptions
- ✅ Statistical analysis and bar charts
- ✅ Interactive dashboard with Streamlit
- ✅ Search functionality by language, job title, or company

##  Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.13 | Core language |
| requests | Communication with JobVision API |
| pandas | Data processing and analysis |
| matplotlib | Chart generation |
| Streamlit | Interactive dashboard |
| openpyxl | Excel export |
| BeautifulSoup4 | HTML parsing (fallback) |

##  Project Structure
job-trend-project/
├── jobvision_crawler.py # Main crawler (uses JobVision API)
├── collect_multiple.py # Collect data from multiple keywords
├── combine_all.py # Merge datasets and remove duplicates
├── final_analysis.py # Final analysis and chart generation
├── time_trend.py # Time-based trend analysis
├── run_project.py # Master script (runs entire pipeline)
├── app.py # Streamlit interactive dashboard
├── output/
│ ├── ALL_JOBS_COMBINED.xlsx
│ ├── FINAL_ANALYSIS.xlsx
│ ├── chart_languages.png
│ └── chart_time.png
└── README.md

##  How to Run

### 1. Install dependencies

```bash
pip install requests pandas matplotlib openpyxl streamlit beautifulsoup4 lxml


