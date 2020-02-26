const URL = '/garden/api/readings.json'
PLOT = document.getElementById('plot');

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
        width:PLOT.offsetWidth*.975,
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
    Plotly.newPlot(PLOT,data, layout, config)
}
let getData = () => {
    // const url = 'https://tylerday.net/garden/api/readings.json'
    fetch(URL)
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
let updateTempReadings = (reading) => {
    tempEnvironment = document.getElementById('tempEnvironment')
    tempGreenhouse = document.getElementById('tempGreenhouse')
    rhEnvironment = document.getElementById('rhEnvironment')
    rhGreenhouse = document.getElementById('rhGreenhouse')
    light = document.getElementById('light')
    timestamp = document.getElementById('timestamp')

    date = new Date(reading.timestamp * 1000)
    // var options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' };
    var options = { timezone:"US/Eastern" };

    tempEnvironment.innerText = `${(reading.temp1 * 1.8 + 32).toFixed(1)}\u00B0 F`
    tempGreenhouse.innerText = `${(reading.temp2 * 1.8 + 32).toFixed(1)}\u00B0 F`
    rhEnvironment.innerText = `${(reading.rh1).toFixed(1)}% RH`
    rhGreenhouse.innerText = `${(reading.rh2).toFixed(1)}% RH`
    light.innerText = reading.light
    timestamp.innerText = date.toLocaleString("en-US", options).toLowerCase()
}

let getLatestReading = () => {
    const url = URL+"?latest=true"
    fetch(url)
    .then((response) => response.json())
    .then((data) => {
        updateTempReadings(data[0])
        updateChart(data[0])
        // console.log(data)
    })
    .catch((e)=> console.log(e))
}
let updateChart = (data) => {
    sensorReading = new SensorReading()
    sensorReading = data
    // console.log(sensorReading)
    update = 
        {
            y:[
                [data.temp1 * 1.8 + 32], 
                [data.temp2 * 1.8 + 32],
                [data.rh1],
                [data.rh2],
                [data.light]
            ],
            x:[[data.timestamp * 1000],[data.timestamp * 1000],
            [data.timestamp * 1000],[data.timestamp * 1000],[data.timestamp * 1000]]
        }
    
//     update = [
//         {
//         y:[[data.temp1 * 1.8 + 32]
//         ],
//         x: [
//             [data.timestamp * 1000]
//         ],
//     }
// ]
    Plotly.extendTraces(PLOT, update, [0,1,2,3,4])
}
function main(){
    if(PLOT){
        getData();
        setInterval(getLatestReading, 30000)
    }
}

main()