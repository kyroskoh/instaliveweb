$(document).ready(function () {
  // clipboard
  var clipboard = new ClipboardJS(".btn");
  clipboard.on("success", function (e) {
    alert("Copied to clipboard");
  });

  $("#startBroadcast").on("click", function () {
    $.ajax({
      type: "get",
      url: "/start_broadcast",
      success: function (response) {
        $("#status_live").text("Running");
        $("#msg_live").val(response.message);
      },
    });
  });

  $("#stopBroadcast").on("click", function () {
    $.ajax({
      type: "get",
      url: "/stop_broadcast",
      success: function (response) {
        $("#status_live").text("Stopped");
        $("#msg_live").val(response.message);
      },
    });
  });
});
