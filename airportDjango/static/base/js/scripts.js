// // Меню с новостях
// // Получаем все ссылки в меню
//   const menuItems = document.querySelectorAll(".leftmenuItem");
//
//   // Обрабатываем клик по ссылкам
//   menuItems.forEach((item) => {
//     item.addEventListener("click", (event) => {
//       // Удаляем класс 'active' у всех ссылок
//       menuItems.forEach((menuItem) => {
//         menuItem.classList.remove("active");
//       });
//
//       // Добавляем класс 'active' к кликнутой ссылке
//       event.currentTarget.classList.add("active");
//
//       // Сохраняем состояние активной вкладки в sessionStorage
//       sessionStorage.setItem("activeTab", event.currentTarget.getAttribute("href"));
//     });
//   });
//
//   // Восстанавливаем активную вкладку при загрузке страницы
//   const activeTab = sessionStorage.getItem("activeTab");
//   if (activeTab) {
//     const activeMenuItem = document.querySelector(`[href="${activeTab}"]`);
//     if (activeMenuItem) {
//       activeMenuItem.classList.add("active");
//     }
//   }


document.addEventListener('DOMContentLoaded', function() {
    var links = document.querySelectorAll('.linkMenuItems');

    links.forEach(function(link) {
        link.addEventListener('click', function(event) {
            // Удаляем класс 'active' у всех ссылок
            links.forEach(function(link) {
                link.classList.remove('active');
            });

            // Добавляем класс 'active' к нажатой ссылке
            event.target.classList.add('active');
        });
    });
});


const parallaxContainer = document.querySelector('.parallax');
const text1 = document.querySelector('#text1');
const text2 = document.querySelector('#text2');

parallaxContainer.addEventListener("mousemove", (e)  => {
    const x = (e.clientX / window.innerWidth) * 100;
    const y = (e.clientY / window.innerHeight) * 100;

    // Задаем скорость движения текста
    const textSpeed = 0; // Вы можете настроить это значение под свои нужды

    // Перемещаем текст в противоположном направлении от движения мыши
    text1.style.transform = `translateY(-${y * textSpeed}px)`;
    text2.style.transform = `translateY(-${y * textSpeed * 0.5}px)`;
});


SmoothScroll({
    // Время скролла 400 = 0.4 секунды
    animationTime    : 800,
    // Размер шага в пикселях
    stepSize         : 75,

    // Дополнительные настройки:

    // Ускорение
    accelerationDelta : 30,
    // Максимальное ускорение
    accelerationMax   : 2,

    // Поддержка клавиатуры
    keyboardSupport   : true,
    // Шаг скролла стрелками на клавиатуре в пикселях
    arrowScroll       : 50,

    // Pulse (less tweakable)
    // ratio of "tail" to "acceleration"
    pulseAlgorithm   : true,
    pulseScale       : 4,
    pulseNormalize   : 1,

    // Поддержка тачпада
    touchpadSupport   : true,
})