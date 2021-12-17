// Navbar Slidebar
const bars = document.getElementById('bars');
const slider = document.querySelector('.slider');
const times = document.getElementById('times');

bars.addEventListener('click', function () {
    if (slider.classList.contains('show-slider')) {
        slider.classList.remove("show-slider")
    } else {
        slider.classList.add("show-slider")
    }
})
times.addEventListener('click', () => {
    slider.classList.remove('show-slider')
})


// Q and A
//using selectors inside the element
const questions = document.querySelectorAll(".question");
questions.forEach(function (question) {
    const btn = question.querySelector(".question-btn");

    btn.addEventListener("click", function () {
    questions.forEach(function (item) {
        if (item !== question) {
        item.classList.remove("show-text");
        }
    });
    question.classList.toggle("show-text");
    });
});


// Testimonials
const Testimonials = [
    // array of local reviews ;
    {
        id: 1,
        name: "Foo Smith",
        img: "/static/kidedu/images/avatar-2.svg",
        title: "I want to thank KIDEDU..",
        text: "Praesent scelerisque lacus eu laoreet scelerisque. In vel pulvinar urna, id ultricies arcu.",
    },
    {
        id: 2,
        name: "John Doe",
        img: "/static/kidedu/images/avatar1.svg",
        title: "Thank you KIDEDU ..",
        text: "Donec pretium laoreet urna, eu dictum elit porttitor sollicitudin. Fusce dui neque, lorem vitae, interdum ornare dolor.",
    },
    {
        id: 3,
        name: "Sara Jones",
        img: "/static/kidedu/images/avatar3.svg",
        title: "I appreciate the hard work you did KIDEDU..",
        text: "vulputate. Nulla vestibulum enim sed enim maximus egestas. Donec ac sem nisi. Sed dapibus faucibus dui.",
    },
    {
        id: 4,
        name: "Susan Smith",
        img: "/static/kidedu/images/comment.svg",
        title: "I like your own website KIDEDU..",
        text: " Nulla vestibulum enim sed enim maximus egestas. Donec ac sem nisi. Sed dapibus faucibus dui.",
    }
]
// Pick all items
const img = document.getElementById("user-img")
const user = document.querySelector(".username_8")
const title = document.getElementById("title_8")
const text = document.getElementById("text_8")

// buttons
let prevBtn = document.querySelector(".left")
let nextBtn = document.querySelector(".right")
const bullets = document.querySelectorAll(".bullets_8 li")

// starting item
let currentItem = 0
let pagContainer = document.createElement('ul')
const bodyContainer = document.querySelector(".part_2")
pagContainer.setAttribute('class', "bullets_8")
for (let i = 1; i <= Testimonials.length; i++){
    let paginItem = document.createElement('li')
    paginItem.setAttribute('data-index', i)
    pagContainer.append(paginItem)
}

bodyContainer.append(pagContainer)
let paginationArr = Array.from(document.querySelectorAll(".bullets_8 li"))
paginationArr[0].classList.add('active')
for (let i = 1; i < paginationArr.length; i++){
    paginationArr[i].onclick = () => {
        currentItem = parseInt(paginationArr[i].dataset.index)
        showPerson(i);
    }
}

function showPerson(person) {
    const item = Testimonials[person]
    removeActive()
    let ul = document.querySelector(".bullets_8")
    ul.children[person].classList.add('active')

    img.src = item.img
    user.textContent = item.name
    title.textContent = item.title
    text.textContent = item.text
}

function removeActive(){
    paginationArr.forEach((bullet) => {
        bullet.classList.remove('active')
    })
}

nextBtn.addEventListener('click', () => {
    currentItem++
    if (currentItem > Testimonials.length - 1) {
        // return the first element
        currentItem = 0
    } else {
        showPerson(currentItem)
    }
})
prevBtn.addEventListener('click', () => {
    currentItem--
    if (currentItem < 0) {
        // return the last item
        currentItem = Testimonials.length -1
    } else {
        showPerson(currentItem)
    }
})


// Memory Game
const cards = document.querySelectorAll(".memory-card")

let hasFlippedCard = false
let lockBoard = false
let firstCard, secondCard
shuffle()  // random card order
function flipcard() {
    if (lockBoard) return;
    if (this === firstCard) return;
    this.classList.toggle('flip')
    if (!hasFlippedCard) {
        // first click
        hasFlippedCard = true
        firstCard = this
        return;
    }

    secondCard = this
    checkForMatch();
}
function checkForMatch() {
    // matching cards
    let isMatch = firstCard.dataset.animal === secondCard.dataset.animal
    isMatch ? disableCards() : unflipCards();
}
function disableCards() {
    firstCard.removeEventListener('click', flipcard)
    secondCard.removeEventListener('click', flipcard)

    resetBoard();
}
function unflipCards() {
    // after card flipped
    lockBoard = true
    setTimeout(() => {
        firstCard.classList.remove("flip")
        secondCard.classList.remove("flip")
        
        resetBoard();
    },1200)
}
function resetBoard() {
    [hasFlippedCard, lockBoard] = [false, false]
    [firstCard, secondCard] = [null, null]
}
function shuffle() {
    cards.forEach(card => {
        let randomNum = Math.floor(Math.random() * 12)
        card.style.order = randomNum;
    })
}
cards.forEach(card => card.addEventListener('click', flipcard))
