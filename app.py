import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import os

# تنظیمات صفحه
st.set_page_config(page_title="تحلیل زبان‌های برنامه‌نویسی", page_icon="💻", layout="wide")

# عنوان
st.title("💻 تحلیل روند تقاضای زبان‌های برنامه‌نویسی")
st.markdown("این داشبورد بر اساس داده‌های استخراج‌شده از سایت **جاب‌ویژن** ساخته شده است.")

# خواندن دیتاست
@st.cache_data
def load_data():
    return pd.read_excel("output/FINAL_ANALYSIS.xlsx")

try:
    df = load_data()
except FileNotFoundError:
    st.error("❌ فایل FINAL_ANALYSIS.xlsx پیدا نشد. لطفاً اول پروژه را اجرا کنید.")
    st.stop()

# ===== سایدبار =====
st.sidebar.header("🔍 جستجو و فیلتر")

# جستجوی زبان
all_languages = [
    "Python", "Java", "JavaScript", "TypeScript", "C#", "C++",
    "PHP", "Go", "Rust", "Kotlin", "Swift", "Ruby", "Scala", "Dart", "SQL"
]
selected_lang = st.sidebar.selectbox("یک زبان برنامه‌نویسی انتخاب کنید:", ["همه زبان‌ها"] + all_languages)

# جستجوی متنی
search_text = st.sidebar.text_input("جستجو در عنوان شغل یا شرکت:", "")

# ===== بخش اصلی =====

# آمار کلی
col1, col2, col3 = st.columns(3)
col1.metric("📊 کل آگهی‌ها", len(df))
col2.metric("🏢 شرکت‌های متمایز", df["شرکت"].nunique())
col3.metric("🌐 زبان‌های شناسایی‌شده", len(all_languages))

st.divider()

# اگر زبان خاصی انتخاب شد
if selected_lang != "همه زبان‌ها":
    st.subheader(f"📈 محبوبیت زبان {selected_lang}")
    
    # فیلتر آگهی‌هایی که این زبان رو دارن
    mask = df["زبان‌های پیدا شده"].str.contains(selected_lang, na=False)
    filtered = df[mask]
    
    pct = len(filtered) / len(df) * 100
    
    col1, col2 = st.columns(2)
    col1.metric(f"تعداد آگهی‌های دارای {selected_lang}", len(filtered))
    col2.metric("درصد از کل آگهی‌ها", f"{pct:.1f}%")
    
    # نمودار دایره‌ای
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.pie(
        [len(filtered), len(df) - len(filtered)],
        labels=[f"دارای {selected_lang}", f"بدون {selected_lang}"],
        autopct="%1.1f%%",
        colors=["#4CAF50", "#E0E0E0"],
        startangle=90
    )
    ax.set_title(f"سهم زبان {selected_lang} در آگهی‌های استخدامی")
    st.pyplot(fig)
    
    # جدول آگهی‌ها
    st.subheader(f"📋 آگهی‌های استخدامی دارای {selected_lang}")
    st.dataframe(
        filtered[["عنوان", "شرکت", "تاریخ انتشار", "زبان‌های پیدا شده"]].head(20),
        use_container_width=True
    )

else:
    # حالت کلی: نمودار همه زبان‌ها
    st.subheader("📊 پرتکرارترین زبان‌های برنامه‌نویسی")
    
    all_langs = []
    for langs_str in df["زبان‌های پیدا شده"]:
        if pd.notna(langs_str) and langs_str != "—":
            all_langs.extend(langs_str.split(", "))
    
    counts = Counter(all_langs)
    
    if counts:
        langs = [l for l, c in counts.most_common()]
        vals = [c for l, c in counts.most_common()]
        
        fig, ax = plt.subplots(figsize=(12, 6))
        bars = ax.bar(langs, vals, color="steelblue")
        ax.set_title("تعداد آگهی‌های استخدامی که هر زبان را ذکر کرده‌اند", fontsize=14)
        ax.set_xlabel("زبان برنامه‌نویسی")
        ax.set_ylabel("تعداد آگهی")
        plt.xticks(rotation=45, ha="right")
        for bar, val in zip(bars, vals):
            ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.3,
                    str(val), ha="center", va="bottom")
        plt.tight_layout()
        st.pyplot(fig)

# ===== جستجوی متنی =====
if search_text:
    st.divider()
    st.subheader(f"🔍 نتایج جستجو برای: «{search_text}»")
    
    mask = (
        df["عنوان"].astype(str).str.contains(search_text, case=False, na=False) |
        df["شرکت"].astype(str).str.contains(search_text, case=False, na=False)
    )
    search_results = df[mask]
    
    st.write(f"تعداد نتایج: **{len(search_results)}** آگهی")
    
    if len(search_results) > 0:
        st.dataframe(
            search_results[["عنوان", "شرکت", "تاریخ انتشار", "زبان‌های پیدا شده"]],
            use_container_width=True
        )
    else:
        st.info("هیچ آگهی‌ای با این عبارت پیدا نشد.")

# ===== فوتر =====
st.divider()
st.caption("📌 داده‌ها از سایت جاب‌ویژن (jobvision.ir) استخراج شده‌اند | پروژه وب اسکرپینگ ارشد")