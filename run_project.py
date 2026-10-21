"""
پروژه: تحلیل روند تقاضای زبان‌های برنامه‌نویسی در آگهی‌های استخدام
این اسکریپت کل فرایند را از صفر تا صد اجرا می‌کند.
"""

import subprocess
import sys
import time
import os

def run_step(title, cmd):
    print(f"\n{'='*70}")
    print(f"▶️  {title}")
    print(f"{'='*70}")
    start = time.time()
    try:
        subprocess.run(cmd, check=True)
        elapsed = time.time() - start
        print(f"✅ {title} در {elapsed:.1f} ثانیه تمام شد")
    except subprocess.CalledProcessError:
        print(f"❌ خطا در: {title}")
        sys.exit(1)

def main():
    print("🎓 شروع پروژه تحلیل روند تقاضای زبان‌های برنامه‌نویسی")
    print("=" * 70)
    
    # مرحله ۱: جمع‌آوری داده از چند کلمه کلیدی
    run_step(
        "مرحله ۱: جمع‌آوری داده از سایت جاب‌ویژن",
        [sys.executable, "collect_multiple.py"]
    )
    
    # مرحله ۲: ترکیب همه فایل‌ها
    run_step(
        "مرحله ۲: ترکیب داده‌ها و حذف تکراری‌ها",
        [sys.executable, "combine_all.py"]
    )
    
    # مرحله ۳: تحلیل نهایی و رسم نمودار
    run_step(
        "مرحله ۳: تحلیل زبان‌ها و رسم نمودار",
        [sys.executable, "final_analysis.py"]
    )
    
    # مرحله ۴: تحلیل روند زمانی (اگر فایلش وجود داشت)
    if os.path.exists("time_trend.py"):
        run_step(
            "مرحله ۴: تحلیل روند زمانی",
            [sys.executable, "time_trend.py"]
        )
    
    print("\n" + "=" * 70)
    print("🎉 پروژه با موفقیت به پایان رسید!")
    print("=" * 70)
    print("\n📂 خروجی‌ها در پوشه output:")
    print("  - ALL_JOBS_COMBINED.xlsx  (دیتاست کامل)")
    print("  - FINAL_ANALYSIS.xlsx     (تحلیل نهایی)")
    print("  - chart_languages.png     (نمودار زبان‌ها)")
    if os.path.exists("output/chart_time.png"):
        print("  - chart_time.png          (نمودار روند زمانی)")

if __name__ == "__main__":
    main()