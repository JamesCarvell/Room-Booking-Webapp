var numberOfMondays = document.querySelectorAll(".mon").length;
for (var i = 0; i<numberOfMondays; i++) {
    document.querySelectorAll(".mon")[i].addEventListener("click", function () {
        this.innerHTML = "";
    });
}
