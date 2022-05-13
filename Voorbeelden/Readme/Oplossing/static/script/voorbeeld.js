const setup = () => {
    let name = document.getElementById("naam")
    let age = document.getElementById("leeftijd")

    let btn = document.getElementById("btn")

    btn.addEventListener("click", e => {
        console.log(name.value)
        console.log(age.value)
        $.ajax({
            type: "POST",
            url: "/_receive_name",
            data: JSON.stringify(name.value),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)

            }
        });

        $.ajax({
            type: "POST",
            url: "/_receive_age",
            data: JSON.stringify(age.value),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
            }
        });

        // We kunnen ook alles in één keer door sturen:
        $.ajax({
            type: "POST",
            url: "/_receive_all",
            data: JSON.stringify([name.value, age.value]),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
            }
        });
    })
}


window.addEventListener("load", setup);