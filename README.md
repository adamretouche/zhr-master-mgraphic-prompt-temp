# ZHR MASTER M.GRAPHIC PROMPT TEMP

منظومة موحدة لهندسة وإخراج مشاريع الموشن جرافيك فائقة التطور (60 FPS) مدعومة بخمس مهارات إخراجية تفاعلية تتولى استخراج المعطيات، التنسيق البصري، وتأكيد المخرجات قبل التنفيذ.

---

## 📖 دليل الاستخدام والتثبيت المفصل (Usage & Installation Guide)
للاطلاع على دليل الاستخدام الكامل خطوة بخطوة وكيفية استدعاء السكلز وسيناريوهات العمل:
👉 **[اقرأ دليل الاستخدام التفصيلي (USAGE_GUIDE.md)](USAGE_GUIDE.md)**

---

## 🚀 التثبيت والمشاركة السريعة (Quick Install & Sharing)

لتثبيت هذا البلاجن مع كافة سكلز الموشن جرافيك على أي جهاز كمبيوتر مباشرة عبر الطرفية:

```bash
git clone https://github.com/adamretouche/zhr-master-mgraphic-prompt-temp.git ~/.gemini/config/plugins/zhr-master-mgraphic-prompt-temp
```

أو عبر تنزيل المستودع كملف مضغوط `ZIP` من الواجهة مباشرة ووضعه في مسار الإضافات `~/.gemini/config/plugins/`.

---

## 🏛️ الركائز التشغيلية الثلاث المعتمدة (The 3 Core Operational Pillars)

1. **الصرامة المطلقة في نقطة الاعتماد (Strict Approval Gate 🛑):**
   - حظر قاطع لتوليد كود الرندرة أو بدء المعالجة قبل تسليم ملخص إخراجي للمشاهد وعرض لوحة المعاينة الأولية (*Contact Sheet*) وتلقي موافقة صريحة من العميل.
2. **بروتوكول الارتباط البصري وجودة الصوت (Audio-Visual Alignment & Preflight):**
   - التحقق المسبق من تردد الصوت (44.1kHz / 48kHz)، عزل السكتات والضوضاء، وربط حركات الكشيدة الحركية وانتقالات الكاميرا بالمللي ثانية مع نبرات الصوت ونبضات الإيقاع.
3. **معمارية الرندرة المجزأة والمستأنفة (Chunked & Resumable Rendering Engine):**
   - رندرة المشاهد كقطع مستقلة (`scene_01.mp4`, `scene_02.mp4`...)؛ لتسريع المعالجة، تفادي انهيار الذاكرة، وإتاحة إعادة رندرة المشهد المعدل فقط دون المساس بباقي المشروع، مع الدمج النهائي الفوري عبر FFmpeg بلا فقدان.

---

## 📦 هيكلية البلاجن (Plugin Structure)

```text
zhr-master-mgraphic-prompt-temp/
├── plugin.json                              # بيان تعريف البلاجن
├── README.md                                # الوثيقة التعريفية السريعة
├── USAGE_GUIDE.md                           # دليل الاستخدام والتثبيت والمشاركة الشامل
├── rules/
│   └── MOTION_RULES.md                      # القواعد الإخراجية الصارمة والركائز الثلاث
├── templates/
│   ├── master_prompts.json                  # قاعدة بيانات البرومبتات والأسئلة (قابلة للتحديث)
│   ├── shared_directives.md                 # معايير الرندرة المجزأة والتايبوغرافي العربي
│   └── Master_Motion_Graphics_Prompts.docx  # مرجع الوورد المنسق والملون
├── scripts/
│   ├── validate_plugin.py                   # أداة فحص صحة وتكامل البلاجن
│   ├── update_prompts.py                    # أداة التحديث البرمجي للبرومبتات
│   └── pipeline_manager.py                  # أداة فحص الصوت ودمج المشاهد المجزأة
└── skills/
    ├── skill-00-director/SKILL.md           # ZHR MASTER PROMPT SKILL 00: Creative Director
    ├── skill-01-explainer/SKILL.md          # ZHR MASTER PROMPT SKILL 01: Educational & Explainer
    ├── skill-02-app-demo/SKILL.md           # ZHR MASTER PROMPT SKILL 02: 3D Devices & App Demo
    ├── skill-03-kinetic-reel/SKILL.md       # ZHR MASTER PROMPT SKILL 03: Kinetic Reel & Collage
    └── skill-04-cutaway/SKILL.md            # ZHR MASTER PROMPT SKILL 04: Mechanical Cutaway
```

---

## ⚡ المهارات المتضمنة (Included Skills)

1. **`ZHR MASTER PROMPT SKILL 00: Creative Director`**: الموجه العام للمشاريع وتحديد المسار الإخراجي الأنسب.
2. **`ZHR MASTER PROMPT SKILL 01: Educational & Explainer`**: شروحات وثائقية تقنية ورسوم بيانية Dark Tech.
3. **`ZHR MASTER PROMPT SKILL 02: 3D Devices & App Demo`**: استعراض التطبيقات والمواقع داخل أجهزة أبل 3D.
4. **`ZHR MASTER PROMPT SKILL 03: Kinetic Reel & Collage`**: إعلانات وريلز سريعة بنمط الكولاج وتفريغ العناصر مع تزامن ضربات SFX.
5. **`ZHR MASTER PROMPT SKILL 04: Mechanical Cutaway`**: تشريح ميكانيكي ثلاثي الأبعاد للأجهزة والآلات كنموذج مقطوع حركياً.
