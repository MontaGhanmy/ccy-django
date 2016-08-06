$("#images-selector").change(function (){
   var fileName = $(this).val();
   $('.images-preview').append("<li><img src='"+fileName+"'></li>");
 });