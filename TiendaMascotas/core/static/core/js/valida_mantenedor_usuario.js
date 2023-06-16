$(document).ready(function() {

    $.validator.addMethod("rutChileno", function(value, element) {
        // Eliminar puntos y guión del RUT
        value = value.replace(/[.-]/g, "");
    
        // Validar que el RUT tenga 8 o 9 dígitos
        if (value.length < 8 || value.length > 9) {
          return false;
        }
    
        // Validar que el último dígito sea un número o una 'K'
        var validChars = "0123456789K";
        var lastChar = value.charAt(value.length - 1).toUpperCase();
        if (validChars.indexOf(lastChar) == -1) {
          return false;
        }
    
        // Calcular el dígito verificador
        var rut = parseInt(value.slice(0, -1), 10);
        var factor = 2;
        var sum = 0;
        var digit;
        while (rut > 0) {
          digit = rut % 10;
          sum += digit * factor;
          rut = Math.floor(rut / 10);
          factor = factor === 7 ? 2 : factor + 1;
        }
        var dv = 11 - (sum % 11);
        dv = dv === 11 ? "0" : dv === 10 ? "K" : dv.toString();
    
        // Validar que el dígito verificador sea correcto
        return dv === lastChar;
      }, "Por favor ingrese un RUT válido."); 


    $('#formulario1').validate({
        rules: {
            InputId: {
                required: true
                
            },
            InputRut: {
                required: true,
                rutChileno: true
            },
            InputNombres: {
                required: true
            },
            InputApellidos: {
                required:true
            },
            InputCorreo: {
                required: true,
                email: true
            },
            InputDireccion: {
                required: true
            },
            InputContraseña: {
                required: true,
                minlength: 5
            }
        },
        messages: {
            InputId: {
                required: "El ID es un campo obligatorio"
            },
            InputRut: {
                required: "El RUT es un campo obligatorio"
            },
            InputNombres: {
                required: "El nombre es un campo obligatorio"
            },
            InputApellidos: {
                required: "Los apellidos son un campo obligatorio"
            },
            InputCorreo: {
                required: "El correo es un campo obligatorio",
                email: "El correo no cumple con el formato de un correo"
            },
            InputDireccion: {
                required: "La dirección es un campo obligatorio"
            },
            InputContraseña: {
                required: "La contraseña es un campo obligatorio",
                minlength: "La longitud mínima es de 5 caracteres"
            }
        }

    });

});