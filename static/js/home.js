let slideIndex = 0;
showSlides();

// Function to show slides
function showSlides() {
    let i;
    let slides = document.getElementsByClassName("mySlides");
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    slideIndex++;
    if (slideIndex >= slides.length) { slideIndex = 0; }    
    slides[slideIndex].style.display = "block";  
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

let hasCounted = false; // Flag to check if counting has occurred

window.addEventListener('scroll', function() {
    const counterSection = document.getElementById('counter-section');
    const sectionTop = counterSection.getBoundingClientRect().top;
    const sectionVisible = window.innerHeight - sectionTop >= 0; // Check if the section is visible

    if (sectionVisible && !hasCounted) {
        const counters = document.querySelectorAll('.counter');
        counters.forEach(counter => {
            const target = +counter.getAttribute('data-target');
            let count = 0;
            const speed = 2000; // Duration for counting in milliseconds
            const increment = target / speed * 100; // Calculate the increment

            const updateCount = setInterval(() => {
                count += increment;
                if (count >= target) {
                    count = target;
                    clearInterval(updateCount);
                }
                counter.innerText = Math.floor(count);
            }, 100);
        });
        hasCounted = true; // Set flag to true to prevent counting again
    }
});