/*	Table OF Contents
==========================
1. Nav - Sticky
2. Nav - One Page 
3. TimeCircles Countdown
4. Magnific Popup
5. Ajax Form
6. Stellar Parallax
7. Owl Carrousel
*/

"use strict";
$(document).ready(function () {

    /*==============================
        5. Ajax Form
    ==============================*/
    $('#ajaxFormSubmit').on('click', function () {
        var Form = $('#ajaxForm');
        $('#fullscreenloading').show();
        $('#boxedResult').show();
        $('#sendResult').html('<div class="uil-rolling-css"><div><div></div><div></div></div></div>');
        $.ajax({
            type: 'POST',
            url: '/submit',
            data: Form.serialize(),
            success: function (msg) {
                console.log(msg);
                $('#sendResult').html('<img src="http://marttinfisher.com/themes/bodas/img/form-icon-ok.png"/><br/><span class="title success">Obrigado!</span><br/>Suas informações foram enviadas.<br /><br/><br /><button class="btn btn-default BtnCloseResult" type="button">Fechar</button>')
                location.reload();
            },
            error: function () {
                $('#sendResult').html('<img src="http://marttinfisher.com/themes/bodas/img/form-icon-error.png"/><br/><span class="title error">Desculpe!</span><br/>Seus dados não foram enviados. Por favor tente novamente.<br /><strong>Erro: #CL001</strong><br /><br /><button class="btn btn-default BtnCloseResult" type="button">Fechar</button>');
            }
        });
    });

});