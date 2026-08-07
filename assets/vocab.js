/* 场景词库 —— 3 场景 × 3 难度
   s = scene, l = level(1基础/2进阶/3地道)
   en = 要说的英文, ex = 例句, zh = 中文意思, def = 简单英文解释, th = 泰文意思 */
window.VOCAB = {
  scenes: [
    { id: "social",   zh: "朋友聚会",   en: "Friends & hangouts", th: "สังสรรค์กับเพื่อน" },
    { id: "business", zh: "商务",       en: "Business",           th: "ธุรกิจ" },
    { id: "couple",   zh: "情侣聊天",   en: "Couples & dating",   th: "คู่รัก" },
    { id: "pro",      zh: "专业词汇",   en: "Technical terms",    th: "ศัพท์เฉพาะทาง" },
    { id: "teach",    zh: "上课授课",   en: "Teaching a class",   th: "การสอน" },
    { id: "law",      zh: "知识产权法", en: "IP law",             th: "กฎหมายทรัพย์สินทางปัญญา" }
  ],
  items: [
    /* ---------- 朋友聚会 ---------- */
    { s: "social", l: 1, en: "What have you been up to?", ex: "Hey! What have you been up to?", zh: "最近在忙什么？", def: "A friendly way to ask what someone has been doing lately.", th: "ช่วงนี้ทำอะไรอยู่บ้าง" },
    { s: "social", l: 1, en: "Long time no see.", ex: "Long time no see! You look well.", zh: "好久不见。", def: "A casual greeting for someone you have not met in a while.", th: "ไม่ได้เจอกันนานเลย" },
    { s: "social", l: 1, en: "Help yourself.", ex: "There's more in the kitchen — help yourself.", zh: "自己拿，别客气。", def: "Tell someone to take food or drink freely.", th: "หยิบเองได้เลย ไม่ต้องเกรงใจ" },
    { s: "social", l: 1, en: "Same here.", ex: "\"I'm exhausted.\" \"Same here.\"", zh: "我也是。", def: "Say that you feel exactly the same.", th: "เหมือนกันเลย" },
    { s: "social", l: 1, en: "It's on me.", ex: "Put your wallet away, it's on me.", zh: "这顿我请。", def: "Tell people you are paying for everyone.", th: "มื้อนี้เลี้ยงเอง" },
    { s: "social", l: 1, en: "I'm good, thanks.", ex: "\"Another beer?\" \"I'm good, thanks.\"", zh: "不用了，谢谢。", def: "A polite way to refuse something offered to you.", th: "พอแล้ว ขอบคุณ" },
    { s: "social", l: 1, en: "Let's catch up soon.", ex: "Let's catch up soon — properly this time.", zh: "改天再好好聚。", def: "Suggest meeting again before long.", th: "ไว้เจอกันใหม่เร็ว ๆ นี้" },
    { s: "social", l: 1, en: "I'd better get going.", ex: "It's late, I'd better get going.", zh: "我得走了。", def: "A polite way to say you are leaving.", th: "ขอตัวกลับก่อนนะ" },



    /* ---------- 商务 ---------- */
    { s: "business", l: 1, en: "Thanks for coming in.", ex: "Thanks for coming in, did you find us okay?", zh: "谢谢你过来。", def: "Greet a visitor at your office or shop.", th: "ขอบคุณที่แวะมานะ" },
    { s: "business", l: 1, en: "Can I get you a coffee?", ex: "Have a seat. Can I get you a coffee?", zh: "要喝杯咖啡吗？", def: "Offer a drink to a guest.", th: "รับกาแฟสักแก้วไหม" },
    { s: "business", l: 1, en: "Let me explain how it works.", ex: "Let me explain how it works, then you can ask anything.", zh: "我解释一下怎么运作。", def: "Signal that an explanation is coming.", th: "ขออธิบายว่ามันทำงานยังไง" },
    { s: "business", l: 1, en: "What's your budget?", ex: "Before I quote — what's your budget?", zh: "你们的预算是多少？", def: "Ask how much they can spend.", th: "งบประมาณเท่าไหร่" },
    { s: "business", l: 1, en: "I'll send you the details.", ex: "I'll send you the details this afternoon.", zh: "我把细节发给你。", def: "Promise to follow up in writing.", th: "เดี๋ยวส่งรายละเอียดให้" },
    { s: "business", l: 1, en: "Does that work for you?", ex: "Tuesday at ten. Does that work for you?", zh: "这样可以吗？", def: "Check whether a plan suits the other person.", th: "แบบนี้สะดวกไหม" },
    { s: "business", l: 1, en: "Let me check and come back to you.", ex: "Good question — let me check and come back to you.", zh: "我确认一下再回复你。", def: "Buy time without refusing.", th: "ขอเช็กก่อนแล้วจะแจ้งกลับ" },
    { s: "business", l: 1, en: "Thanks for your time.", ex: "Thanks for your time, I know you're busy.", zh: "谢谢你抽时间。", def: "Close a meeting politely.", th: "ขอบคุณที่สละเวลา" },



    /* ---------- 情侣聊天 ---------- */
    { s: "couple", l: 1, en: "How was your day?", ex: "Hey, how was your day?", zh: "今天过得怎么样？", def: "The everyday caring question.", th: "วันนี้เป็นยังไงบ้าง" },
    { s: "couple", l: 1, en: "I miss you.", ex: "I miss you. Come back soon.", zh: "我想你。", def: "Say you want them near you.", th: "คิดถึงนะ" },
    { s: "couple", l: 1, en: "Get home safe.", ex: "It's raining — get home safe.", zh: "路上小心。", def: "Show care when they leave.", th: "กลับบ้านปลอดภัยนะ" },
    { s: "couple", l: 1, en: "I'm on my way.", ex: "I'm on my way, five minutes.", zh: "我在路上了。", def: "Tell them you are coming now.", th: "กำลังไปแล้วนะ" },
    { s: "couple", l: 1, en: "Text me when you get there.", ex: "Text me when you get there, okay?", zh: "到了给我发个信息。", def: "Ask them to confirm they arrived.", th: "ถึงแล้วทักมานะ" },
    { s: "couple", l: 1, en: "You look nice today.", ex: "You look nice today. Is that new?", zh: "你今天很好看。", def: "A simple, safe compliment.", th: "วันนี้ดูดีนะ" },
    { s: "couple", l: 1, en: "Sorry, that was my fault.", ex: "Sorry, that was my fault. I should have called.", zh: "对不起，是我的错。", def: "A short, clean apology.", th: "ขอโทษนะ เป็นความผิดเราเอง" },
    { s: "couple", l: 1, en: "Sleep well.", ex: "Sleep well. Talk tomorrow.", zh: "好好睡。", def: "A warm good night.", th: "ฝันดีนะ" },



    { s: "social", l: 2, en: "Let's meet next week.", up: "meet next week", col: "meet next week · meet after work", ex: "Let's meet next week after you check the details.", zh: "我们下星期见面吧。", def: "Suggest a clear time to meet again.", th: "ไว้เจอกันสัปดาห์หน้า" },
    { s: "social", l: 2, en: "I'm very busy this week.", up: "very busy", col: "busy this week · busy with work", ex: "I'm very busy this week. Can we meet on Sunday instead?", zh: "我这个星期很忙。", def: "Explain that you do not have much free time.", th: "สัปดาห์นี้ยุ่งมาก" },
    { s: "social", l: 2, en: "Sorry, I forgot about it.", up: "I forgot", col: "forgot about it · completely forgot", ex: "Sorry, I forgot about it. Thank you for reminding me.", zh: "对不起，我忘记了。", def: "Apologise clearly when you forget something.", th: "ขอโทษนะ ลืมเรื่องนี้ไปเลย" },
    { s: "social", l: 2, en: "Sorry, I can't make it.", up: "cannot come", col: "can't make it tonight · can't make the meeting", ex: "Sorry, I can't make it tonight. Can we meet another day?", zh: "对不起，我来不了。", def: "Say politely that you cannot attend.", th: "ขอโทษนะ วันนี้ไปไม่ได้" },
    { s: "social", l: 2, en: "Can my brother join us?", up: "join us", col: "join us for dinner · join the group", ex: "Can my brother join us for dinner?", zh: "我弟弟可以和我们一起吗？", def: "Ask if another person may come with the group.", th: "น้องชายมาร่วมกับเราได้ไหม" },
    { s: "social", l: 2, en: "Either one is fine with me.", up: "both are fine", col: "either one is fine · both are fine", ex: "Thai or Japanese? Either one is fine with me.", zh: "两个我都可以。", def: "Say clearly that you have no preference.", th: "อย่างไหนก็ได้สำหรับฉัน" },
    { s: "social", l: 2, en: "Please let me know.", up: "tell me", col: "let me know when · please let me know", ex: "Please let me know when you arrive.", zh: "请告诉我。", def: "Ask someone to give you information later.", th: "ช่วยบอกให้ฉันรู้ด้วยนะ" },
    { s: "social", l: 2, en: "Shall we stay a little longer?", up: "stay longer", col: "stay a little longer · stay for a while", ex: "We finished dinner. Shall we stay a little longer?", zh: "我们要不要再待一会儿？", def: "Suggest spending a little more time together.", th: "อยู่ต่ออีกสักหน่อยไหม" },

    { s: "social", l: 3, en: "hit it off", up: "get along well", col: "hit it off straight away · really hit it off", ex: "They hit it off straight away, which I did not expect.", zh: "一见如故", def: "Get on well with someone immediately.", th: "ถูกคอกันตั้งแต่แรกเจอ" },
    { s: "social", l: 3, en: "read the room", up: "notice the mood", col: "read the room · failed to read the room", ex: "He told that joke twice. He really can't read the room.", zh: "看气氛 / 看场合", def: "Sense the mood of a group and adjust.", th: "อ่านบรรยากาศในวงให้ออก" },
    { s: "social", l: 3, en: "on the fence", up: "not sure yet", col: "still on the fence · sitting on the fence", ex: "I'm still on the fence about Saturday, honestly.", zh: "还在犹豫", def: "Undecided between two options.", th: "ยังลังเลอยู่" },
    { s: "social", l: 3, en: "par for the course", up: "normal for him", col: "that's par for the course", ex: "He was forty minutes late, but that's par for the course.", zh: "他一向如此 / 见怪不怪", def: "Typical and unsurprising, usually about something annoying.", th: "ก็ปกติของเขาแหละ" },
    { s: "social", l: 3, en: "cut it fine", up: "almost too late", col: "cut it a bit fine · cutting it fine", ex: "We cut it a bit fine getting to the airport.", zh: "时间掐得太紧", def: "Leave yourself almost no margin of time.", th: "เฉียดฉิวเรื่องเวลา" },
    { s: "social", l: 3, en: "wear thin", up: "stop being funny", col: "wearing thin · patience wearing thin", ex: "That joke's starting to wear thin.", zh: "腻了 / 快没耐心了", def: "Become tiresome after too much repetition.", th: "เริ่มเบื่อ เริ่มหมดความอดทน" },
    { s: "social", l: 3, en: "go overboard", up: "do too much", col: "go overboard with · don't go overboard", ex: "Don't go overboard, it's just a casual dinner.", zh: "做过头了", def: "Do far more than the situation calls for.", th: "ทำเกินไปหน่อยแล้ว" },
    { s: "social", l: 3, en: "a bit of a blur", up: "I don't remember much", col: "the whole night was a blur", ex: "After the second bottle the whole evening was a bit of a blur.", zh: "整晚记忆模糊", def: "You remember it only vaguely.", th: "ทั้งคืนจำอะไรไม่ค่อยได้" },

    { s: "business", l: 2, en: "We don't have enough time or staff.", up: "not enough resources", col: "enough time · enough staff", ex: "We don't have enough time or staff to take on this project now.", zh: "我们现在没有足够的时间或人手。", def: "Explain clearly that your team cannot accept more work.", th: "ตอนนี้เรามีเวลาหรือพนักงานไม่เพียงพอ" },
    { s: "business", l: 2, en: "This is not included in phase one.", up: "not included", col: "included in the price · included in phase one", ex: "Training is not included in phase one.", zh: "这个不包括在第一阶段。", def: "Clarify what a project does not cover.", th: "สิ่งนี้ไม่รวมอยู่ในระยะแรก" },
    { s: "business", l: 2, en: "This price depends on a two-year contract.", up: "depends on", col: "depends on the contract · depends on the quantity", ex: "This price depends on a two-year contract.", zh: "这个价格以两年合约为条件。", def: "Explain a condition for the price in plain English.", th: "ราคานี้ขึ้นอยู่กับสัญญาสองปี" },
    { s: "business", l: 2, en: "Could you give me an estimated price?", up: "estimated price", col: "give an estimate · estimated cost", ex: "Could you give me an estimated price before we continue?", zh: "你可以给我一个估计价格吗？", def: "Ask for an approximate cost before receiving a final quote.", th: "ขอราคาประมาณการได้ไหม" },
    { s: "business", l: 2, en: "Let's agree on the numbers first.", up: "agree first", col: "agree on the price · agree on the numbers", ex: "Let's agree on the numbers before we speak to finance.", zh: "我们先确认这些数字。", def: "Make sure everyone accepts the same figures.", th: "มาตกลงตัวเลขกันก่อน" },
    { s: "business", l: 2, en: "Let's confirm everything in writing.", up: "write it down", col: "confirm in writing · put it in writing", ex: "Let's confirm what you will deliver in writing.", zh: "我们把所有内容书面确认。", def: "Ask for a written record of what was agreed.", th: "มายืนยันทุกอย่างเป็นลายลักษณ์อักษร" },
    { s: "business", l: 2, en: "It will take about two weeks to get started.", up: "two weeks to start", col: "get started · take about two weeks", ex: "It will take about two weeks for our team to get started.", zh: "我们大约需要两个星期才能开始。", def: "Give a clear timeline for starting work.", th: "ทีมของเราจะใช้เวลาประมาณสองสัปดาห์เพื่อเริ่มงาน" },
    { s: "business", l: 2, en: "Let's discuss the price again later.", up: "discuss it later", col: "discuss the price · discuss it again", ex: "Let's discuss the price again after we confirm the work.", zh: "确认工作内容后，我们再谈价格。", def: "Say clearly that you will return to a topic later.", th: "ค่อยคุยเรื่องราคาอีกครั้งหลังจากยืนยันขอบเขตงาน" },

    { s: "business", l: 3, en: "mitigate", up: "make it less risky", col: "mitigate the risk · a mitigating factor", ex: "We can mitigate that with a staged rollout.", zh: "缓解 / 降低（风险）", def: "Make a risk or a bad effect less severe.", th: "ลดความเสี่ยงให้เบาลง" },
    { s: "business", l: 3, en: "material", up: "important", col: "a material change · material to the decision", ex: "That's not a material change to the agreement.", zh: "实质性的", def: "Significant enough to affect a decision.", th: "มีนัยสำคัญพอที่จะเปลี่ยนการตัดสินใจ" },
    { s: "business", l: 3, en: "defer", up: "delay it", col: "defer a decision · defer payment", ex: "I'd rather defer the decision than rush it.", zh: "推迟 / 押后", def: "Deliberately postpone something to a later point.", th: "เลื่อนออกไปอย่างตั้งใจ" },
    { s: "business", l: 3, en: "leverage", up: "we have an advantage", col: "have leverage · leverage our position", ex: "We've got more leverage here than they realise.", zh: "筹码 / 议价能力", def: "The advantage that lets you get better terms.", th: "อำนาจต่อรอง" },
    { s: "business", l: 3, en: "concede", up: "give in", col: "concede a point · make a concession", ex: "I'm prepared to concede on delivery, not on price.", zh: "让步", def: "Give way on one specific point in a negotiation.", th: "ยอมในบางประเด็น" },
    { s: "business", l: 3, en: "commercially viable", up: "worth doing", col: "commercially viable · not viable at that volume", ex: "It isn't commercially viable at that volume.", zh: "商业上跑得通", def: "Able to make money, not just technically possible.", th: "คุ้มค่าในเชิงธุรกิจ" },
    { s: "business", l: 3, en: "discretionary", up: "optional", col: "discretionary spend · at our discretion", ex: "That budget is discretionary, so it's first to go.", zh: "可自由裁量的 / 非必要的", def: "Spent only if you choose to, not committed.", th: "ใช้จ่ายตามดุลพินิจ ไม่ใช่รายจ่ายบังคับ" },
    { s: "business", l: 3, en: "underwrite", up: "pay for it", col: "underwrite the cost · underwrite the risk", ex: "Are you willing to underwrite the setup cost?", zh: "承担 / 兜底（成本或风险）", def: "Take financial responsibility if something costs more or goes wrong.", th: "รับผิดชอบต้นทุนหรือความเสี่ยงแทน" },

    { s: "couple", l: 2, en: "Please don't misunderstand me.", up: "understand me", col: "don't misunderstand me · please understand", ex: "Please don't misunderstand me. I'm just tired today.", zh: "请不要误会我。", def: "Ask someone not to take your meaning the wrong way.", th: "อย่าเข้าใจฉันผิดนะ" },
    { s: "couple", l: 2, en: "Please tell me how you feel.", up: "tell me", col: "tell me how you feel · share your feelings", ex: "Please tell me how you feel. I want to understand.", zh: "请告诉我你的感受。", def: "Invite someone to speak honestly about their feelings.", th: "บอกฉันหน่อยว่าคุณรู้สึกอย่างไร" },
    { s: "couple", l: 2, en: "I didn't mean to sound cold.", up: "not my intention", col: "didn't mean to sound · sound cold", ex: "I didn't mean to sound cold earlier. I'm sorry.", zh: "我不是故意让语气听起来很冷淡。", def: "Explain that your tone did not match your intention.", th: "ฉันไม่ได้ตั้งใจพูดให้ฟังดูเย็นชา" },
    { s: "couple", l: 2, en: "Can we talk calmly?", up: "talk calmly", col: "talk calmly · discuss this calmly", ex: "Can we talk calmly? I want to solve this together.", zh: "我们可以冷静地谈吗？", def: "Ask to discuss a problem without arguing.", th: "เราคุยกันอย่างใจเย็นได้ไหม" },
    { s: "couple", l: 2, en: "Please don't ignore this.", up: "do not ignore it", col: "don't ignore this · important to me", ex: "Please don't ignore this. It is important to me.", zh: "请不要忽略这件事。", def: "Say clearly that an issue matters to you.", th: "อย่าเพิกเฉยเรื่องนี้นะ มันสำคัญกับฉัน" },
    { s: "couple", l: 2, en: "Maybe there is another explanation.", up: "another reason", col: "another explanation · maybe there is", ex: "Maybe there is another explanation. Let's ask before we decide.", zh: "也许还有别的解释。", def: "Suggest considering a kinder possibility first.", th: "อาจมีคำอธิบายอีกแบบก็ได้" },
    { s: "couple", l: 2, en: "Let's make time for each other.", up: "spend time together", col: "make time for each other · spend time together", ex: "We are both busy, but let's make time for each other.", zh: "我们为彼此留一点时间吧。", def: "Plan time together even when both people are busy.", th: "มาหาเวลาให้กันและกันนะ" },
    { s: "couple", l: 2, en: "I don't want us to become distant.", up: "stay close", col: "become distant · stay close", ex: "I don't want us to become distant because we are both busy.", zh: "我不想让我们变得疏远。", def: "Say that you want the relationship to stay close.", th: "ฉันไม่อยากให้เราห่างเหินกัน" },

    { s: "couple", l: 3, en: "walk on eggshells", up: "be scared to speak", col: "walking on eggshells around", ex: "Lately I feel like I'm walking on eggshells around you.", zh: "如履薄冰 / 说话都要小心翼翼", def: "Behave very carefully to avoid upsetting someone.", th: "รู้สึกเหมือนต้องระวังทุกคำพูด" },
    { s: "couple", l: 3, en: "blow it out of proportion", up: "make it too big", col: "blowing it out of proportion", ex: "I think we're both blowing this out of proportion.", zh: "小题大做", def: "Treat something as far more serious than it is.", th: "ทำเรื่องเล็กให้เป็นเรื่องใหญ่" },
    { s: "couple", l: 3, en: "meet you halfway", up: "both give a bit", col: "meet me halfway · meet you halfway", ex: "I'm willing to meet you halfway on this.", zh: "各让一步", def: "Compromise so both sides give something.", th: "ยอมถอยคนละก้าว" },
    { s: "couple", l: 3, en: "keep score", up: "remember every mistake", col: "keeping score · we can't keep score", ex: "We can't keep score, it just makes us both worse.", zh: "算旧账", def: "Track each other's faults as if competing.", th: "คอยนับความผิดของกันและกัน" },
    { s: "couple", l: 3, en: "shut down", up: "stop talking to me", col: "shut down · shuts down whenever", ex: "You shut down every time I bring this up.", zh: "把自己关起来 / 不回应", def: "Emotionally withdraw and stop engaging.", th: "ปิดตัวเงียบ ไม่คุยต่อ" },
    { s: "couple", l: 3, en: "hold it against you", up: "stay angry about it", col: "won't hold it against you", ex: "It's fine, I won't hold it against you.", zh: "记恨这件事", def: "Keep resenting someone for something they did.", th: "เก็บเรื่องนี้ไว้โกรธ" },
    { s: "couple", l: 3, en: "come to terms with", up: "accept it slowly", col: "still coming to terms with", ex: "I'm still coming to terms with how that evening went.", zh: "慢慢接受 / 消化", def: "Gradually accept something difficult.", th: "ค่อย ๆ ทำใจยอมรับ" },
    { s: "couple", l: 3, en: "take a step back", up: "calm down first", col: "take a step back · both step back", ex: "Can we both take a step back before we say something we regret?", zh: "先退一步", def: "Pause and get perspective before continuing.", th: "ถอยออกมาตั้งสติก่อน" },

    /* ---------- 专业词汇（咖啡 / 餐饮）col = 常见搭配 ---------- */
    { s: "pro", l: 1, en: "extraction", col: "even extraction · under-extracted · over-extracted", ex: "That shot's under-extracted, that's why it tastes sour.", zh: "萃取", def: "How much flavour you pull out of the coffee.", th: "การสกัด" },
    { s: "pro", l: 1, en: "grind size", col: "adjust the grind · go finer · go coarser", ex: "Let's adjust the grind size before we touch anything else.", zh: "研磨度", def: "How fine or coarse the coffee is ground.", th: "ความละเอียดของการบด" },
    { s: "pro", l: 1, en: "dose", col: "dose in · an 18-gram dose", ex: "We're dosing eighteen grams in.", zh: "粉量", def: "The weight of dry coffee you put in.", th: "ปริมาณกาแฟที่ใส่" },
    { s: "pro", l: 1, en: "yield", col: "a 36-gram yield · in and out", ex: "Eighteen in, thirty-six out.", zh: "液重 / 出液量", def: "The weight of liquid coffee that comes out.", th: "ปริมาณกาแฟที่ได้ออกมา" },
    { s: "pro", l: 1, en: "tamp", col: "tamp level · an even tamp", ex: "Keep the tamp level, that's all that matters.", zh: "压粉", def: "Pressing the coffee flat in the basket.", th: "การกดกาแฟ" },
    { s: "pro", l: 1, en: "purge the steam wand", col: "purge before and after", ex: "Always purge the steam wand before you start.", zh: "放蒸汽 / 排水", def: "Release steam to clear the wand.", th: "ไล่น้ำในหัวสตีม" },
    { s: "pro", l: 1, en: "texture the milk", col: "silky texture · stretch the milk", ex: "Texture the milk until it looks like wet paint.", zh: "打奶泡", def: "Steam milk to the right smooth consistency.", th: "ตีฟองนม" },
    { s: "pro", l: 1, en: "brew ratio", col: "a 1:2 ratio · tighten the ratio", ex: "We run a one-to-two brew ratio on this blend.", zh: "粉液比", def: "Coffee weight compared with liquid weight.", th: "อัตราส่วนกาแฟต่อน้ำ" },

    { s: "pro", l: 2, en: "channelling", col: "get channelling · cause channelling", ex: "If the puck's uneven you'll get channelling.", zh: "通道效应", def: "Water finding one fast path through the coffee.", th: "น้ำไหลลัดช่อง" },
    { s: "pro", l: 2, en: "distribution", col: "good distribution · distribute evenly", ex: "Good distribution before you tamp fixes most problems.", zh: "布粉", def: "Spreading the grounds evenly before tamping.", th: "การเกลี่ยผงกาแฟ" },
    { s: "pro", l: 2, en: "body", col: "more body · a thin body · mouthfeel", ex: "This one's got more body than the washed.", zh: "醇厚度 / 口感", def: "How heavy the coffee feels in your mouth.", th: "ความหนักแน่นในปาก" },
    { s: "pro", l: 2, en: "acidity", col: "bright acidity · sharp acidity · flat", ex: "It's got a bright acidity, almost like green apple.", zh: "酸质", def: "The sharp, lively quality in the taste.", th: "ความเปรี้ยว" },
    { s: "pro", l: 2, en: "cupping", col: "cup a batch · a cupping session", ex: "We cup every new batch before it goes on the bar.", zh: "杯测", def: "Tasting coffees side by side to judge them.", th: "การชิมกาแฟ" },
    { s: "pro", l: 2, en: "roast profile", col: "a light profile · adjust the profile", ex: "The roast profile is a bit light for espresso.", zh: "烘焙曲线", def: "How the beans were roasted over time.", th: "โปรไฟล์การคั่ว" },
    { s: "pro", l: 2, en: "dial in", col: "dial in the beans · dialled in", ex: "Give me ten minutes to dial in the new beans.", zh: "调参数 / 出品校准", def: "Adjust settings until the shot tastes right.", th: "ปรับค่าจนได้รสที่ต้องการ" },
    { s: "pro", l: 2, en: "consistency", col: "shot-to-shot consistency", ex: "Consistency matters more than one perfect shot.", zh: "稳定性", def: "Getting the same result every time.", th: "ความสม่ำเสมอ" },

    { s: "pro", l: 3, en: "traceability", col: "full traceability · farm to cup", ex: "We can show full traceability, farm to cup.", zh: "可追溯性", def: "Being able to prove where the coffee came from.", th: "การตรวจสอบย้อนกลับ" },
    { s: "pro", l: 3, en: "single origin", col: "a single origin · versus a blend", ex: "This is a single origin, not a blend.", zh: "单品豆", def: "Coffee from one farm or region only.", th: "กาแฟแหล่งเดียว" },
    { s: "pro", l: 3, en: "degas", col: "let it degas · four days off roast", ex: "Give it four days to degas before you serve it.", zh: "养豆 / 排气", def: "Letting fresh-roasted coffee release gas.", th: "การพักกาแฟให้คายแก๊ส" },
    { s: "pro", l: 3, en: "throughput", col: "morning throughput · handle the volume", ex: "That machine can't handle our morning throughput.", zh: "出杯量 / 处理量", def: "How much you can produce in a period.", th: "ปริมาณที่ทำได้ต่อช่วงเวลา" },
    { s: "pro", l: 3, en: "wastage", col: "cut wastage · wastage rate", ex: "We cut wastage by about fifteen percent last quarter.", zh: "损耗", def: "Product thrown away instead of sold.", th: "ของเสีย / การสูญเสีย" },
    { s: "pro", l: 3, en: "spec sheet", col: "send the spec sheet · to spec", ex: "I'll send you the spec sheet with the tolerances.", zh: "规格表", def: "The document listing exact technical requirements.", th: "เอกสารสเปก" },
    { s: "pro", l: 3, en: "lead time", col: "a six-week lead time · shorten the lead time", ex: "The lead time on that grinder is six weeks.", zh: "交期", def: "How long between ordering and receiving.", th: "ระยะเวลาส่งมอบ" },
    { s: "pro", l: 3, en: "margin", col: "gross margin · a thin margin", ex: "The margin on retail bags is much better than on drinks.", zh: "毛利", def: "What you keep after the cost of the product.", th: "กำไรขั้นต้น" },

    /* ---------- 上课授课 ---------- */
    { s: "teach", l: 1, en: "Let's start with the basics.", ex: "Let's start with the basics, then build up.", zh: "我们从基础开始。", def: "Open a lesson simply.", th: "เริ่มจากพื้นฐานกันก่อน" },
    { s: "teach", l: 1, en: "Watch me first, then you try.", ex: "Watch me first, then you try. No rush.", zh: "先看我做，然后你试。", def: "Set up a demonstration.", th: "ดูผมทำก่อน แล้วค่อยลองเอง" },
    { s: "teach", l: 1, en: "Any questions so far?", ex: "Any questions so far, before we move on?", zh: "到这里有问题吗？", def: "Check understanding mid-lesson.", th: "ถึงตรงนี้มีคำถามไหม" },
    { s: "teach", l: 1, en: "Take your time.", ex: "Take your time. Speed comes later.", zh: "慢慢来。", def: "Remove time pressure from a student.", th: "ค่อย ๆ ทำ ไม่ต้องรีบ" },
    { s: "teach", l: 1, en: "Try it again, slowly.", ex: "Good attempt. Try it again, slowly.", zh: "再试一次，慢一点。", def: "Ask for a second attempt.", th: "ลองอีกครั้ง ช้า ๆ นะ" },
    { s: "teach", l: 1, en: "That's it, exactly.", ex: "That's it, exactly. Do that every time.", zh: "对，就是这样。", def: "Confirm they got it right.", th: "ใช่ แบบนั้นเลย" },
    { s: "teach", l: 1, en: "Let me show you one more time.", ex: "Let me show you one more time, watch my wrist.", zh: "我再示范一次。", def: "Repeat a demonstration.", th: "ขอสาธิตอีกรอบนะ" },
    { s: "teach", l: 1, en: "We'll come back to that later.", ex: "Good question. We'll come back to that later.", zh: "这个我们等下再讲。", def: "Postpone a question without ignoring it.", th: "เดี๋ยวเรากลับมาเรื่องนี้ทีหลัง" },

    { s: "teach", l: 2, en: "Feel the weight in your wrist.", ex: "Feel the weight in your wrist, not your arm.", zh: "感受手腕的重量。", def: "Direct their attention to a body sensation.", th: "รู้สึกถึงน้ำหนักที่ข้อมือ" },
    { s: "teach", l: 2, en: "Notice what changed when you did that.", ex: "Notice what changed when you did that. Taste it.", zh: "注意刚才那样做，变了什么。", def: "Make them observe cause and effect.", th: "สังเกตว่าอะไรเปลี่ยนไปตอนทำแบบนั้น" },
    { s: "teach", l: 2, en: "What do you think went wrong there?", ex: "Before I tell you, what do you think went wrong there?", zh: "你觉得刚才哪里出问题了？", def: "Let the student diagnose first.", th: "คิดว่าตรงไหนพลาดไป" },
    { s: "teach", l: 2, en: "Nearly, just one small thing.", ex: "Nearly, just one small thing. Lower the jug.", zh: "差一点，就差一个小地方。", def: "Correct without discouraging.", th: "เกือบแล้ว เหลืออีกนิดเดียว" },
    { s: "teach", l: 2, en: "Don't worry about speed yet.", ex: "Don't worry about speed yet. Get it clean first.", zh: "先别管快慢。", def: "Set the right priority for a beginner.", th: "ยังไม่ต้องห่วงเรื่องความเร็ว" },
    { s: "teach", l: 2, en: "Do it ten times, then we'll talk.", ex: "Do it ten times, then we'll talk about what you felt.", zh: "先做十次，我们再聊。", def: "Assign repetition before discussion.", th: "ทำสิบครั้งก่อน แล้วค่อยคุยกัน" },
    { s: "teach", l: 2, en: "Everyone gather round for a second.", ex: "Everyone gather round for a second, I want to show you this.", zh: "大家过来一下。", def: "Call the class together.", th: "ทุกคนมารวมกันตรงนี้แป๊บนึง" },
    { s: "teach", l: 2, en: "Who wants to go first?", ex: "Right, who wants to go first?", zh: "谁想先来？", def: "Invite a volunteer.", th: "ใครอยากลองก่อน" },

    { s: "teach", l: 3, en: "Let's break that down into three steps.", ex: "It looks hard. Let's break that down into three steps.", zh: "我们把它拆成三步。", def: "Make a complex skill manageable.", th: "มาแยกเป็นสามขั้นตอนกัน" },
    { s: "teach", l: 3, en: "The mistake most people make here is rushing the tamp.", ex: "The mistake most people make here is rushing the tamp.", zh: "大多数人在这一步的错是压粉太急。", def: "Warn them before the common error happens.", th: "จุดที่คนส่วนใหญ่พลาดคือรีบกดกาแฟ" },
    { s: "teach", l: 3, en: "Once that becomes automatic, we'll add the next layer.", ex: "Once that becomes automatic, we'll add the next layer.", zh: "等这个变成本能，我们再加下一层。", def: "Explain how the course is structured.", th: "พอทำได้อัตโนมัติ ค่อยเพิ่มขั้นถัดไป" },
    { s: "teach", l: 3, en: "I'd rather you did it slowly and correctly.", ex: "I'd rather you did it slowly and correctly than fast and messy.", zh: "我宁可你慢但做对。", def: "State your standard clearly but kindly.", th: "อยากให้ทำช้าแต่ถูก มากกว่าเร็วแต่มั่ว" },
    { s: "teach", l: 3, en: "That's a really good question, actually.", ex: "That's a really good question, actually. Let me think.", zh: "这个问题问得真好。", def: "Reward a student for asking.", th: "คำถามนี้ดีมากเลยนะ" },
    { s: "teach", l: 3, en: "You're overthinking it, trust your hands.", ex: "You're overthinking it, trust your hands.", zh: "你想太多了，相信你的手。", def: "Free a student who is stuck in their head.", th: "คิดมากไปแล้ว เชื่อมือตัวเอง" },
    { s: "teach", l: 3, en: "Let's park the theory and just make some coffee.", ex: "Let's park the theory and just make some coffee.", zh: "理论先放一边，我们直接做。", def: "Switch the class from talking to doing.", th: "พักทฤษฎีไว้ก่อน มาลงมือชงกันเลย" },
    { s: "teach", l: 3, en: "By the end of today you'll be able to do this without me.", ex: "By the end of today you'll be able to do this without me.", zh: "今天结束你就能自己做了。", def: "Set the goal at the start of a session.", th: "จบวันนี้คุณจะทำเองได้โดยไม่ต้องมีผม" },

    /* ---------- 知识产权法（给 IP 律师）
       L1 定义取自 WIPO 官方口径，L2 程序词取自 USPTO 词表，L3 是跟客户开口的说法。
       泰文是「日常解释」，不是泰国法条术语 —— 术语他比我准。 ---------- */
    { s: "law", l: 1, en: "patent", col: "file a patent · grant a patent · a granted patent", ex: "The patent was granted in March.", zh: "专利", def: "An exclusive right granted for an invention (WIPO).", th: "สิทธิบัตร: สิทธิผูกขาดที่ให้กับสิ่งประดิษฐ์" },
    { s: "law", l: 1, en: "trademark", col: "register a trademark · a registered trademark", ex: "We registered the trademark in five countries.", zh: "商标", def: "A sign that distinguishes one enterprise's goods or services from another's (WIPO).", th: "เครื่องหมายการค้า: สัญลักษณ์ที่แยกสินค้าหรือบริการของแต่ละกิจการออกจากกัน" },
    { s: "law", l: 1, en: "copyright", col: "hold the copyright · assign copyright", ex: "The author still holds the copyright.", zh: "著作权", def: "The right creators have over their literary and artistic works (WIPO).", th: "ลิขสิทธิ์: สิทธิของผู้สร้างสรรค์เหนืองานวรรณกรรมและศิลปกรรม" },
    { s: "law", l: 1, en: "trade secret", col: "protect a trade secret · misappropriation", ex: "The formula is protected as a trade secret, not a patent.", zh: "商业秘密", def: "IP rights over confidential information that may be sold or licensed (WIPO).", th: "ความลับทางการค้า: สิทธิเหนือข้อมูลลับที่ขายหรือให้สิทธิใช้ได้" },
    { s: "law", l: 1, en: "industrial design", col: "register a design · design rights", ex: "The shape of the bottle is protected as an industrial design.", zh: "工业设计（外观设计）", def: "The ornamental or aesthetic aspect of an article (WIPO).", th: "การออกแบบอุตสาหกรรม: ลักษณะภายนอกหรือความสวยงามของผลิตภัณฑ์" },
    { s: "law", l: 1, en: "infringement", col: "allege infringement · a finding of infringement", ex: "They allege infringement of two claims.", zh: "侵权", def: "Using someone's IP right without permission.", th: "การละเมิด: ใช้สิทธิของผู้อื่นโดยไม่ได้รับอนุญาต" },
    { s: "law", l: 1, en: "licence", col: "grant a licence · an exclusive licence · royalties", ex: "We can grant you a non-exclusive licence.", zh: "许可（授权）", def: "Permission to use an IP right, usually for a fee.", th: "การอนุญาตให้ใช้สิทธิ: ให้สิทธิใช้ทรัพย์สินทางปัญญา มักมีค่าตอบแทน" },
    { s: "law", l: 1, en: "filing date", col: "the filing date · backdate · priority date", ex: "Everything turns on the filing date.", zh: "申请日", def: "The date an application is officially received.", th: "วันยื่นคำขอ: วันที่สำนักงานรับคำขออย่างเป็นทางการ" },

    { s: "law", l: 2, en: "prior art", col: "search prior art · cite prior art · anticipated by", ex: "That disclosure counts as prior art, so novelty is gone.", zh: "现有技术", def: "Any evidence the invention was already known before the filing date (USPTO).", th: "งานที่มีอยู่ก่อน: หลักฐานว่าสิ่งประดิษฐ์นี้เป็นที่รู้แล้วก่อนวันยื่นคำขอ" },
    { s: "law", l: 2, en: "office action", col: "respond to an office action · a final office action", ex: "We have three months to respond to the office action.", zh: "审查意见通知书", def: "The examiner's written decision on patentability, with the grounds for rejection (USPTO).", th: "หนังสือแจ้งผลการตรวจสอบจากนายทะเบียน พร้อมเหตุผลที่ปฏิเสธ" },
    { s: "law", l: 2, en: "prosecution", col: "patent prosecution · during prosecution", ex: "That argument was made during prosecution, so we're stuck with it.", zh: "（专利）审查程序", def: "The whole process of pushing an application through examination.", th: "กระบวนการดำเนินคำขอจนผ่านการตรวจสอบ" },
    { s: "law", l: 2, en: "claims", col: "draft claims · narrow the claims · claim scope", ex: "We'll need to narrow the claims to get around that reference.", zh: "权利要求", def: "The numbered sentences that define exactly what a patent covers.", th: "ข้อถือสิทธิ: ข้อความที่กำหนดขอบเขตความคุ้มครองของสิทธิบัตร" },
    { s: "law", l: 2, en: "cease and desist letter", col: "send a cease and desist · receive one", ex: "They sent a cease and desist letter last Friday.", zh: "停止侵权函", def: "A letter demanding that you stop using the accused mark or right (USPTO).", th: "หนังสือให้ยุติการกระทำ: จดหมายเรียกร้องให้หยุดใช้สิทธิที่ถูกกล่าวหาว่าละเมิด" },
    { s: "law", l: 2, en: "opposition", col: "file an opposition · oppose a mark", ex: "We filed an opposition within the two-month window.", zh: "异议", def: "A formal challenge to someone else's application before it registers.", th: "การคัดค้าน: การโต้แย้งคำขอของผู้อื่นก่อนได้รับจดทะเบียน" },
    { s: "law", l: 2, en: "due diligence", col: "run due diligence · an IP due diligence", ex: "We're running IP due diligence before the acquisition closes.", zh: "尽职调查", def: "Checking what IP a company really owns before a deal.", th: "การตรวจสอบสถานะ: ตรวจว่าบริษัทเป็นเจ้าของสิทธิอะไรจริงก่อนทำดีล" },
    { s: "law", l: 2, en: "assignment", col: "record the assignment · assign the rights", ex: "The assignment was never recorded, which is our problem.", zh: "权利转让", def: "Transferring ownership of an IP right to someone else.", th: "การโอนสิทธิ: โอนความเป็นเจ้าของไปยังบุคคลอื่น" },

    { s: "law", l: 3, en: "My reading of it is…", col: "my reading of it is · as I read it", ex: "My reading of it is that the licence never covered software.", zh: "我的理解是……", def: "Give a legal opinion while marking it as your view.", th: "ผมตีความว่า… (บอกความเห็นโดยระบุว่าเป็นมุมมองของเรา)" },
    { s: "law", l: 3, en: "It's arguable either way.", col: "arguable either way · finely balanced", ex: "Honestly, it's arguable either way. A court could go with them.", zh: "两边都说得通。", def: "Tell a client the outcome is genuinely uncertain.", th: "เถียงได้ทั้งสองทาง (บอกลูกค้าว่าผลลัพธ์ไม่แน่นอนจริง ๆ)" },
    { s: "law", l: 3, en: "I'd want to see the file history first.", col: "the file history · the prosecution history", ex: "Before I commit, I'd want to see the file history first.", zh: "我想先看审查历史再下结论。", def: "Refuse to give a snap opinion without the documents.", th: "ขอดูประวัติแฟ้มคำขอก่อนถึงจะสรุปได้" },
    { s: "law", l: 3, en: "That exposes you to a damages claim.", col: "exposure · exposed to a claim", ex: "Launching now exposes you to a damages claim.", zh: "这会让你面临索赔风险。", def: "Name the risk plainly to a client.", th: "แบบนั้นทำให้คุณเสี่ยงถูกเรียกค่าเสียหาย" },
    { s: "law", l: 3, en: "The commercial answer may not be the legal one.", col: "commercially · from a legal standpoint", ex: "The commercial answer may not be the legal one. Let's talk cost.", zh: "从生意角度和从法律角度，答案可能不一样。", def: "Separate what is legally right from what is worth doing.", th: "คำตอบทางธุรกิจอาจไม่ใช่คำตอบทางกฎหมาย" },
    { s: "law", l: 3, en: "We can push back on that.", col: "push back on · take issue with", ex: "Their scope claim is too wide. We can push back on that.", zh: "这一点我们可以反驳。", def: "Signal you will challenge the other side.", th: "เรื่องนี้เราโต้กลับได้" },
    { s: "law", l: 3, en: "Let's not put that in writing yet.", col: "in writing · on the record", ex: "Let's not put that in writing yet, it becomes discoverable.", zh: "这个先别落成文字。", def: "Warn a client about creating a record.", th: "เรื่องนี้อย่าเพิ่งเขียนเป็นลายลักษณ์อักษร" },
    { s: "law", l: 3, en: "Worst case, here's what it costs you.", col: "worst case · best case · realistically", ex: "Worst case, here's what it costs you: an injunction and legal fees.", zh: "最坏的情况，代价是这些。", def: "Frame risk in money and consequences, not law.", th: "กรณีแย่ที่สุด นี่คือสิ่งที่คุณต้องจ่าย" }
  ]
};
