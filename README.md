# RedNoesis

### A Streamlit-Based Web Application for Data-Driven Retail Analytics & Strategic Business Intelligence

**Built with Python | Streamlit | Pandas | Matplotlib | ReportLab**

**Analyze Performance. Uncover Opportunities. Inform Decisions.**

RedNoesis is an interactive retail analytics web application developed using Python and Streamlit. It transforms retail transaction data into meaningful performance metrics, interactive visualizations, and rule-based business insights to help users evaluate sales performance and identify potential business opportunities.

By combining data preprocessing, sales analysis, performance comparisons, business recommendations, and PDF report generation in a single interface, RedNoesis makes retail data easier to understand and supports informed, data-driven decision-making.

## Key Features

* **Sales Performance Analytics:** Analyze total revenue, total profit, order volume, and average order value.
* **Interactive Data Visualization:** Explore revenue, profit, and quantity across product categories, states, cities, and payment methods.
* **Retail Opportunity Scanner:** Compare category revenue against average performance to identify potential growth opportunities and areas requiring attention.
* **Discount Impact Simulation:** Experiment with different discount percentages to explore hypothetical revenue scenarios.
* **Business Insights Engine:** Generate rule-based summaries of top-performing categories, weaker-performing categories, leading states, popular payment methods, and profitability.
* **Revenue Risk Indicators:** Flag categories with below-average revenue for further investigation.
* **Business Recommendations:** Present rule-based suggestions to support retail performance analysis and planning.
* **PDF Report Generation:** Generate and download reports containing analytical findings.

## Technology Stack

| Technology | Purpose                                         |
| ---------- | ----------------------------------------------- |
| Python     | Core programming language and application logic |
| Streamlit  | Interactive web application framework           |
| Pandas     | Data cleaning, processing, and analysis         |
| Matplotlib | Data visualization                              |
| ReportLab  | PDF report generation                           |

## How It Works

1. **Upload Data:** Import retail transaction data in CSV format.
2. **Clean Data:** Remove duplicate records, convert numeric fields, and handle invalid or unusable rows.
3. **Analyze Performance:** Calculate key metrics to summarize sales, profitability, order volume, and average order value.
4. **Visualize Insights:** Explore charts showing revenue, profit, quantity, categories, locations, and payment methods.
5. **Identify Opportunities:** Compare category performance and explore hypothetical discount scenarios.
6. **Generate Reports:** Download a PDF report containing analytical findings.

## Getting Started

### Prerequisites

* Python 3.9 or a compatible version supported by the dependencies
* Git, if cloning the repository
* A retail sales dataset in CSV format containing the columns required by the application

### Installation and Setup

**Step 1: Clone the repository**

```bash
git clone https://github.com/sujankharvi167/RedNoesis.git
cd RedNoesis
```

**Step 2: Install dependencies**

```bash
pip install -r requirements.txt
```

**Step 3: Run the application**

```bash
streamlit run app.py
```

**Step 4: Open the dashboard**

Open the local URL displayed in your terminal to access RedNoesis in your web browser.

## Deployment

RedNoesis can be run locally or deployed online using **Streamlit Community Cloud**.

### Deploy Using Streamlit Community Cloud

1. Push the project files to your GitHub repository.
2. Visit [Streamlit Community Cloud](https://share.streamlit.io/).
3. Sign in using your GitHub account.
4. Create a new application and select the RedNoesis repository.
5. Choose the appropriate branch and set the main file path to `app.py`.
6. Deploy the application.

After successful deployment, the application will have a public URL that users can open in their browsers.

## Business Applications

RedNoesis can support retail analysis by helping users:

* Review sales and profitability.
* Compare performance across product categories and locations.
* Identify underperforming categories that may require further investigation.
* Explore hypothetical discount scenarios.
* Understand payment method distributions.
* Evaluate business performance using visualizations and summary metrics.
* Generate reports for business reviews and planning.

## Project Scope and Limitations

RedNoesis currently focuses on descriptive analytics, data visualization, threshold-based indicators, hypothetical simulations, and rule-based business recommendations.

The current implementation does not claim to perform machine learning, predictive forecasting, causal analysis, or verified fraud and revenue-leakage detection.

Below-average category revenue indicates relative underperformance, not confirmed revenue leakage. Discount simulations are simplified calculations and do not predict actual customer behavior or guarantee increased sales.

The quality of the results depends on the accuracy, completeness, and structure of the uploaded dataset.

## Project Information

* **Project Name:** RedNoesis
* **Application Type:** Streamlit-Based Web Application
* **Domain:** Retail Analytics and Business Intelligence
* **Programming Language:** Python
* **Framework:** Streamlit
* **Data Processing:** Pandas
* **Visualization:** Matplotlib
* **Report Generation:** ReportLab
* **Deployment Platform:** Streamlit Community Cloud

## Project Objective

The objective of RedNoesis is to transform raw retail transaction data into understandable performance indicators, comparative visualizations, and actionable analytical insights through an accessible web-based dashboard.

## Future Scope

Potential future enhancements include:

* Sales trend analysis over time.
* Machine learning-based sales forecasting.
* Interactive filtering by date, category, and location.
* Advanced customer and product segmentation.
* AI-powered natural-language business queries.

These are potential future enhancements and are not claimed as existing features.

---

**RedNoesis — From Retail Data to Strategic Insights.**
