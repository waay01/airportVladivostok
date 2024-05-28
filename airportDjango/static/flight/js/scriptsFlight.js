// Получаем все элементы с классом "choose"
const chooseLinks = document.querySelectorAll('.choose');

// Получаем все div-элементы, которые мы хотим показывать/скрывать
const divsToShowHide = document.querySelectorAll('.one, .two, .three, .four, .five');

// Добавляем обработчик события для каждой ссылки
chooseLinks.forEach(link => {
    link.addEventListener('click', function (event) {
        // Отменяем стандартное действие ссылки
        event.preventDefault();

        // Убираем активный класс у всех ссылок
        chooseLinks.forEach(link => {
            link.classList.remove('activeChoose');
        });

        // Добавляем активный класс только выбранной ссылке
        this.classList.add('activeChoose');

        // Получаем значение атрибута data-target выбранной ссылки
        const target = this.getAttribute('data-target');

        // Показываем только соответствующий div, скрывая остальные
        divsToShowHide.forEach(div => {
            if (div.classList.contains(target)) {
                div.style.display = 'block';
            } else {
                div.style.display = 'none';
            }
        });
    });
});
