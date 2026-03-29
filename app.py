import streamlit as st
import time
import random
from fpdf import FPDF
import base64

# --- إعدادات الصفحة والهوية ---
st.set_page_config(page_title="Sovereign Core v3", page_icon="🌾", layout="wide")

# --- دمج صورة الخلفية (الماتريكس الزراعية) ---
# رابط الصورة التي قمنا بتوليدها
IMG_URL = "https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png"

st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Cairo:wght@400;700&display=swap');
    
    /* خلفية الماتريكس المتحركة */
    .stApp {{
        background-image: url("{IMG_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* تنسيق العناصر العائمة */
    .stApp > header {{ display: none; }}
    .main {{ background-color: rgba(5, 5, 5, 0.6); color: white; font-family: 'Cairo', sans-serif; }}
    
    /* تصميم Cyberpunk الاحترافي */
    .cyber-box {{ 
        background: rgba(10, 10, 30, 0.7); 
        border: 1px solid #7000ff; 
        padding: 20px; 
        border-radius: 15px; 
        box-shadow: 0 0 15px rgba(112, 0, 255, 0.5);
        backdrop-filter: blur(5px);
    }}
    
    .stMetric {{ color: #00f2ff; }}
    
    /* تنسيق الدردشة الـ AI */
    .chat-box {{ background: rgba(0, 0, 0, 0.8); border: 1px solid #bc13fe; padding: 10px; border-radius: 10px; margin-bottom: 5px; }}
    .user-msg {{ color: #00f2ff; }}
    .ai-msg {{ color: #bc13fe; font-weight: bold; }}
    
    /* أزرار Cyber Buttons */
    .stButton>button {{ width: 100%; border-radius: 20px; background: linear-gradient(45deg, #7000ff, #00f2ff); color: white; border: none; transition: 0.3s; font-family: 'Orbitron', sans-serif;}}
    .stButton>button:hover {{ transform: scale(1.03); box-shadow: 0 0 25px #00f2ff; }}
    
    /* العناوين السيادية */
    h1 {{ text-shadow: 0 0 15px #7000ff; color: #ffffff; text-align: center; font-family: 'Orbitron', sans-serif; }}
</style>
""", unsafe_allow_html=True)

# --- نظام الجلسة ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- بوابة الدخول السيادية (Security Layer) ---
if not st.session_state.logged_in:
    st.markdown("<h1>🌾 SOVEREIGN ACCESS GATE</h1>", unsafe_allow_html=True)
    st.markdown("<div class='cyber-box' style='width: 50%; margin: auto; text-align: center;'>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pwd = st.text_input("ENTER COMMAND (حديديها):", type="password")
        if st.button("ACTIVATE CORE"):
            if pwd == "حديديها":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("INTERFERENCE DETECTED. ACCESS DENIED.")
    st.markdown("</div>", unsafe_allow_html=True)
else:
    # --- الواجهة الرئيسية (The Cyber Core) ---
    st.markdown("<h1>🔮 NUCLEAR OPERATIONS CENTER | ABD AL-KHALIQ</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='text-align: center; color: #bc13fe;'>نظام الماتريكس الزراعية - وهران 2026</h4>", unsafe_allow_html=True)
    
    st.write("---")
    
    col_metrics, col_chat = st.columns([2, 1])
    
    with col_metrics:
        # قسم الإحصائيات في Cyber Boxes
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        st.subheader("🌐 أصول الحقل الرقمي")
        m1, m2, m3 = st.columns(3)
        m1.metric("Status", "ENCRYPTED", "99.9%")
        m2.metric("Semiotic ETH", "12.4", "+1.2%")
        m3.metric("AI Agents", "Active", "v3.1")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.write("---")
        
        # قسم إصدار الشهادات
        with st.expander("📝 صكوك الملكية الرقمية (NFT Certificates)"):
            c_name = st.text_input("اسم المستثمر الجديد:")
            c_type = st.selectbox("نوع الأصل:", ["NFT Land Oran #442", "Simei Seed v1.2"])
            if st.button("توليد العقد المشفر"):
                st.success(f"تم توليد العقد للأخ {c_name} بنجاح!")
    
    with col_chat:
        st.markdown("<div class='cyber-box'>", unsafe_allow_html=True)
        st.markdown("### 🤖 مساعد جيمني (AI Chatbot)")
        
        # عرض الرسائل
        for msg in st.session_state.messages:
            role = "ai-msg" if msg["role"] == "assistant" else "user-msg"
            st.markdown(f'<div class="chat-box"><span class="{role}">{msg["content"]}</span></div>', unsafe_allow_html=True)
            
        user_input = st.chat_input("اسأل الوكيل عن الأراضي...")
        if user_input:
            st.session_state.messages.append({"role": "user", "content": user_input})
            # رد الذكاء الاصطناعي (محاكاة جيمني)
            with st.spinner("تفكير سيادي..."):
                time.sleep(1)
                ai_reply = f"تحليل بيانات جيمني لـ '{user_input}': الأراضي في وهران مستقرة وتحت حماية Mirage Vault."
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    # --- التذييل السيادي ---
    st.sidebar.markdown("### 🛡️ Mirage Control")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()
    st.sidebar.caption("حقوق الملكية لـ عبد الخالق © 2026")
