// fully booked dates passed to script element in index.html as const variable
// unavailableDict. format is {"Month YYYY"}
const numberOfDates = document.querySelectorAll("td").length;
const cssClassStartDate = "start-date"
const cssClassEndDate = "end-date"
let startDate = null;
let endDate = null;

for (let i = 0; i<numberOfDates; i++) {
    let j = document.querySelectorAll("td")[i];
    if (j.classList.contains("noday") || j.classList.contains("past") || j.classList.contains("unavailable")) continue;

    j.addEventListener("click", function () {
        if (startDate === null) {
            this.classList.add(cssClassStartDate);
            document.querySelector("input[name='start_date']").value = j.innerHTML;
            startDate = parseInt(this.innerHTML);
        } else if (endDate === null) {
            endDate = parseInt(this.innerHTML);
            if (startDate > endDate) {
                let tempDate = startDate;
                startDate = endDate;
                endDate = tempDate;

                document.querySelector("." + cssClassStartDate).classList.add(cssClassEndDate);
                document.querySelector("." + cssClassStartDate).classList.remove(cssClassStartDate);
                this.classList.add(cssClassStartDate);

                document.querySelector("input[name='end_date']").value = document.querySelector("input[name='start_date']").value;
                document.querySelector("input[name='start_date']").value = j.innerHTML;
            } else {
                this.classList.add(cssClassEndDate);
                document.querySelector("input[name='end_date']").value = j.innerHTML;
            }

            // ToDo: add classes between edge dates
        } else {
            document.querySelector("." + cssClassStartDate).classList.remove(cssClassStartDate);
            document.querySelector("." + cssClassEndDate).classList.remove(cssClassEndDate);
            this.classList.add(cssClassStartDate);
            document.querySelector("input[name='start_date']").value = j.innerHTML;
            document.querySelector("input[name='end_date']").value = "";
            startDate = parseInt(this.innerHTML);
            endDate = null;
        }
    });
}
