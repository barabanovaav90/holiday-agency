document.addEventListener('DOMContentLoaded', function () {

    // --- 1. Кнопка "Наверх" (Scroll to Top) ---
    const scrollToTopBtn = document.getElementById('scrollToTopBtn');

    if (scrollToTopBtn) {
        // Показываем кнопку, если прокрутили больше 300px
        window.addEventListener('scroll', function () {
            if (window.scrollY > 300) {
                scrollToTopBtn.classList.remove('d-none');
                scrollToTopBtn.classList.add('fade-in');
            } else {
                scrollToTopBtn.classList.add('d-none');
                scrollToTopBtn.classList.remove('fade-in');
            }
        });

        // Плавная прокрутка наверх при клике
        scrollToTopBtn.addEventListener('click', function () {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    // --- 2. Калькулятор стоимости на странице услуг ---
    const calculatorCard = document.getElementById('calculatorCard');
    const toggleBtn = document.getElementById('toggleCalculatorBtn');

    // Логика сворачивания/разворачивания по кнопке с сохранением состояния
    if (toggleBtn && calculatorCard) {

        // Восстанавливаем состояние при загрузке
        const isCalcOpen = localStorage.getItem('calculatorOpen') === 'true';
        if (isCalcOpen) {
            calculatorCard.classList.remove('d-none');
        }

        toggleBtn.addEventListener('click', function () {
            if (calculatorCard.classList.contains('d-none')) {
                // Раскрыть
                calculatorCard.classList.remove('d-none');
                localStorage.setItem('calculatorOpen', 'true');
            } else {
                // Скрыть
                calculatorCard.classList.add('d-none');
                localStorage.setItem('calculatorOpen', 'false');
            }
        });
    }

    const calculatorBody = document.getElementById('costCalculator');

    if (calculatorBody) {
        const serviceSelect = document.getElementById('serviceSelect');
        const hoursInput = document.getElementById('hoursInput');
        const guestsInput = document.getElementById('guestsInput');
        const totalSpan = document.getElementById('totalCost');
        const calculateBtn = document.getElementById('calculateBtn');

        function calculateCost() {
            const basePrice = parseFloat(serviceSelect.options[serviceSelect.selectedIndex].dataset.price) || 0;
            const hours = parseInt(hoursInput.value) || 0;
            const guests = parseInt(guestsInput.value) || 0;

            // Примерная формула: (Цена услуги * Часы) + (Гости * 500р за человека)
            let total = (basePrice * hours) + (guests * 500);

            totalSpan.textContent = total.toLocaleString('ru-RU');
        }

        calculateBtn.addEventListener('click', calculateCost);

    }

    const dropdowns = document.querySelectorAll('.accessibility-dropdown');
    dropdowns.forEach(function (dropdown) {
        const menu = dropdown.querySelector('.dropdown-menu');
        if (menu) {
            dropdown.addEventListener('mouseenter', function () {
                menu.classList.add('show');
                menu.setAttribute('data-bs-popper', 'static');
            });
            dropdown.addEventListener('mouseleave', function () {
                menu.classList.remove('show');
                menu.removeAttribute('data-bs-popper');
            });
        }
    });
});
