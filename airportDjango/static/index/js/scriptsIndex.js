// const inputDep = document.getElementById('inputDep');
// const inputArr = document.getElementById('inputArr');
// const invisibleLabelDep = document.getElementById('invisibleLabelDep');
// const invisibleLabelArr = document.getElementById('invisibleLabelArr');

// inputDep.addEventListener('focus', () => {
//     inputDep.placeholder = '';
//     invisibleLabelDep.style.opacity = '1';
// });

// inputDep.addEventListener('blur', () => {
//     if (inputDep.value === '') {
//         inputDep.placeholder = 'Откуда';
//         invisibleLabelDep.style.opacity = '0';
//     }
// });

// inputArr.addEventListener('focus', () => {
//     inputArr.placeholder = '';
//     invisibleLabelArr.style.opacity = '1';
// });

// inputArr.addEventListener('blur', () => {
//     if (inputArr.value === '') {
//         inputArr.placeholder = 'Откуда';
//         invisibleLabelArr.style.opacity = '0';
//     }
// });

// window.addEventListener('DOMContentLoaded', function () {
//     var screenWidth = window.innerWidth;

//     // Проверьте, какой элемент скрывать при загрузке страницы
//     if (screenWidth <= 1400) {
//         document.getElementById('carousel').style.display = 'block';
//         document.getElementById('cards').style.display = 'none';
//     } else {
//         document.getElementById('carousel').style.display = 'none';
//         document.getElementById('cards').style.display = 'block';
//     }
// });

// window.addEventListener('resize', function () {
//     var screenWidth = window.innerWidth;

//     if (screenWidth <= 1400) {
//         document.getElementById('carousel').style.display = 'block';
//         document.getElementById('cards').style.display = 'none';
//         document.getElementById('carousel').style.padding = '0px 80px';
//     } else {
//         document.getElementById('carousel').style.display = 'none';
//         document.getElementById('cards').style.display = 'block';
//     }
// });

document.addEventListener("DOMContentLoaded", function () {
    const descriptions = document.querySelectorAll(".description");
    const slider = document.getElementById("mainSlider");

    slider.addEventListener("slid.bs.carousel", function () {
        const activeSlide = slider.querySelector(".carousel-item.active");
        const slideIndex = Array.from(slider.querySelectorAll(".carousel-item")).indexOf(activeSlide);

        // Определяем индекс активного слайда и обновляем описание
        if (descriptions[slideIndex]) {
            descriptions.forEach((description) => {
                description.style.display = "none";
            });
            descriptions[slideIndex].style.display = "block";
        }
    });
});


window.addEventListener('scroll', function () {
    let nav = document.querySelector('nav'); // Выбираем навигационный элемент
    let windowHeight = 150;

    if (nav) {
        if (window.scrollY > windowHeight) {
            // nav.style.backgroundColor = '#7caf7c'; // Измените фоновый цвет по вашему выбору
            nav.style.backgroundColor = '#242424'; // Измените фоновый цвет по вашему выбору
        } else {
            nav.style.backgroundColor = ''; // Верните фоновый цвет по умолчанию
        }
    }
});


// Создаем DOMParser один раз
const parser = new DOMParser();

async function getFlightCount() {
    try {
        const response = await fetch('https://www.flightaware.com/live/airport/UHWW', { cache: 'reload' });
        const html = await response.text();

        // Парсим HTML-контент
        const doc = parser.parseFromString(html, 'text/html');

        // Находим элемент на странице с информацией о количестве рейсов
        const flightCountElement = doc.getElementById('enroute-board');

        if (flightCountElement) {
            const flightCount = flightCountElement.textContent.trim();
            console.log(`Количество рейсов: ${flightCount}`);
        } else {
            console.log('Информация о количестве рейсов не найдена на странице.');
        }
    } catch (error) {
        console.error('Произошла ошибка:', error);
    }
}

getFlightCount();
