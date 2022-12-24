window.addEventListener("scroll", function(){
    var header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY> 0);
    let value = window.scrollY;
    document.getElementById('wave1').style.backgroundPositionX = 400 + value * 4 + 'px';
    document.getElementById('wave2').style.backgroundPositionX = 300 + value * -4 + 'px';
    document.getElementById('wave3').style.backgroundPositionX = 200 + value * 2 + 'px';
    document.getElementById('wave4').style.backgroundPositionX = 100 + value * -2 + 'px';
});
/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(e) {
if (!e.target.matches('.dropbtn')) {
var myDropdown = document.getElementById("myDropdown");
    if (myDropdown.classList.contains('show')) {
    myDropdown.classList.remove('show');
    }
}
};

const $drowdownArrow = document.querySelector('.arrow');
const $checkbox = document.getElementById('openDropdown');
const $dropdownMenu = document.querySelector('.dropdown-menu');

$dropdownMenu.addEventListener('click', (e) => {
  $checkbox.checked = false;
  // setting checked to false won't trigger 'change'
  // event, manually dispatch an event to rotate
  // dropdown arrow icon
  $checkbox.dispatchEvent(new Event('change'));
});

const $drowdownArrow1 = document.querySelector('.arrow1');
const $checkbox1 = document.getElementById('openDropdown1');
const $dropdownMenu1 = document.querySelector('.dropdown-menu1');

$dropdownMenu1.addEventListener('click', (e) => {
  $checkbox1.checked = false;
  $checkbox1.dispatchEvent(new Event('change'));
});

const $drowdownArrow2 = document.querySelector('.arrow2');
const $checkbox2 = document.getElementById('openDropdown2');
const $dropdownMenu2 = document.querySelector('.dropdown-menu2');

$dropdownMenu2.addEventListener('click', (e) => {
  $checkbox2.checked = false;
  $checkbox2.dispatchEvent(new Event('change'));
});

const $drowdownArrow3 = document.querySelector('.arrow3');
const $checkbox3 = document.getElementById('openDropdown3');
const $dropdownMenu3 = document.querySelector('.dropdown-menu3');

$dropdownMenu3.addEventListener('click', (e) => {
  $checkbox3.checked = false;
  $checkbox3.dispatchEvent(new Event('change'));
});

function openForm() {
  document.getElementById("myForm").style.display = "block";
}

function closeForm() {
  document.getElementById("myForm").style.display = "none";
} 


