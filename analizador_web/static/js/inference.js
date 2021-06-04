$(document).ready(function (){
  $('#file-inference-btn').on('click', function (e) {
  e.preventDefault()
  var form_data = new FormData($('#analize-file-form')[0]);
      $.ajax({
          url: '/obtener_datos',
          data: form_data,
          type: 'POST',
          contentType: false,
          processData: false,
          success: function(response){
              $("#imagen-freq").attr('src','data:image/png;base64,'+response.data);
          },
          error: function(error){
      console.log("Error");
          }
      }); 
  });
});
