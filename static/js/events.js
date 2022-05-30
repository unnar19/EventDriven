$(document).ready(function (){
    $('#search-btn').on('click',function (e){
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url:'/events?search_filter=' + searchText,
            type: 'GET',
            success: function(resp){
                var newHtml = resp.data.map(d => {
                    return `<div class="well_events"> 
                                <a href="/events/${d.id}">
                                    <img class="events_img" src="${d.image_url}" />
                                    <h4> ${d.name}</h4>
                                    <p>${d.start_date}</p>
                                </a> 
                            </div>`
                });
                $('.list_of_events').html(newHtml.join(''));
                $('#search-box').val('');
            },
            error: function(xhr, status, error) {
                console.error(error);
            }
        })
    });
});