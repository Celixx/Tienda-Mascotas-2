$(document).ready(function() {
    $('#formulario').validate({
        rules: {
            InputCant:{
                required: true
            },
            InputDscOferta:{
                required: true,
                min: 1
            }
        },
        messages:{
            InputCant:{
                required: "La cantidad es un campo obligatorio",
                
            },
            InputDscOferta:{
                required: "La cantidad es un campo obligatorio",
                min: "El minimo es mayor que 1"
            }
        }
    });

    var sin_imagen = '/static/core/images/sin-imagen.png';

    $("#id_categoria").change(function() {
      var categoriaId = $(this).val();
      if (categoriaId) {
        $.ajax({
          url: $('#url_obtener_productos').val(),
          data: {
            'categoria_id': categoriaId
          },
          dataType: 'json',
          success: function(data) {
            $("#id_producto").empty();
            $('#admin-bodega-imagen').attr('src', sin_imagen);
            if (data.length === 0) {
              $("#id_producto").append(`<option value="-1" data-imagen="${sin_imagen}">No hay productos disponibles</option>`);
            } else {
              $("#id_producto").append(`<option value="-1" selected="" data-imagen="${sin_imagen}">---------</option>`);
              $.each(data, function(key, value) {
                $("#id_producto").append(`<option value="${value.id}" data-imagen="${value.imagen}"> ${value.nombre} </option>`);
              });
            }
            $("#id_producto").prop('disabled', false);
          }
        });
      } else {
        $("#id_producto").empty();
        $("#id_producto").prop('disabled', true);
      }
    });
  
    $("#id_producto").change(function() {
      var opcionSeleccionada = $(this).find(':selected');
      var imagen = opcionSeleccionada.data('imagen');
      $('#admin-bodega-imagen').attr('src', imagen);
    });
  
    $("#id_nuevo").click(function() {
      $("#id_categoria").val('');
      $("#id_producto").empty();
      $("#id_producto").prop('disabled', true);
      $("#id_cantidad").val('');
      $('#admin-bodega-imagen').attr('src', sin_imagen);
      $("#id_categoria").focus();
    });
  
});




  