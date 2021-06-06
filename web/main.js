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
                document.getElementsByClassName('stat_content')[0].innerHTML = `<img src="data:image/jpg;base64,${event.base64_1}" width="100%" />`;
                document.getElementsByClassName('stat_content2')[0].innerHTML = `<img src="data:image2/jpg;base64,${event.base64_2}" width="100%" />`;
                document.getElementsByClassName('stat_content_x')[0].innerHTML = `<div>Хи^2 = ${event.xi_2}</div>`;
                return false;
            });
        } else {
            alert('Выберите файл');
        }
        return false;
    });
});
