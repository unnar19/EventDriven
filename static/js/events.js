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
                                <a href="/even  ts/${d.id}">
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
    $('#filter-btn').on('click',function (e){
        console.log('filter press')
        e.preventDefault();

        var searchText = '';
        var searchlist = [];
        $('input[class="form-check-input"]:checked').each(function() {
            searchlist.push($(this).attr('name'));
        });
        var searchText = searchlist.toString();
        searchText = searchText.replace(new RegExp(',', 'g'),"")

        $.ajax({
            url:'/events?event_filter=' + searchText,
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
                $('#flexCheckDefault').val('');
            },
            error: function(xhr, status, error) {
                console.error(error)
            }
        })
    });
});


// Amount counter
$(document).ready(function (){
    let subtotal = $('#subtotal').text();
    $('#sub_form').val(parseInt(subtotal))

    $('#add').on('click',function (e){
        e.preventDefault();
        var amount = parseInt($('#amount').text());
        if ( amount < 10 ) {
            $('#amount').html(amount + 1);
            $('#sub').prop('disabled', false);
            $('#subtotal').html(parseInt(subtotal)*(amount+1))
            $('#sub_form').val(parseInt(subtotal)*(amount+1))
            $('#form-amount').val(amount + 1)
        } if ( (amount >= 10) || (amount < 1) ) {
            $('#amount').html(10);
            amount = parseInt($('#amount').text());
            $('#sub').prop('disabled', false);
            $('#subtotal').html(parseInt(subtotal)*(amount))
            $('#sub_form').val(parseInt(subtotal)*(amount))
            $('#add').prop('disabled', true);
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
            $('#sub_form').val(parseInt(subtotal)*(amount-1))
            $('#form-amount').val(amount - 1)
        } if ( (amount > 10) || (amount < 1) ) {
            $('#amount').html(1);
            amount = parseInt($('#amount').text());
            $('#add').prop('disabled', false);
            $('#subtotal').html(parseInt(subtotal)*(amount))
            $('#sub_form').val(parseInt(subtotal)*(amount))
            $('#sub').prop('disabled', true);
        } if ( amount == 2 ) {
            $('#sub').prop('disabled', true);
        }
    });
    
});

// Accordion Navigation
$(document).ready(function (){
    $('#acc1').css({"background-color": "#c93b3b","color":"white"})
    $('#acc2').css({"background-color": "#c93b3b","color":"white"})
    $('#acc3').css({"background-color": "#c93b3b","color":"white"})
    $('#acc4').css({"background-color": "#c93b3b","color":"white"})

    $('#postal_delivery').on('click',function (){
        $('#acc1').prop('disabled', false)
        $('#acc2').prop('disabled', false)
        $('#acc2').html('Delivery information')
        $('#acc2').css({"background-color": "#c93b3b","color":"white"})   //;
    });
    $('#email_delivery').on('click',function (){
        $('#acc1').prop('disabled', false)
        $('#acc2').prop('disabled', true)
        $('#acc2').html('Delivery information (skipped)')
        $('#acc2').css({"background-color": "#db7171","color":"white"})   //#c93b3b;
    });
    $('#del_next').on('click',function (){
        $('#acc3').prop('disabled', false)
    });
    $('#pay_next').on('click',function (){
        $('#acc4').prop('disabled', false)
    });
});

// CVC
$(document).ready(function (){
    $('#cvc_input').on('input',function (){
        if ($('#cvc_input').val.toString().length > 3) {
            $('#cvc_input').val($('#cvc_input').val().toString().slice(0,3))
        }
    });
});

// EXP
$(document).ready(function (){    
    $('#month').on('input',function (){
        value = $('#month').val()
        if (isNaN(value)) {
            $('#month').val(1)
        } else if (value.toString().length > 2) {
                $('#month').val(value.toString().slice(0,-2))
        } 
        value = $('#month').val()
        if (value > 12) {
            $('#month').val(12)
        }
    });
    $('#year').on('input',function (){
        value = $('#year').val()
        if (value <1 || isNaN(value)) {
            $('#year').val(1)
        }
    });
});

// Card Number
$(document).ready(function (){
    $('#card_no').on('input',function (){
        value = $('#card_no').val()
        if ($('#card_no').val.toString().length > 16) {
            $('#card_no').val(value.toString().slice(0,16))
        }
    });
});

$(document).ready(function (){
$('#confirm').on('click',function (e){
        e.preventDefault();
        $('#delform_btn').trigger('click');
    });
});