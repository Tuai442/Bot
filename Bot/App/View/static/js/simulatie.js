// import {layout, candle, line} from './graph.js';

const layout = {
    dragmode: 'zoom', 
    width: 1000,
    height: 700,
    plot_bgcolor:"#171c24",
    paper_bgcolor:"#171c24",

    margin: {
      r: 10, 
      t: 25, 
      b: 40, 
      l: 60
    }, 
    showlegend: false, 
    xaxis: {
      autorange: true, 

      title: 'Date', 
      type: 'date',

      tickcolor: "#696666",
      tickwidth: 0.5,
      
      gridcolor: "#696666",
      gridwidth: 1,   
    }, 
    yaxis: {
      autorange: true, 
      type: 'linear',
      tickcolor: "#696666",
      tickwidth: 0.5,
      
      gridcolor: "#696666",
      gridwidth: 0.5,
      
      zerolinecolor: "#696666",
      zerolinewidth: 1,
    },
    
    // annotations: [
    //   {
    //     x: '2021-12-01',
    //     y: 0.9,
    //     xref: 'x',
    //     yref: 'paper',
    //     text: 'largest movement',
    //     font: {color: 'magenta'},
    //     showarrow: true,
    //     xanchor: 'right',
    //     ax: -20,
    //     ay: 0
    //   }
    // ],
    
    shapes: []
  };

const candle = {
  
    x: [], 
    
    close: [], 
    
    decreasing: {line: {color: '#bf3230'}}, 
    
    high: [], 
    
    increasing: {line: {color: '#30bf35'}}, 
    
    line: {color: 'rgba(31,119,180,1)'}, 
    
    low: [], 
    
    open: [], 

    
    type: 'candlestick', 
    xaxis: 'x', 
    yaxis: 'y'
  };

const trend = {
    x: [],
    y: [],
    mode: 'line',
    fill: 'tonexty',
    name: '/',
    line: {
        color: '',
        width: 3
    }
}


class Table{
    
    constructor(root, width){
        this.root = root
        this.root.style.width = width
        this.columnLength = null
    }

    insert(data){
        this.clear();

        if (this.columnLength != null){
            if (data.length != this.columnLength){
                throw 'De lengte van de colomen en headers moeten gelijk zijn!'
            }
        }
        let rows = document.createElement("tr")
        data.forEach(d =>{
            let col = document.createElement("td")
            col.innerHTML = d
            rows.appendChild(col)
        })
        this.root.appendChild(rows)
    }

    clear(){
        // nog voorzien
    }

    setHeader(headerColumns){ 
        this.columnLength = headerColumns.length
        console.log(headerColumns)
        headerColumns.forEach(h =>{
            if (h !== null){
                let header = document.createElement("th")
                header.innerHTML = h
                console.log(header)
                this.root.appendChild(header)
            }

        })
        
    }

}

class Form{
    constructor(root){
        this.root = root
        this.br = document.createElement("br")
    }

    addField(name, text, inputNeeded=true, defaultInput=""){
        let field = document.createElement("label")
        field.innerText = text
        field.setAttribute("name", name)
        this.root.appendChild(field)
        if (inputNeeded){
            let input = document.createElement("input")
            input.setAttribute("name", name)
            input.value = defaultInput
            this.root.appendChild(input)
        }

    }

    addOption(name, data, defaultOption=""){
        let select = document.createElement("select")
        select.setAttribute("name", name)
        data.forEach(x => {
            let option = document.createElement("option")
            option.text = x
            option.value = x
            select.appendChild(option)
        })
        select.value = defaultOption
        this.root.appendChild(select)
    }

   // addSubmit(action){
   //     let submit = document.createElement("input")
   //     submit.setAttribute("type", "button")
   //     submit.addEventListener("click", test)
   //     submit.value = "Maak strategie"
   //     this.root.appendChild(submit)
   // }


}

class GraphSimulator{
    constructor(root, symbol, interval, strategy=null){
        this.root = root
        this.symbol = symbol
        this.interval = interval
        this.strategy = strategy

        const defaultSpeed = 1000
        this.timer = ms => new Promise(res => setTimeout(res, ms))

        this.data = null
        this.pauze = false
        this.strategyIsInitiated = false

        this.slider = document.getElementById("slider")
        this.scrollbar = document.getElementById("table-scroll-2")
        this.rows = document.getElementById("table-2").rows
        this.pauzeBtn = document.getElementById("pauze")
        this.btnGroup = document.getElementById("btn-group")
        this.titleBar = document.getElementById("title-bar")
        this.wallet = document.getElementById("wallet")

        this.showBounces = true
        this.showTrends = true
    }

    StartSimulation() {
        if (this.data !== null) {
            if (this.strategyIsInitiated) {
                console.log(this.data)
                this.Menu()
                this.Load()
            }
            else {
                alert("Er is geen strategy gemaakt")
            }
        }
        else{
            alert("Data is leeg.")
            }
        }

    async Load() {
        let res = null
        for (var i = 0; i < this.data.length; i++) {
            // Pauze
            // nog te maken...

            // auto scroll -> nog niet goed ...
            //this.scrollbar.scrollBy(start + 20, end + 20) // snelheid klopt niet ingvergelijking met de graph NOG AAN TE PASSEN

            // cursor
            this.rows[i].classList.add("current-row")

            // Update graph
            candle["x"].push(this.data[i][0])
            candle["close"].push(this.data[i][4])
            candle["high"].push(this.data[i][2])
            candle["low"].push(this.data[i][3])
            candle["open"].push(this.data[i][1])

            await this.timer(1000);


            // Response
            $.ajax({
                type: "POST",
                url: "/_process_candles",
                data: JSON.stringify([this.data[i]]),
                contentType: "application/json",
                dataType: 'json',
                success: function (response) {
                    res = response;
                }
            });

            this.ProcessResponse(res)

            Plotly.newPlot('graph', [candle], layout);
            this.rows[i].classList.remove("current-row")
        }
    }

    ChangeSymbol(symbol){
        this.symbol = symbol
    }

    ChangeInterval(interval){
        this.interval = interval
    }

    SetData(data){
        this.data = data
    }

    StrategyIsInitiated(){
        this.strategyIsInitiated = true
    }

    Menu(){
        this.slider.addEventListener("change", function (e) {
            var val = document.getElementById("slider").value
            // nog aan werken!
            if (val > 50){
                speed =  defaultSpeed + (val * 30)
            }
            else{
                speed = defaultSpeed - (val * 30)
            }

        })
        this.slider.addEventListener("input", function (e) {
            var val = document.getElementById("slider").value
            if (val > 50){
                speed =  defaultSpeed + (val * 20)
            }
            else{
                speed = defaultSpeed - (val * 25)
            }
        })
        this.pauzeBtn.addEventListener("click", function (e) {
            if (pauzeBtn.value === "pauze"){
                this.pauze = true
                pauzeBtn.value = "resume"
            }
            else{
                this.pauze = false
                pauzeBtn.value = "pauze"
            }


        })

        let checkBoxBounce = document.createElement("input")
        checkBoxBounce.setAttribute("type", "checkbox")
        checkBoxBounce.checked = true
        checkBoxBounce.addEventListener("change", e =>{
            this.showBounces = e.target.checked
        })
        let labelBounce = document.createElement("label")
        labelBounce.innerText = "Toon bounces"

        let checkBoxTrend = document.createElement("input")
        checkBoxTrend.setAttribute("type", "checkbox")
        checkBoxTrend.checked = true
        checkBoxTrend.addEventListener("change", e =>{
            this.showTrends = e.target.checked
        })
        let labelTrend = document.createElement("label")
        labelTrend.innerText = "Toon bounces"

        this.btnGroup.appendChild(checkBoxBounce)
        this.btnGroup.appendChild(labelBounce)
        this.btnGroup.appendChild(checkBoxTrend)
        this.btnGroup.appendChild(labelTrend)
    }

    ProcessResponse(res) {
        console.log(res)
        if (res !== null) {
            // Bij levels geven we de grafiek 7 regio's met verschillende achtergrond kleuren.
            if (res["shapes"] !== null) {
                layout["shapes"] = res["shapes"]
                }

            if (this.showBounces){
                if (res["annotations"] !== null) {
                    layout["annotations"] = res["annotations"]
                }
            }else{
                layout["annotations"] = []
            }

            if (res["wallet"] !== null){
                this.wallet.innerText =`${res["wallet"]} Euro.`
            }

            /*if (this.showTrends){
                if (res["annotations"] !== null) {
                    layout["annotations"] = res["annotations"]
                }
            }else{
                layout["annotations"] = []
            }*/

        }
    }
}



const defaultSpeed = 1000
let speed = defaultSpeed
let strategy = null
let symbol = "BTCUSDT"
let interval = "1m"
let strategyIsInitiated = false
function setup (){
    let start = document.getElementById("start")
    const strategySelector = document.getElementById("strategy-select")
    const symbolSelector = document.getElementById("symbol-select")
    const intervalSelector = document.getElementById("interval-select")
    const submitBtn = document.getElementById("submit-btn")
    strategy = strategySelector[0].value
    const csvFileInput = document.getElementById("csvFileInput");

    let csvData = []

    let simulator = new GraphSimulator("graph", symbol, interval)
    CreateForm(csvData)

    // -----------------------------------------------

    start.addEventListener("click", e =>{
        // if (csvData !== null && strategyIsInitiated === true){
        //     console.log("start")
        //     StartSimulation(csvData)
        // }
        simulator.StartSimulation()
    })

    strategySelector.addEventListener("change", e => {
        CreateForm(csvData)
    })

    symbolSelector.addEventListener("change", e => {
        // symbol = symbolSelector.value
        simulator.ChangeSymbol(symbol)
    })

    intervalSelector.addEventListener("change", e => {
        // interval = intervalSelector.value
        simulator.ChangeInterval(interval)
    })

    csvFileInput.addEventListener("input", e =>{
        e.preventDefault();
        const input = csvFileInput.files[0];
        let fileName = document.getElementById("fileName")
        fileName.textContent = `Dataset: ${input.name}`
        const reader = new FileReader();
        
        reader.onload = function (e) {
            const text = e.target.result;
            csvData = csvToArray(text);
            simulator.SetData(csvData)
            CreateForm(csvData)
            CreateTable("table-2", csvData, 500)
            };
        reader.readAsText(input);
    });

    submitBtn.addEventListener("click", ev => {
        const form = document.getElementById("setup")
        let data = {}
        data["type"] = strategy
        data["symbol"] = symbol
        data["interval"] = interval
        data["data"] = csvData
        console.log(form)
        Array.from(form.elements).forEach(e => {
            data[e.name] = e.value
        })
        $.ajax({
            type: "POST",
            url: "/_create_strategy",
            data: JSON.stringify(data),
            contentType: "application/json",
            dataType: 'json',
            success: function (response) {}

        });
        simulator.StrategyIsInitiated()
    })
}

function CreateForm(csvData) {
    const strategySelector = document.getElementById("strategy-select")
    let form = document.getElementById("setup")

    strategy = strategySelector.value
    form.innerHTML = ""
    let customForm = new Form(form)
    customForm.addField("wallet", "Geef een start budget in", inputNeeded=true, defaultInput="10")
    if (strategy === "fibonacci") {

        customForm.addField("name", "Naam", inputNeeded=true, defaultInput="Test")
        let availableDates = csvData.map(function (x) {
            return x[0];
        })
        customForm.addField("/", "Geef een start data set", inputNeeded=false)
        customForm.addOption("init-data", availableDates, availableDates[10]) // alleen beschikbare datums
        customForm.addField("bounce-margin", "Geef een bounce marge in:", inputNeeded=true, defaultInput="10")
        customForm.addField("trend-interval", "Geef een trend interval in", inputNeeded=true, defaultInput="5")
    } else if (strategy === "rsi") {
        console.log("niks")
    }

}

function CreateTable(table_id, data, width){
    let t = document.getElementById(table_id)
    let table = new Table(t, width);
    table.setHeader(data[0])
    data.shift();

    data.forEach(x =>{
        table.insert(x);
    })
    
}

function csvToArray(str, delimiter = ",", header=true) {
    const parsed_arr = []
    
    if (header){
        const h = str.slice(0, str.indexOf("\n")).split(delimiter);
        str = str.replace(str.substring(0, str.indexOf('\n')), "").trim()
        parsed_arr.push(h)
    }

    while (str.substring(0, str.indexOf('\n'))){
        const arr = str.slice(0, str.indexOf("\n")).split(delimiter);
        str = str.replace(str.substring(0, str.indexOf('\n')), "").trim()
        let index = 0
        const temp = []
        arr.forEach( i =>{
            if (index === 0){
                //temp.push(new Date(i).toLocaleString("be-BE"))//Date.parse(i)
                temp.push(i)
            }
            else{
                i = i.replace("\r", "")
                temp.push(parseFloat(i))
                
            }
            index ++
           
        })
        parsed_arr.push(temp)
    }
    
    return parsed_arr
   
    }

window.addEventListener('load',setup);

