jQuery(document).ready(function () {
    CreateLoading();
});

function showDialog(dialogId) {
    $("#" + dialogId).dialog("open");
    $("#ui-datepicker-div").css("z-index", "9999");
    return false;
}
function HideDialog(dialogId) {
    $("#" + dialogId).dialog("close");
    return false;
}

function validateEmail(email) {
    var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(email);
}

function CreateLoading() {
    $("#loadingScreen").dialog({
        autoOpen: false,
        dialogClass: "loadingScreenWindow",
        closeOnEscape: false,
        draggable: false,
        width: 350,
        minHeight: 50,
        modal: true,
        buttons: {},
        resizable: false
        //open: function () {
        //    $('body').css('overflow', 'hidden');
        //},
        //close: function () {
        //    $('body').css('overflow', 'auto');
        //}
    });
}

function waitingDialog(waiting) {
    $("#loadingScreen").html(waiting.message && '' != waiting.message ? waiting.message : 'Espere, por favor...');
    $("#loadingScreen").dialog('option', 'title', waiting.title && '' != waiting.title ? waiting.title : 'Cargando');
    $("#loadingScreen").dialog('open');
}
function closeWaitingDialog() {
    $("#loadingScreen").dialog('close');
}

function compare_dates(fecha, fecha2) {

    var xMonth = fecha.substring(3, 5);
    var xDay = fecha.substring(0, 2);
    var xYear = fecha.substring(6, 10);
    var yMonth = fecha2.substring(3, 5);
    var yDay = fecha2.substring(0, 2);
    var yYear = fecha2.substring(6, 10);
    if (xYear > yYear) {
        return (true)
    }
    else {
        if (xYear == yYear) {
            if (xMonth > yMonth) {
                return (true)
            }
            else {
                if (xMonth == yMonth) {
                    if (xDay > yDay)
                        return (true);
                    else
                        return (false);
                }
                else
                    return (false);
            }
        }
        else
            return (false);
    }
}

function IsValidUrl(value) {
    var matcher = /(^|\s)((https?:\/\/)?[\w-]+(\.[\w-]+)+\.?(:\d+)?(\/\S*)?)/gi;

    var match = value.match(matcher)
    if (match)
        return true;
    else
        return false;
}

// valida si ha ocurrido un timeout durante una llamada ajax
function checkTimeout(data) {
    //debugger;
    var thereIsStillTime = true;

    if (data)
    {
        if (data.responseText)
        {
            if ((data.responseText.indexOf("<title>Login</title>") > -1) || (data.responseText.indexOf("<title>Object moved</title>") > -1) || (data.responseText === '"_Logon_"'))
                thereIsStillTime = false;
        }
        else
        {
            if (data == "_Logon_")
                thereIsStillTime = false;
        }

        if (!thereIsStillTime) {
            //window.location.href = "/Login/Timeout";
            //window.location.href = "https://stsqa.somosbelcorp.com/adfs/ls/?wa=wsignout1.0";
            window.location.href = "/SesionExpirada.html";
        }
    }
    else
    {
        //debugger;
        $.ajax({
            url: "/Dummy/",
            type: 'POST',
            dataType: 'json',
            contentType: 'application/json; charset=utf-8',
            async: false,
            complete: function (result) {
                thereIsStillTime = checkTimeout(result);
            }
        });
    }
    return thereIsStillTime;
}

//R2116-INICIO
FuncionesGenerales =
    {
        ValidarSoloNumeros: function (e) {
            var tecla = (document.all) ? e.keyCode : e.which;
            if (tecla == 8) return true;
            var patron = /[0-9]/;
            var te = String.fromCharCode(tecla);
            return patron.test(te);
        },

        ValidarSoloNumerosAndSpecialCharater: function (e) {
            var tecla = (document.all) ? e.keyCode : e.which;
            if (tecla == 8) return true;
            var patron = /[0-9-\-]/;
            var te = String.fromCharCode(tecla);
            return patron.test(te);
        }
    }
//R2116-FIN
