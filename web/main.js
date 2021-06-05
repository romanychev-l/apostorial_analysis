$(document).ready(function() {
    $("#inputfile").change((e) => {
        document.getElementsByClassName('input_file_label')[0].innerHTML = 'Изменить файл';

        if (e.target.files[0]) {
            var formData = new FormData(document.getElementById("form_gen"));

            $.ajax({
                type: "POST",
                url: "https://romanychev.online/dip/get_file",
                data: formData,
                processData: false,
                contentType: false

            }).done((event) => {
                console.log(event);
                document.getElementsByClassName('stat_block')[0].style.display = 'block';
                document.getElementsByClassName('stat_content')[0].innerHTML = `<img src="data:image/jpg;base64,${event.base64}" width="100%" />`;
                return false;
            });
        } else {
            alert('Выберите файл');
        }
        return false;
    });
});
