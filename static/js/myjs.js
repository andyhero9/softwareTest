$(document).ready(function () {
    var i = 12;
    var title = {
        text: 'Top50 Distributed in Genres'
    };

    var colorAxis = {
        minColor: '#FFFFFF',
        maxColor: Highcharts.getOptions().colors[0]
    };

    var series = [{
        type: "treemap",
        layoutAlgorithm: 'squarified',
        data: [{
            name: 'drama',
            value: i,
            colorValue: 1
     }, {
            name: 'action',
            value: 6,
            colorValue: 2
     }, {
            name: 'romance',
            value: 4,
            colorValue: 3
     }, {
            name: 'animation',
            value: 3,
            colorValue: 4
     }, {
            name: 'musical',
            value: 2,
            colorValue: 5
     }, {
            name: 'adventure',
            value: 2,
            colorValue: 6
     }, {
            name: 'sci-fic',
            value: 2,
            colorValue: 7
     }, {
            name: 'other',
            value: 1,
            colorValue: 8
     }]
   }];

    var json = {};
    json.title = title;
    json.colorAxis = colorAxis;
    json.series = series;

    $('#container').highcharts(json);
});


$(document).ready(function () {
    var title = {
        text: 'Top50 Distributed in Decades'
    };

    var colorAxis = {
        minColor: '#FFFFFF',
        maxColor: Highcharts.getOptions().colors[5]
    };

    var series = [{
        type: "treemap",
        layoutAlgorithm: 'squarified',
        data: [{
            name: '1970s',
            value: 6,
            colorValue: 1.5
     }, {
            name: '1980s',
            value: 10,
            colorValue: 2
     }, {
            name: '1990s',
            value: 15,
            colorValue: 3
     }, {
            name: '2000s',
            value: 11,
            colorValue: 4
     }, {
            name: '2010s',
            value: 8,
            colorValue: 4.5
     }]
   }];

    var json = {};
    json.title = title;
    json.colorAxis = colorAxis;
    json.series = series;

    $('#container2').highcharts(json);
});


$(document).ready(function () {
    var chart = {
        zoomType: 'x'
    };
    var title = {
        text: 'Movie Num from 1997 though 2014'
    };
    var subtitle = {
        text: document.ontouchstart === undefined ?
            'Click and drag in the plot area to zoom in' : 'Pinch the chart to zoom in'
    };
    var xAxis = {
        type: 'area',
        minRange: 1
    };
    var yAxis = {
        title: {
            text: 'Number'
        }
    };
    var legend = {
        enabled: false
    };
    var plotOptions = {
        area: {
            fillColor: {
                linearGradient: {
                    x1: 0,
                    y1: 0,
                    x2: 0,
                    y2: 1
                },
                stops: [
               [0, Highcharts.getOptions().colors[0]],
               [1, Highcharts.Color(Highcharts.getOptions().colors[0]).setOpacity(0).get('rgba')]
            ]
            },
            marker: {
                radius: 2
            },
            lineWidth: 1,
            states: {
                hover: {
                    lineWidth: 1
                }
            },
            threshold: null
        }
    };
    var series = [{
            type: 'area',
            name: 'movie amount',
            pointInterval: 1,
            pointStart: 1977,
            data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 231, 231, 23, 324, 234, 234, 212, 321, 2, 12, 3, 12, 31, 231, 221
         ]
      }
   ];

    var json = {};
    json.chart = chart;
    json.title = title;
    json.subtitle = subtitle;
    json.legend = legend;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    $('#container3').highcharts(json);

});

$(document).ready(function () {
    var title = {
        text: '各类型电影发展趋势'
    };
    var subtitle = {
        text: 'Source: runoob.com'
    };
    var xAxis = {
        categories: ['1976', '1978', '1980', '1982', '1984', '1986',
         '1988', '1990', '1992', '1994', '1996', '1998'
                    , '2000', '2002', '2004', '2006', '2008', '2010', '2012', '2014']
    };
    var yAxis = {
        title: {
            text: 'Number'
        },
        plotLines: [{
            value: 0,
            width: 1,
            color: '#808080'
      }]
    };

    var legend = {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle',
        borderWidth: 0
    };

    var series = [
        {
            name: 'comedy',
            data: [7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 25.2,
            26.5, 23.3, 18.3, 13.9, 9.6, 10, 12, 32, 22, 13, 12, 32, 11]
      },
        {
            name: 'action',
            data: [-0.2, 0.8, 5.7, 11.3, 17.0, 22.0, 24.8,
            24.1, 20.1, 14.1, 8.6, 2.5, 7.0, 6.9, 9.5, 14.5, 18.2, 21.5, 6.9, 9.5]
      },
        {
            name: 'sci-fiction',
            data: [3.9, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0,
            16.6, 14.2, 10.3, 6.6, 4.8, 9.6, 10, 12, 32, 18.2, 21.5]
      }
   ];

    var json = {};

    json.title = title;
    json.subtitle = subtitle;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.legend = legend;
    json.series = series;

    $('#container4').highcharts(json);
});


$(document).ready(function () {
    var chart = {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false
    };
    var title = {
        text: '三角形用例测试分析'
    };
    var tooltip = {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    };
    var plotOptions = {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: false
            },
            showInLegend: true
        }
    };
    var series = [{
        type: 'pie',
        name: 'percentage',
        data: [
         ['等腰三角形', 45.0],
         ['非三角形', 26.8],
            {
                name: '2~3',
                y: 12.8,
                sliced: true,
                selected: true
         },
         ['直角三角形', 6.2],
         ['输入错误', 12.2]
      ]
   }];

    var json = {};
    json.chart = chart;
    json.title = title;
    json.tooltip = tooltip;
    json.series = series;
    json.plotOptions = plotOptions;
    $('#container5').highcharts(json);
});


$(document).ready(function () {
    var chart = {
        type: 'column'
    };
    var title = {
        text: 'Scores of movies acted by XXX'
    };
    var xAxis = {
        categories: ['0~1', '1~2', '2~3', '3~4', '4~5'],
        crosshair: true
    };
    var yAxis = {
        min: 0,
        title: {
            text: 'Number'
        }
    };
    var tooltip = {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    };
    var plotOptions = {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    };
    var credits = {
        enabled: false
    };

    var series = [{
       name: 'acting',
        data: [13, 11, 51, 15, 30]
   }];

    var json = {};
    json.chart = chart;
    json.title = title;
    json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    json.credits = credits;
    $('#container6').highcharts(json);

});

$(document).ready(function () {
    var chart = {
        type: 'column'
    };
    var title = {
        text: 'movie的季度分布'
    };
    var xAxis = {
        categories: ['1st quarter', '2nd quarter', '3rd quarter', '4th quarter'],
        crosshair: true
    };
    var yAxis = {
        min: 0,
        title: {
            text: 'Number'
        }
    };
    var tooltip = {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:#FC9B18;padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    };
    var plotOptions = {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    };
    var credits = {
        enabled: false
    };

    var series = [{
        name: 'amazon movies',
        data: [10060, 20030, 30543, 40323]
   }];

    var json = {};
    json.chart = chart;
    json.title = title;
    // json.subtitle = subtitle;
    json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    json.credits = credits;
    $('#container7').highcharts(json);

});

$(document).ready(function () {
    var chart = {
        type: 'column'
    };
    var title = {
        text: 'Movies from Monday through Sunday'
    };
    var xAxis = {
        categories: ['Monday', 'Tuesday', 'Wednsday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        crosshair: true
    };
    var yAxis = {
        min: 0,
        title: {
            text: 'Number'
        }
    };
    var tooltip = {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    };
    var plotOptions = {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    };
    var credits = {
        enabled: false
    };

    var series = [{
        name: 'amazon movies',
        data: [53423, 43133, 45654, 32434, 56775, 67654, 76453]
   }];

    var json = {};
    json.chart = chart;
    json.title = title;
    // json.subtitle = subtitle;
    json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    json.credits = credits;
    $('#container9').highcharts(json);

});

$(document).ready(function () {
    var chart = {
        type: 'column'
    };
    var title = {
        text: 'Movie in Months'
    };
    var xAxis = {
        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
        crosshair: true
    };
    var yAxis = {
        min: 0,
        title: {
            text: 'Number'
        }
    };
    var tooltip = {
        headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
        pointFormat: '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y}</b></td></tr>',
        footerFormat: '</table>',
        shared: true,
        useHTML: true
    };
    var plotOptions = {
        column: {
            pointPadding: 0.2,
            borderWidth: 0
        }
    };
    var credits = {
        enabled: false
    };

    var series = [{
        name: 'amazon movies',
        data: [10060, 20030, 30543, 40323, 23434, 53423, 13133, 45654, 32434, 56775, 67654, 76453]
   }];

    var json = {};
    json.chart = chart;
    json.title = title;
    // json.subtitle = subtitle;
    json.tooltip = tooltip;
    json.xAxis = xAxis;
    json.yAxis = yAxis;
    json.series = series;
    json.plotOptions = plotOptions;
    json.credits = credits;
    $('#container8').highcharts(json);

});
