(function () {
  "use strict";
  var params = new URLSearchParams(location.search);
  var id = params.get("id") || "0002";
  var item = COURSE.filter(function (x) { return x.id === id; })[0];
  var activeSpeech = null;
  function L(o) { var l = Store.lang(); return o[l] || o.en || o.zh; }
  function T(zh, en, th) { return Store.T(zh, en, th); }
  function escapeHtml(s) { return String(s).replace(/[&<>"']/g, function (c) { return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c]; }); }
  function speak(text, button) {
    if (!("speechSynthesis" in window)) return;
    window.speechSynthesis.cancel();
    if (activeSpeech === button && button.classList.contains("speaking")) { button.classList.remove("speaking"); activeSpeech = null; return; }
    document.querySelectorAll(".speak-btn.speaking").forEach(function (b) { b.classList.remove("speaking"); });
    var u = new SpeechSynthesisUtterance(text); u.lang = "en-GB"; u.rate = .82;
    activeSpeech = button; button.classList.add("speaking");
    u.onend = u.onerror = function () { button.classList.remove("speaking"); activeSpeech = null; };
    window.speechSynthesis.speak(u);
  }
  function renderMissing() {
    document.getElementById("lessonShell").innerHTML = '<div class="ask">' + T("找不到这节课。", "Lesson not found.", "ไม่พบบทเรียน") + ' <a href="course.html">' + T("返回课程目录", "Return to course", "กลับไปหน้าหลักสูตร") + '</a></div>';
  }
  function render() {
    if (!item) { renderMissing(); return; }
    document.title = item.id + " · " + L(item.title);
    var index = COURSE.map(function (x) { return x.id; }).indexOf(item.id);
    var prev = COURSE[index - 1], next = COURSE[index + 1];
    var translationLabel = Store.lang() === "th" ? "คำแปลไทย: " : (Store.lang() === "zh" ? "中文：" : "Meaning: ");
    var html = '';
    html += '<div class="lesson-progress"><span>' + T("第 " + item.week + " 周 · Lesson " + item.id, "Week " + item.week + " · Lesson " + item.id, "สัปดาห์ที่ " + item.week + " · บทเรียน " + item.id) + '</span><a href="course.html">' + T("查看全部 24 课", "View all 24 lessons", "ดูทั้งหมด 24 บท") + '</a></div>';
    html += '<p class="kicker">12 min speaking lesson</p><h1>' + escapeHtml(L(item.title)) + '</h1><p class="lede">' + escapeHtml(L(item.goal)) + '</p>';
    html += '<div class="lesson-tags-top">' + L(item.tags).map(function (x) { return '<span>' + escapeHtml(x) + '</span>'; }).join("") + '</div>';
    html += '<section class="lesson-focus"><p class="eyebrow">Today\'s focus</p><h2>' + T("今天只掌握一个重点", "Master one idea today", "วันนี้เรียนให้ได้หนึ่งประเด็น") + '</h2><p>' + escapeHtml(L(item.focus)) + '</p></section>';
    html += '<div class="section-heading"><div><p class="eyebrow">Listen · Repeat · Use</p><h2>' + T("5 句核心英文", "Five core lines", "5 ประโยคหลัก") + '</h2></div><p>' + T("每句按发音，跟读两次。", "Listen and repeat each line twice.", "ฟังและพูดตามแต่ละประโยคสองครั้ง") + '</p></div><div class="lesson-phrases">';
    item.phrases.forEach(function (p, i) {
      html += '<article class="lesson-phrase"><span class="phrase-index">' + (i + 1) + '</span><div><strong lang="en">' + escapeHtml(p.en) + '</strong><p>' + translationLabel + escapeHtml(L(p)) + '</p></div><button type="button" class="speak-btn" data-speak="' + escapeHtml(p.en) + '">🔊 ' + T("发音", "Listen", "ฟังเสียง") + '</button></article>';
    });
    html += '</div>';
    html += '<section class="partner-drill"><div><p class="eyebrow">Malaysia ↔ Thailand</p><h2>' + T("两人练习：一说一回应", "Partner drill: speak and respond", "ฝึกคู่: คนหนึ่งพูด อีกคนตอบ") + '</h2><p>' + T("马来西亚学生先选择一句，用自己的工作或生活资料替换关键词；泰国学生先复述意思，再用英文回应。然后交换。每轮只纠正一个错误。", "The Malaysian learner chooses a line and replaces its key details. The Thai learner restates the meaning, then responds in English. Switch roles and correct only one error per round.", "ผู้เรียนมาเลเซียเลือกหนึ่งประโยคและเปลี่ยนรายละเอียดให้เข้ากับชีวิตจริง ผู้เรียนไทยทวนความหมายแล้วตอบเป็นภาษาอังกฤษ จากนั้นสลับบทบาท และแก้เพียงหนึ่งจุดต่อรอบ") + '</p></div><div class="drill-turns"><span><b>A</b>' + T("说目标句", "Say the target line", "พูดประโยคเป้าหมาย") + '</span><i>→</i><span><b>B</b>' + T("复述 + 回应", "Restate + respond", "ทวน + ตอบ") + '</span><i>→</i><span><b>↺</b>' + T("交换角色", "Switch roles", "สลับบทบาท") + '</span></div></section>';
    html += '<div class="section-heading"><div><p class="eyebrow">Quick check</p><h2>' + T("马上检查", "Check it now", "ตรวจทันที") + '</h2></div></div>';
    html += '<div class="quiz" data-answer="' + item.quiz.answer + '"><div class="q">' + escapeHtml(L(item.quiz.q)) + '</div>';
    item.quiz.options.forEach(function (op) { html += '<button class="opt" data-why="' + escapeHtml(item.quiz.why.zh) + '" data-why-en="' + escapeHtml(item.quiz.why.en) + '" data-why-th="' + escapeHtml(item.quiz.why.th) + '" lang="en">' + escapeHtml(op) + '</button>'; });
    html += '<p class="why" hidden></p></div>';
    html += '<section class="lesson-mission"><p class="eyebrow">Real-world mission</p><h2>' + T("今天就把英文用出去", "Use it with a real person", "นำไปใช้กับคนจริงวันนี้") + '</h2><p>' + escapeHtml(L(item.mission)) + '</p><div data-practice="' + item.id + '"></div><div class="complete-slot" data-complete="' + item.id + '"></div></section>';
    html += '<nav class="lesson-pagination">';
    html += prev ? '<a href="' + prev.file + '"><small>' + T("上一课", "Previous", "บทก่อนหน้า") + '</small><strong>← ' + escapeHtml(L(prev.title)) + '</strong></a>' : '<a href="course.html"><small>' + T("课程目录", "Course", "หลักสูตร") + '</small><strong>← 24 Lessons</strong></a>';
    html += next ? '<a href="' + next.file + '"><small>' + T("下一课", "Next", "บทถัดไป") + '</small><strong>' + escapeHtml(L(next.title)) + ' →</strong></a>' : '<a href="course.html"><small>' + T("完成", "Complete", "เสร็จสิ้น") + '</small><strong>' + T("查看全部进度 →", "View full progress →", "ดูความคืบหน้าทั้งหมด →") + '</strong></a>';
    html += '</nav>';
    document.getElementById("lessonShell").innerHTML = html;
    document.querySelectorAll("[data-speak]").forEach(function (button) { button.addEventListener("click", function () { speak(button.dataset.speak, button); }); });
    Store.protectEnglish();
  }
  render();
  document.addEventListener("langchange", function () { render(); Store.refreshWidgets(); });
})();
