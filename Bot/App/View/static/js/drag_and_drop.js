
function setup (){
document.querySelectorAll(".drop-zone__input").forEach((inputElement) => {
    const dropZoneElement = inputElement.closest(".drop-zone");
  
    dropZoneElement.addEventListener("dragover", (e) => {
        e.preventDefault();
        dropZoneElement.classList.add("drop-zone--over");
    });

    // dragend is cancel a drag
    ["dragleave", "dragend"].forEach(type => {
        dropZoneElement.addEventListener(type, e => {
            dropZoneElement.classList.remove("drop-zone--over");
        });
    });

    dropZoneElement.addEventListener("drop", e => {
        e.preventDefault();

        // data ophalen en opslaan in inputelment
        if(e.dataTransfer.files.length){

            inputElement.files = e.dataTransfer.files;
            console.log(inputElement.files)
            updateThumbnail(dropZoneElement, e.dataTransfer.files[0]);
        }

        dropZoneElement.classList.remove("drop-zone--over");

    })
   
});


function updateThumbnail(dropZoneElement, file){
    let thumbnailElement = dropZoneElement.querySelector(".dorp-zone__thumb");

    // verwijder de prompt
    if(dropZoneElement.querySelector(".drop-zone__prompt")){
        dropZoneElement.querySelector(".drop-zone__prompt").remove();
    }

    // first time create thumbnail element
    if(!thumbnailElement){
        thumbnailElement = document.createElement("div");
        thumbnailElement.classList.add("drop-zone__thumb");
        dropZoneElement.appendChild(thumbnailElement);
        
    }

    thumbnailElement.dataset.label = file.name;
    //console.log(file.type)
    //show thumbnail for images files
    if(file.type.startsWith("application/")){
        
        
        //const csvFileInput = document.querySelector("#csvFileInput");
       
        const tableRoot = document.querySelector("#csvRoot");
        const tableCsv = new csvHandler(tableRoot);
        Papa.parse(file, {
            
            delimiter: ',',
            skipEmptyLines: true,
            complete: results => {
                tableCsv.update(results.data.slice(1), results.data[0]);
            }
        })

    }

}

}

window.addEventListener('load',setup);
