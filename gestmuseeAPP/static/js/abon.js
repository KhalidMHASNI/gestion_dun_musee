const sign_in_btn = document.querySelector("#sign-in-btn");
const sign_up_btn = document.querySelector("#sign-up-btn");
const sign_in = document.querySelector(".sign-in-form");
const sign_up = document.querySelector(".sign-up-form");
const container = document.querySelector(".container");

sign_up_btn.addEventListener("click", () => {
    container.classList.add("sign-up-mode");
});

sign_in_btn.addEventListener("click", () => {
    container.classList.remove("sign-up-mode");
});

const sign_up_btn2 = document.querySelector("#sign-up-btn2");
const sign_in_btn2 = document.querySelector("#sign-in-btn2");

sign_up_btn2.addEventListener("click", () => {
    container.classList.add("sign-up-mode2");
});

sign_in_btn2.addEventListener("click", () => {
    container.classList.remove("sign-up-mode2");
});
