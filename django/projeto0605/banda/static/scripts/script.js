let navbar = document.querySelector('nav');
let colinha = nav.offsetTop;

function grudou(){
    if (window.pageYOffset >= colinha){
        navbar.classList.add('fixo');
    }
    else{
        navbar.classList.remove('fixo');
    }
}

window.onscroll = grudou();

alert('AAAAAAA');