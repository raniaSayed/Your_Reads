
var stars = document.getElementsByClassName('fa');
var checked = 0;
for (var i = 0; i < stars.length; i++) {
  stars[i].addEventListener('click',function () {
      $(this).prevAll().addClass( "checked" );
      $(this).addClass( "checked" );

      $(this).nextAll().removeClass( "checked" );
      var n = $(this).index('.fa');
      checked=1;
      var book_id = document.getElementById("book_id").getAttribute("book_id");
      console.log(book_id)

      $.ajax({
         url: '/book/rate/'+ (n + 1)+"/"+book_id,
         // url: "{% url 'rate_book' "+(n+1)+" %}",
         method:'POST',
         dataType: 'json',
         success: function (data) {
             console.log(data);
         }
       });

      //make ajax call to insert user_rate
  });
  stars[i].addEventListener('mouseenter',function () {
      if(!checked){
          // $(this).prevAll().addClass( "checked" );
          // $(this).addClass( "checked" );

      }
  }),
  stars[i].addEventListener('mouseleave',function () {
    // if(!checked){
    //   $(this).prevAll().removeClass( "checked" );
    //   $(this).removeClass( "checked" );
    // }
  });

}
