// solowork 原型：离线缓存壳 + 推送。页面走网络优先（有新版就换），静态文件缓存优先。
const CACHE = 'solowork-9';
const LOG = 'solowork-pushlog';
const SHELL = ['./', './index.html', './app.css?v=4', './app.js?v=4', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-180.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request; if (req.method !== 'GET') return;
  if (new URL(req.url).pathname.startsWith('/api/')) return;             // 推送接口不缓存
  const html = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (html) { e.respondWith(fetch(req).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put('./index.html', copy)); return r; }).catch(() => caches.match('./index.html'))); return; }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => { if (r.ok && new URL(req.url).origin === location.origin) { const copy = r.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return r; })));
});

// 🔔 推送：通知里带客户 id，点开直达那个客户（不是首页）
self.addEventListener('push', e => {
  let d = {};
  try { d = e.data ? e.data.json() : {}; } catch { d = { body: e.data && e.data.text() }; }
  const now = Date.now();
  const lag = d.sentAt ? (now - d.sentAt) / 1000 : null;                       // 服务器推出去 → 你手机收到，用了几秒
  const title = d.title || '🆘 有客户在等';
  const body = (d.body || '') + (lag !== null ? `\n⏱ ${lag.toFixed(1)} 秒到${d.kind ? ' · ' + d.kind : ''}` : '');
  e.waitUntil(Promise.all([
    self.registration.showNotification(title, { body, icon: './icon-192.png', badge: './icon-192.png',
      tag: 'sos-' + now, renotify: true, requireInteraction: !!d.sticky,
      data: { cid: d.cid || '', sentAt: d.sentAt || now, at: now, kind: d.kind || '' } }),
    // 存一笔，app 下次打开会读走 —— 你不点它也算数
    caches.open(LOG).then(c => c.put('/__push/' + now, new Response(JSON.stringify({ sentAt: d.sentAt || now, at: now, kind: d.kind || '' }), { headers: { 'content-type': 'application/json' } }))),
  ]));
});
self.addEventListener('notificationclick', e => {
  e.notification.close();
  const cid = (e.notification.data && e.notification.data.cid) || '';
  const url = './' + (cid ? '?c=' + encodeURIComponent(cid) : '');
  e.waitUntil(clients.matchAll({ type: 'window', includeUncontrolled: true }).then(list => {
    for (const c of list) if ('focus' in c) { c.postMessage({ type: 'open', cid, sentAt: e.notification.data && e.notification.data.sentAt }); return c.focus(); }
    return clients.openWindow(url);
  }));
});
