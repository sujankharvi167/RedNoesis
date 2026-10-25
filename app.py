import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import io
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
st.set_page_config(page_title="Retail Sales Intelligence Dashboard", layout="wide")
st.markdown("""
<style>
.stApp {background-color: #black;}
[data-testid="stMetric"] {background-color: black; padding: 15px; border-radius: 10px; box-shadow: 0 2px 5px rgba(0,0,0,0.1);}
[data-testid="stDataFrame"] {background-color: black;}
h1 {color: #1f4e79;}
</style>
""", unsafe_allow_html=True)
st.title("Retail Sales Intelligence Dashboard")
st.caption("AI-Powered Retail Analytics, Revenue Optimization and Business Decision Support")
uploaded_file = st.file_uploader("Upload Retail Sales CSV Dataset", type=["csv"])
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file)
        required_columns = ["Amount", "Profit", "Quantity", "Category", "PaymentMode", "State", "City"]
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            st.error(f"Missing required columns: {', '.join(missing_columns)}")
            st.stop()
        df = df.drop_duplicates()
        for col in ["Amount", "Profit", "Quantity"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        df = df.dropna(subset=required_columns)
        if df.empty:
            st.error("The dataset contains no valid rows after cleaning.")
            st.stop()
        revenue = df["Amount"].sum()
        profit = df["Profit"].sum()
        orders = len(df)
        avg_order = revenue / orders if orders else 0
        category_sales = df.groupby("Category")["Amount"].sum().sort_values(ascending=False)
        quantity_sales = df.groupby("Category")["Quantity"].sum()
        payment_sales = df.groupby("PaymentMode")["Amount"].sum()
        state_sales = df.groupby("State")["Amount"].sum().sort_values(ascending=False)
        profit_category = df.groupby("Category")["Profit"].sum()
        city_sales = df.groupby("City")["Amount"].sum().sort_values(ascending=False).head(10)
        st.subheader("Key Performance Indicators")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Total Revenue", f"{revenue:,.2f}")
        col2.metric("Total Profit", f"{profit:,.2f}")
        col3.metric("Total Orders", f"{orders:,}")
        col4.metric("Average Order Value", f"{avg_order:,.2f}")
        st.subheader("Sales Analytics")
        row1_col1, row1_col2 = st.columns(2)
        with row1_col1:
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            category_sales.plot(kind="bar", ax=ax1)
            ax1.set_title("Revenue by Category")
            ax1.set_xlabel("Category")
            ax1.set_ylabel("Revenue")
            fig1.tight_layout()
            st.pyplot(fig1)
            plt.close(fig1)
        with row1_col2:
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            state_sales.plot(kind="bar", ax=ax2, color="orange")
            ax2.set_title("Revenue by State")
            ax2.set_xlabel("State")
            ax2.set_ylabel("Revenue")
            fig2.tight_layout()
            st.pyplot(fig2)
            plt.close(fig2)
        row2_col1, row2_col2 = st.columns(2)
        with row2_col1:
            fig3, ax3 = plt.subplots(figsize=(6, 4))
            payment_sales.plot(kind="pie", autopct="%1.1f%%", ax=ax3)
            ax3.set_ylabel("")
            ax3.set_title("Revenue by Payment Mode")
            fig3.tight_layout()
            st.pyplot(fig3)
            plt.close(fig3)
        with row2_col2:
            fig4, ax4 = plt.subplots(figsize=(6, 4))
            quantity_sales.plot(kind="bar", ax=ax4, color="green")
            ax4.set_title("Quantity Sold by Category")
            ax4.set_xlabel("Category")
            ax4.set_ylabel("Quantity")
            fig4.tight_layout()
            st.pyplot(fig4)
            plt.close(fig4)
        row3_col1, row3_col2 = st.columns(2)
        with row3_col1:
            st.subheader("Top 10 Revenue Generating Cities")
            fig5, ax5 = plt.subplots(figsize=(6, 4))
            city_sales.plot(kind="bar", ax=ax5, color="purple")
            ax5.set_title("Top 10 Cities by Revenue")
            ax5.set_xlabel("City")
            ax5.set_ylabel("Revenue")
            fig5.tight_layout()
            st.pyplot(fig5)
            plt.close(fig5)
        with row3_col2:
            st.subheader("Profit by Category")
            fig6, ax6 = plt.subplots(figsize=(6, 4))
            profit_category.plot(kind="bar", ax=ax6, color="teal")
            ax6.set_title("Profit by Category")
            ax6.set_xlabel("Category")
            ax6.set_ylabel("Profit")
            fig6.tight_layout()
            st.pyplot(fig6)
            plt.close(fig6)
        st.subheader("Retail Opportunity Scanner")
        avg_rev = category_sales.mean()
        opp_df = pd.DataFrame({
            "Category": category_sales.index,
            "Revenue": category_sales.values,
            "Zone": ["Growth Engine" if x > avg_rev else "Recovery Zone" for x in category_sales.values],
            "Recommended Action": ["Scale Aggressively" if x > avg_rev else "Improve Promotion" for x in category_sales.values]
        })
        opp_df.index = range(1, len(opp_df) + 1)
        st.dataframe(opp_df, use_container_width=True)
        st.subheader("Discount Simulation Engine")
        discount = st.slider("Adjust Discount Percentage", 0, 30, 10)
        projected_revenue = revenue * (1 - discount / 100)
        st.info(f"Projected Revenue after {discount}% Discount: {projected_revenue:.2f}")
        st.subheader("Revenue Leakage Detector")
        leakage_df = pd.DataFrame({
            "Category": category_sales.index,
            "Revenue": category_sales.values,
            "Status": ["Healthy" if x >= avg_rev else "Leakage Risk" for x in category_sales.values]
        })
        leakage_df.index = range(1, len(leakage_df) + 1)
        st.dataframe(leakage_df, use_container_width=True)
        st.subheader("Smart Business Insights")
        top_category = category_sales.idxmax()
        weak_category = category_sales.idxmin()
        top_state = state_sales.idxmax()
        top_payment = payment_sales.idxmax()
        st.success(f"""
### Key Insights
**Top Performing Category:** {top_category}\n
**Weakest Category:** {weak_category}\n
**Highest Revenue State:** {top_state}\n
**Most Used Payment Mode:** {top_payment}\n
**Total Profit:** {profit:.2f}
**Projected Revenue after {discount}% Discount:** {projected_revenue:.2f}
""")
        st.subheader("How to Increase Sales")
        st.success(f"""
1. Scale **{top_category}** with premium marketing campaigns.
2. Improve sales of **{weak_category}** through discounts and bundle offers.
3. Focus marketing efforts in **{top_state}**.
4. Encourage customers to use **{top_payment}** with cashback offers.
5. Optimize inventory for high-selling categories.
6. Increase promotions in leakage-risk categories.
7. Cross-sell products from high-profit categories.
8. Improve customer retention with loyalty programs.
""")
        pdf_buffer = io.BytesIO()
        doc = SimpleDocTemplate(pdf_buffer)
        styles = getSampleStyleSheet()
        elements = [Paragraph("Retail Sales Intelligence Report", styles["Title"]), Spacer(1, 20)]
        report_data = [
            ["Metric", "Value"],
            ["Total Revenue", f"{revenue:.2f}"],
            ["Total Profit", f"{profit:.2f}"],
            ["Total Orders", str(orders)],
            ["Average Order Value", f"{avg_order:.2f}"],
            ["Projected Revenue", f"{projected_revenue:.2f}"],
            ["Top Category", str(top_category)],
            ["Weakest Category", str(weak_category)],
            ["Top State", str(top_state)],
            ["Most Used Payment", str(top_payment)]
        ]
        table = Table(report_data)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkgrey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10)
        ]))
        elements.extend([table, Spacer(1, 20), Paragraph("Business Insights", styles["Heading2"])])
        insights = f"""
Top Performing Category: <b>{top_category}</b><br/><br/>
Weakest Category: <b>{weak_category}</b><br/><br/>
Highest Revenue State: <b>{top_state}</b><br/><br/>
Most Used Payment Mode: <b>{top_payment}</b><br/><br/>
Projected Revenue after {discount}% discount: <b>{projected_revenue:.2f}</b><br/><br/>
Revenue leakage detected in below-average revenue categories.
"""
        elements.extend([Paragraph(insights, styles["Normal"]), Spacer(1, 20), Paragraph("Recommendations", styles["Heading2"])])
        recommendations = f"""
1. Scale <b>{top_category}</b> using premium marketing campaigns.<br/><br/>
2. Improve sales of <b>{weak_category}</b> with promotional offers.<br/><br/>
3. Focus expansion in <b>{top_state}</b> where revenue is highest.<br/><br/>
4. Optimize inventory for high-selling categories.<br/><br/>
5. Increase promotions for leakage-risk categories.<br/><br/>
6. Improve customer retention through loyalty programs.<br/><br/>
7. Encourage customers to use <b>{top_payment}</b> with cashback or rewards.<br/><br/>
8. Continuously monitor profit and category performance using this dashboard.
"""
        elements.append(Paragraph(recommendations, styles["Normal"]))
        doc.build(elements)
        st.download_button(label="Download PDF Report", data=pdf_buffer.getvalue(), file_name="Retail_Sales_Report.pdf", mime="application/pdf")
    except Exception as e:
        st.error(f"Error processing file: {e}")
else:
    st.info("Upload the CSV file to view analytics, business insights, charts, and generate a PDF report.")