/*show menu */

const navMenu = document.getElementById('nav-menu'),
      navToggle = document.getElementById('nav-toggle'),
      navClose = document.getElementById('nav-close')

      if(navToggle) {
          navToggle.addEventListener('click', () => {
              navMenu.classList.add('show-menu')
          })
      }

      if(navClose) {
          navClose.addEventListener('click', () => {
              navMenu.classList.remove('show-menu')
          })
      }


    const navLink = document.querySelectorAll('.navLink')

    function linkAction() {
        const navMenu = document.getElementById('.navLink')
        navMenu.classList.remove('show-menu')
    }

    navLink.forEach(n => n.addEventListener('click', linkAction))


    /* header change color */

    function scrollHeader() {
        const header = document.getElementById('header')
        if(this.scrollY >= 50) header.classList.add('scroll-header');
        else header.classList.remove('scroll-header')
    }

    window.addEventListener('scroll', scrollHeader)


    /* slider*/
    let newSwiper = new Swiper(".new-swiper", {
        centerdSlides: true,
        slidesPerView: "auto",
        loop: 'true',
        spaceBetween: 16,
    })    

    /*actvie menu */

    const sections = document.querySelectorAll('section[id]')

    function scrollActive() {
        const scrollY = window.pageYOffset

        sections.forEach(current => {
            const sectionHeight = current.offsetHeight,
            sectionTop = current.offsetTop -58,
            sectionId = current.getAttribute('id')

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                document.querySelector('.navM a[href*='+ sectionId +']').classList.add('active-link')

            }else {
                document.querySelector('.navM a[href*='+ sectionId +']').classList.remove('active-link')
            }
        })

      
    }

    window.addEventListener('scroll', scrollActive)



        /*scroll up */

function scrollUp () {
    const scrollUp = document.getElementById('scroll-up')

    if(this.scrollY >= 460) scrollUp.classList.add('show-scroll'); 
    else scrollUp.classList.remove('show-scroll')

}

window.addEventListener('scroll', scrollUp)

/* animation section */
const sr = ScrollReveal({
    origin: 'top',
    distance: '60px',
    duration: 2500,
    delay: 400,


})

sr.reveal(`.home-swiper, .new-swiper, .newslc`)
sr.reveal(`catdata, .footercontent`, {interval: 100})
sr.reveal(`.abdata, .disimg`, {origin:'left'})
sr.reveal(`.aboutimg, .disdata`, {origin:'left'})