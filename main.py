import quantstats as qs
import pandas as pd

if __name__ == '__main__':

    timeframes = ['15m', '1h', '4h', '1d']

    for timeframe in timeframes:
        dataframe = pd.read_csv(
            f'data/Combined-Returns/SuperTrend_vs_BTC_Benchmark_{timeframe}_returns.csv',
            usecols=['datetime', 'superTrend_return', 'btc_return'],
            parse_dates=['datetime'],
            date_format='%d/%m/%Y %H:%M')


        dataframe['datetime'] = pd.to_datetime(dataframe['datetime'])
        dataframe.set_index('datetime', inplace=True)

        qs.reports.html(
            dataframe['superTrend_return'],
            dataframe['btc_return'],
            title='SuperTrend VS Benchmark',
            output='SuperTrend_vs_BTC.html',
            download_filename=f'data/Analytics-Reports/SuperTrend_vs_BTC_{timeframe}.html'
        )