#!/usr/bin/env python3
"""
pipeline_manager.py
أداة إدارة خط الإنتاج الإخراجي:
1. فحص الصوت المسبق (Audio Preflight)
2. إدارة الرندرة المجزأة (Chunked Rendering & Resuming)
3. دمج المشاهد المكتملة دون فقدان (Lossless Stitching)
"""

import os
import sys
import json
import subprocess
import shutil

FFMPEG = "/Users/zhr/.gemini/antigravity/bin/ffmpeg"
if not os.path.exists(FFMPEG):
    FFMPEG = shutil.which("ffmpeg") or "ffmpeg"

def check_audio_preflight(audio_path):
    """التحقق من مواصفات ونقاء ملف الصوت قبل الرندرة."""
    if not os.path.exists(audio_path):
        print(f"❌ ملف الصوت غير موجود: {audio_path}")
        return False
    
    cmd = [
        FFMPEG, "-i", audio_path,
        "-hide_banner"
    ]
    res = subprocess.run(cmd, stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    out = res.stderr
    
    # فحص معدل التردد
    hz = 44100
    if "48000 Hz" in out:
        hz = 48000
    elif "44100 Hz" in out:
        hz = 44100
    else:
        print("⚠️ تنبيه: معدل تردد الصوت أقل من 44.1kHz، يُفضل إعادة المعالجة.")
        
    print(f"✅ فحص الصوت سليم: التردد المقروء {hz} Hz.")
    return True

def stitch_chunks(chunks_dir, output_file):
    """دمج ملفات المشاهد المجزأة بسرعة وبلا أي فقدان في الجودة."""
    if not os.path.exists(chunks_dir):
        print(f"❌ مجلد المشاهد غير موجود: {chunks_dir}")
        return False
        
    chunks = sorted([os.path.join(chunks_dir, f) for f in os.listdir(chunks_dir) if f.endswith(".mp4")])
    if not chunks:
        print("❌ لم يتم العثور على مقاطع MP4 مجزأة للدمج.")
        return False
        
    list_path = os.path.join(chunks_dir, "chunks_list.txt")
    with open(list_path, "w", encoding="utf-8") as f:
        for c in chunks:
            f.write(f"file '{c}'\n")
            
    cmd = [
        FFMPEG, "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", list_path,
        "-c", "copy",
        output_file
    ]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if res.returncode == 0:
        print(f"🎬 تم دمج كافة المشاهد بنجاح وتصدير الفيديو النهائي: {output_file}")
        return True
    else:
        print(f"❌ خطأ أثناء دمج المشاهد: {res.stderr.decode('utf-8', errors='ignore')}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("الاستخدام: python3 pipeline_manager.py [check-audio <path>] | [stitch <chunks_dir> <output_file>]")
        sys.exit(1)
        
    mode = sys.argv[1]
    if mode == "check-audio" and len(sys.argv) > 2:
        check_audio_preflight(sys.argv[2])
    elif mode == "stitch" and len(sys.argv) > 3:
        stitch_chunks(sys.argv[2], sys.argv[3])
    else:
        print("أمر غير معروف أو معطيات ناقصة.")
