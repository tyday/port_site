plot = document.getElementById('plot');
// Plotly.newPlot( TESTER, [{
// x: [1, 2, 3, 4, 5],
// y: [1, 2, 4, 8, 16] }], {
// margin: { t: 0 } } );

class SensorReading {
    constructor(id, temp1, temp2, rh1, rh2, light, timestamp){
        this.id = id;
        this.temp1 = temp1;
        this.temp2 = temp2;
        this.rh1 = rh1;
        this.rh2 = rh2;
        this.light = light;
        this.timestamp = timestamp;
    }

    getTemp1F(){
        return this.temp1 * 1.8 + 32;
    }
    getTemp2F(){
        return this.temp2 * 1.8 + 32;
    }
}
let createPlot = (timestamp, temp1, temp2, rh1, rh2, light) => {
    var data = [
        {
            x: timestamp,
            y: temp1 ,
            name:"Env temp"
        },
        {
            x: timestamp,
            y: temp2 ,
            name: "GH Temp"
        },
        {
            x: timestamp,
            y: rh1 ,
            name: "Env RH"
        },
        {
            x: timestamp,
            y: rh2 ,
            name: "GH RH"
        },        
        {
            x: timestamp,
            y: light ,
            name: "Light",
            yaxis: 'y2'
        }
    ]
    var layout = {
        title: 'Garden conditions',
        // autosize: true,
        width:plot.offsetWidth*.975,
        margin: {
            l: 50,
            r: 50,
            b: 100,
            t: 100,
            pad: 4
          },
        // yaxis: {title: 'yaxis title'},
        yaxis2: {
          title: 'Light',
          titlefont: {color: 'rgb(148, 103, 189)'},
          tickfont: {color: 'rgb(148, 103, 189)'},
          overlaying: 'y',
          side: 'right'
        }
    }
    var config = {
        responsive: true,
    }
    Plotly.newPlot(plot,data, layout, config)
}
let getData = () => {
    // const url = 'http://127.0.0.1:8000/garden/api/readings.json'
    const url = 'https://tylerday.net/garden/api/readings.json'
    fetch(url)
    .then(response => response.json())
    .then(function(data){
        let timestamps = data.map(x => new Date(x.timestamp*1000))
        let temp1 = data.map(x => x.temp1 * 1.8 + 32)
        let temp2 = data.map(x => x.temp2 * 1.8 + 32)
        let rh1 = data.map(x => x.rh1)
        let rh2 = data.map(x => x.rh2)
        let light = data.map(x => x.light)
        createPlot(timestamps, temp1, temp2, rh1, rh2, light)
    })
}

getData();