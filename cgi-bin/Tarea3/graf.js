let bar;
let line;
let pie;

let prevCensosData;
let prevTiposData;
let prevPerrosData;
let prevGatosData;


function init() {
    console.log('INIT');
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'graf.py');
    xhr.timeout = 1000;
    xhr.onload = (data) => {
        let dataText = data.currentTarget.responseText;
        let info = JSON.parse(dataText);
        line = LineGraph(info['LineChart']);
        pie = PieGraph(info['PieChart']);
        bar = BarGraph(info['BarChart']);
    }
    xhr.send();
    console.log("Charts Created");
}


function graficos() {
    let xhr = new XMLHttpRequest();
    xhr.open('GET', 'graf.py');
    xhr.timeout = 1000;
    xhr.onload = (data) => {
        let dataText = data.currentTarget.responseText;
        let info = JSON.parse(dataText);

        let LineData = [];
        let linekeys = Object.keys(info['LineChart']);
        linekeys.forEach((key) => {
            LineData.push(info['LineChart'][key]);
        });

        let PieData = [];
        let PieKeys = Object.keys(info['PieChart']).reverse();
        for (let i = 0; i < PieKeys.length; i++) {
            PieData.push({
                name: PieKeys[i],
                y: info['PieChart'][PieKeys[i]]
            })
        }

        let dogData = info['BarChart']['perro'];
        let catData = info['BarChart']['gato'];

        if(JSON.stringify(prevCensosData) != JSON.stringify(LineData)) {
            line.xAxis[0].update({categories: linekeys});
            line.series[0].setData(LineData);
            prevCensosData = LineData;
        }
        if(JSON.stringify(prevTiposData) != JSON.stringify(PieData)){
            pie.series[0].setData(PieData);
            prevTiposData = PieData;
        }
        if(JSON.stringify(prevPerrosData) != JSON.stringify(dogData)) {
            bar.series[0].setData(dogData);
            prevPerrosData = dogData;
        }
        if(JSON.stringify(prevGatosData) != JSON.stringify(catData)) {
            bar.series[1].setData(catData);
            prevGatosData = catData;
        }
        console.log("Charts Updated");
    }
    xhr.send();
}

function PieGraph(obj) {
    let typesData = [];
    let keys = Object.keys(obj).reverse();
    console.log(keys);
    for (let i = 0; i < keys.length; i++) {
        typesData.push({
            name: keys[i],
            y: obj[keys[i]]
        })
    }
    prevTiposData = typesData;
    const chart = Highcharts.chart('graficoTorta', {
        chart: {
            type: 'pie'
        },
        title: {
            text: 'Cantidad Tipo Mascotas'
        },
        subtitle: {
            text: 'Cuantas mascotas se han censado por tipo'
        },
        tooltip: {
            pointFormat: '{series.name}: <b>{point.y}</b>'
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    format: '<b>{point.name}</b>: {point.y}'
                }
            }
        },
        series: [{
            name: 'Tipos',
            colorByPoint: true,
            data: typesData
        }]
    });
    console.log("PieChart Created");
    return chart;
}

function LineGraph(obj) {
    let censosData = [];
    let keys = Object.keys(obj);
    keys.forEach((key) => {
        censosData.push(obj[key]);
    });
    prevCensosData = censosData;
    let chart = Highcharts.chart('graficoLineas', {
        chart: {
            type: 'line'
        },
        title: {
            text: 'Censos por Dia'
        },
        subtitle: {
            text: 'Cantidad de domicilios censados cada día'
        },
        xAxis: {
            categories: keys,
            title: {
                text: 'Día'
            }
        },
        yAxis: {
            title: {
                text: 'Cantidad de Censos'
            },
            min: 0
        },
        tooltip: {
            pointFormat: '{point.y}'
        },
        colors: ['#251f44', '#d3dbff', '#ffe0f7', '#fe91ca'],
        series: [{
            name: 'Cantidad de Censos',
            data: censosData
        }]
    });
    console.log("LineChart Created");
    return chart;
}

function BarGraph(obj) {
    let meses = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
    ];
    prevPerrosData = obj['perros'];
    prevGatosData = obj['gatos'];
    let chart = Highcharts.chart('graficoBarras', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Gatos y Perros por mes'
        },
        subtitle: {
            text: 'Cantidad de perros y gatos censados por cada mes del 2020'
        },
        xAxis: {
            categories: meses,
            crosshair: true
        },
        yAxis: {
            min: 0,
            title: {
                text: 'Cantidad de censos'
            }
        },
        tooltip: {
            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
            pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
                '<td style="padding:0"><b>{point.y} censos</b></td></tr>',
            footerFormat: '</table>',
            shared: true,
            useHTML: true
        },
        colors: ['#251f44', '#fe91ca', '#d3dbff', '#ffe0f7'], 
        series: [{
            name: 'Perros',
            data: obj['perros']
        }, {
            name: 'Gatos',
            data: obj['gatos']
        }]
    });
    console.log("BarChart Created");
    return chart;
}


document.addEventListener('DOMContentLoaded', () => {
    init();
    setInterval(graficos, 5000);
})

