var chart_context = $('#graph')[0].getContext('2d')
var chart = new Chart(chart_context, {
    type: 'bar',
    data: {
        labels: time_labels,
        datasets: [{
            backgroundColor: 'rgb(0,99,132)',
            data: count_data,
        }]
    }
});

function update_graph(count, time){
    if (chart.data.datasets[0].data.length >= 10){
        chart.data.datasets[0].data.shift();
        chart.data.labels.shift();
    }

    chart.data.datasets[0].data.push(count);
    chart.data.labels.push(time);
    
    chart.update();
}

function post_request(){
    $.ajax({
        type: 'POST',
        dataType: 'json',
        data:{
            csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
        }, success: function(data){
            update_graph(data['current_count'],data['current_time']);
        }

    });
}
//post_request();

setInterval(post_request, 10000);