import csvHandler from "./csvHandler.js";

const tableRoot = document.querySelector("#csvRoot");
const tableCsv = new csvHandler(tableRoot);


const csvFileInput = document.querySelector("#csvFileInput");

csvFileInput.addEventListener("change", e =>{
    console.log(csvFileInput)
    Papa.parse(csvFileInput.files[0])

    Papa.parse(csvFileInput.files[0], {
        delimiter: ',',
        skipEmptyLines: true,
        complete: results => {
            tableCsv.update(results.data.slice(1), results.data[0]);

        }
    })
});


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

export default class {
    /**
     * 
     * @param {HTMLTableElement} root the table element witch will display the CSV data
     */
    
    constructor(root) {
        this.root = root;
        
    }

    update(data, headerColumns=[]){
        this.clear();
        this.setHeader(headerColumns);
        this.setBody(data);
    }

    
    clear(){
        this.root.innerHTML = "";
    }


    setHeader(headerColumns){
        this.root.insertAdjacentHTML("afterbegin", `
        <thead>
            <tr>
                ${headerColumns.map(text => `<th>${text}</th>`).join("")}
            </tr>
        </thead>
        `);
    }

    setBody(data){
        const rowsHtml = data.map(row => {
            return `
            <tr>
                ${row.map(text => `<td>${text}</td>`).join("")}
            </tr>
            `;
        });

        this.root.insertAdjacentHTML('beforeend', `
        <tbody>
            ${rowsHtml.join("")}
        </tbody>
        `);
    }
}