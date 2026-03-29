import streamlit as st
import pandas as pd
import time
from fpdf import FPDF
import base64

# وظيفة توليد شهادة الملكية السيادية
def create_certificate(name, asset_type, asset_id):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("helvetica", 'B', 16)
    pdf.cell(0, 10, "Sovereign Digital Field - Ownership Certificate", ln=True, align='C')
    pdf.ln(10)
    pdf.set_font("helvetica", size=12)
    pdf.cell(0, 10, f"Owner Name: {name}", ln=True)
    pdf.cell(0, 10, f"Asset Category: {asset_type}", ln=True)
    pdf.cell(0, 10, f"Asset Identifier: {asset_id}", ln=True)
    pdf.cell(0, 10, f"Issuance Date: 2026-03-29", ln=True)
    pdf.ln(20)
    pdf.cell(0, 10, "Authorized by: Abd Al-Khaliq AI Core", ln=True, align='C')
    return pdf.output()

# بوابة الدخول
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown("<h2 style='text-align: center;'>🔐 Sovereign Access Portal</h2>", unsafe_allow_html=True)
    password = st.text_input("Security Phrase (حديديها):", type="password")
    if st.button("Activate Core"):
        if password == "حديديها":
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("Access Denied: Data Interference Detected.")

if not st.session_state.logged_in:
    login()
else:
    st.title("🛡️ مركز العمليات السيادي | عبد الخالق")
    with st.sidebar:
        st.success("Authorized Access Active")
        if st.button("Exit Session"):
            st.session_state.logged_in = False
            st.rerun()

    # ركن الشهادات للزبائن
    st.subheader("👤 إدارة الزبائن")
    c_name = st.text_input("اسم الزبون الجديد:")
    c_asset = st.selectbox("الأصل الرقمي:", ["NFT Land #442", "Simei Seed v1", "AI Guard Agent"])
    if st.button("Generate PDF Certificate"):
        if c_name:
            pdf_bytes = create_certificate(c_name, c_asset, "SN-2026-ORAN")
            b64 = base64.b64encode(pdf_bytes).decode()
            href = f'<a href="data:application/pdf;base64,{b64}" download="Cert_{c_name}.pdf" style="background-color:#4CAF50; color:white; padding:10px; border-radius:5px; text-decoration:none;">📥 تحميل الشهادة</a>'
            st.markdown(href, unsafe_allow_html=True)

    st.markdown("---")
    st.caption("نظام السيادة الرقمية 2026 | تحت إدارة عبد الخالق")
