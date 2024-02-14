// used for rating stars in the feedback.html page

document.addEventListener('DOMContentLoaded', function () {
    const stars = document.querySelectorAll('.star-rating i');
    stars.forEach(star => {
        star.addEventListener('click', setRating);
    });

    function setRating(e) {
        const starValue = parseInt(e.target.getAttribute('data-value'), 10);
        const starIndex = starValue - 1;
        document.getElementById('ratingInput').value = starValue;
        updateStars(starIndex);
    }

    function updateStars(index) {
        stars.forEach((star, idx) => {
            if (idx <= index) {
                star.classList.remove('far');
                star.classList.add('fas');
            } else {
                star.classList.add('far');
                star.classList.remove('fas');
            }
        });
    }
});
