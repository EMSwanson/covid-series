import requests
import pandas as pd
import io
from contextlib import closing
import codecs
import csv

DATA_URL = """https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_19-covid-Confirmed.csv"""


def get_covid(url):
    with closing(requests.get(url, stream=True)) as r:
        r.headers
        reader = csv.reader(codecs.iterdecode(r.iter_lines(), 
                            'utf-8'), delimiter=',', quotechar='"')
        for row in reader:
            print (row)
    

def get_covid_pandas(url):
    data = pd.read_csv(url)
    return data


def tidy_covid_dataframe(dataframe):
    covid_dataframe = pd.melt(dataframe, 
                              id_vars=['Province/State', 
                                       'Country/Region', 
                                       'Lat', 
                                       'Long'], 
                              var_name='date', 
                              value_name='n_cases')
    return covid_dataframe


def main():
    covid_dataframe = get_covid_pandas(DATA_URL)
    td_dataframe = tidy_covid_dataframe(covid_dataframe)
    return td_dataframe


if __name__ == '__main__':
    main()    
