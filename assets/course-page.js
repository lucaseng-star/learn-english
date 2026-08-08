(function () {
  "use strict";
  function L(o) { var l = Store.lang(); return o[l] || o.en || o.zh; }
  function T(zh, en, th) { return Store.T(zh, en, th); }
  function render() {
    var data = Store.load();
    var doneCount = COURSE.filter(function (x) { return data.done[x.id]; }).length;
    var next = COURSE.filter(function (x) { return !data.done[x.id]; })[0] || COURSE[COURSE.length - 1];
    var pct = Math.round(doneCount / COURSE.length * 100);
    document.getElementById("courseScore").textContent = doneCount + " / " + COURSE.length;
    document.getElementById("coursePercent").textContent = pct + "%";
    document.getElementById("courseProgressBar").style.width = pct + "%";
    document.getElementById("continueCourse").href = next.file;

    var wrap = document.getElementById("courseWeeks"); wrap.textContent = "";
    for (var week = 1; week <= 12; week++) {
      var group = COURSE.filter(function (x) { return x.week === week; });
      var section = document.createElement("section"); section.className = "course-week";
      var head = document.createElement("div"); head.className = "week-head";
      var title = document.createElement("div");
      title.innerHTML = '<p class="eyebrow">' + T("第 " + week + " 周", "Week " + week, "สัปดาห์ที่ " + week) + '</p><h2>' + L(group[0].title) + ' → ' + L(group[1].title) + '</h2>';
      var status = document.createElement("span"); status.className = "week-status";
      var weekDone = group.filter(function (x) { return data.done[x.id]; }).length;
      status.textContent = weekDone + " / 2 " + T("完成", "done", "เสร็จ");
      head.appendChild(title); head.appendChild(status); section.appendChild(head);

      var grid = document.createElement("div"); grid.className = "course-lesson-grid";
      group.forEach(function (x) {
        var a = document.createElement("a"); a.href = x.file; a.className = "course-lesson-card";
        if (data.done[x.id]) a.classList.add("is-done");
        if (x.id === next.id) a.classList.add("is-current");
        var badge = data.done[x.id] ? "✓" : (x.id === next.id ? "▶" : x.id.slice(-2));
        a.innerHTML = '<span class="lesson-number">' + badge + '</span><div class="lesson-card-copy"><small>' + T("Lesson ", "Lesson ", "บทเรียน ") + x.id + ' · ' + x.minutes + T(" 分钟", " min", " นาที") + '</small><h3>' + L(x.title) + '</h3><p>' + L(x.goal) + '</p><span class="lesson-tags">' + L(x.tags).join(" · ") + '</span></div><i aria-hidden="true">→</i>';
        grid.appendChild(a);
      });
      section.appendChild(grid); wrap.appendChild(section);
    }
  }
  render();
  document.addEventListener("langchange", render);
})();
