
let slideIndex = 0;
showSlides();

function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex >= slides.length) { slideIndex = 0; }
    slides[slideIndex].style.display = "block";
    setTimeout(showSlides, 3000);
}

let hasCounted = false;
window.addEventListener('scroll', function () {
    const counterSection = document.getElementById('counter-section');
    const sectionTop = counterSection.getBoundingClientRect().top;
    const sectionVisible = window.innerHeight - sectionTop >= 0;

    if (sectionVisible && !hasCounted) {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            let count = 0;
            const speed = 2000;
            const increment = target / speed * 100;

            const updateCount = setInterval(() => {
                count += increment;
                if (count >= target) {
                    count = target;
                    clearInterval(updateCount);
                }
                counter.innerText = Math.floor(count);
            }, 100);
        });
        hasCounted = true;
    }
});

document.addEventListener("DOMContentLoaded", function () {
    const element = document.getElementById("typewriter-text");
    const fullText = element.innerText;
    let index = 0;
    let isDeleting = false;

    function typeEffect() {
        if (!isDeleting) {
            element.innerText = fullText.slice(0, index);
            index++;
            if (index > fullText.length) {
                isDeleting = true;
                setTimeout(typeEffect, 1000);
                return;
            }
        } else {
            element.innerText = fullText.slice(0, index);
            index--;
            if (index < 0) {
                isDeleting = false;
                setTimeout(typeEffect, 1000);
                return;
            }
        }
        setTimeout(typeEffect, isDeleting ? 40 : 80);
    }

    typeEffect();
});
