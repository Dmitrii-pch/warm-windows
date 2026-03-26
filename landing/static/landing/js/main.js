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

function scrollToSection(id) {
    const el = document.getElementById(id);
    if (el) {
        el.scrollIntoView({ behavior: 'smooth' });
    }
}

// Quiz
var quizData = {};

function quizSelect(btn, field, value) {
    var options = btn.parentElement.querySelectorAll('.quiz-option');
    options.forEach(function (o) { o.classList.remove('selected'); });
    btn.classList.add('selected');
    quizData[field] = value;
    var nextBtn = btn.closest('.quiz-step').querySelector('.quiz-next');
    nextBtn.disabled = false;
}

function quizNext(step) {
    document.getElementById('quiz-step-' + step).style.display = 'none';
    document.getElementById('quiz-step-' + (step + 1)).style.display = 'block';
    if (step === 3) {
        document.getElementById('quiz_type').value = quizData['type'] || '';
        document.getElementById('quiz_count').value = quizData['count'] || '';
        document.getElementById('quiz_time').value = quizData['time'] || '';
    }
}