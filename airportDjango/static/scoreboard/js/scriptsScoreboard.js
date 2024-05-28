// setInterval(function () {
//     document.getElementById('reload').classList.add('fade-out');
//     setTimeout(function () {
//         location.reload();
//     }, 1000); // 1000 миллисекунд = 1 секунда (длительность анимации)
// }, 20000); // 15000 миллисекунд = 15 секунд


// Получите текущий URL
let currentUrl = window.location.href;

// Получите все ссылки с классом "nav-link"
let navLinks = document.querySelectorAll('.flightLink');

// Переберите ссылки и проверьте их href
for (let i = 0; i < navLinks.length; i++) {
    let link = navLinks[i];
    let linkHref = link.getAttribute('href');

    // Проверьте, содержит ли текущий URL часть href
    if (currentUrl.indexOf(linkHref) !== -1) {
        // Если ссылка соответствует текущему URL, добавьте класс "active"
        link.classList.add('activeFlight');
    }
}
