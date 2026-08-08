/* 共用组件：语言(中/英/泰) + 难度 + 进度存储 + 测验 + 开口任务记录
   Shared: language (zh/en/th), level, progress store, quizzes, practice log.
   每页只要 <script src="../assets/app.js" defer></script> 就能用 */
(function () {
  "use strict";

  var LANGS = [["zh", "中文"], ["en", "English"], ["th", "ไทย"]];
  var WHO_KEY = "eng:who";
  var LANG_KEY = "eng:lang";
  var LEVEL_KEY = "eng:level";

  var ok = true;
  try { localStorage.setItem("eng:t", "1"); localStorage.removeItem("eng:t"); }
  catch (e) { ok = false; }

  // ---------- 语言 ----------
  function lang() {
    var l = ok ? localStorage.getItem(LANG_KEY) : document.documentElement.getAttribute("data-lang");
    return (l === "en" || l === "th") ? l : "zh";
  }
  function applyLang(l) {
    document.documentElement.setAttribute("data-lang", l);
    document.documentElement.setAttribute("lang", l);
    repaintQuizzes();
    document.dispatchEvent(new CustomEvent("langchange", { detail: l }));
  }
  function setLang(l) {
    if (ok) localStorage.setItem(LANG_KEY, l);
    applyLang(l);
  }
  // T("中文", "English", "ไทย") -> 当前语言那一个（缺泰文就退回英文）
  function T(zh, en, th) {
    var l = lang();
    if (l === "en") return en;
    if (l === "th") return th || en;
    return zh;
  }

  // ---------- 难度 ----------
  function level() {
    var n = parseInt(ok ? localStorage.getItem(LEVEL_KEY) : null, 10);
    return (n === 1 || n === 2 || n === 3) ? n : 2;
  }
  function setLevel(n) {
    if (ok) localStorage.setItem(LEVEL_KEY, String(n));
    document.documentElement.setAttribute("data-level", String(n));
    document.dispatchEvent(new CustomEvent("levelchange", { detail: n }));
  }

  // ---------- 顶部导航（每页自动出现，不用逐页写）----------
  var NAV = [
    { f: "index.html",      zh: "今天", en: "Today",    th: "วันนี้" },
    { f: "plan.html",       zh: "学习", en: "Learn",    th: "เรียน" },
    { f: "grammar.html",    zh: "语法", en: "Grammar",  th: "ไวยากรณ์" },
    { f: "vocab.html",      zh: "练习", en: "Practice", th: "ฝึก" },
    { f: "exam.html",       zh: "测验", en: "Check",    th: "ทดสอบ" },
    { f: "classmates.html", zh: "进度", en: "Progress", th: "ความคืบหน้า" }
  ];
  // 用样式表的相对路径推算根目录，子目录页面（lessons/、reference/）也能正确链接
  function base() {
    var link = document.querySelector('link[rel="stylesheet"]');
    var href = link ? link.getAttribute("href") : "assets/style.css";
    return href.replace(/assets\/style\.css.*$/, "");
  }
  function mountNav(langBar) {
    var b = base();
    var here = location.pathname.split("/").pop() || "index.html";

    // 跳到主内容（键盘用户不用一路 Tab 过导航）
    var skip = null;
    var h1 = document.querySelector("h1");
    if (h1) {
      if (!h1.id) h1.id = "top";
      h1.setAttribute("tabindex", "-1");
      skip = document.createElement("a");
      skip.className = "skip";
      skip.href = "#" + h1.id;
      skip.textContent = T("跳到主内容", "Skip to main content", "ข้ามไปยังเนื้อหาหลัก");
      document.addEventListener("langchange", function () {
        skip.textContent = T("跳到主内容", "Skip to main content", "ข้ามไปยังเนื้อหาหลัก");
      });
    }

    var shell = document.createElement("header");
    shell.className = "topbar";
    var brand = document.createElement("a");
    brand.className = "brand";
    brand.href = b + "index.html";
    brand.innerHTML = '<span class="brandmark" aria-hidden="true">E</span><span class="brandcopy"><strong>English OS</strong><small>Speaking workspace</small></span>';

    var nav = document.createElement("nav");
    nav.className = "topnav";
    nav.setAttribute("aria-label", T("主导航", "Main navigation", "เมนูหลัก"));
    document.addEventListener("langchange", function () {
      nav.setAttribute("aria-label", T("主导航", "Main navigation", "เมนูหลัก"));
    });
    NAV.forEach(function (n) {
      var a = document.createElement("a");
      a.href = b + n.f;
      a.dataset.f = n.f;
      if (n.f === here) a.setAttribute("aria-current", "page");
      nav.appendChild(a);
    });
    function paint() {
      Array.prototype.forEach.call(nav.children, function (a) {
        var n = NAV.filter(function (x) { return x.f === a.dataset.f; })[0];
        a.textContent = T(n.zh, n.en, n.th);
      });
    }
    paint();
    document.addEventListener("langchange", paint);
    shell.appendChild(brand);
    shell.appendChild(nav);
    if (langBar) shell.appendChild(langBar);
    document.body.insertBefore(shell, document.body.firstChild);
    // 跳转链接必须是 Tab 的第一站，所以最后插，插在最前面
    if (skip) document.body.insertBefore(skip, document.body.firstChild);
  }

  function mountLangSwitch() {
    var bar = document.createElement("div");
    bar.className = "langbar";
    LANGS.forEach(function (pair) {
      var b = document.createElement("button");
      b.type = "button";
      b.textContent = pair[1];
      b.dataset.l = pair[0];
      b.setAttribute("lang", pair[0]);
      b.addEventListener("click", function () { setLang(pair[0]); });
      bar.appendChild(b);
    });
    function paint() {
      Array.prototype.forEach.call(bar.children, function (b) {
        var on = b.dataset.l === lang();
        b.classList.toggle("on", on);
        b.setAttribute("aria-pressed", on ? "true" : "false");
      });
    }
    paint();
    document.addEventListener("langchange", paint);
    return bar;
  }

  // ---------- 难度选择器 <div data-levelpicker></div> ----------
  var LEVEL_NAMES = [
    null,
    { zh: "① 基础", en: "① Basic", th: "① พื้นฐาน" },
    { zh: "② 亚洲通用", en: "② International", th: "② สากล" },
    { zh: "③ 地道", en: "③ Native-like", th: "③ เหมือนเจ้าของภาษา" }
  ];
  var LEVEL_HINTS = [
    null,
    { zh: "短句为主，先求说得出、说得对。", en: "Short lines. The goal is to get the words out correctly.", th: "ประโยคสั้น เน้นพูดออกมาให้ถูกก่อน" },
    { zh: "亚洲跨国交流常用的清楚英文：自然、礼貌、容易听懂。", en: "Clear international English: natural, polite, and easy to understand across Asia.", th: "ภาษาอังกฤษสากลที่ชัดเจน เป็นธรรมชาติ สุภาพ และเข้าใจง่ายทั่วเอเชีย" },
    { zh: "带语气和分寸的说法，听起来像本地人。", en: "Lines with tone and nuance. This is where you stop sounding foreign.", th: "ประโยคที่มีน้ำเสียงและชั้นเชิง ฟังแล้วเหมือนคนท้องถิ่น" }
  ];
  function mountLevelPicker() {
    Array.prototype.forEach.call(document.querySelectorAll("[data-levelpicker]"), function (slot) {
      var bar = document.createElement("div");
      bar.className = "levelbar";
      var hint = document.createElement("p");
      hint.className = "why";
      [1, 2, 3].forEach(function (n) {
        var b = document.createElement("button");
        b.type = "button";
        b.dataset.n = String(n);
        b.addEventListener("click", function () { setLevel(n); });
        bar.appendChild(b);
      });
      function paint() {
        Array.prototype.forEach.call(bar.children, function (b) {
          var n = parseInt(b.dataset.n, 10);
          b.textContent = T(LEVEL_NAMES[n].zh, LEVEL_NAMES[n].en, LEVEL_NAMES[n].th);
          var on = n === level();
          b.classList.toggle("on", on);
          b.setAttribute("aria-pressed", on ? "true" : "false");
        });
        var h = LEVEL_HINTS[level()];
        hint.textContent = T(h.zh, h.en, h.th);
        hint.hidden = false;
      }
      paint();
      document.addEventListener("langchange", paint);
      document.addEventListener("levelchange", paint);
      slot.appendChild(bar);
      slot.appendChild(hint);
    });
  }

  // ---------- 进度 ----------
  function who() {
    if (!ok) return "guest";
    return localStorage.getItem(WHO_KEY) || "";
  }
  function setWho(name) { if (ok) localStorage.setItem(WHO_KEY, name); }

  function load() {
    if (!ok) return { done: {}, log: [], plan: {}, exams: [] };
    try {
      var raw = localStorage.getItem("eng:data:" + (who() || "guest"));
      var d = raw ? JSON.parse(raw) : {};
      return { done: d.done || {}, log: d.log || [], plan: d.plan || {}, exams: d.exams || [] };
    } catch (e) { return { done: {}, log: [], plan: {}, exams: [] }; }
  }
  function save(d) {
    if (!ok) return;
    localStorage.setItem("eng:data:" + (who() || "guest"), JSON.stringify(d));
  }
  // 本地日期，不是 UTC。toISOString() 在 UTC+8 会把早上 8 点前记成前一天
  function today() {
    var d = new Date();
    return d.getFullYear() + "-" +
      String(d.getMonth() + 1).padStart(2, "0") + "-" +
      String(d.getDate()).padStart(2, "0");
  }
  // 展示用日期：交给 Intl，不硬编码格式
  var LOCALES = { zh: "zh-Hans", en: "en-GB", th: "th-TH" };
  function fmtDate(iso) {
    if (!iso) return "";
    var p = String(iso).split("-");
    if (p.length !== 3) return String(iso);
    var d = new Date(Number(p[0]), Number(p[1]) - 1, Number(p[2]));
    if (isNaN(d.getTime())) return String(iso);
    try {
      return new Intl.DateTimeFormat(LOCALES[lang()] || "en-GB",
        { day: "numeric", month: "short", year: "numeric" }).format(d);
    } catch (e) { return String(iso); }
  }

  window.Store = {
    available: ok,
    who: who, setWho: setWho, load: load, save: save, today: today, fmtDate: fmtDate,
    lang: lang, setLang: setLang, T: T,
    // 异步提示统一走这里，保证被屏幕阅读器播报
    say: function (el, text) { if (!el) return; el.textContent = text; el.hidden = false; },
    protectEnglish: function () { protectEnglish(); },
    level: level, setLevel: setLevel, levelName: function (n) {
      var x = LEVEL_NAMES[n || level()];
      return T(x.zh, x.en, x.th);
    },
    isDone: function (id) { return !!load().done[id]; },
    addLog: function (entry) {
      var d = load();
      d.log.unshift({ date: today(), lesson: entry.lesson || "", text: entry.text || "" });
      save(d); return d;
    },
    addExam: function (r) {
      var d = load();
      d.exams.unshift({
        date: today(), scene: r.scene, level: r.level,
        score: r.score, total: r.total,
        pct: Math.round((r.score / r.total) * 100)
      });
      d.exams = d.exams.slice(0, 200);
      save(d); return d;
    },
    // 一份可分享的快照（同学进度页用）
    snapshot: function () {
      var d = load();
      return { who: who() || "?", level: level(), done: d.done, plan: d.plan, exams: d.exams, logCount: d.log.length, updated: today() };
    },
    friends: function () {
      if (!ok) return [];
      try { return JSON.parse(localStorage.getItem("eng:friends") || "[]"); }
      catch (e) { return []; }
    },
    saveFriend: function (snap) {
      if (!ok) return [];
      var list = this.friends().filter(function (f) { return f.who !== snap.who; });
      list.push(snap);
      localStorage.setItem("eng:friends", JSON.stringify(list.slice(0, 30)));
      return list;
    },
    removeFriend: function (name) {
      if (!ok) return [];
      var list = this.friends().filter(function (f) { return f.who !== name; });
      localStorage.setItem("eng:friends", JSON.stringify(list));
      return list;
    }
  };

  function warnNoStorage() {
    var w = document.createElement("p");
    w.className = "ask";
    w.setAttribute("role", "alert");
    w.textContent = T(
      "浏览器挡住了本地存储，进度不会被保存。换 Chrome 打开这个文件就正常了。",
      "Your browser is blocking local storage, so progress will not be saved. Opening this file in Chrome fixes it.",
      "เบราว์เซอร์บล็อกการเก็บข้อมูล ความคืบหน้าจะไม่ถูกบันทึก เปิดไฟล์นี้ด้วย Chrome แล้วจะใช้ได้ปกติ"
    );
    document.body.insertBefore(w, document.body.firstChild);
  }

  // ---------- 测验 ----------
  function whyText(quiz) {
    var picked = quiz.dataset.picked;
    if (picked === undefined) return null;
    var i = parseInt(picked, 10);
    var answer = parseInt(quiz.getAttribute("data-answer"), 10);
    var btn = quiz.querySelectorAll("button.opt")[i];
    var l = lang();
    var msg = btn.getAttribute("data-why");
    if (l === "en") msg = btn.getAttribute("data-why-en") || msg;
    if (l === "th") msg = btn.getAttribute("data-why-th") || btn.getAttribute("data-why-en") || msg;
    return (i === answer ? "✅ " : "❌ ") + (msg || "");
  }
  function repaintQuizzes() {
    Array.prototype.forEach.call(document.querySelectorAll(".quiz[data-answer]"), function (quiz) {
      var why = quiz.querySelector(".why");
      var t = whyText(quiz);
      if (why && t !== null) { why.textContent = t; why.hidden = false; }
    });
  }
  function mountQuizzes() {
    Array.prototype.forEach.call(document.querySelectorAll(".quiz[data-answer]"), function (quiz) {
      var answer = parseInt(quiz.getAttribute("data-answer"), 10);
      var opts = quiz.querySelectorAll("button.opt");
      var why = quiz.querySelector(".why");
      // aria-live 必须在内容变化「之前」就存在，否则不会被播报
      if (why) {
        why.setAttribute("aria-live", "polite");
        why.setAttribute("role", "status");
      }
      Array.prototype.forEach.call(opts, function (btn, i) {
        btn.type = "button";
        btn.addEventListener("click", function () {
          if (quiz.dataset.picked !== undefined) return;
          quiz.dataset.picked = String(i);
          Array.prototype.forEach.call(opts, function (b, j) {
            b.disabled = true;
            if (j === answer) {
              b.classList.add("right");
              b.setAttribute("aria-label", b.textContent + T("（正确答案）", " (correct answer)", " (คำตอบที่ถูก)"));
            }
          });
          if (i !== answer) {
            btn.classList.add("wrong");
            btn.setAttribute("aria-label", btn.textContent + T("（你选的，错）", " (your answer, wrong)", " (คำตอบของคุณ ผิด)"));
          }
          repaintQuizzes();
        });
      });
    });
  }

  // 英文教学内容不能被浏览器自动翻译掉
  function protectEnglish() {
    var sel = '[lang="en"], .en, .say, .entry .phrase, .entry .ex, .entry .col, .quiz button.opt';
    Array.prototype.forEach.call(document.querySelectorAll(sel), function (el) {
      el.setAttribute("translate", "no");
    });
  }

  // ---------- 「我做完了」 ----------
  function mountComplete() {
    Array.prototype.forEach.call(document.querySelectorAll("[data-complete]"), function (slot) {
      var id = slot.getAttribute("data-complete");
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "act";
      function paint() {
        var done = Store.isDone(id);
        btn.textContent = done
          ? T("✓ 已完成（点一下取消）", "✓ Done (tap to undo)", "✓ เสร็จแล้ว (แตะเพื่อยกเลิก)")
          : T("标记这一课做完了", "Mark this lesson done", "ทำบทเรียนนี้เสร็จแล้ว");
        btn.classList.toggle("ghost", done);
      }
      btn.addEventListener("click", function () {
        var d = load();
        if (d.done[id]) delete d.done[id]; else d.done[id] = today();
        save(d); paint();
      });
      paint();
      document.addEventListener("langchange", paint);
      slot.appendChild(btn);
    });
  }

  // ---------- 开口任务记录 ----------
  function mountPractice() {
    Array.prototype.forEach.call(document.querySelectorAll("[data-practice]"), function (slot) {
      var id = slot.getAttribute("data-practice");
      var lab = document.createElement("label");
      lab.setAttribute("for", "p-" + id);
      var ta = document.createElement("textarea");
      ta.id = "p-" + id;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "act";
      var msg = document.createElement("p");
      msg.className = "why";
      msg.setAttribute("aria-live", "polite");
      msg.setAttribute("role", "status");
      msg.hidden = true;

      function paint() {
        lab.textContent = T(
          "今天你真的说了哪一句？在什么场合？对方什么反应？",
          "Which line did you actually say today? Where? How did they react?",
          "วันนี้คุณพูดประโยคไหนออกไปจริง ๆ ที่ไหน แล้วอีกฝ่ายตอบสนองยังไง"
        );
        ta.placeholder = T(
          "例：跟设备供应商谈价，说了 That's a bit more than we budgeted for，对方主动降了 5%。",
          "e.g. Told a supplier \"That's a bit more than we budgeted for\" and he offered 5% off.",
          "เช่น บอกซัพพลายเออร์ว่า \"That's a bit more than we budgeted for\" แล้วเขาลดให้ 5%"
        );
        btn.textContent = T("存进我的记录", "Save to my log", "บันทึกไว้");
      }
      paint();
      document.addEventListener("langchange", paint);

      btn.addEventListener("click", function () {
        var t = ta.value.trim();
        if (!t) {
          msg.textContent = T("先写一句再存。", "Write something first.", "เขียนอะไรสักอย่างก่อน");
          msg.hidden = false; return;
        }
        Store.addLog({ lesson: id, text: t });
        ta.value = "";
        msg.textContent = T("✅ 存好了。回首页能看到全部记录。",
          "✅ Saved. You can see every entry on the home page.",
          "✅ บันทึกแล้ว ดูทั้งหมดได้ที่หน้าแรก");
        msg.hidden = false;
      });
      slot.appendChild(lab); slot.appendChild(ta); slot.appendChild(btn); slot.appendChild(msg);
    });
  }

  document.addEventListener("DOMContentLoaded", function () {
    applyLang(lang());
    document.documentElement.setAttribute("data-level", String(level()));
    var langBar = mountLangSwitch();
    mountNav(langBar);
    mountLevelPicker();
    if (!ok) warnNoStorage();
    mountQuizzes(); mountComplete(); mountPractice();
    protectEnglish();
  });
  document.addEventListener("langchange", protectEnglish);
})();
