$(function () {
    $("#id_data").datepicker({ dateFormat: 'dd-mm-yy' });
    $('#id_horario').timepicker({
        timeFormat: 'HH:mm',
        interval: 15, // intervalo de 15 minutos
        scrollbar: true, // exibir barra de rolagem para selecionar horas
        dropdown: true, // permitir menu para selecionar horas
        onSelect: function(timeText, inst) {
            // $('#id_horario').val(''); // removido para evitar limpar o valor atual
            $('#id_horario').val(timeText); // atribui o novo valor de hora selecionado ao campo de entrada
        }
    });
});
