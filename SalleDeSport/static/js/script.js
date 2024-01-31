
// Afficher la barre de menu
const nav = document.querySelector('.nav');
const toggle = document.querySelector('.nav-toggle');

toggle.onclick = () => {
    nav.classList.toggle('show-menu');
}

// Supprimer la barre de menu
const navLinks = document.querySelectorAll('.nav-link');

function linkAction() {
    const navMenu = document.querySelector('.nav');
    navMenu.classList.remove('show-menu');
}

navLinks.forEach(link => link.addEventListener('click', linkAction));

// Changer la couleur du lien
const linkColors = document.querySelectorAll('.nav-link');

function colorLink() {
    // Utilisez l'argument de la fonction pour accéder à l'élément actuel
    linkColors.forEach(link => link.classList.remove('active'));
    this.classList.add('active');
}

linkColors.forEach(link => link.addEventListener('click', colorLink));
//Change header Background when scroll
const header = document.querySelector('.header')
window.addEventListener('scroll' , ()=>{
    if(window.scrollY >= 70){
        header.classList.add('header-shadaw')
    }
    else header.classList.remove('header-shadow')
})
//Sroll Top Button
const up = document.querySelector('.up')
Window.onscroll = () => {
    up.classList.toggle('show' , window.scrollY >= 560)
}
up.onclick = () => {
    window.scrollTo({behavior: 'smooth' , top: '0'})
}




