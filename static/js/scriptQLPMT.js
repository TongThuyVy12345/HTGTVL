$(document).ready(function() {
    $("#gototop").hide()
      $("#tototop").click(function(){
        $('html, body').animate({
            scrollTop:0
        });

    });


    $(window).scroll(function() {
        if ($(this).scrollTop() >=80){
            $('nav').css({
                "position":"fixed",
                "left":0,
                "right":0,
                "z-index":9999,
                "border-radius": "0px 0px 40px 40px",
                "background-color": "white",
            })
        }
        else
            $('nav').css({
                "position":"relative",
                "left":0,
                "right":0,
                "z-index":9999,
                "background-color": "#ffffff00",
                "border-radius": "0px 0px 0px 0px"
            })


       if ($(window).scrollTop() >= 100)
            $("#gototop").show("slow")
       else
            $("#gototop").hide("slow")
    })




    $("#gototop").click(function(){
        if (".trangchu"){
            $('html, body').animate({scrollTop:0},1000);
        }
    });

    $("#gioithieu").click(function(){
        if (".trangchu"){
            $('html, body').animate({scrollTop:500},500);
        }
    });





})
$(window).on('load',function(event){
    $('body').removeClass('preload')
    $('.load').delay(300).fadeOut('fast');
})




