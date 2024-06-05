document.addEventListener("DOMContentLoaded", function () {
    const desktopSlider = document.getElementById("mainSliderDesktop");
    const mobileSlider = document.getElementById("mainSliderMobile");

    if (desktopSlider) {
        const desktopDescriptions = document.querySelectorAll("[id^='descriptionDesktop']");
        desktopSlider.addEventListener("slid.bs.carousel", function () {
            const activeSlide = desktopSlider.querySelector(".carousel-item.active");
            const slideIndex = Array.from(desktopSlider.querySelectorAll(".carousel-item")).indexOf(activeSlide);

            if (desktopDescriptions[slideIndex]) {
                desktopDescriptions.forEach((description) => {
                    description.style.display = "none";
                });
                desktopDescriptions[slideIndex].style.display = "block";
            }
        });
    }

    if (mobileSlider) {
        const mobileDescriptions = document.querySelectorAll("[id^='descriptionMobile']");
        mobileSlider.addEventListener("slid.bs.carousel", function () {
            const activeSlide = mobileSlider.querySelector(".carousel-item.active");
            const slideIndex = Array.from(mobileSlider.querySelectorAll(".carousel-item")).indexOf(activeSlide);

            if (mobileDescriptions[slideIndex]) {
                mobileDescriptions.forEach((description) => {
                    description.style.display = "none";
                });
                mobileDescriptions[slideIndex].style.display = "block";
            }
        });
    }
});


window.addEventListener('scroll', function () {
    let nav = document.querySelector('nav'); // Выбираем навигационный элемент
    let windowHeight = 50;

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
        const response = await fetch('https://www.flightaware.com/live/airport/UHWW', {cache: 'reload'});
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


document.addEventListener('DOMContentLoaded', function () {
    function applyLineClamp() {
        const activeCarouselItem = document.querySelector('.carousel-item.active');
        const activeImage = activeCarouselItem.querySelector('.news-image');
        const descriptions = document.querySelectorAll('.description');

        if (activeImage) {
            const imageHeight = activeImage.clientHeight;

            descriptions.forEach(description => {
                const textContainer = description.querySelector('.truncate');

                // Find the corresponding active description
                const isActive = getComputedStyle(description).display !== 'none';

                if (isActive && textContainer) {
                    const lineHeight = parseInt(window.getComputedStyle(textContainer).lineHeight, 10);
                    const lines = Math.floor(imageHeight / lineHeight - 9);

                    // Debugging output
                    console.log(`Image height: ${imageHeight}px`);
                    console.log(`Line height: ${lineHeight}px`);
                    console.log(`Calculated lines: ${lines}`);

                    textContainer.style.webkitLineClamp = lines;
                }
            });
        }
    }

    const carousel = document.querySelector('#mainSlider, #mainSliderDesktop');

    carousel.addEventListener('slid.bs.carousel', function () {
        applyLineClamp();
    });

    window.addEventListener('resize', applyLineClamp);
    window.addEventListener('load', applyLineClamp);

    // Apply line clamp on initial load
    applyLineClamp();
});
