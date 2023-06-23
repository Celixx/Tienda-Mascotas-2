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

    
});

$(document).ready(function() {
    $('#formulario1').validate({
        rules: {
            rut: {
                required: true,
                rutChileno: true
            },
            username: {
                required: true
            },
            nombre: {
                required: true
            },
            apellido: {
                required: true
            },
            correo: {
                required: true,
                email: true
            },
            direccion: {
                required: true,
            },
            subscrito: {
                required: false,
            },
            password1: {
                required: true,
                minlength: 5
            },
            password2: {
                required: true,
                equalTo: "#id_password1"
            },
            imagen: {
                required: true,
            },
        },
        messages: {
            rut: {
                required: "El RUT es un campo obligatorio",
                rutChnileno: "El formato del rut es incorrecto"
            },
            username: {
                required: "El username es un campo obligatorio"
            },
            nombre: {
                required: "El nombre es un campo obligatorio"
            },
            apellido: {
                required: "El apellido es un campo obligatorio"
            },
            correo: {
                required: "El correo es un campo obligatorio",
                email: "El correo no cumple con el formato de un correo"
            },
            direccion: {
                required: "La dirección es un campo obligatorio"
            },
            password1: {
                required: "La contraseña es un campo obligatorio",
                minlength: "La longitud mínima es de 5 caracteres"
            },
            password2: {
                required: "Verificar la contraseña es obligatorio",
                equalTo: "Las contraseñas no coinciden"
            },
        }
    });
});

$(document).ready(function() {
    $('#formulario2').validate({
        rules: {
            InputCorreo:{
                required: true,
                email: true
            },
            InputClave:{
                required: true,
                minlength: 5
            }
        },
        messages:{
            InputCorreo:{
                required: "El correo es un campo obligatorio",
                email: "El correo no cumple con el formato de un correo"
            },
            InputClave:{
                required: "La contraseña es un campo obligatorio",
                minlength: "La longitud mínima es de 5 caracteres"
            }
        }
    });

});

$(document).ready(function(){
    $('#formulario3').validate({
        rules: {
            InputId:{
                required: true,
                email: false
            },
            InputPrecio:{
                required: true,
                email: false
            },
            select:{
                required: true
            }
        },
        messages: {
            InputId:{
                required: "La id es un campo obligatorio"
            },
            InputPrecio:{
                required: "El precio es un campo obligatorio"
            },
            select:{
                required: "Debe seleccionar una categoria"
            }
        }
    });
});