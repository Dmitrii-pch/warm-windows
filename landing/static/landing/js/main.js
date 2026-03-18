function toggleMenu() {
    const nav = document.querySelector('.nav');
    if (nav) {
        nav.classList.toggle('nav-open');
    }
}

function scrollToForm() {
    const el = document.getElementById('lead-form') || document.getElementById('products');
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
    }
}
