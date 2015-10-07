$(function(){
    $('#header_nav').data('size','big');
});

$(window).scroll(function(){
    if($(document).scrollTop() > 0)
    {
        if($('#header_nav').data('size') == 'big')
        {
            $('#header_nav').data('size','small');
            $('#header_nav').stop().animate({
                fontSize:'25px'
            },600);
            $('#header_nav').stop().animate({
                fontSize:'25px',
                marginLeft: '-50px',
                marginTop: '-30px'
            },600);
        }
    }
    else
    {
        if($('#header_nav').data('size') == 'small')
        {
            $('#header_nav').data('size','big');
            $('#header_nav').stop().animate({
                fontSize:'42px'
            },600);
            $('#header_nav').stop().animate({
                fontSize:'82px',
                marginLeft: '510px',
                marginTop: '0px'
            },600);
        }
    }
});
