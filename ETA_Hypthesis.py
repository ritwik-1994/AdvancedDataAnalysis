import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('/home/shipsy/Downloads/ETA_Actual_Data.csv')
DPI65926 = df[df['store_id']=='DPI65926']
DPI65926 = DPI65926.reset_index()
#DPI65926['difference'] = [DPI65926['Actual Delvery Time'] - DPI65926['Google ETA']]
temp_diff = []
plt.figure(figsize=(150,150))
for i in range(len(DPI65926)):
	temp_diff.append(round(DPI65926['Actual Delvery Time'][i]-DPI65926['Google ETA'][i],2))
DPI65926['difference'] = temp_diff	
DPI65926_Late = DPI65926[DPI65926['difference']<0].reset_index()
#DPI65926_Late.describe().to_csv('/home/shipsy/Downloads/DPI65926/DPI65926_Late_Describe.csv')
#f = open('/home/shipsy/Downloads/DPI65926_describe.CSV','w+')
#DPI67247.describe().to_csv('/home/shipsy/Downloads/DPI65926/DPI67247_describe.CSV')
#print(DPI67247.describe())
DPI65926_Late['difference'][:1500].plot(kind='line', color = 'r')
plt.xlabel('Order Index : DPI67247_Late')
plt.ylabel('Actual Delivery Time - Google ETA')
plt.xticks((0,150,300,450,600,750,1050,1200,1350,900,1500), ('0','250','500','750','1000','1250','1500','1750','2000','2250','2530'))
plt.show()
#DPI65926['difference'][500:1000].plot(kind='line')
#plt.show()
#print(DPI65926.describe())
#exceptions = {}

#for i in range(len(DPI65926)):
#	if(DPI65926['
#	exceptions{}

