document.addEventListener('DOMContentLoaded', function () {
    const videoItems = document.querySelectorAll('.video-item');
    const videoPlayer = document.getElementById('video-player');
    const videoSource = document.getElementById('video-source');
    const videoTitle = document.getElementById('video-title');

    videoItems.forEach(item => {
        item.addEventListener('click', function () {
            // Удаляем класс active у всех элементов
            videoItems.forEach(i => i.classList.remove('active'));
            // Добавляем класс active к текущему элементу
            this.classList.add('active');

            // Обновляем видео и заголовок
            const videoUrl = this.getAttribute('data-video-url');
            const title = this.getAttribute('data-video-title');

            videoSource.setAttribute('src', videoUrl);
            videoTitle.textContent = title;

            // Перезагружаем видео
            videoPlayer.load();
            videoPlayer.play();
        });
    });
});