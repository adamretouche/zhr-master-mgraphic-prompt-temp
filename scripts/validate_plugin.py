#!/usr/bin/env python3
import os
import json
import sys

PLUGIN_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def validate():
    print(f"🔍 Validating plugin at: {PLUGIN_DIR}")
    
    # 1. Check plugin.json
    pjson_path = os.path.join(PLUGIN_DIR, "plugin.json")
    if not os.path.exists(pjson_path):
        print("❌ Missing plugin.json")
        return False
    with open(pjson_path, "r", encoding="utf-8") as f:
        pdata = json.load(f)
    print(f"✅ Plugin manifest loaded: {pdata.get('displayName')} (v{pdata.get('version')})")
    
    # 2. Check master_prompts.json
    templates_path = os.path.join(PLUGIN_DIR, "templates", "master_prompts.json")
    if not os.path.exists(templates_path):
        print("❌ Missing templates/master_prompts.json")
        return False
    with open(templates_path, "r", encoding="utf-8") as f:
        tdata = json.load(f)
    print(f"✅ Master prompts JSON loaded: {len(tdata.get('archetypes', {}))} archetypes defined.")
    
    # 3. Check skills
    skills_dir = os.path.join(PLUGIN_DIR, "skills")
    expected_skills = [
        "skill-00-director",
        "skill-01-explainer",
        "skill-02-app-demo",
        "skill-03-kinetic-reel",
        "skill-04-cutaway"
    ]
    
    for s in expected_skills:
        skill_file = os.path.join(skills_dir, s, "SKILL.md")
        if not os.path.exists(skill_file):
            print(f"❌ Missing skill file: {skill_file}")
            return False
        with open(skill_file, "r", encoding="utf-8") as f:
            content = f.read()
            if "name:" not in content or "description:" not in content:
                print(f"❌ Skill {s} is missing frontmatter metadata.")
                return False
        print(f"✅ Skill verified: {s}")
        
    print("\n🎉 ALL PLUGIN VALIDATION CHECKS PASSED SUCCESSFULLY!")
    return True

if __name__ == "__main__":
    if not validate():
        sys.exit(1)
