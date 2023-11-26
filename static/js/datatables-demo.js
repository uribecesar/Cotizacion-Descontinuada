// Call the dataTables jQuery plugin
// $(document).ready(function() {
//   $('#dataTable').DataTable();
// });
$(document).ready(function() {
  $('#dataTable').DataTable({
    "language": {
      "sProcessing": "Procesando...",
      "sLengthMenu": "Mostrar _MENU_ registros",
      "sZeroRecords": "No se encontraron resultados",
      "sEmptyTable": "Ningún dato disponible en esta tabla =(",
      "sInfo": "Mostrando del _START_ al _END_ de un total de _TOTAL_",
      "sInfoEmpty": "Mostrando del 0 al 0 de un total de 0",
      "sInfoFiltered": "(filtrado de un total de _MAX_ registros)",
      "sInfoPostFix": "",
      "sSearch": "Buscar:",
      "sUrl": "",
      "sInfoThousands": ",",
      "sLoadingRecords": "Cargando...",
      "oPaginate": {
        "sFirst": "<<",
        "sLast": ">>",
        "sNext": ">",
        "sPrevious": "<"
      },
      "oAria": {
        "sSortAscending": ": Activar para ordenar la columna de manera ascendente",
        "sSortDescending": ": Activar para ordenar la columna de manera descendente"
      },
      "buttons": {
        "copy": "Copiar",
        "colvis": "Visibilidad"
      }
    },
    "columnDefs": [
      { "orderable": false, "targets": 'no-ordenar' }
    ],
    "order": [[ 0, "desc" ]
    ]
  });
});
