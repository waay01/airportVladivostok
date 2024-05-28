// // Функция для обработки кликов по страницам
// function handlePaginationClick(event) {
//     event.preventDefault();
//     const pageLink = event.target;
//     if (!pageLink.classList.contains('active')) {
//         // Удалите класс 'active' у всех ссылок на страницы
//         const pageLinks = document.querySelectorAll('.page-item');
//         pageLinks.forEach(link => link.classList.remove('active'));
//
//         // Добавьте класс 'active' к выбранной ссылке на страницу
//         pageLink.parentElement.classList.add('active');
//
//         // Вы можете использовать AJAX для получения и отображения содержимого выбранной страницы здесь
//         // Замените содержимое в ваших div с классом 'col-lg-4' на новые данные с сервера
//         // Пример: Используйте fetch() для отправки запроса на сервер и обновления содержимого
//     }
// }
//
// // Добавьте обработчики событий для ссылок пагинации
// const paginationLinks = document.querySelectorAll('.page-link');
// paginationLinks.forEach(link => link.addEventListener('click', handlePaginationClick));
