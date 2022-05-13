const setup = () => {
    let name = document.getElementById("naam")
    let btn = document.getElementById("btn")

    btn.addEventListener("click", e =>{
        console.log(name.value)
        $.ajax({
            type: "POST",
            url: "/_receive_data",
            data: JSON.stringify(name.value),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {
                console.log(response)
                if(!response){
                    alert("Naam moet in hoofd letter zijn.")
                }
            }
        });
    })
}

window.addEventListener("load", setup);