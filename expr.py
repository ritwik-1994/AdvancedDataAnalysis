import numpy as np
import pandas as pd
from datetime import datetime

gene_exp = pd.read_csv('/home/shipsy/Downloads/gene_expr.csv')
gene_expr = gene_exp.iloc[0:,1:]
sampleinfo = pd.read_csv("/home/shipsy/Downloads/SI_expr.csv")
cols = sampleinfo['filename']
#print(cols)
#gene_expr=gene_expr[cols]
#sampleinfo['dates']=datetime.strptime(str(sampleinfo['date']),'%Y-%m-%d')
#sampleinfo['year']=sampleinfo['date']
#sampleinfo['month']=sampleinfo['date']
#for x in range(len(sampleinfo)):
#	sampleinfo['month'][x] = str(sampleinfo['date'][x]).split('-')[1]
#	sampleinfo['year'][x] = str(sampleinfo['date'][x]).split('-')[0]
#	sampleinfo['date'][x] = datetime.strptime(sampleinfo['date'][x],'%Y-%m-%d')
#sampleinfo['elapsedindays'] = sampleinfo['date'] - datetime.strptime('2002-10-31','%Y-%m-%d')
sampleinfoCEU = sampleinfo[sampleinfo['ethnicity'] == 'CEU']
colsCEU = sampleinfoCEU['filename']
gene_exprCEU = gene_expr[colsCEU]

