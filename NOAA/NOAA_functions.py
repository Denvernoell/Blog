from my_secrets import Token
import requests
import pandas as pd
from IPython.display import display

headers = {"token": Token}
base_url = f"https://www.ncdc.noaa.gov/cdo-web/api/v2"
offset = 0
limit = 10


def get_df(endpoint):
    full_df = pd.DataFrame()
    finished = False
    while finished == False:
        response = requests.get(
            f"{base_url}/{endpoint}/&limit={limit}&offset={offset}", headers=headers)

        try:
            r = response.json()['results']
            df = pd.DataFrame(r)
            full_df.append(df)
            if len(df) != limit:
                finished = True

        except:
            return response

# endpoints = ['datasets?locationid=CITY:Visalia/GHCND']
# endpoints = ['data?datasetid=GHCND&locationid=ZIP:93292&units=standard']


def get_data(
        locationid='ZIP:93292',
        startdate='2020-01-01',
        enddate='2021-01-01',
        units='standard',
        datasetid='GHCND',
        datatypeid='PRCP',
):
    return 'data?'+'&'.join([
        f'datasetid={datasetid}',
        f'locationid={locationid}',
        f'startdate={startdate}',
        f'enddate={enddate}',
        f'units={units}',
        f'datatypeid={datatypeid}',
    ])


# criteria = get_data(
#     locationid='ZIP:93292',
#     startdate='2020-01-01',
#     enddate='2021-01-01',
#     units='standard',
#     datasetid='GHCND',
#     datatypeid='PRCP',
# )
# endpoints = [criteria]
# endpoint_dfs = {e: get_df(e) for e in endpoints}
# print(endpoint_dfs)
