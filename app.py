import streamlit as st
import pandas as pd
import random
import time

# --- Page Config ---
st.set_page_config(page_title="الحقل الرقمي | وهران", page_icon="🌾", layout="wide")

# --- UI Styling ---
st.markdown("""<style>.main { background-color: #f7f9fc; } .stMetric { background-color: white; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; }</style>""", unsafe_allow_html=True)

st.title("🌾 منصة الحقل الرقمي السيادي")
st.info("نظام الزراعة الافتراضية المستقبلي - وهران، الجزائر")

# --- Visual Mockup ---
st.image("https://images.unsplash.com/photo-1558449028-b53a39d100fc?auto=format&fit=crop&q=80&w=1000", use_container_width=True, caption="محاكاة الحقل الرقمي السيادي: تقنيات البلوك تشين تلتقي بالزراعة")

# --- Metrics ---
c1, c2, c3 = st.columns(3)
c1.metric("الأراضي الرقمية", "1,240 NFT", "+5%")
c2.metric("سعر ETH الحالي", "3,200$", "+1.2%")
c3.metric("قوة Mirage Vault", "99.9%", "حماية قصوى")

# --- Sidebar ---
with st.sidebar:
    st.header("🗄️ Mirage Vault")
    st.success("البروتوكول نشط")
    st.write("🔹 الرصيد: **12.4 ETH**")
    st.write("📍 الموقع: **وهران**")

# --- Tabs ---
t1, t2 = st.tabs(["🗺️ سوق الأراضي", "🌱 المختبر"])
with t1:
    st.subheader("قطع الأراضي NFT")
    st.write("الأراضي المتاحة في قطاع وهران الشرقي.")
    if st.button("شراء قطعة أرض رقمية"):
        st.balloons()
        st.success("تم تسجيل الطلب في البلوك تشين!")

with t2:
    st.subheader("تطوير البذور")
    st.slider("معدل النمو الرقمي", 0, 100, 75)
    st.button("تخصيب البذرة السيميائية")

st.markdown("---")
st.caption("حقوق الملكية الفكرية محفوظة لـ عبد الخالق © 2026")
