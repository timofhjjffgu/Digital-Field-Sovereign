import streamlit as st
import pandas as pd
import random
import time

# --- إعدادات الصفحة الاحترافية ---
st.set_page_config(
    page_title="الحقل الرقمي السيادي | وهران",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- تنسيق CSS مخصص لتحسين المظهر ---
st.markdown("""
    <style>
    .main { background-color: #f7f9fc; }
    .stMetric { background-color: #ffffff; padding: 20px; border-radius: 12px; border: 1px solid #e0e0e0; box-shadow: 0 4px 6px rgba(0,0,0,0.02); }
    div[data-testid="stExpander"] { background-color: white; border-radius: 10px; border: 1px solid #e0e0e0;}
    .css-1avcm0n {font-weight: bold;}
    .land-card { border: 1px solid #e0e0e0; padding: 15px; border-radius: 10px; background-color: white; margin-bottom: 20px;}
    .seed-card { text-align: center; border: 2px solid #57ca85; padding: 10px; border-radius: 8px; background-color: #e8f7ee; }
    </style>
    """, unsafe_allow_html=True)

# --- القسم الرئيسي: العنوان والشعار الفني ---
st.title("🌾 منصة الحقل الرقمي السيادي | وهران")
st.markdown("##### نموذج أولي للزراعة الافتراضية السيبرانية (Cybergpoyonics) على البلوك تشين")
st.markdown("---")

# --- محاكاة مرئية خارج الصندوق: "شاشة التحكم في البيئة" ---
# هذه الصورة هي "محاكاة" للمزرعة من منظور طائرة بدون طيار
st.image("https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png", use_container_width=True, caption="محاكاة بانورامية: منظور طائرة بدون طيار فوق الحقل الرقمي في وهران (التربة السيميائية المضاءة بالليزر) - تم عرض الأصول الرقمية المربوطة")

# --- القسم الأول: إحصائيات السوق الرقمي الحية ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="الأراضي المباعة (NFT Land)", value="1,240", delta="+12 NFT (24h)")
with col2:
    st.metric(label="سعر الأرض الأدنى (Floor Price)", value="0.75 ETH", delta="+8%")
with col3:
    st.metric(label="البذور النشطة (Cyber-Seeds)", value="8,500", delta="طلب مرتفع")
with col4:
    st.metric(label="قوة حماية Mirage Vault", value="95.5 MHz", delta="كاملة")

# --- شريط جانبي لنظام Mirage Vault (محدث) ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/2092/2092663.png", width=80)
    st.header("🗄️ Mirage Vault")
    st.info("🔓 تم تفعيل بروتوكول البلوك تشين - الجزائر")
    
    st.write("---")
    st.subheader("إحصائيات محفظتك")
    st.write("🔹 الرصيد الحالي: **12.4 ETH**")
    st.write("📍 الموقع المرتبط: **وهران، الجزائر**")
    st.write("🚜 الأصول الخاصة: **3 قطع أراضي / 20 بذرة**")
    
    st.markdown("---")
    if st.button("تحديث بيانات الشبكة"):
        with st.spinner('جاري مزامنة العوالم السيميائية...'):
            time.sleep(2)
            st.rerun()

# --- القسم الثاني: إدارة الأصول (Tabs) مع صور المحاكاة ---
tab_land, tab_seeds, tab_market = st.tabs(["🗺️ سوق الأراضي (NFT Land)", "🌱 مختبر البذور الإلكترونية", "🛒 تداول المحاصيل"])

with tab_land:
    st.subheader("إدارة قطع الأراضي الرقمية المتاحة")
    st.write("اختر قطعة أرض لتملكها وتثبيت ملكيتك على الشبكة السيميائية.")
    
    # Grid for Land Cards
    c1, c2 = st.columns(2)
    with c1:
        # محاكاة صورة قطعة الأرض #442 (سيميائية)
        st.markdown('<div class="land-card">', unsafe_allow_html=True)
        st.image("https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png", caption="📍 محاكاة قطعة #442 (تربة سيميائية مضاءة) - وهران", width=350)
        st.write("---")
        with st.expander("📍 تفاصيل قطعة #442"):
            st.write("**النوع:** تربة سيميائية")
            st.write("**معدل الإنتاج:** 98%")
            st.write("**المالك الحالي:** 0x71...f92 (أنت)")
        if st.button("عرض شهادة الملكية (NFT)"):
            st.warning("جاري الاتصال بالعقد الذكي `0xabc123...`")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        # محاكاة صورة قطعة الأرض #443 (مائية)
        st.markdown('<div class="land-card">', unsafe_allow_html=True)
        st.image("https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png", caption="📍 محاكاة قطعة #443 (مائية سيبرانية مضاءة) - القطاع البحري", width=350)
        st.write("---")
        with st.expander("📍 تفاصيل قطعة #443"):
            st.write("**النوع:** مائية سيبرانية")
            st.write("**معدل الإنتاج:** 88%")
            st.write("**المالك الحالي:** 0x82...a1c")
        st.button("شراء الآن", key="buy_2")
        st.markdown('</div>', unsafe_allow_html=True)

with tab_seeds:
    st.subheader("مختبر البذور الإلكترونية (Digital Seeds Lab)")
    st.write("اختر نوع البذرة المربوطة لزرعها على أرضك.")
    
    col_a, col_b = st.columns([1, 2])
    with col_a:
        # محاكاة صورة البذرة السيبرانية المضاءة
        st.markdown('<div class="seed-card">', unsafe_allow_html=True)
        st.image("https://replicate.delivery/pbxt/P2W1qf1oH3h3G0pU7iJ1R9K1b5pG7nU6f4C3G2k3B5w4A6D5A/output_1.png", caption="🌱 بذرة القمح السيبرانية (مضاءة بالنيون)", width=200)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_b:
        seed_type = st.selectbox("اختر البذرة المراد تطويرها:", ["قمح سيميائي", "نخيل مشفر", "بذور الطاقة"])
        st.write(f"🧬 **خصائص جينية متقدمة لـ {seed_type}:**")
        val = random.randint(60, 95)
        st.progress(val, text=f"كفاءة الامتصاص الرقمي: {val}%")
        st.write(f"- مستوى النُدرة: **عالية (Rare)**")
        st.write(f"- وقت النمو المتوقع: **3 أيام**")
        if st.button("بدء عملية الزراعة (Stake Seed)"):
            st.toast("جاري تأكيد المعاملة على البلوك تشين...")

with tab_harvest:
    st.subheader("سوق المحاصيل والـ NFTs")
    st.write("قائمة بآخر المحاصيل الرقمية التي تم حصادها وجاهزة للبيع كـ NFTs:")
    
    harvest_data = {
        "المحصول Digital Harvest": ["قمح ذهبي سيميائي", "تمور مشفرة وهرانية", "رحيق مشفر طاقة"],
        "الكمية": ["500 وحدة", "200 وحدة", "150 وحدة"],
        "السعر (ETH)": [0.02, 0.05, 0.03]
    }
    df = pd.DataFrame(harvest_data)
    st.dataframe(df, use_container_width=True)

# --- التذييل الإبداعي (Footer) ---
st.markdown("---")
st.markdown("<h4 style='text-align: center; color: #57ca85;'>تكنولوجيا المستقبل - الجزائرية المستقلة لإدارة الأصول الرقمية</h4>", unsafe_allow_html=True)
st.caption("نظام الحقل الرقمي السيادي - الإصدار 2.0.0 | تم تطويره وتكييفه تحت إدارة رنينك الذري")
