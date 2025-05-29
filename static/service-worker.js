self.addEventListener('install', function(event) {
    console.log('Service Worker installing.');
});

self.addEventListener('activate', function(event) {
    console.log('Service Worker activating.');
});

self.addEventListener('push', function(event) {
    const data = event.data.json();
    self.registration.showNotification(data.title, {
        body: data.body,
        icon: '/static/icons/icon-192.png'
    });
});