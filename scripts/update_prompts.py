#!/usr/bin/env python3
"""
update_prompts.py
سكريبت لتحديث أو إضافة أنماط إخراجية جديدة إلى المنظومة برمجياً.
يقرأ ملف templates/master_prompts.json ويضمن تزامن السكلز.
"""
import os
import json

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROMPTS_JSON = os.path.join(PLUGIN_DIR, "templates", "master_prompts.json")

def load_prompts():
    with open(PROMPTS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def save_prompts(data):
    with open(PROMPTS_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✅ Prompts database updated at {PROMPTS_JSON}")

if __name__ == "__main__":
    data = load_prompts()
    print(f"Current version: {data.get('version')}")
    print(f"Archetypes registered: {list(data.get('archetypes', {}).keys())}")
