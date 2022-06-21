import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import requests
from datetime import date

st.title('US Census API Data For Resillence and Community Service')

current_year=date.today().year

st.sidebar.header('User Input Features (data of year after 2019 might not be available for scraping currently)')
selected_year =  st.sidebar.selectbox('Input Year', list(reversed(range(2005,current_year+1))))



# Choose the year, read api keys file and assign variables
census_api_key = "663083891f5b9346c0f75af604c1bb8f7e48712b"
YEAR = 2019
YEAR = selected_year



#Create function that can convert json data to dataframe
def json_to_dataframe(response):
    """
    Convert response to dataframe
    """
    return pd.DataFrame(response.json()[1:], columns=response.json()[0])

#Get the API Data for each variables. (Poverty in Jefferson county by race)
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001_001E,B17001_002E,B17001_003E,B17001_017E,B17010_003E,B17010_010E,B17010_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001A_001E,B17001A_002E,B17001A_003E,B17001A_017E,B17010A_003E,B17010A_010E,B17010A_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001B_001E,B17001B_002E,B17001B_003E,B17001B_017E,B17010B_003E,B17010B_010E,B17010B_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001C_001E,B17001C_002E,B17001C_003E,B17001C_017E,B17010C_003E,B17010C_010E,B17010C_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001D_001E,B17001D_002E,B17001D_003E,B17001D_017E,B17010D_003E,B17010D_010E,B17010D_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001E_001E,B17001E_002E,B17001E_003E,B17001E_017E,B17010E_003E,B17010E_010E,B17010E_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlF = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001F_001E,B17001F_002E,B17001F_003E,B17001F_017E,B17010F_003E,B17010F_010E,B17010F_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlG = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001G_001E,B17001G_002E,B17001G_003E,B17001G_017E,B17010G_003E,B17010G_010E,B17010G_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001H_001E,B17001H_002E,B17001H_003E,B17001H_017E,B17010H_003E,B17010H_010E,B17010H_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001I_001E,B17001I_002E,B17001I_003E,B17001I_017E,B17010I_003E,B17010I_010E,B17010I_016E&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key)

#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfJ_General = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                  DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfJ_General.columns=["Location", "Total population","Poverty population", "Male","Female", "Married couple","Male householder","Female householder","State Code","County Code", "Race"]

#Drop the code for State and County.
dfJ_General = dfJ_General.drop(["State Code", "County Code"], axis=1)

st.header('General Data on Poverty in Jefferson County, KY')
st.write('Data Dimension: ' + str(dfJ_General.shape[0]) + ' rows and ' + str(dfJ_General.shape[1]) + ' columns.')
st.dataframe(dfJ_General)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfJ_General), unsafe_allow_html=True)


#Get the API Data for each variables. (Poverty in Kentucky by race)
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001_001E,B17001_002E,B17001_003E,B17001_017E,B17010_003E,B17010_010E,B17010_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001A_001E,B17001A_002E,B17001A_003E,B17001A_017E,B17010A_003E,B17010A_010E,B17010A_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001B_001E,B17001B_002E,B17001B_003E,B17001B_017E,B17010B_003E,B17010B_010E,B17010B_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001C_001E,B17001C_002E,B17001C_003E,B17001C_017E,B17010C_003E,B17010C_010E,B17010C_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001D_001E,B17001D_002E,B17001D_003E,B17001D_017E,B17010D_003E,B17010D_010E,B17010D_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001E_001E,B17001E_002E,B17001E_003E,B17001E_017E,B17010E_003E,B17010E_010E,B17010E_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlF = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001F_001E,B17001F_002E,B17001F_003E,B17001F_017E,B17010F_003E,B17010F_010E,B17010F_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlG = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001G_001E,B17001G_002E,B17001G_003E,B17001G_017E,B17010G_003E,B17010G_010E,B17010G_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001H_001E,B17001H_002E,B17001H_003E,B17001H_017E,B17010H_003E,B17010H_010E,B17010H_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001I_001E,B17001I_002E,B17001I_003E,B17001I_017E,B17010I_003E,B17010I_010E,B17010I_016E&for=state:21&key={1}"\
    .format(YEAR,census_api_key)

#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfK_general = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                 DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfK_general.columns = ["Location", "Total population","Poverty population","Male","Female", "Married couple", "Male householder", "Female householder","State Code", "Race"]

#Drop the State code column.
dfK_general = dfK_general.drop("State Code", axis=1)

st.header('General Data on Poverty in Kentucky')
st.write('Data Dimension: ' + str(dfK_general.shape[0]) + ' rows and ' + str(dfK_general.shape[1]) + ' columns.')
st.dataframe(dfK_general)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfK_general), unsafe_allow_html=True)


#Get the API Data for each variables. (Poverty in the US by race)
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001_001E,B17001_002E,B17001_003E,B17001_017E,B17010_003E,B17010_010E,B17010_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001A_001E,B17001A_002E,B17001A_003E,B17001A_017E,B17010A_003E,B17010A_010E,B17010A_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001B_001E,B17001B_002E,B17001B_003E,B17001B_017E,B17010B_003E,B17010B_010E,B17010B_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001C_001E,B17001C_002E,B17001C_003E,B17001C_017E,B17010C_003E,B17010C_010E,B17010C_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001D_001E,B17001D_002E,B17001D_003E,B17001D_017E,B17010D_003E,B17010D_010E,B17010D_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001E_001E,B17001E_002E,B17001E_003E,B17001E_017E,B17010E_003E,B17010E_010E,B17010E_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlF ="https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001F_001E,B17001F_002E,B17001F_003E,B17001F_017E,B17010F_003E,B17010F_010E,B17010F_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlG ="https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001G_001E,B17001G_002E,B17001G_003E,B17001G_017E,B17010G_003E,B17010G_010E,B17010G_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001H_001E,B17001H_002E,B17001H_003E,B17001H_017E,B17010H_003E,B17010H_010E,B17010H_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,B17001I_001E,B17001I_002E,B17001I_003E,B17001I_017E,B17010I_003E,B17010I_010E,B17010I_016E&for=us:*&key={1}"\
    .format(YEAR,census_api_key)
#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfUS_general = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                 DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfUS_general.columns = ["Location", "Total population","Poverty population","Male","Female", "Married couple", "Male householder", "Female householder", "US", "Race"]

#Drop the State code column.
dfUS_general = dfUS_general.drop("US", axis=1)

st.header('General Data on Poverty in the US')
st.write('Data Dimension: ' + str(dfUS_general.shape[0]) + ' rows and ' + str(dfUS_general.shape[1]) + ' columns.')
st.dataframe(dfUS_general)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfUS_general), unsafe_allow_html=True)


#joint the tables
#Join the three tables
dfMerge1 = pd.concat([dfJ_General, dfK_general, dfUS_general])
dfMerge1["Year"]=YEAR

st.header('General Data on Poverty Join table')
st.write('Data Dimension: ' + str(dfMerge1.shape[0]) + ' rows and ' + str(dfMerge1.shape[1]) + ' columns.')
st.dataframe(dfMerge1)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfMerge1), unsafe_allow_html=True)



#Store the age variables
#Create Variables for different racies
varT= "B17001_004E,B17001_005E,B17001_006E,B17001_007E,B17001_008E,B17001_009E,B17001_010E,B17001_011E,B17001_012E,B17001_013E,B17001_014E,B17001_015E,B17001_016E,B17001_018E,B17001_019E,B17001_020E,B17001_021E,B17001_022E,B17001_023E,B17001_024E,B17001_025E,B17001_026E,B17001_027E,B17001_028E,B17001_029E,B17001_030E"
varA= "B17001A_004E,B17001A_005E,B17001A_006E,B17001A_007E,B17001A_008E,B17001A_009E,B17001A_010E,B17001A_011E,B17001A_012E,B17001A_013E,B17001A_014E,B17001A_015E,B17001A_016E,B17001A_018E,B17001A_019E,B17001A_020E,B17001A_021E,B17001A_022E,B17001A_023E,B17001A_024E,B17001A_025E,B17001A_026E,B17001A_027E,B17001A_028E,B17001A_029E,B17001A_030E"
varB= "B17001B_004E,B17001B_005E,B17001B_006E,B17001B_007E,B17001B_008E,B17001B_009E,B17001B_010E,B17001B_011E,B17001B_012E,B17001B_013E,B17001B_014E,B17001B_015E,B17001B_016E,B17001B_018E,B17001B_019E,B17001B_020E,B17001B_021E,B17001B_022E,B17001B_023E,B17001B_024E,B17001B_025E,B17001B_026E,B17001B_027E,B17001B_028E,B17001B_029E,B17001B_030E"
varC= "B17001C_004E,B17001C_005E,B17001C_006E,B17001C_007E,B17001C_008E,B17001C_009E,B17001C_010E,B17001C_011E,B17001C_012E,B17001C_013E,B17001C_014E,B17001C_015E,B17001C_016E,B17001C_018E,B17001C_019E,B17001C_020E,B17001C_021E,B17001C_022E,B17001C_023E,B17001C_024E,B17001C_025E,B17001C_026E,B17001C_027E,B17001C_028E,B17001C_029E,B17001C_030E"
varD= "B17001D_004E,B17001D_005E,B17001D_006E,B17001D_007E,B17001D_008E,B17001D_009E,B17001D_010E,B17001D_011E,B17001D_012E,B17001D_013E,B17001D_014E,B17001D_015E,B17001D_016E,B17001D_018E,B17001D_019E,B17001D_020E,B17001D_021E,B17001D_022E,B17001D_023E,B17001D_024E,B17001D_025E,B17001D_026E,B17001D_027E,B17001D_028E,B17001D_029E,B17001D_030E"
varE= "B17001E_004E,B17001E_005E,B17001E_006E,B17001E_007E,B17001E_008E,B17001E_009E,B17001E_010E,B17001E_011E,B17001E_012E,B17001E_013E,B17001E_014E,B17001E_015E,B17001E_016E,B17001E_018E,B17001E_019E,B17001E_020E,B17001E_021E,B17001E_022E,B17001E_023E,B17001E_024E,B17001E_025E,B17001E_026E,B17001E_027E,B17001E_028E,B17001E_029E,B17001E_030E"
varF= "B17001F_004E,B17001F_005E,B17001F_006E,B17001F_007E,B17001F_008E,B17001F_009E,B17001F_010E,B17001F_011E,B17001F_012E,B17001F_013E,B17001F_014E,B17001F_015E,B17001F_016E,B17001F_018E,B17001F_019E,B17001F_020E,B17001F_021E,B17001F_022E,B17001F_023E,B17001F_024E,B17001F_025E,B17001F_026E,B17001F_027E,B17001F_028E,B17001F_029E,B17001F_030E"
varG= "B17001G_004E,B17001G_005E,B17001G_006E,B17001G_007E,B17001G_008E,B17001G_009E,B17001G_010E,B17001G_011E,B17001G_012E,B17001G_013E,B17001G_014E,B17001G_015E,B17001G_016E,B17001G_018E,B17001G_019E,B17001G_020E,B17001G_021E,B17001G_022E,B17001G_023E,B17001G_024E,B17001G_025E,B17001G_026E,B17001G_027E,B17001G_028E,B17001G_029E,B17001G_030E"
varH= "B17001H_004E,B17001H_005E,B17001H_006E,B17001H_007E,B17001H_008E,B17001H_009E,B17001H_010E,B17001H_011E,B17001H_012E,B17001H_013E,B17001H_014E,B17001H_015E,B17001H_016E,B17001H_018E,B17001H_019E,B17001H_020E,B17001H_021E,B17001H_022E,B17001H_023E,B17001H_024E,B17001H_025E,B17001H_026E,B17001H_027E,B17001H_028E,B17001H_029E,B17001H_030E"
varI= "B17001I_004E,B17001I_005E,B17001I_006E,B17001I_007E,B17001I_008E,B17001I_009E,B17001I_010E,B17001I_011E,B17001I_012E,B17001I_013E,B17001I_014E,B17001I_015E,B17001I_016E,B17001I_018E,B17001I_019E,B17001I_020E,B17001I_021E,B17001I_022E,B17001I_023E,B17001I_024E,B17001I_025E,B17001I_026E,B17001I_027E,B17001I_028E,B17001I_029E,B17001I_030E"

#Name of the variables above
name= ["Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17","Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64","Male 65-74","Male 75 and older", "Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17","Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64","Female 65-74","Female 75 and older"]

#Detailed age data
#Get the API Data for each variables. (Poverty in Jefferson county by race)
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varT)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varA)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varB)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varC)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varD)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varE)
urlF = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varF)
urlG = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varG)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varH)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varI)

#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfageJ = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                  DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfageJ.columns = ["Location", "Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17","Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64","Male 65-74","Male 75 and older", "Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17","Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64","Female 65-74","Female 75 and older","State code","County code","info"]


#Add new measures by combine columns
dfageJ["Male under 18"]= dfageJ[["Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17"]].sum(axis =1, skipna=True)
dfageJ["Female under 18"]= dfageJ[["Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17"]].sum(axis =1, skipna=True)
dfageJ["Male Above 64"]= dfageJ[["Male 65-74","Male 75 and older"]].sum(axis =1, skipna=True)
dfageJ["Female Above 64"]= dfageJ[["Female 65-74","Female 75 and older"]].sum(axis =1, skipna=True)
dfageJ["Male 18-64"]= dfageJ[["Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64"]].sum(axis =1, skipna=True)
dfageJ["Female 18-64"]= dfageJ[["Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64"]].sum(axis =1, skipna=True)

#Drop the State code column.
dfageJ = dfageJ.drop(["State code","County code"], axis=1)

st.header('Poverty By Age Groups in Jefferson County, KY')
st.write('Data Dimension: ' + str(dfageJ.shape[0]) + ' rows and ' + str(dfageJ.shape[1]) + ' columns.')
st.dataframe(dfageJ)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfageJ), unsafe_allow_html=True)


#Detailed age data for the state of KY
#Get the API Data for each variables. 
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varT)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varA)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varB)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varC)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varD)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varE)
urlF = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varF)
urlG = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varG)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varH)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varI)

#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfageK = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                  DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfageK.columns = ["Location", "Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17","Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64","Male 65-74","Male 75 and older", "Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17","Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64","Female 65-74","Female 75 and older","State code","info"]


#Add new measures by combine columns
dfageK["Male under 18"]= dfageK[["Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17"]].sum(axis =1, skipna=True)
dfageK["Female under 18"]= dfageK[["Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17"]].sum(axis =1, skipna=True)
dfageK["Male Above 64"]= dfageK[["Male 65-74","Male 75 and older"]].sum(axis =1, skipna=True)
dfageK["Female Above 64"]= dfageK[["Female 65-74","Female 75 and older"]].sum(axis =1, skipna=True)
dfageK["Male 18-64"]= dfageK[["Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64"]].sum(axis =1, skipna=True)
dfageK["Female 18-64"]= dfageK[["Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64"]].sum(axis =1, skipna=True)


#Drop the State code column.
dfageK = dfageK.drop(["State code"], axis=1)

st.header('Poverty By Age Groups in Kentucky')
st.write('Data Dimension: ' + str(dfageK.shape[0]) + ' rows and ' + str(dfageK.shape[1]) + ' columns.')
st.dataframe(dfageK)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfageK), unsafe_allow_html=True)


#Detailed age data for the US
#Get the API Data for each variables. 
urlT = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varT)
urlA = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varA)
urlB = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varB)
urlC = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varC)
urlD = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varD)
urlE = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varE)
urlF = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varF)
urlG = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varG)
urlH = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varH)
urlI = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varI)

#Transfer the json data to dataframe
DFT = json_to_dataframe(requests.request("GET", urlT))
DFA = json_to_dataframe(requests.request("GET", urlA))
DFB = json_to_dataframe(requests.request("GET", urlB))
DFC = json_to_dataframe(requests.request("GET", urlC))
DFD = json_to_dataframe(requests.request("GET", urlD))
DFE = json_to_dataframe(requests.request("GET", urlE))
DFF = json_to_dataframe(requests.request("GET", urlF))
DFG = json_to_dataframe(requests.request("GET", urlG))
DFH = json_to_dataframe(requests.request("GET", urlH))
DFI = json_to_dataframe(requests.request("GET", urlI))

#Add additional info for the race
DFT['info'] = "Total poverty population"
DFA['info'] = "White Alone"
DFB['info'] = "Black or African American Alone"
DFC['info'] = "American Indian and Alaska Native Alone"
DFD['info'] = "Asian Alone"
DFE['info'] = "Native Hawaiian ana Other Pacific Islander Alone"
DFF['info'] = "Some Other Race Alone"
DFG['info'] = "Two or More Races"
DFH['info'] = "White Alone, Not Hispanic or Latino"
DFI['info'] = "Hispanic or Latino"

#Concate the dataframes into one dataframe
dfageUS = pd.DataFrame(np.concatenate([DFT.values, DFA.values, DFB.values,DFC.values, DFD.values,
                                  DFE.values,DFF.values, DFG.values, DFH.values,DFI.values]))

#Add column name
dfageUS.columns = ["Location", "Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17","Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64","Male 65-74","Male 75 and older", "Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17","Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64","Female 65-74","Female 75 and older","US","info"]


#Add new measures by combine columns
dfageUS["Male under 18"]= dfageUS[["Male less than 5","Male 5","Male 6-11","Male 12-14","Male 15","Male 16-17"]].sum(axis =1, skipna=True)
dfageUS["Female under 18"]= dfageUS[["Female less than 5","Female 5","Female 6-11","Female 12-14","Female 15","Female 16-17"]].sum(axis =1, skipna=True)
dfageUS["Male Above 64"]= dfageUS[["Male 65-74","Male 75 and older"]].sum(axis =1, skipna=True)
dfageUS["Female Above 64"]= dfageUS[["Female 65-74","Female 75 and older"]].sum(axis =1, skipna=True)
dfageUS["Male 18-64"]= dfageUS[["Male 18-24","Male 25-34","Male 35-44","Male 45-54","Male 55-64"]].sum(axis =1, skipna=True)
dfageUS["Female 18-64"]= dfageUS[["Female 18-24","Female 25-34","Female 35-44", "Female 45-54", "Female 55-64"]].sum(axis =1, skipna=True)

#Drop the State code column.
dfageUS = dfageUS.drop(["US"], axis=1)

st.header('Poverty By Age Groups in the US')
st.write('Data Dimension: ' + str(dfageUS.shape[0]) + ' rows and ' + str(dfageUS.shape[1]) + ' columns.')
st.dataframe(dfageUS)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfageUS), unsafe_allow_html=True)

#Join the three tables
dfageMerge = pd.concat([dfageJ, dfageK, dfageUS])

#Add Year 
dfageMerge["Year"]=YEAR

st.header('Poverty By Age Groups Joint Table')
st.write('Data Dimension: ' + str(dfageMerge.shape[0]) + ' rows and ' + str(dfageMerge.shape[1]) + ' columns.')
st.dataframe(dfageMerge)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfageMerge), unsafe_allow_html=True)


#Store the Education variables
#less than high school graduate
varu1= "B17003_004E,B17003_009E"
#High school graduate
varu2= "B17003_005E,B17003_010E"
#some college, associate's degree
varu3= "B17003_006E,B17003_011E"
#Bachelor's degree or higher
varu4= "B17003_007E,B17003_012E"

#Education data for Jefferson County
url1 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu1)
url2 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu2)
url3 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu3)
url4 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu4)

#Transfer the json data to dataframe
DF1 = json_to_dataframe(requests.request("GET", url1))
DF2 = json_to_dataframe(requests.request("GET", url2))
DF3 = json_to_dataframe(requests.request("GET", url3))
DF4 = json_to_dataframe(requests.request("GET", url4))

#Add additional info for the race
DF1['info'] = "Less than high school graduate"
DF2['info'] = "High school graduate"
DF3['info'] = "Some college, associate's degree"
DF4['info'] = "Bachlor's degree or higher"

#Concate the dataframes into one dataframe
dfeJ = pd.DataFrame(np.concatenate([DF1.values, DF2.values, DF3.values,DF4.values]))

#Add column name
dfeJ.columns = ["Location", "Male","Female", "State", "County","info"]

#Drop the State code column.
dfeJ = dfeJ.drop(["State","County"], axis=1)


st.header('Poverty By Education in Jefferson County, KY')
st.write('Data Dimension: ' + str(dfeJ.shape[0]) + ' rows and ' + str(dfeJ.shape[1]) + ' columns.')
st.dataframe(dfeJ)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfeJ), unsafe_allow_html=True)



#Education data for the State of kentucky
url1 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu1)
url2 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu2)
url3 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu3)
url4 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varu4)

#Transfer the json data to dataframe
DF1 = json_to_dataframe(requests.request("GET", url1))
DF2 = json_to_dataframe(requests.request("GET", url2))
DF3 = json_to_dataframe(requests.request("GET", url3))
DF4 = json_to_dataframe(requests.request("GET", url4))


#Add additional info for the race
DF1['info'] = "Less than high school graduate"
DF2['info'] = "High school graduate"
DF3['info'] = "Some college, associate's degree"
DF4['info'] = "Bachlor's degree or higher"

#Concate the dataframes into one dataframe
dfeK = pd.DataFrame(np.concatenate([DF1.values, DF2.values, DF3.values,DF4.values]))

#Add column name
dfeK.columns = ["Location", "Male","Female", "State","info"]

#Drop the State code column.
dfeK = dfeK.drop(["State"], axis=1)

st.header('Poverty By Education in Kentucky')
st.write('Data Dimension: ' + str(dfeK.shape[0]) + ' rows and ' + str(dfeK.shape[1]) + ' columns.')
st.dataframe(dfeK)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfeK), unsafe_allow_html=True)




#Education data for the US 
url1 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varu1)
url2 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varu2)
url3 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varu3)
url4 = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varu4)

#Transfer the json data to dataframe
DF1 = json_to_dataframe(requests.request("GET", url1))
DF2 = json_to_dataframe(requests.request("GET", url2))
DF3 = json_to_dataframe(requests.request("GET", url3))
DF4 = json_to_dataframe(requests.request("GET", url4))


#Add additional info for the race
DF1['info'] = "Less than high school graduate"
DF2['info'] = "High school graduate"
DF3['info'] = "Some college, associate's degree"
DF4['info'] = "Bachlor's degree or higher"

#Concate the dataframes into one dataframe
dfeUS = pd.DataFrame(np.concatenate([DF1.values, DF2.values, DF3.values,DF4.values]))

#Add column name
dfeUS.columns = ["Location", "Male","Female", "us","info"]

#Drop the State code column.
dfeUS = dfeUS.drop(["us"], axis=1)

st.header('Poverty By Education in US')
st.write('Data Dimension: ' + str(dfeUS.shape[0]) + ' rows and ' + str(dfeUS.shape[1]) + ' columns.')
st.dataframe(dfeUS)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfeUS), unsafe_allow_html=True)

#Join the three tables
dfeMerge = pd.concat([dfeJ, dfeK, dfeUS])

#Add the Year column 
dfeMerge['Year']=YEAR

st.header('Poverty By Education Join Table')
st.write('Data Dimension: ' + str(dfeMerge.shape[0]) + ' rows and ' + str(dfeMerge.shape[1]) + ' columns.')
st.dataframe(dfeMerge)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(dfeMerge), unsafe_allow_html=True)


#Rent poverty information
#Variables
census_api_key = "663083891f5b9346c0f75af604c1bb8f7e48712b"
YEAR = 2019

varRent="B25070_001E,B25070_002E,B25070_003E,B25070_004E,B25070_005E,B25070_006E,B25070_007E,B25070_008E,B25070_009E,B25070_010E,B25070_011E"
#Description of the variables
#('Total','Less than 10.0 percent','10.0 to 14.9 percent','15.0 to 19.9 percent','20.0 to 24.9 percent',
#'25.0 to 29.9 percent','30.0 to 34.9 percent','35.0 to 39.9 percent','40.0 to 49.9 percent','50.0 percent or more','Not computed')
#Request Data from US Census API 
#Jefferson county
urlJ = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varRent)
#Ky
urlK = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varRent)
#US
urlUS = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varRent)


#Transfer the json data to dataframe
DFJ = json_to_dataframe(requests.request("GET", urlJ))
DFK = json_to_dataframe(requests.request("GET", urlK))
DFUS = json_to_dataframe(requests.request("GET", urlUS))

#Drop the columns for state, county which are different in the three dataframes.
DFJ = DFJ.drop(["state", "county"], axis=1)
DFK = DFK.drop(["state"], axis=1)
DFUS = DFUS.drop(["us"], axis=1)

#Concate the dataframes into one dataframe
DF_rent = pd.DataFrame(np.concatenate([DFJ.values, DFK.values, DFUS.values]))

#Add column name
DF_rent.columns = ['Name','Total','Less than 10.0 percent','10.0 to 14.9 percent','15.0 to 19.9 percent','20.0 to 24.9 percent',
              '25.0 to 29.9 percent','30.0 to 34.9 percent','35.0 to 39.9 percent','40.0 to 49.9 percent','50.0 percent or more','Not computed']

DF_rent['Year']=YEAR

st.header('Rent Information')
st.write('Data Dimension: ' + str(DF_rent.shape[0]) + ' rows and ' + str(DF_rent.shape[1]) + ' columns.')
st.dataframe(DF_rent)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(DF_rent), unsafe_allow_html=True)

#**MORTGAGE STATUS BY SELECTED MONTHLY OWNER COSTS AS A PERCENTAGE OF HOUSEHOLD INCOME IN THE PAST 12 MONTHS**

#New variables for home owner cost
varHOC= "B25091_001E,B25091_002E,B25091_003E,B25091_004E,B25091_005E,B25091_006E,B25091_007E,B25091_008E,B25091_009E,B25091_010E,B25091_011E,B25091_012E"
#Description of the variables
#'Total','Housing units with a mortgage','Less than 10.0 percent','10.0 to 14.9 percent','15.0 to 19.9 percent','20.0 to 24.9 percent',
#'25.0 to 29.9 percent','30.0 to 34.9 percent','35.0 to 39.9 percent','40.0 to 49.9 percent','50.0 percent or more',
#'Not computed'

#Request Data from US Census API 
#Jefferson county
urlJ = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=county:111&in=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varHOC)
#Ky
urlK = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=state:21&key={1}"\
    .format(YEAR,census_api_key,A=varHOC)
#US
urlUS = "https://api.census.gov/data/{0}/acs/acs1?get=NAME,{A}&for=us:*&key={1}"\
    .format(YEAR,census_api_key,A=varHOC)


#Transfer the json data to dataframe
DFJ = json_to_dataframe(requests.request("GET", urlJ))
DFK = json_to_dataframe(requests.request("GET", urlK))
DFUS = json_to_dataframe(requests.request("GET", urlUS))

#Drop the columns for state, county which are different in the three dataframes.
DFJ = DFJ.drop(["state", "county"], axis=1)
DFK = DFK.drop(["state"], axis=1)
DFUS = DFUS.drop(["us"], axis=1)

#Concate the dataframes into one dataframe
DF_Morg = pd.DataFrame(np.concatenate([DFJ.values, DFK.values, DFUS.values]))

#Add column name
DF_Morg.columns = ['Name','Housing units with a mortgage','Total','Less than 10.0 percent','10.0 to 14.9 percent','15.0 to 19.9 percent','20.0 to 24.9 percent',
              '25.0 to 29.9 percent','30.0 to 34.9 percent','35.0 to 39.9 percent','40.0 to 49.9 percent','50.0 percent or more','Not computed']
DF_Morg['Year']=YEAR

st.header('Mortgage Status')
st.write('Data Dimension: ' + str(DF_Morg.shape[0]) + ' rows and ' + str(DF_Morg.shape[1]) + ' columns.')
st.dataframe(DF_Morg)

#download data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
def filedownload(df):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href
st.markdown(filedownload(DF_Morg), unsafe_allow_html=True)












