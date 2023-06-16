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

});