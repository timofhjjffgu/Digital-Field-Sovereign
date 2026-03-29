import streamlit as st
import pandas as pd
import random
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="الحقل الرقمي السيادي | وهران",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Custom CSS for Styling ---
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; }
    div[data-testid="stExpander"] { background-color: white; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.title("🌾 منصة الحقل الرقمي السيادي")
st.info("نظام متكامل لإدارة الأراضي والبذور الرقمية (NFT Farming & Metaverse)")
st.markdown("---")

# --- Key Metrics (Market Data) ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="إجمالي الأراضي", value="2,500 NFT", delta="محدودة")
with col2:
    st.metric(label="سعر الأرض الأدنى", value="0.45 ETH", delta="+2.3%")
with col3:
    st.metric(label="البذور المتاحة", value="12,340", delta="طلب مرتفع")
with col4:
    st.metric(label="قوة التشفير", value="95.5 MHz", delta="حماية كاملة")

# --- Sidebar (Mirage Vault) ---
with st.sidebar:
    st.header("🗄️ Mirage Vault")
    st.write("حالة الاتصال: **نشط**")
    st.success("تم تفعيل بروتوكول البلوك تشين")
    st.markdown("---")
    
    st.subheader("إحصائيات المحفظة")
    st.write("🔹 الرصيد: **12.4 ETH**")
    st.write("📍 الموقع: **وهران، الجزائر**")
    
    st.markdown("---")
    if st.button("تحديث البيانات"):
        with st.spinner('جاري مزامنة الأصول...'):
            time.sleep(1.5)
            st.rerun()

# --- Main Content Tabs ---
tab_land, tab_seeds, tab_harvest = st.tabs(["🗺️ سوق الأراضي", "🌱 مختبر البذور", "💰 تداول المحاصيل"])

with tab_land:
    st.subheader("الأراضي الرقمية المتاحة (Digital Land Plots)")
    st.write("اختر قطعة أرض لتملكها وتثبيت ملكيتك على الشبكة.")
    
    # Grid for Land Cards
    c1, c2 = st.columns(2)
    with c1:
        with st.expander("📍 قطعة أرض #442 (وهران)"):
            st.write("**النوع:** تربة سيميائية")
            st.write("**معدل الإنتاج:** 94%")
            st.button("شراء الآن", key="buy_1")
            
    with c2:
        with st.expander("📍 قطعة أرض #443 (القطاع البحري)"):
            st.write("**النوع:** مائية")
            st.write("**معدل الإنتاج:** 88%")
            st.button("شراء الآن", key="buy_2")

with tab_seeds:
    st.subheader("نظام البذور الإلكترونية (Digital Seeds)")
    seed_choice = st.selectbox("اختر البذرة المراد تطويرها:", ["قمح سيميائي", "نخيل مشفر", "بذور الطاقة"])
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        st.write("🧬 **الخصائص الجينية:**")
        st.write("- النُدرة: **عالية**")
        st.write("- وقت النمو: **3 أيام**")
    with col_b:
        st.write("📊 **إحصائيات النمو المتوقع:**")
        val = random.randint(60, 90)
        st.progress(val, text=f"كفاءة الامتصاص الرقمي: {val}%")
        if st.button("بدء الزراعة في الحقل"):
            st.toast("جاري نقل البذرة إلى الأرض المختارة...")

with tab_harvest:
    st.subheader("سوق المحاصيل والـ NFTs")
    st.write("قائمة بآخر المحاصيل التي تم حصادها وجاهزة للبيع:")
    
    harvest_data = {
        "المحصول": ["قمح ذهبي", "تمور مشفرة", "زيت سيبراني"],
        "الكمية": ["500 كجم", "200 كجم", "150 لتر"],
        "السعر (ETH)": [0.02, 0.05, 0.03]
    }
    df = pd.DataFrame(harvest_data)
    st.dataframe(df, use_container_width=True)

# --- Footer ---
st.markdown("---")
st.markdown("<h4 style='text-align: center;'>هذه البيانات ملكية فكرية مستقلة تحت إدارة رنينك الذري</h4>", unsafe_allow_html=True)
st.caption("نظام الحقل الرقمي السيادي - الإصدار 1.0.0")
