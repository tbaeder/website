$(document).ready(function() {
  $(".delete-message").on("click", delete_message)
})

var delete_message = function(event) {
  var $clicked_message = $(event.target).parent().parent()[0];
  var message_id = $clicked_message.dataset["id"];
  $.post({
    url: "/messages/delete/",
    data: {"message_id": message_id},
    success: update_after_delete,
  })
}

var update_after_delete = function(data) {
  id = data["data-id"]
  $(".message[data-id="+id+"]").remove();
}
