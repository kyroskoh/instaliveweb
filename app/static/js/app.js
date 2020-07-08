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
      beforeSend: function (xhr) {
        showLoading();
      },
      success: function (response) {
        $("#status_live").text("Running");
        $("#msg_live").val(response.message);
        hideLoading();

        Swal.fire("You're Live!", "Live Streaming is Starting...!", "success");

        $("#stopBroadcast").prop("disabled", false);
        $("#startBroadcast").prop("disabled", true);
      },
      error: function (response) {
        Swal.fire(
          "Stream Key Expired",
          "Please re-login to regenerate the key",
          "error"
        ).then(function () {
          window.location = "/";
        });
        hideLoading();
      },
    });
  });

  $("#stopBroadcast").on("click", function () {
    $.ajax({
      type: "get",
      url: "/stop_broadcast",
      beforeSend: function (xhr) {
        showLoading();
      },
      success: function (response) {
        $("#status_live").text("Stopped");
        $("#msg_live").val(response.message);
        hideLoading();

        Swal.fire("You're Off!", "Live Streaming is Stopping...!", "success");

        $("#stopBroadcast").prop("disabled", true);
        $("#startBroadcast").prop("disabled", false);
      },
      error: function (response) {
        Swal.fire(
          "Stream Key Expired",
          "Please re-login for refreshing the key",
          "error"
        );
        hideLoading();
      },
    });
  });
});

function showLoading() {
  $("#dashboard_action").LoadingOverlay("show", {
    background: "rgba(0, 0, 0, 0.5)",
    imageColor: "#fff",
  });
}

function hideLoading() {
  $("#dashboard_action").LoadingOverlay("hide", {
    background: "rgba(0, 0, 0, 0.5)",
    imageColor: "#fff",
  });
}
