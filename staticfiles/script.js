    $(document).ready(function(){
    $(window).scroll(function(){
        if(this.scrollY > 20){
            $('.navbar1').addClass("sticky");
        }else{
             $('.navbar1').removeClass("sticky");
        }
        if(this.scrollY > 500){
            $('.scroll-up-btn').addClass("show");
        }else{
            $('.scroll-up-btn').removeClass("show");
        }
    });

    // slide-up script
    $('.scroll-up-btn').click(function(){
        $('html').animate({scrollTop: 0});
    });
    //toggle menu bar script
    $('.menu-btn').click(function(){
        $('.navbar1 .menu').toggleClass("active");
         $('.menu-btn i').toggleClass("active");
    });

    //carousel-code
    //owl carousel script
    $('.carousel').owlCarousel({
       margin: 30,
       loop: true,
       items: 4,
       responsive: {
           0:{
               items: 1,
              
           },
           600:{
               items: 2,
               
           },
           1000:{
               items: 4,
               
           }
       }
    });

    
});