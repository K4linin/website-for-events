document.addEventListener('DOMContentLoaded', function () {
    console.log("main.js loaded");

    const videoItems = document.querySelectorAll('.video-item');
    const videoPlayer = document.getElementById('video-player');
    const videoSource = document.getElementById('video-source');
    const videoTitle = document.getElementById('video-title');

    console.log("Found video items:", videoItems.length);
    console.log("Video player:", videoPlayer);
    console.log("Video source:", videoSource);
    console.log("Video title element:", videoTitle);

    if (!videoItems.length) {
        console.error("No video items found. Check your HTML.");
        return;
    }

    if (!videoPlayer || !videoSource || !videoTitle) {
        console.error("Video player elements not found. Check your HTML IDs.");
        return;
    }

    videoItems.forEach(item => {
        item.addEventListener('click', function () {
            console.log("Video item clicked:", this);

            // Удаляем класс active у всех элементов
            videoItems.forEach(i => i.classList.remove('active'));
            // Добавляем класс active к текущему элементу
            this.classList.add('active');

            // Обновляем видео и заголовок
            const videoUrl = this.getAttribute('data-video-url');
            const title = this.getAttribute('data-video-title');

            console.log("Switching to video:", videoUrl, title);

            if (!videoUrl || !title) {
                console.error("Invalid video URL or title:", videoUrl, title);
                return;
            }

            // Обновляем источник видео
            videoSource.setAttribute('src', videoUrl);
            videoTitle.textContent = title;

            // Перезагружаем и воспроизводим видео
            videoPlayer.pause(); // Останавливаем текущее видео
            videoPlayer.load();  // Загружаем новое видео

            // Проверяем, можно ли автоматически воспроизвести видео
            const playPromise = videoPlayer.play();
            if (playPromise !== undefined) {
                playPromise.then(() => {
                    console.log("Video playback started successfully");
                }).catch(error => {
                    console.error("Error playing video:", error);
                    // Если автозапуск заблокирован, уведомляем пользователя
                    if (error.name === 'NotAllowedError') {
                        console.warn("Autoplay blocked. User interaction required.");
                        videoTitle.textContent += " (Нажмите на видео для воспроизведения)";
                    }
                });
            }
        });
    });
});