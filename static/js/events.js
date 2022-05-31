$(document).ready(function (){
    $('#search-btn').on('click',function (e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        // var checkbox = $()
        $.ajax({
            url:'/events?search_filter=' + searchText,
            type: 'GET',
            success: function(resp = {}){
                console.log(resp.data)
                var newHtml = resp.data.map(d => {
                    return `<div class="well_events"> 
                                <a href="/events/${d.id}">
                                    <img class="events_img" src="${d.image}">
                                    <h1> ${d.name}</h1>
                                    <h2>${d.start_date}</h2>
                                </a> 
                            </div>`
                });
                
                $('#list_of_events').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error)
            }
        })
    });
});

$(document).ready(function (){
    let subtotal = $('#subtotal').text();

    $('#add').on('click',function (e){
        e.preventDefault();
        var amount = parseInt($('#amount').text());
        if ( amount < 10 ) {
            $('#amount').html(amount + 1);
            $('#sub').prop('disabled', false);
            $('#subtotal').html(parseInt(subtotal)*(amount+1))
        } if ( amount == 9 ) {
            $('#add').prop('disabled', true);
        }
    });
    $('#sub').on('click',function (e){
        e.preventDefault();
        var amount = parseInt($('#amount').text());
        if (amount > 1) {
            $('#amount').html(amount - 1);
            $('#add').prop('disabled', false);
            $('#subtotal').html(parseInt(subtotal)*(amount-1))
        } if ( amount == 2 ) {
            $('#sub').prop('disabled', true);
        }
    });
});