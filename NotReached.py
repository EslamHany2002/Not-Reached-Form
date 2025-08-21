import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# عنوان التطبيق
st.title("Dashboard - Evidence Not Submitted per Track")

# رفع ملف Excel
uploaded_file = st.file_uploader("Students_Form_Status.xlsx", type=["xlsx"])
if uploaded_file:
    # قراءة الملف
    xls = pd.ExcelFile(uploaded_file)
    st.write("Sheet Names:", xls.sheet_names)

    # قراءة Sheet1
    sheet1 = pd.read_excel(uploaded_file, sheet_name="Sheet1")
    evidance = pd.read_excel(uploaded_file, sheet_name="Evidance")
    
    # عرض أول صفوف للتأكد من البيانات
    st.subheader("Preview Sheet1")
    st.dataframe(sheet1.head())

    st.subheader("Preview Evidance")
    st.dataframe(evidance.head())

    # تصفية حالات Not Submitted
    not_submitted = sheet1[sheet1["Form Status"].str.contains("Not Submitted", case=False, na=False)]

    # تجميع عدد Evidence لكل Track
    dashboard = not_submitted.groupby("Track Name")["Evidence Attachment"].count().reset_index()
    dashboard = dashboard.rename(columns={"Evidence Attachment": "Evidence Count"})

    st.subheader("Dashboard Table")
    st.dataframe(dashboard)

    # رسم الرسم البياني
    st.subheader("Dashboard Chart")
    fig, ax = plt.subplots(figsize=(10,6))
    ax.bar(dashboard["Track Name"], dashboard["Evidence Count"])
    plt.xticks(rotation=45, ha="right")
    plt.title("Evidences For All Track (Not Submitted)")
    plt.xlabel("Track Name")
    plt.ylabel("Evidence Count")
    st.pyplot(fig)
