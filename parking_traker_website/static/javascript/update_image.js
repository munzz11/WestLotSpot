
var index = 0;
function refresh_image(){
    source = $("#parking_image").attr("src");
    //remove previously added timestamps
    source = source.split("?", 1);
    new_source = source + "?timestamp="  + new Date().getTime();
    $("#parking_image").attr("src", new_source);
}

function refresh_data(current){
    // $('#total_count').attr('value', total);
    // $('#total_count').html('Total Spaces: '+total);
    refresh_image()
    var total = $('#total_count').attr('value');

    $('#current_count').attr('value', current);
    $('#current_count').html('Current Count: '+current);

    $('#available_count').attr('value', total-current);
    $('#available_count').html('Available Spaces: '+(total-current));
    //refresh_image()
}

function post_request(){
    //index++;
    //if (index>9){index = 0}
    //refresh_data()
    //console.log(index)
    $.ajax({
        type: 'POST',
        dataType: 'json',
        data:{
            //'index': index,
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }, success: function(data){
            //console.log('image is refreshed');
            refresh_data(data['count']);
            console.log($('#available_count').attr('value'))
        }

    });
}
//post_request();

setInterval(post_request, 10000);
