Swal.fire({
  title: "Error al Guardar Registro",
  text: "El alumno ya existe. No se puede crear el registro porque ya existe el DNI ingresado.",
  icon: "error"
}).then((result) => {
  if (result.isConfirmed) {
    window.location.href = "/registrar/"
  }
});

