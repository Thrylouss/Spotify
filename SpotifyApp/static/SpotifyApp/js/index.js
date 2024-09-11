document.addEventListener("DOMContentLoaded", function() {

    document.querySelector('.aside-btn').addEventListener('click', function() {
        document.querySelector('.aside').classList.toggle('active');
        document.querySelector('.main').classList.toggle('clear')
    })
})