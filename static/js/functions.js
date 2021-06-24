function mensaje(tit, msg, icon = 'success') {
  Swal.fire({
    title: tit,
    text: msg,
    icon: icon,
  });
}

function mensajeToast(tit, icon = 'success') {
  var Toast = Swal.mixin({
    toast: true,
    position: 'top-end',
    showConfirmButton: false,
    timer: 5500
  });

  Toast.fire({
    icon: icon,
    title: tit,
  });
}

function sweet_alert_action(title, content, icono, button, callback) {
  Swal.fire({
    title: title,
    text: content,
    icon: icono,
    showDenyButton: false,
    showCancelButton: true,
    confirmButtonColor: '#d33',
    confirmButtonText: button,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      callback();
    };
  })
}

function submit_with_ajax(url, parameters, title, content, icono, button, callback) {
  Swal.fire({
    title: title,
    text: content,
    icon: icono,
    showDenyButton: false,
    showCancelButton: true,
    confirmButtonText: button,
  }).then((result) => {
    /* Read more about isConfirmed, isDenied below */
    if (result.isConfirmed) {
      $.ajax({
        url: url, //window.location.pathname
        type: 'POST',
        data: parameters,
        dataType: 'json',
        processData: false,
        contentType: false,
      }).done(function (data) {
        console.log(data);
        if (!data.hasOwnProperty('error')) {
          callback();
          return false;
        }
        mensaje('Error', data.error, 'error');
      }).fail(function (jqXHR, textStatus, errorThrown) {
        alert(textStatus + ': ' + errorThrown);
      }).always(function (data) {

      });
    };
  })
};

/* Funcion para cambiar el lenguaje de la fecha en el timepicker */

function flatParameters() {
  var parametros = {
    firstDayOfWeek: 1,
    weekdays: {
      shorthand: ['Do', 'Lu', 'Ma', 'Mi', 'Ju', 'Vi', 'Sa'],
      longhand: ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado'],
    },
    months: {
      shorthand: ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Оct', 'Nov', 'Dic'],
      longhand: ['Enero', 'Febrero', 'Мarzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    },
  };

  return parametros
}