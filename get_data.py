import PyDST
import pandas as pd


conn = PyDST.connection(language = 'da')


City = conn.get_data(
                table_id = 'TURIST',
                variables = ['overnatf', 'område', 'nation1', 'periode', 'tid'],
                
                values = {'overnatf':['100','110','130', '140', '150','160','170'], 
                          'område':['000','084','01','02','03','04'], 
                          'nation1':['TOT', 'DAN', 'UDLAN', 'BELU', 'BUL', 'CYP', 'EST', 'FIN', 
                                     'FRA', 'FÆR', 'GRÆ', 'GRØ', 'HOL', 'IRL', 'ISL', 'ITA', 'KRO', 
                                     'LET', 'LIT', 'LUX', 'MAL', 'NOR', 'POL', 'POR', 'RUM', 'RUS', 
                                     'SCH', 'SLV', 'SLO', 'SPA', 'STO', 'SVE', 'TJR', 'TYR', 'TYS', 
                                     'UKR', 'UNG', 'ØST', 'EUØ', 'SYD', 'AFRX', 'BRA', 'CAN', 
                                     'USA', 'AMØ', 'KIN', 'JAP', 'KOR', 'IND', 'THA', 'SØA', 'AUS', 'OCEX', 'ANDRE'
                                     ], 
                                                    
                          'periode':['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'],
                          
                          'tid': ['2007', '2008', '2009', '2010', '2011', '2012', '2013',
                                  '2014', '2015', '2016', '2017', '2018']},
                
                     )

#df[df.columns[5]] indeholder både str og ints. 


df = City.df
df.head(5)


df['Timestamp']=df['PERIODE'].map(str) + ['-'] + df['TID'].map(str)
df['Timestamp']=df['Timestamp'].str.replace('Januar','01-01')
df['Timestamp']=df['Timestamp'].str.replace('Februar','01-02')
df['Timestamp']=df['Timestamp'].str.replace('Marts','01-03')
df['Timestamp']=df['Timestamp'].str.replace('April','01-04')
df['Timestamp']=df['Timestamp'].str.replace('Maj','01-05')
df['Timestamp']=df['Timestamp'].str.replace('Juni','01-06')
df['Timestamp']=df['Timestamp'].str.replace('Juli','01-07')
df['Timestamp']=df['Timestamp'].str.replace('August','01-08')
df['Timestamp']=df['Timestamp'].str.replace('September','01-09')
df['Timestamp']=df['Timestamp'].str.replace('Oktober','01-10')
df['Timestamp']=df['Timestamp'].str.replace('November','01-11')
df['Timestamp']=df['Timestamp'].str.replace('December','01-12')

df.Timestamp = pd.to_datetime(df['Timestamp'], dayfirst = 'TRUE')