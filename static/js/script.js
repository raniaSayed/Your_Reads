
var stars = document.getElementsByClassName('fa');
var checked = 0;
for (var i = 0; i < stars.length; i++) {
  stars[i].addEventListener('click',function () {
      $(this).prevAll().addClass( "checked" );
      $(this).addClass( "checked" );

      $(this).nextAll().removeClass( "checked" );
      checked=1;

      //make ajax call to insert user_rate
  });
  stars[i].addEventListener('mouseenter',function () {
      if(!checked){
          $(this).prevAll().addClass( "checked" );
          $(this).addClass( "checked" );
      }
  }),
  stars[i].addEventListener('mouseleave',function () {
    if(!checked){
      $(this).prevAll().removeClass( "checked" );
      $(this).removeClass( "checked" );
    }
  });

}
