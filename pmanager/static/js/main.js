$(document).ready(function(){


    console.log("jquery loads");


    $('body').addClass("ready");
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();

    $('#description').text().trim();

});
