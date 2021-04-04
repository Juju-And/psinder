function saveAnswer(answer, dataId) {
    var csrftoken = $("[name=csrfmiddlewaretoken]").val();

    console.log("create post is working!") // sanity check
//    console.log($('#product-name').val())
        $.ajax({
            url: "http://127.0.0.1:8000/matching/",
            data: JSON.stringify({'answer': answer,
            "data-id": dataId}),
            headers:{
            "X-CSRFToken": csrftoken
            },
            type: "POST",
            dataType: "json"
        }).done(function(response) {
            console.log('odpowiedź przesłana')
        }).fail(function(xhr,status,err) {
        }).always(function(xhr,status) {
        });
}

$(function() {
     $('#btn-reject').on('click', function(event){
        event.preventDefault();
        console.log("Rejected")
        let dataId = $(event.target).attr('data-id')
        saveAnswer("rejected", dataId)
        })
     $('#btn-accept').on('click', function(event){
        event.preventDefault();
        console.log("Accepted")
        let dataId = $(event.target).attr('data-id')
        saveAnswer("accepted", dataId)
        })
})