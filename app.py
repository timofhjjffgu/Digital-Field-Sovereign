import streamlit as st
import time
import random
from fpdf import FPDF
import base64

# --- إعدادات الهوية السيادية ---
st.set_page_config(page_title="Sovereign Core v3.1", page_icon="🌾", layout="wide")

# --- رابط صورة الماتريكس (الخلفية) ---
IMG_URL = "https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png"

# --- تصميم الواجهة السيبرانية ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@400;700&display=swap');
    
    .stApp {{
        background-image: url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    .main {{ background-color: rgba(0, 0, 0, 0.6); color: #00f2ff; font-family: 'Cairo', sans-serif; }}
    
    /* تصميم الصناديق الزجاجية */
    .cyber-box {{ 
        background: rgba(10, 10, 30, 0.8); 
        border: 2px solid #7000ff; 
        padding: 25px; 
        border-radius: 20px; 
        box-shadow: 0 0 20px rgba(112, 0, 255, 0.6);
        backdrop-filter: blur(8px);
    }}
    
    /* أزرار الطاقة */
    .stButton>button {{ 
        width: 100%; 
        border-radius: 25px; 
        background: linear-gradient(90deg, #7000ff, #00f2ff); 
        color: white; 
        border: none; 
        font-family: 'Orbitron', sans-serif;
        font-weight: bold;
        height: 50px;
        transition: 0.4s;
    }}
    .stButton>button:hover {{ transform: scale(1.05); box-shadow: 0 0 30px #00f2ff; }}
    
    /* المحادثة الذكية */
    .chat-container {{ height: 300px; overflow-y: auto; padding: 10px; }}
    .ai-bubble {{ background: rgba(188, 19, 254, 0.2); border-left: 4px solid #bc13fe; padding: 10px; border-radius: 5px; margin: 10px 0; }}
    .user-bubble {{ background: rgba(0, 242, 255, 0.1); border-right: 4px solid #00f2ff; padding: 10px; border-radius: 5px; margin: 10px 0; text-align: right; }}
    
    h1 {{ text-shadow: 0 0 20px #7000ff; color: #ffffff; text-align: center; font-family: 'Orbitron', sans-serif; letter-spacing: 2px; }}
</style>
""", unsafe_allow_html=True)

# --- إدارة الحالة (Session State) ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- وظيفة توليد الشهادة السيادية ---
def generate_pdf(name, asset):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(10, 10, 30)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("helvetica", 'B', 20)
    pdf.cell(0, 20, "SOVEREIGN OWNERSHIP CERTIFICATE", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("helvetica", size=14)
    pdf.cell(0, 10, f"Holder Name: {name}", ln=True)
    pdf.cell(0, 10, f"Asset ID: {asset}", ln=True)
    pdf.cell(0, 10, f"Sector: Oran Digital Field", ln=True)
    pdf.cell(
