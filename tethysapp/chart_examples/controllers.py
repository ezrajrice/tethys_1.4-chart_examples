from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import AreaRange, TimeSeries
from datetime import datetime


@login_required()
def home(request):
    """
    Controller for the app home page.
    """
    # TIMESERIES PLOT (HIGHCHARTS)
    ts_data1 = [[datetime(2008, 12, 2), 0.8], [datetime(2008, 12, 9), 0.6], [datetime(2008, 12, 16), 0.6],
                [datetime(2008, 12, 28), 0.67], [datetime(2009, 1, 1), 0.81], [datetime(2009, 1, 8), 0.78],
                [datetime(2009, 1, 12), 0.98], [datetime(2009, 1, 27), 1.84], [datetime(2009, 2, 10), 1.80],
                [datetime(2009, 2, 18), 1.80], [datetime(2009, 2, 24), 1.92], [datetime(2009, 3, 4), 2.49],
                [datetime(2009, 3, 11), 2.79], [datetime(2009, 3, 15), 2.73], [datetime(2009, 3, 25), 2.61],
                [datetime(2009, 4, 2), 2.76], [datetime(2009, 4, 6), 2.82], [datetime(2009, 4, 13), 2.8],
                [datetime(2009, 5, 3), 2.1], [datetime(2009, 5, 26), 1.1], [datetime(2009, 6, 9), 0.25],
                [datetime(2009, 6, 12), 0]]

    timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Single Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008',
            'data': ts_data1
        }]
    )

    # MULTIPLE TIMESERIES ON ONE PLOT (HIGHCHARTS)
    ts_data2 = [[datetime(2008, 12, 2), 1.8], [datetime(2008, 12, 9), 1.6], [datetime(2008, 12, 16), 1.6],
                [datetime(2008, 12, 28), 1.67], [datetime(2009, 1, 1), 1.81], [datetime(2009, 1, 8), 1.78],
                [datetime(2009, 1, 12), 1.98], [datetime(2009, 1, 27), 2.84], [datetime(2009, 2, 10), 2.80],
                [datetime(2009, 2, 18), 2.80], [datetime(2009, 2, 24), 2.92], [datetime(2009, 3, 4), 3.49],
                [datetime(2009, 3, 11), 3.79], [datetime(2009, 3, 15), 3.73], [datetime(2009, 3, 25), 3.61],
                [datetime(2009, 4, 2), 3.76], [datetime(2009, 4, 6), 3.82], [datetime(2009, 4, 13), 3.8],
                [datetime(2009, 5, 3), 3.1], [datetime(2009, 5, 26), 2.1], [datetime(2009, 6, 9), 1.25],
                [datetime(2009, 6, 12), 1]]

    multi_timeseries_plot = TimeSeries(
        height='500px',
        width='500px',
        engine='highcharts',
        title='Multiple Timeseries Plot',
        y_axis_title='Snow depth',
        y_axis_units='m',
        series=[{
            'name': 'Winter 2007-2008 (1)',
            'data': ts_data2  # I switched these so that the shorter series was in front of the larger
        }, {
            'name': 'Winter 2007-2008 (2)',
            'data': ts_data1
        }]
    )

    averages = [
        [datetime(2009, 7, 1), 21.5], [datetime(2009, 7, 2), 22.1], [datetime(2009, 7, 3), 23],
        [datetime(2009, 7, 4), 23.8], [datetime(2009, 7, 5), 21.4], [datetime(2009, 7, 6), 21.3],
        [datetime(2009, 7, 7), 18.3], [datetime(2009, 7, 8), 15.4], [datetime(2009, 7, 9), 16.4],
        [datetime(2009, 7, 10), 17.7], [datetime(2009, 7, 11), 17.5], [datetime(2009, 7, 12), 17.6],
        [datetime(2009, 7, 13), 17.7], [datetime(2009, 7, 14), 16.8], [datetime(2009, 7, 15), 17.7],
        [datetime(2009, 7, 16), 16.3], [datetime(2009, 7, 17), 17.8], [datetime(2009, 7, 18), 18.1],
        [datetime(2009, 7, 19), 17.2], [datetime(2009, 7, 20), 14.4],
        [datetime(2009, 7, 21), 13.7], [datetime(2009, 7, 22), 15.7], [datetime(2009, 7, 23), 14.6],
        [datetime(2009, 7, 24), 15.3], [datetime(2009, 7, 25), 15.3], [datetime(2009, 7, 26), 15.8],
        [datetime(2009, 7, 27), 15.2], [datetime(2009, 7, 28), 14.8], [datetime(2009, 7, 29), 14.4],
        [datetime(2009, 7, 30), 15], [datetime(2009, 7, 31), 13.6]
    ]

    ranges = [
        [datetime(2009, 7, 1), 14.3, 27.7], [datetime(2009, 7, 2), 14.5, 27.8], [datetime(2009, 7, 3), 15.5, 29.6],
        [datetime(2009, 7, 4), 16.7, 30.7], [datetime(2009, 7, 5), 16.5, 25.0], [datetime(2009, 7, 6), 17.8, 25.7],
        [datetime(2009, 7, 7), 13.5, 24.8], [datetime(2009, 7, 8), 10.5, 21.4], [datetime(2009, 7, 9), 9.2, 23.8],
        [datetime(2009, 7, 10), 11.6, 21.8], [datetime(2009, 7, 11), 10.7, 23.7], [datetime(2009, 7, 12), 11.0, 23.3],
        [datetime(2009, 7, 13), 11.6, 23.7], [datetime(2009, 7, 14), 11.8, 20.7], [datetime(2009, 7, 15), 12.6, 22.4],
        [datetime(2009, 7, 16), 13.6, 19.6], [datetime(2009, 7, 17), 11.4, 22.6], [datetime(2009, 7, 18), 13.2, 25.0],
        [datetime(2009, 7, 19), 14.2, 21.6], [datetime(2009, 7, 20), 13.1, 17.1], [datetime(2009, 7, 21), 12.2, 15.5],
        [datetime(2009, 7, 22), 12.0, 20.8], [datetime(2009, 7, 23), 12.0, 17.1], [datetime(2009, 7, 24), 12.7, 18.3],
        [datetime(2009, 7, 25), 12.4, 19.4], [datetime(2009, 7, 26), 12.6, 19.9], [datetime(2009, 7, 27), 11.9, 20.2],
        [datetime(2009, 7, 28), 11.0, 19.3], [datetime(2009, 7, 29), 10.8, 17.8], [datetime(2009, 7, 30), 11.8, 18.5],
        [datetime(2009, 7, 31), 10.8, 16.1]
    ]

    area_range_plot = AreaRange(
        width='500px',
        height='500px',
        engine='highcharts',
        title='July Temperatures',
        y_axis_title='Temperature',
        y_axis_units='*C',
        series=[{
            'name': 'Temperature',
            'data': averages,
            'zIndex': 1,
            'marker': {
                'lineWidth': 2,
            }
        }, {
            'name': 'Range',
            'data': ranges,
            'type': 'arearange',
            'lineWidth': 0,
            'linkedTo': ':previous',
            'fillOpacity': 0.3,
            'zIndex': 0
        }]
    )

    context = {
        'timeseries_plot': timeseries_plot,
        'multi_timeseries_plot': multi_timeseries_plot,
        'area_range_plot': area_range_plot,
    }

    return render(request, 'chart_examples/home.html', context)
