// 秒回 v4 原型：离线缓存壳，页面走网络优先（有新版就换），静态文件缓存优先。
const CACHE = 'solowork-2';
const SHELL = ['./', './index.html', './app.css?v=4', './app.js?v=4', './manifest.webmanifest', './icon-192.png', './icon-512.png', './icon-180.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== CACHE).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  const req = e.request; if (req.method !== 'GET') return;
  const html = req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html');
  if (html) { e.respondWith(fetch(req).then(r => { const copy = r.clone(); caches.open(CACHE).then(c => c.put('./index.html', copy)); return r; }).catch(() => caches.match('./index.html'))); return; }
  e.respondWith(caches.match(req).then(hit => hit || fetch(req).then(r => { if (r.ok && new URL(req.url).origin === location.origin) { const copy = r.clone(); caches.open(CACHE).then(c => c.put(req, copy)); } return r; })));
});
