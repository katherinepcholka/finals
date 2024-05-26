let questions = document.querySelectorAll(".catalog-menu-container");

questions.forEach((elem) => {
    elem.addEventListener("click", (event) => openQuestion(event));
});

function openQuestion(question) {
    question.target.children[1].style.display = "flex";
}