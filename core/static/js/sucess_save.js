Swal.fire({
    title: "Registro Guardado",
    text: "El registro se guardo correctamente. ¿Desea agregar otro mas?",
    icon: "sucess",
    showCancelButton: true, // Muestra el botón "Cancelar"
  confirmButtonText: "Aceptar", // Texto del botón "Aceptar"
  cancelButtonText: "Cancelar", // Texto del botón "Cancelar"
  }).then((result) => {
    if (result.isConfirmed) {
      // El usuario hizo clic en "Aceptar"
      window.location.href = "/registrar/"
    } else if (result.dismiss === Swal.DismissReason.cancel) {
      window.location.href = "/"
    }});

  
  
  
  
  
  
  
  
