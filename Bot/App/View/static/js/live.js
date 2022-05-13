
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
    showlegend: true, 
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
  };

const candle_template = {
  
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


let current_symbol = "btcusdt"
let current_interval = "1m"
let endpoint = `${current_symbol}@kline_${current_interval}`
let wss = `wss://stream.binance.com:9443/ws/${endpoint}`
const setup = () => {
    let symbols = document.getElementById("symbols")
    let intervals = document.getElementById("intervals")

    symbols.addEventListener("change", e =>{
        let current_symbol = e.target.value.toLowerCase()
        endpoint = `${current_symbol}@kline_${current_interval}`
        wss = `wss://stream.binance.com:9443/ws/${endpoint}`

        console.log(wss)
        let candle = JSON.parse(JSON.stringify(candle_template))
        SetHistoricalCandles(current_symbol, current_interval, candle)
        Load(wss, candle)
    })

    intervals.addEventListener("change", e =>{
        let current_interval = e.target.value.toLowerCase()
        endpoint = `${current_symbol}@kline_${current_interval}`
        wss = `wss://stream.binance.com:9443/ws/${endpoint}`

        console.log(wss)
        let candle = JSON.parse(JSON.stringify(candle_template))
        SetHistoricalCandles(current_symbol, current_interval, candle)
        Load(wss, candle)
    })

    let candle = JSON.parse(JSON.stringify(candle_template))
    SetHistoricalCandles(current_symbol, current_interval, candle)
    Load(wss, candle)
}


function SetHistoricalCandles(symbol, interval, candle){
    let result = []
    $.ajax({
        type: "POST",
        url: "/_historical_candles",
        async: false,
        data: JSON.stringify([symbol, interval]),
        contentType: "application/json",
        dataType: 'json',
        success: function (response) {
            result = response;
            }
        });

    // Historische data in laden
    result.forEach(c =>{
        candle["x"].push(moment(c['time'] * 1000).format("YYYY-MM-DD h:mm:ss"))
        candle["close"].push(parseFloat(c['close']))
        candle["high"].push(parseFloat(c['high']))
        candle["low"].push(parseFloat(c['low']))
        candle["open"].push(parseFloat(c['open']))
    })    
}

function Load(wss, candle) {
    var binanceSocket = new WebSocket(wss);
    
    binanceSocket.onmessage = function (event) {
    	var message = JSON.parse(event.data);
    	var candlestick = message.k;
        candle["x"].push(moment(candlestick.t).format("YYYY-MM-DD h:mm:ss"))
        candle["close"].push(parseFloat(candlestick.c))
        candle["high"].push(parseFloat(candlestick.h))
        candle["low"].push(parseFloat(candlestick.l))
        candle["open"].push(parseFloat(candlestick.o))
        
        Plotly.newPlot('graph', [candle], layout);
        
    }
}

window.addEventListener("load", setup);
