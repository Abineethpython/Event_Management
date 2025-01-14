let currentIndex = 0;

function showSlide(index) {
    const slides = document.querySelectorAll('.carousel-image');
    if (index >= slides.length) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = slides.length - 1;
    } else {
        currentIndex = index;
    }

    const offset = -currentIndex * 100; // Calculate offset
    document.querySelector('.carousel-images').style.transform = `translateX(${offset}%)`;
}

function moveSlide(direction) {
    showSlide(currentIndex + direction); // Update slide index based on direction
}

// Automatic sliding (optional)
setInterval(() => {
    moveSlide(1);
}, 3000); // Change slide every 3 seconds