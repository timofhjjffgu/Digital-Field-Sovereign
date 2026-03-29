import streamlit as st
import time
import random
from fpdf import FPDF
import base64

# --- إعدادات الهوية السيادية ---
st.set_page_config(page_title="Sovereign Core v3", page_icon="🔮", layout="wide")

# --- تصميم واجهة Cyberpunk الاحترافية ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&display=swap');
    
    .main { background-color: #050505; color: #00f2ff; font-family: 'Orbitron', sans-serif; }
    .stApp { background: radial-gradient(circle, #0f0c29, #302b63, #24243e); }
    
    /* Custom AI Chat Box */
    .chat-box { background: rgba(0, 0, 0, 0.7); border: 1px solid #7000ff; padding: 15px; border-radius: 15px; margin-bottom: 10px; }
    .user-msg { color: #00f2ff; }
    .ai-msg { color: #bc13fe; font-weight: bold; }
    
    /* Buttons Customization */
    .stButton>button { width: 100%; border-radius: 20px; background: linear-gradient(45deg, #7000ff, #00f2ff); color: white; border: none; transition: 0.3s; }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 20px #7000ff; }
    
    /* Title Styling */
    h1 { text-shadow: 2px 2px 10px #7000ff; color: #ffffff; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- نظام الجلسة ---
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

# --- بوابة الدخول (Security Layer) ---
if not st.session_state.logged_in:
    st.markdown("<h1>🔒 SOVEREIGN ACCESS GATE</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        pwd = st.text_input("ENTER COMMAND (حديديها):", type="password")
        if st.button("EXECUTE"):
            if pwd == "حديديها":
                st.session_state.logged_in = True
                st.rerun()
            else:
                st.error("INTERFERENCE DETECTED. ACCESS DENIED.")
else:
    # --- الواجهة الرئيسية (The Core) ---
    st.markdown("<h1>🌾 NUCLEAR OPERATIONS CENTER | ABD AL-KHALIQ</h1>", unsafe_allow_html=True)
    
    col_main, col_chat = st.columns([2, 1])
    
    with col_main:
        st.subheader("📊 أصول الحقل الرقمي - وهران")
        m1, m2, m3 = st.columns(3)
        m1.metric("Status", "ENCRYPTED", "99.9%")
        m2.metric("Market ETH", "12.4", "+1.2%")
        m3.metric("AI Agents", "Active", "v3.0")
        
        st.write("---")
        # قسم إصدار الشهادات بشكل منمق
        with st.expander("📝 صكوك الملكية الرقمية (NFT Certificates)"):
            c_name = st.text_input("اسم المستثمر الجديد:")
            c_type = st.selectbox("نوع الأصل:", ["NFT Land Oran", "Semiotic Energy Seed"])
            if st.button("إصدار وتشفير الشهادة"):
                st.success(f"تم توليد العقد للأخ {c_name} بنجاح!")
                # هنا نضع زر التحميل كما فعلنا سابقاً
    
    with col_chat:
        st.markdown("### 🤖 مساعد جيمني الذكي (AI Agent)")
        st.write("الوكيل يرد على الزبائن تلقائياً...")
        
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
                responses = [
                    "أهلاً بك في حقل عبد الخالق الرقمي. الأراضي في وهران مستقرة حالياً.",
                    "بناءً على تحليلي للضوضاء، هذا هو الوقت المثالي للاستثمار في NFT Land #442.",
                    "نحن نستخدم بروتوكولات تشفير Mirage Vault لحماية أصولك."
                ]
                ai_reply = random.choice(responses)
                st.session_state.messages.append({"role": "assistant", "content": ai_reply})
                st.rerun()

    st.sidebar.markdown("### 🛡️ Mirage Control")
    if st.sidebar.button("LOGOUT"):
        st.session_state.logged_in = False
        st.rerun()
