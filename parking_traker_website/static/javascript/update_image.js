
function refresh_image(){

    
    source = $("#parking_image").attr("src");
    //remove previously added timestamps
    source = source.split("?", 1);
    new_source = source + "?timestamp="  + new Date().getTime();
    $("#parking_image").attr("src", new_source);
}

function post_request(){
    $.ajax({
        type: 'POST',
        dataType: 'json',
        data:{
            'result': 'success',
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }, success: function(data){
            console.log('image is refreshed');
            refresh_image();
        }

    });
}

//setInterval(post_request, 10000);
