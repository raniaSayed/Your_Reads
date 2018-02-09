
var stars = document.getElementsByClassName('fa-star');
var heart = document.getElementsByClassName('fa-heart');

for (var i = 0; i < heart.length; i++) {
  heart[i].addEventListener('click',function () {

      if($(this).hasClass("checked")){
        $(this).removeClass( "checked" );
      }else{
        $(this).addClass( "checked" );
      }

      var category_id = this.getAttribute("cat_id");
      console.log(category_id)

      //make ajax call to insert user_rate
      $.ajax({
         url: '/book/category/'+category_id,
         // url: "{% url 'rate_book' "+(n+1)+" %}",
         method:'POST',
         dataType: 'json',
         success: function (data) {
             console.log(data);
         }
       });

  });
}
for (var i = 0; i < stars.length; i++) {
  stars[i].addEventListener('click',function () {
      $(this).prevAll().addClass( "checked" );
      $(this).addClass( "checked" );

      $(this).nextAll().removeClass( "checked" );
      var n = $(this).index('.fa');
      checked=1;
      var book_id = document.getElementById("book_id").getAttribute("book_id");
      console.log(book_id)

      //make ajax call to insert user_rate
      $.ajax({
         url: '/book/rate/'+ (n + 1)+"/"+book_id,
         // url: "{% url 'rate_book' "+(n+1)+" %}",
         method:'POST',
         dataType: 'json',
         success: function (data) {
             console.log(data);
         }
       });

  });
}
