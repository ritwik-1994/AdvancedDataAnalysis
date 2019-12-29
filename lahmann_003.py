import pandas as pd
import requests
import zipfile
import StringIO
#salaries = pd.read_csv('/home/shipsy/Downloads/baseballdatabank-2019.2/core/Salaries.Csv')
#teams = pd.read_csv('/home/shipsy/Downloads/baseballdatabank-2019.2/core/Teams.Csv')

r = requests.get('http://seanlahman.com/files/database/lahman-csv_2014-02-14.zip')
zipFile = zipfile.ZipFile(StringIO.StringIO(r.content))
salariedDF = pd.read_csv(zipFile.open('Salaries.csv'))
teamsDF = pd.read_csv(zipFile.open('Teams.csv'))
#SalSummary = salariedDF.groupby(['teamID','yearID']).sum()
newSummary = teamsDF.merge(salariedDF, how ='inner', on = ['teamID','yearID'])

print(newSummary.groupby(['teamID','yearID']).sum().loc[:,['teamID','yearID','W','salary']].head())
