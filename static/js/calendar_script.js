// fully booked dates passed to script element in index.html as const variable
// unavailableDict. format is {"Month YYYY"}
const arrayOfDateCells = document.querySelectorAll("td");
const numberOfDateCells = arrayOfDateCells.length;
const arrayOfMonths = document.querySelectorAll("th.month");
const numberOfMonths = arrayOfMonths.length;
const cssClassStartDate = "start-date";
const cssClassEndDate = "end-date";
const cssClassInnerDate = "inner-date";
let startDate = null;
let endDate = null;

document.querySelector("#start_date").setAttribute("readonly", "");
document.querySelector("#end_date").setAttribute("readonly", "");

for (let i = 0; i<numberOfDateCells; i++) {
    let dateCell = arrayOfDateCells[i];
    if (dateCell.classList.contains("noday") || dateCell.classList.contains("past") || dateCell.classList.contains("unavailable")) continue;

    dateCell.addEventListener("click", function () {
        if (startDate === null) {
            this.classList.add(cssClassStartDate);
            
            let monthAndYearString = this.parentElement.parentElement.firstElementChild.firstElementChild.innerHTML;
            let monthAndYearArray = monthAndYearString.split(" ");
            let dateMonth = monthAndYearArray[0];
            let dateYear = monthAndYearArray[1];

            let dateDay = this.innerHTML;
            startDate = new Date(dateMonth + " " + dateDay + ", " + dateYear);
            document.querySelector("input[name='start_date']").value = startDate.toISOString().split('T')[0];
        } else if (endDate === null) {
            let monthAndYearString = this.parentElement.parentElement.firstElementChild.firstElementChild.innerHTML;
            let monthAndYearArray = monthAndYearString.split(" ");
            let dateMonth = monthAndYearArray[0];
            let dateYear = monthAndYearArray[1];
            
            let dateDay = this.innerHTML;
            endDate = new Date(dateMonth + " " + dateDay + ", " + dateYear);

            if (startDate > endDate) {
                let tempDate = startDate;
                startDate = endDate;
                endDate = tempDate;

                document.querySelector("." + cssClassStartDate).classList.add(cssClassEndDate);
                document.querySelector("." + cssClassStartDate).classList.remove(cssClassStartDate);
                this.classList.add(cssClassStartDate);

                document.querySelector("input[name='end_date']").value = document.querySelector("input[name='start_date']").value;
                document.querySelector("input[name='start_date']").value = startDate.toISOString().split('T')[0];
            } else {
                this.classList.add(cssClassEndDate);
                document.querySelector("input[name='end_date']").value = endDate.toISOString().split('T')[0];
            }
            
            // let startEndDelta = Math.ceil(Math.abs(endDate - startDate) / (1000 * 60 * 60 * 24));
            // for (let j = 1; j<startEndDelta; j++) {
            //     let innerDate = startDate + j
            //     for (let k = 0; k<numberOfMonths; k++) {
            //         arrayOfMonths[k];
            //         // add inner-date css class
            //     }
            // }
        } else {
            document.querySelector("." + cssClassStartDate).classList.remove(cssClassStartDate);
            document.querySelector("." + cssClassEndDate).classList.remove(cssClassEndDate);
            
            let numberOfInnerDates = document.querySelectorAll("." + cssClassInnerDate).length;
            for (let j = 0; j<numberOfInnerDates; j++) {
                document.querySelector("." + cssClassInnerDate).classList.remove(cssClassInnerDate);
            }

            this.classList.add(cssClassStartDate);
            
            let monthAndYearString = this.parentElement.parentElement.firstElementChild.firstElementChild.innerHTML;
            let monthAndYearArray = monthAndYearString.split(" ");
            let dateMonth = monthAndYearArray[0];
            let dateYear = monthAndYearArray[1];
            
            let dateDay = this.innerHTML;
            startDate = new Date(dateMonth + " " + dateDay + ", " + dateYear);
            endDate = null;
            document.querySelector("input[name='start_date']").value = startDate.toISOString().split('T')[0];
            document.querySelector("input[name='end_date']").value = "";
        }
    });
}
