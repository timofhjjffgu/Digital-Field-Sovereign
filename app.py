import streamlit as st
import time
import random
from fpdf import FPDF
import base64

# --- ضبط الهوية السيادية ---
st.set_page_config(page_title="Sovereign Core v3.1", page_icon="🔮", layout="wide")

# رابط صورة الماتريكس الزراعية
IMG_URL = "https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png"

# --- تصميم الواجهة السيبرانية المحسنة ---
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@400;700&display=swap');
    .stApp {{
        background-image: url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .main {{ background-color: rgba(0, 0, 0, 0.7); color: #00f2ff; font-family: 'Cairo', sans-serif; }}
    .cyber-box {{ 
        background: rgba(10, 10, 30, 0.85); 
        border: 2px solid #7000ff; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 0 20px rgba(112, 0, 255, 0.6);
        backdrop-filter: blur(10px);
    }}
    .stButton>button {{ 
        width: 100%; border-radius: 20px; background: linear-gradient(45deg, #7000ff, #00f2ff); 
        color: white; border: none; font-family: 'Orbitron', sans-serif; transition: 0.3s;
    }}
    .stButton>button:hover {{ transform: scale(1.05); box-shadow: 0 0 25px #00f2ff; }}
    .ai-bubble {{ background: rgba(112, 0, 255, 0.2); border-left: 5px solid #7000ff; padding: 10px; border-radius: 10px; margin: 5px 0; }}
</style>
""", unsafe_allow_html=True)

# --- إدارة الجلسة ---
if 'messages' not in st.session_state: st.session_state.messages = []
if 'logged_in' not in st.session_state: st.session_state.logged_in = False

# --- وظيفة إصدار الشهادة (تم إصلاح الأقواس هنا) ---
def generate_pdf(name, asset):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_fill_color(5, 5, 20)
    pdf.rect(0, 0, 210, 297, 'F')
    pdf.set_text_color(0, 242, 255)
    pdf.set_font("helvetica", 'B', 20)
    pdf.cell(0, 20, "SOVEREIGN OWNERSHIP DEED", ln=True, align='C')
    pdf.ln(20)
    pdf.set_font("helvetica", size=14)
    pdf.cell(0, 10, f"Holder: {name}", ln=True)
    pdf.cell(0, 10, f"Asset: {asset}", ln=True)
    pdf.cell(0, 10, "Sector: Oran Digital Field", ln=True)
    pdf.ln(40)
    pdf.set_font("helvetica", 'I', 10)
    pdf.cell(0, 10, "Protected by Abd Al-Khaliq AI Core - 2026", align='C')
    return pdf.output()

# --- منطق الواجهة ---
if not st.session_state.logged_in:
    st.markdown("<h1 style='text-align:center; color:white; font-family:Orbitron;'>🔐 CORE ACCESS</h1>", unsafe_allow_html=True)
    col_l, col_c, col_r = st.columns([1, 2, 1])
    with col_c:
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        pwd = st.text_input("Security Phrase (حديديها):", type="password")
        if st.button("ACTIVATE"):
            if pwd == "حديديها":
                st.session_state.logged_in = True
                st.rerun()
            else: st.error("ACCESS DENIED.")
        st.markdown("</div>", unsafe_allow_html=True)
else:
    st.markdown("<h1 style='text-align:center; color:white; font-family:Orbitron;'>🌾 SOVEREIGN OPERATIONS CENTER</h1>", unsafe_allow_html=True)
    c_main, c_chat = st.columns([2, 1])
    
    with c_main:
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        st.subheader("📊 إحصائيات الأصول")
        m1, m2, m3 = st.columns(3)
        m1.metric("Vault Status", "SECURE", "Mirage Active")
        m2.metric("Asset Value", "12.8 ETH", "+2%")
        m3.metric("Digital Plots", "1,240", "Ready")
        st.markdown("</div><br>", unsafe_allow_html=True)
        
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        st.subheader("📝 إصدار صك ملكية لزبون")
        name = st.text_input("اسم الزبون:")
        asset = st.selectbox("الأصل الرقمي:", ["NFT Land #442", "Simei Seed v1.2"])
        if st.button("إصدار وتشفير"):
            if name:
                pdf_data = generate_pdf(name, asset)
                b64 = base64.b64encode(pdf_data).decode()
                st.markdown(f'<a href="data:application/pdf;base64,{b64}" download="Deed_{name}.pdf"><button style="width:100%; padding:10px; background:green; color:white; border-radius:10px; border:none;">📥 تحميل الصك الموقع</button></a>', unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

    with c_chat:
        st.markdown("<div class='cyber-box' style='height: 500px;'>", unsafe_allow_html=True)
        st.markdown("### 🤖 مساعد جيمني الذكي")
        for m in st.session_state.messages:
            st.markdown(f"<div class='ai-bubble'>{m['content']}</div>", unsafe_allow_html=True)
        
        u_in = st.chat_input("تحدث مع الوكيل...")
        if u_in:
            st.session_state.messages.append({"role": "user", "content": u_in})
            with st.spinner("Processing..."):
                time.sleep(1)
                reply = f"تحليل جيمني لـ '{u_in}': العقود في وهران تحت السيطرة السيادية."
                st.session_state.messages.append({"role": "assistant", "content": reply})
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()
