/* Grammar path: clear International English for Chinese- and Thai-speaking learners. */
window.GRAMMAR = [
  {
    id: "b1", level: "basic", icon: "●",
    title: { zh: "be 动词：am / is / are", en: "The verb be: am / is / are", th: "คำกริยา be: am / is / are" },
    rule: { zh: "说身份、状态、地点时，英文句子不能漏掉 be 动词。", en: "Use be for identity, condition, and location. Do not leave it out.", th: "ใช้ be เมื่อบอกตัวตน สภาพ หรือสถานที่ ห้ามละคำกริยา be" },
    formula: "I am · You/We/They are · He/She/It is",
    example: "She is busy today.",
    meaning: { zh: "她今天很忙。", en: "She is in a busy state today.", th: "วันนี้เธอยุ่ง" },
    my: { zh: "中文可以说“她今天很忙”，英文必须加 is。", en: "Chinese may omit be before an adjective; English needs is here.", th: "ภาษาจีนอาจละ be หน้าคำคุณศัพท์ แต่ภาษาอังกฤษต้องมี is" },
    thai: { zh: "泰语说“วันนี้เธอยุ่ง”不需要 be；英文必须说 She is busy。", en: "Thai does not need be in วันนี้เธอยุ่ง; English requires She is busy.", th: "ภาษาไทยพูดว่า “วันนี้เธอยุ่ง” ได้โดยไม่ต้องมี be แต่ภาษาอังกฤษต้องพูด She is busy" }
  },
  {
    id: "b2", level: "basic", icon: "↻",
    title: { zh: "一般现在时：习惯与事实", en: "Present simple: habits and facts", th: "Present simple: นิสัยและข้อเท็จจริง" },
    rule: { zh: "日常习惯和长期事实用一般现在时；he / she / it 后面的动词通常加 -s。", en: "Use the present simple for habits and facts. Usually add -s after he, she, or it.", th: "ใช้ present simple กับนิสัยและข้อเท็จจริง โดยทั่วไปเติม -s หลัง he, she และ it" },
    formula: "I/You/We/They work · He/She works",
    example: "He teaches coffee classes every week.",
    meaning: { zh: "他每星期教授咖啡课程。", en: "This is his regular weekly activity.", th: "เขาสอนคลาสกาแฟทุกสัปดาห์" },
    my: { zh: "别忘记第三人称 -s：He work ✕ → He works ✓。", en: "Remember third-person -s: He work ✕ → He works ✓.", th: "อย่าลืม -s สำหรับประธานบุรุษที่สาม: He work ✕ → He works ✓" },
    thai: { zh: "泰语动词不会随主语变化；英文 he / she / it 要特别检查 -s。", en: "Thai verbs do not change with the subject; check -s after he, she, and it.", th: "กริยาไทยไม่เปลี่ยนตามประธาน แต่ภาษาอังกฤษต้องตรวจ -s หลัง he, she และ it" }
  },
  {
    id: "b3", level: "basic", icon: "←",
    title: { zh: "一般过去时：已经结束的事", en: "Past simple: finished events", th: "Past simple: เหตุการณ์ที่จบแล้ว" },
    rule: { zh: "有 yesterday、last week 或明确过去时间时，用过去式。", en: "Use the past form with a finished time such as yesterday or last week.", th: "ใช้รูปอดีตเมื่อมีเวลาที่จบแล้ว เช่น yesterday หรือ last week" },
    formula: "regular: work → worked · irregular: go → went",
    example: "We met the supplier yesterday.",
    meaning: { zh: "我们昨天见了供应商。", en: "The meeting happened and finished yesterday.", th: "เราเจอซัพพลายเออร์เมื่อวาน" },
    my: { zh: "口语里别让时间词代替时态：Yesterday we meet ✕ → met ✓。", en: "Do not let the time word replace the tense: Yesterday we meet ✕ → met ✓.", th: "อย่าใช้คำบอกเวลาแทน tense: Yesterday we meet ✕ → met ✓" },
    thai: { zh: "泰语靠“เมื่อวาน”表达过去，动词不变；英文动词仍要改成 met。", en: "Thai marks the past with เมื่อวาน without changing the verb; English still changes meet to met.", th: "ภาษาไทยใช้ “เมื่อวาน” โดยกริยาไม่เปลี่ยน แต่ภาษาอังกฤษต้องเปลี่ยน meet เป็น met" }
  },
  {
    id: "b4", level: "basic", icon: "?",
    title: { zh: "问题句：do / does / did", en: "Questions with do / does / did", th: "ประโยคคำถามด้วย do / does / did" },
    rule: { zh: "一般动词的问题把 do / does / did 放在主语前，后面的动词回到原形。", en: "Put do, does, or did before the subject. The main verb returns to its base form.", th: "วาง do, does หรือ did หน้าประธาน และใช้กริยาหลักรูปเดิม" },
    formula: "Do you work…? · Does she work…? · Did they work…?",
    example: "Did you receive my email?",
    meaning: { zh: "你收到我的邮件了吗？", en: "A question about a finished past action.", th: "คุณได้รับอีเมลของฉันไหม" },
    my: { zh: "用了 did 后不要再用过去式：Did you received ✕ → Did you receive ✓。", en: "After did, do not use the past form again: Did you received ✕ → receive ✓.", th: "หลัง did ห้ามใช้กริยารูปอดีตซ้ำ: Did you received ✕ → receive ✓" },
    thai: { zh: "泰语常在句尾加“ไหม”；英文要把助动词放到句首。", en: "Thai often adds ไหม at the end; English moves the helper verb to the front.", th: "ภาษาไทยมักเติม “ไหม” ท้ายประโยค แต่ภาษาอังกฤษต้องวางกริยาช่วยไว้ข้างหน้า" }
  },
  {
    id: "b5", level: "basic", icon: "A",
    title: { zh: "冠词：a / an / the", en: "Articles: a / an / the", th: "คำนำหน้านาม: a / an / the" },
    rule: { zh: "第一次提到一个可数事物用 a / an；双方都知道是哪一个时用 the。", en: "Use a or an for one new countable thing; use the when both people know which one.", th: "ใช้ a หรือ an เมื่อพูดถึงสิ่งที่นับได้เป็นครั้งแรก และใช้ the เมื่อทั้งสองฝ่ายรู้ว่าหมายถึงสิ่งไหน" },
    formula: "a client · an order · the client we met",
    example: "I spoke to a client. The client wants a quotation.",
    meaning: { zh: "我和一位客户谈过。这位客户想要报价。", en: "First mention: a client. Known second mention: the client.", th: "ฉันคุยกับลูกค้าคนหนึ่ง ลูกค้าคนนั้นต้องการใบเสนอราคา" },
    my: { zh: "中文没有冠词，写完句子后检查每个单数可数名词。", en: "Chinese has no articles; check every singular countable noun after writing.", th: "ภาษาจีนไม่มี article จึงควรตรวจคำนามนับได้เอกพจน์ทุกคำ" },
    thai: { zh: "泰语也没有 a / an / the 的对应系统，要把“新信息/已知信息”当成习惯。", en: "Thai has no equivalent article system; build the habit around new versus known information.", th: "ภาษาไทยไม่มีระบบ a / an / the แบบเดียวกัน ให้ฝึกแยกข้อมูลใหม่กับข้อมูลที่รู้แล้ว" }
  },
  {
    id: "b6", level: "basic", icon: "＋",
    title: { zh: "单复数与 some / any", en: "Plurals with some / any", th: "พหูพจน์และ some / any" },
    rule: { zh: "可数名词超过一个通常加 -s；肯定句常用 some，问题和否定句常用 any。", en: "Add -s to most countable nouns above one. Use some mainly in positive statements and any in questions or negatives.", th: "คำนามนับได้มากกว่าหนึ่งมักเติม -s ใช้ some ในประโยคบอกเล่า และ any ในคำถามหรือปฏิเสธ" },
    formula: "some samples · any questions · no problems",
    example: "Do you have any questions about the samples?",
    meaning: { zh: "你对这些样品有任何问题吗？", en: "A question about an unknown number of questions.", th: "คุณมีคำถามเกี่ยวกับตัวอย่างเหล่านี้ไหม" },
    my: { zh: "数量词后检查复数：two sample ✕ → two samples ✓。", en: "Check plural nouns after numbers: two sample ✕ → two samples ✓.", th: "ตรวจคำนามพหูพจน์หลังตัวเลข: two sample ✕ → two samples ✓" },
    thai: { zh: "泰语名词通常不变复数；英文 two、many、several 后面要检查 -s。", en: "Thai nouns often stay unchanged; in English, check -s after two, many, and several.", th: "คำนามไทยมักไม่เปลี่ยนรูป แต่ภาษาอังกฤษต้องตรวจ -s หลัง two, many และ several" }
  },
  {
    id: "a1", level: "advanced", icon: "✓",
    title: { zh: "现在完成时：经历与现在结果", en: "Present perfect: experience and present result", th: "Present perfect: ประสบการณ์และผลถึงปัจจุบัน" },
    rule: { zh: "时间不重要或结果影响现在，用 have / has + 过去分词；有明确过去时间则用一般过去时。", en: "Use have or has plus a past participle when the time is not important or the result matters now. Use the past simple with a finished time.", th: "ใช้ have/has + past participle เมื่อเวลาไม่สำคัญหรือผลยังเกี่ยวกับปัจจุบัน ใช้ past simple เมื่อระบุเวลาในอดีตชัดเจน" },
    formula: "I have sent it. · I sent it yesterday.",
    example: "I have sent the quotation, so you can check it now.",
    meaning: { zh: "我已经发了报价，你现在可以查看。", en: "The completed action has a result now.", th: "ฉันส่งใบเสนอราคาแล้ว คุณตรวจดูได้ตอนนี้" },
    my: { zh: "不要把 yesterday 和现在完成时放一起：I have sent it yesterday ✕。", en: "Do not combine yesterday with the present perfect: I have sent it yesterday ✕.", th: "อย่าใช้ yesterday กับ present perfect: I have sent it yesterday ✕" },
    thai: { zh: "泰语用“แล้ว”表达完成；英文需要根据时间选择 have sent 或 sent。", en: "Thai uses แล้ว for completion; English chooses have sent or sent according to the time meaning.", th: "ภาษาไทยใช้ “แล้ว” บอกความสำเร็จ แต่ภาษาอังกฤษต้องเลือก have sent หรือ sent ตามความหมายของเวลา" }
  },
  {
    id: "a2", level: "advanced", icon: "◇",
    title: { zh: "条件句：真实计划与假设", en: "Conditionals: real plans and hypotheticals", th: "ประโยคเงื่อนไข: แผนจริงและสมมติ" },
    rule: { zh: "可能发生的条件用 if + 现在时，will + 动词；假设或较不可能的情况用 if + 过去式，would + 动词。", en: "For a real possibility, use if + present and will. For a hypothetical or less likely situation, use if + past and would.", th: "เงื่อนไขที่เป็นไปได้ใช้ if + present กับ will ส่วนสถานการณ์สมมติใช้ if + past กับ would" },
    formula: "If you order today, we will deliver Friday. · If I had more time, I would join.",
    example: "If you confirm today, we will start on Monday.",
    meaning: { zh: "如果你今天确认，我们星期一开始。", en: "This is a realistic future condition.", th: "ถ้าคุณยืนยันวันนี้ เราจะเริ่มวันจันทร์" },
    my: { zh: "if 从句通常不用 will：If you will confirm ✕ → If you confirm ✓。", en: "Usually do not put will in the if-clause: If you will confirm ✕ → If you confirm ✓.", th: "โดยทั่วไปไม่ใส่ will ใน if-clause: If you will confirm ✕ → If you confirm ✓" },
    thai: { zh: "泰语条件句不改变动词形式；英文真实条件和假设条件的时态不同。", en: "Thai conditional verbs do not inflect this way; English tense shows whether the condition is real or hypothetical.", th: "เงื่อนไขภาษาไทยไม่เปลี่ยนรูปกริยาแบบนี้ แต่ tense อังกฤษบอกว่าเงื่อนไขจริงหรือสมมติ" }
  },
  {
    id: "a3", level: "advanced", icon: "◎",
    title: { zh: "情态动词：礼貌请求与建议", en: "Modals: polite requests and advice", th: "Modal verbs: คำขอและคำแนะนำอย่างสุภาพ" },
    rule: { zh: "can 直接，could / would 更柔和；情态动词后面永远用动词原形。", en: "Can is direct; could and would are softer. Always use the base verb after a modal.", th: "can ตรงกว่า ส่วน could/would นุ่มกว่า และต้องใช้กริยารูปเดิมหลัง modal เสมอ" },
    formula: "Could you send…? · Would you mind checking…? · You should try…",
    example: "Could you send the details by Friday?",
    meaning: { zh: "你可以在星期五前发送详细资料吗？", en: "A polite but clear request.", th: "ช่วยส่งรายละเอียดภายในวันศุกร์ได้ไหม" },
    my: { zh: "could 后面不用过去式：could sent ✕ → could send ✓。", en: "Do not use a past form after could: could sent ✕ → could send ✓.", th: "หลัง could ห้ามใช้กริยาอดีต: could sent ✕ → could send ✓" },
    thai: { zh: "泰语常靠语气词表示礼貌；英文可以用 could / would 把礼貌写进句型。", en: "Thai often marks politeness with particles; English can build it into the sentence with could or would.", th: "ภาษาไทยมักใช้คำลงท้ายแสดงความสุภาพ ส่วนอังกฤษใช้ could หรือ would ในโครงสร้างประโยค" }
  },
  {
    id: "a4", level: "advanced", icon: "↗",
    title: { zh: "关系从句：把资料合成一句", en: "Relative clauses: combine information", th: "Relative clauses: รวมข้อมูลในประโยคเดียว" },
    rule: { zh: "用 who 说明人，which 说明物，that 两者都可用于限定信息。", en: "Use who for people, which for things, and that for defining information about either.", th: "ใช้ who กับคน which กับสิ่งของ และ that กับข้อมูลจำกัดความได้ทั้งสองแบบ" },
    formula: "the trainer who helped us · the machine that we bought",
    example: "The client who visited yesterday approved the design.",
    meaning: { zh: "昨天来访的客户批准了设计。", en: "The clause identifies which client approved it.", th: "ลูกค้าที่มาเมื่อวานอนุมัติแบบแล้ว" },
    my: { zh: "不要重复主语：The client who he visited ✕。", en: "Do not repeat the subject inside the clause: The client who he visited ✕.", th: "อย่าใส่ประธานซ้ำใน clause: The client who he visited ✕" },
    thai: { zh: "泰语常用“ที่”连接人和物；英文要根据对象选择 who / which / that。", en: "Thai often uses ที่ for both people and things; English chooses who, which, or that.", th: "ภาษาไทยมักใช้ “ที่” เชื่อมทั้งคนและสิ่งของ แต่อังกฤษเลือก who, which หรือ that ตามชนิดของคำนาม" }
  },
  {
    id: "a5", level: "advanced", icon: "⇄",
    title: { zh: "被动语态：强调结果或流程", en: "Passive voice: focus on result or process", th: "Passive voice: เน้นผลลัพธ์หรือกระบวนการ" },
    rule: { zh: "不重要或不知道谁做时，用 be + 过去分词，把重点放在事情本身。", en: "Use be plus a past participle when the doer is unknown or unimportant and the action matters more.", th: "ใช้ be + past participle เมื่อไม่รู้หรือไม่เน้นผู้กระทำ แต่เน้นการกระทำหรือผลลัพธ์" },
    formula: "The order was confirmed. · The beans are roasted weekly.",
    example: "Your order has been confirmed.",
    meaning: { zh: "你的订单已经确认。", en: "The confirmation matters more than who confirmed it.", th: "คำสั่งซื้อของคุณได้รับการยืนยันแล้ว" },
    my: { zh: "被动语态不能只放过去分词：The order confirmed ✕ → was confirmed ✓。", en: "A passive needs be: The order confirmed ✕ → was confirmed ✓.", th: "Passive ต้องมี be: The order confirmed ✕ → was confirmed ✓" },
    thai: { zh: "泰语被动表达方式不同；英文先找时态，再选择 is / was / has been。", en: "Thai forms passives differently; in English, identify the tense first, then choose is, was, or has been.", th: "ภาษาไทยสร้างประโยค passive ต่างออกไป ในอังกฤษให้หา tense ก่อนแล้วเลือก is, was หรือ has been" }
  },
  {
    id: "a6", level: "advanced", icon: "≈",
    title: { zh: "连接词：让解释有逻辑", en: "Linking ideas clearly", th: "คำเชื่อม: อธิบายอย่างมีเหตุผล" },
    rule: { zh: "because 给原因，so 给结果，although 表示让步，however 开启相反观点。", en: "Because gives a reason, so gives a result, although introduces contrast, and however starts an opposing point.", th: "because ให้เหตุผล so บอกผล although แสดงความขัดแย้ง และ however เปิดประเด็นตรงข้าม" },
    formula: "because + reason · so + result · although + clause · However, + sentence",
    example: "The price is higher because the materials are imported.",
    meaning: { zh: "价格较高，因为材料是进口的。", en: "The second part gives the reason for the higher price.", th: "ราคาสูงกว่าเพราะวัสดุนำเข้า" },
    my: { zh: "一个原因不要同时用 because 和 so：Because…, so… ✕。", en: "Do not use because and so together for the same link: Because…, so… ✕.", th: "อย่าใช้ because และ so พร้อมกันเพื่อเชื่อมเหตุผลเดียวกัน: Because…, so… ✕" },
    thai: { zh: "泰语可连续使用连接词；正式英文通常每个逻辑关系选一个最准确的词。", en: "Thai can stack connectors; clear formal English usually chooses one precise connector for each relationship.", th: "ภาษาไทยอาจใช้คำเชื่อมต่อกันได้ แต่ภาษาอังกฤษที่ชัดเจนควรเลือกคำเชื่อมที่ตรงที่สุดหนึ่งคำต่อความสัมพันธ์" }
  }
];

window.GRAMMAR_QUIZ = [
  { level: "basic", q: { zh: "选择正确句子", en: "Choose the correct sentence", th: "เลือกประโยคที่ถูกต้อง" }, options: ["She busy today.", "She is busy today.", "She are busy today."], answer: 1 },
  { level: "basic", q: { zh: "他说每星期授课。", en: "He teaches every week.", th: "เขาสอนทุกสัปดาห์" }, options: ["He teach every week.", "He teaches every week.", "He teaching every week."], answer: 1 },
  { level: "basic", q: { zh: "昨天发生的事情", en: "An event that happened yesterday", th: "เหตุการณ์ที่เกิดเมื่อวาน" }, options: ["We meet yesterday.", "We met yesterday.", "We have meet yesterday."], answer: 1 },
  { level: "basic", q: { zh: "正确的问题是？", en: "Which question is correct?", th: "คำถามข้อใดถูกต้อง" }, options: ["Did you received it?", "Did you receive it?", "You did receive it?"], answer: 1 },
  { level: "advanced", q: { zh: "报价刚发出，现在可以查看。", en: "The quotation was just sent and can be checked now.", th: "เพิ่งส่งใบเสนอราคาและตรวจได้ตอนนี้" }, options: ["I have sent the quotation.", "I have send the quotation.", "I sent the quotation tomorrow."], answer: 0 },
  { level: "advanced", q: { zh: "真实的未来条件", en: "A real future condition", th: "เงื่อนไขอนาคตที่เป็นไปได้จริง" }, options: ["If you confirm, we will start.", "If you will confirm, we start.", "If you confirmed, we will started."], answer: 0 },
  { level: "advanced", q: { zh: "礼貌地要求资料", en: "Ask for details politely", th: "ขอรายละเอียดอย่างสุภาพ" }, options: ["Send me details.", "Could you send the details?", "Could you sent the details?"], answer: 1 },
  { level: "advanced", q: { zh: "正确的被动句", en: "Choose the correct passive", th: "เลือกประโยค passive ที่ถูกต้อง" }, options: ["The order has confirmed.", "The order has been confirmed.", "The order been confirm."], answer: 1 }
];
