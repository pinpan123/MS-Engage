import matplotlib
import streamlit as st
import pandas as pd
from jedi.api.refactoring import inline
#%matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
DATA_URL = ("Automobile data-Cleaned.csv")
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Data Analysis for Automotive Industry')
st.image('car1.png')

st.sidebar.title("Choose Analysis type")
user_menu = st.sidebar.radio(
    'Select an Option',
    ('Univariate','Bivariate','Multivariate')
)
df = pd.read_csv(DATA_URL)
# return df
st.markdown('### Dataframe')
st.write(df)
st.markdown("### Looking at the dataset post cleaning:")



st.markdown("#### Shape")

st.write('Number of rows: {}, Number of columns: {}'.format(*df.shape))

st.markdown("#### Count")
st.write('Number of Car makers considered: {}'.format(*df['Make'].unique().shape))
st.write(df['Make'].value_counts())
st.write('Total number of cars: {}'.format(*df['Model'].shape))

st.markdown("## Data Visualization:")


if user_menu=='Univariate':

 def uni():
  st.markdown('###  Univariate Analysis')
 st.markdown('##### Frequency Distribution graphs')
st.markdown('###### A. Numeric Attributes:')
st.image('hist1.png')
st.markdown('##### **Findings:**')
st.info(' 1. About 94% of the vehicles have 4 gears and the rest mainly range between 5-8 gears')
st.info('2. The cars mostly have 4 or 5 doors, 2 being the b=number for the Coupes')
st.info('3. The number of valves per cylinder in the cars ranges from >2 to <=6')
st.info('4. 5 to 6 seaters are the most popular choice')
st.info('5. All cars have atleast 2 airbags, which is the most common occurence, followed by 6 airbags')
st.info('6. Only in a few models, have more than 1 USB Ports provided')
st.info('7. Fuel tank capacity for most cars is around 50 Litres')
st.info('8. Displacement is less than 3750 cc for most cars')

st.markdown('##### B. Object Attributes:')
st.write('1. Make')
df['Make'].value_counts(normalize=True).plot(kind='bar',color='Red')
plt.title("Make frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Make')
st.pyplot()
st.info('1. Xuv500 has the highest share of the sales with more than 3.5 %')

st.write('2. Emission Norm')
plt.subplot()
df['Emission_Norm'].value_counts(normalize=True).plot(figsize=(8,5),kind='bar',color='orange')
plt.title("Emission_Norm frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Emission_Norm');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('2. More than 70% of the cars only follow BS1V Emission norms')

st.write('3. Fuel Tank Capacity')
plt.subplot()
df['Fuel_Tank_Capacity(in Litres)'].value_counts(normalize=True).plot(kind='bar',color='orange')
plt.title("Fuel_Tank_Capacity frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Fuel_Tank_Capacity(in Litres)');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('3. 45 Litres fuel capacity is most commonly bought with 65 L being the least popular')

st.write('4. Fuel Type')
plt.subplot()
df['Fuel_Type'].value_counts(normalize=True).plot(figsize=(8,3),kind='bar',color='orange')
plt.title("Fuel_Type frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Fuel_Type');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('4. Hybrid cars make up less than 10% of the sales')

st.write('5. Type')
plt.subplot()
df['Type'].value_counts(normalize=True).plot(figsize=(5,3),kind='bar',color='Green')
plt.title("Type frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Type');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('5. Manual cars remain the most popular choice with more than 40% sales')

st.write('6. Body Type')
plt.subplot()
df['Body_Type'].value_counts(normalize=True).plot(figsize=(8,5),kind='bar',color='orange')
plt.title("Body_Type frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Body_Type');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('6. Sedan+SUV sale make up around 70% of the sales')


st.write('7. Basic Warranty')
plt.subplot()
df['Basic_Warranty'].value_counts(normalize=True).plot(figsize=(8,8),kind='bar',color='orange')
plt.title("Basic_Warranty frequency diagram")
plt.ylabel('Number of cars')
plt.xlabel('Basic_Warranty');
plt.tight_layout()
plt.show()
st.pyplot()
st.info('7. About 40% of the cars provide 2 years/Unlimited Kms basic warranty')

g3=sns.catplot(data=df, x="Keyless_Entry", y="Boot_Space(in)",kind="violin")
g3.fig.set_figwidth(20)
g3.fig.set_figheight(8)
st.pyplot()

if user_menu=='Bivariate':
 def bi():
    st.markdown('###  Bivariate Analysis')

st.write('1. Make v/s Price')
st.image('bi1.png')
st.info('1. Bentley has the highest price range, followed by Aston Martin and Porsche, but a specific Lamborghini model is the most expensive car at Rs. 4 Crore')

st.write('2. Fuel type v/s Price')
plt.rcParams['figure.figsize']=(23,10)
ax = sns.boxplot(x="Fuel_Type", y="Ex-Showroom_Price (in Rupees)", data=df)
st.pyplot()
st.info('2. Hybrid cars make up less than 10% of the sales')

st.write('3. Body type v/s Price')
plt.rcParams['figure.figsize']=(23,10)
ax = sns.boxplot(x="Body_Type", y="Ex-Showroom_Price (in Rupees)", data=df)
st.pyplot()
st.info('3. The range for Coupes is the highest and broadest, while Hatchbacks and Crossovers have the lowest prices. Sedans have a widely varying range')

st.write('4. Body type v/s Boot space')
plt.rcParams['figure.figsize']=(30,10)
#plt.figure(figsize=(16,8))
ax = sns.boxplot(x="Body_Type", y="Boot_Space(in)", data=df)
st.pyplot()
st.info('4. SUVs provide the most Boot space, upto 1400 Litres.')



if user_menu=='Multivariate':
 def multi():
  st.markdown('###  Multivariate Analysis')
st.markdown('#### **A. No of cars by Make considered with respect to:**')
st.write('1. Start/Stop button')
pd.crosstab(df['Make'],df['Start_/_Stop_Button']).plot.bar(stacked=True)
st.pyplot()
st.info('1. No Fiat and Premier cars have Start/Stop Button')

st.write('2. Central Locking system')
pd.crosstab(df['Make'],df['Central_Locking']).plot.bar(stacked=True)
st.pyplot()
st.info('2. Toyota has >10 models without a Central Locking systems')

st.write('3. Child safety locks')
pd.crosstab(df['Make'],df['Child_Safety_Locks']).plot.bar(stacked=True)
st.pyplot()
st.info('3. No Lamborghini or DC cars have Child safety locks. Nissan, BMW AND Hyundai have less than 10 cars without it')

st.write('4. Clock')
pd.crosstab(df['Make'],df['Clock']).plot.bar(stacked=True)
st.pyplot()
st.info('4. Porsche provides analog clocks')

st.write('5. Cup Holders')
pd.crosstab(df['Make'],df['Cup_Holders']).plot.bar(stacked=True)
st.pyplot()
st.info('5. Front and Rear cupholders are seen in most cars with Mitsubishi and Tata offering them in the centre in a few models. Fiat has cars with no cup holders too')

st.write('6. Engine Malfunction Light')
pd.crosstab(df['Make'],df['Engine_Malfunction_Light']).plot.bar(stacked=True)
st.pyplot()
st.info('6. BMW, Honda and Toyota do not have Engine Malfunction Light for some models')


st.write('7. FM Radio')
pd.crosstab(df['Make'],df['FM_Radio']).plot.bar(stacked=True)
st.pyplot()
st.info('7. All makers have FM Radio inbuilt except some Maruti Suzuki and Toyota cars')

st.write('8. Fuel lid opener and Fuel Gauge')
pd.crosstab(df['Make'],df['Fuel-lid_Opener']).plot.bar(stacked=True)
st.pyplot()

pd.crosstab(df['Make'],df['Fuel_Gauge']).plot.bar(stacked=True)
st.pyplot()
st.info('8. All Jeeps have a remote-controlled lid-opener system. BMW provides the option of both- Manual+with Remote')

st.write('9. Instrument Console')
pd.crosstab(df['Make'],df['Instrument_Console']).plot.bar(stacked=True)
st.pyplot()
st.info('9. Mahindra has the most Digital Instrument consoles')

st.write('10. Low Fuel Warning')
pd.crosstab(df['Make'],df['Low_Fuel_Warning']).plot.bar(stacked=True)
st.pyplot()
st.info('10. Except some Fiats and Hondas, all provide Low Fuel warning')




st.markdown('#### **B. No of cars by Body Type considered with respect to:**')

st.write('1. Ambient Lightning')
pd.crosstab(df['Body_Type'],df['Ambient_Lightning']).plot.bar(stacked=True)
st.pyplot()
st.info('1. SUVs and Sedans have ambient lighting in about 10 models')

st.write('2. Hill Assist')
pd.crosstab(df['Body_Type'],df['Hill_Assist']).plot.bar(stacked=True)
st.pyplot()
st.info('2. All Convertibles, Sedan coupes and sedan convertibles have Hill-Assist, with Coupes and SUVs having it in the majority. Crossovers do not have this')

st.write('3. Cargo/Boot_Lights')
pd.crosstab(df['Body_Type'],df['Cargo/Boot_Lights']).plot.bar(stacked=True)
st.pyplot()
st.info('3. Only 37 cars have Cargo/Boot Lights')

st.write('4. High Speed Alert System')
pd.crosstab(df['Body_Type'],df['High_Speed_Alert_System']).plot.bar(stacked=True)
st.pyplot()
st.info('4. Sedans have the highest range of cars with High-speed alert system >25')

st.write('5. Lane Watch Camera/ Side Mirror Camera')
pd.crosstab(df['Body_Type'],df['Lane_Watch_Camera/_Side_Mirror_Camera']).plot.bar(stacked=True)
st.pyplot()
st.info('5. Convertibles have the majority with Lane watch/side mirror camera')

st.write('6. Voice_Recognition')
pd.crosstab(df['Body_Type'],df['Voice_Recognition']).plot.bar(stacked=True)
st.pyplot()
st.info('6. Voice-recognition system is most widely available in sedans')

st.write('7. ABS_(Anti-lock Braking System) and Door Ajar Warning')
pd.crosstab(df['Body_Type'],df['ABS_(Anti-lock_Braking_System)']).plot.bar(stacked=True)
st.pyplot()
pd.crosstab(df['Body_Type'],df['Door_Ajar_Warning']).plot.bar(stacked=True)
st.pyplot()
st.info('7. Except for 2 Hatchbacks, all have an Anti-lock Braking System and Door ajar warning system')

st.write('8. Gear Shift Reminder')
pd.crosstab(df['Body_Type'],df['Gear_Shift_Reminder']).plot.bar(stacked=True)
st.pyplot()
st.info('8. The gear-shift reminder is majorly absent in MUVs')


st.write('9. Android Auto and Apple CarPlay')
pd.crosstab(df['Body_Type'],df['Android_Auto']).plot.bar(stacked=True)
st.pyplot()
pd.crosstab(df['Body_Type'],df['Apple_CarPlay']).plot.bar(stacked=True)
st.pyplot()
st.info('Android Auto and Apple Carplay is only seen in a few Hatchbacks, MUVs, Sedans and SUVs')

st.write('10. Cigarette_Lighter')
pd.crosstab(df['Body_Type'],df['Cigarette_Lighter']).plot.bar(stacked=True)
st.pyplot()
st.info('10. 8/10 Coupes do not have a Cigarette lighter')

st.write('11. EBA (Electronic Brake Assist)')
pd.crosstab(df['Body_Type'],df['EBA_(Electronic_Brake_Assist)']).plot.bar(stacked=True)
st.pyplot()
st.info('No crossovers have Electronic Brake Assist')

st.write('12. Tyre Pressure Monitoring System')
pd.crosstab(df['Body_Type'],df['Tyre_Pressure_Monitoring_System']).plot.bar(stacked=True)
st.pyplot()
st.info('12. Sedans>Hatchbacks>SUVs without Tyre Pressure Monitoring system')

st.write('13. Rain Sensing Wipers')
pd.crosstab(df['Body_Type'],df['Rain_Sensing_Wipers']).plot.bar(stacked=True)
st.pyplot()
st.info('13. Hatchbacks and Crossovers are majorly without Rain-sensing Wipers')

st.write('14. Cruise Control')
pd.crosstab(df['Body_Type'],df['Cruise_Control']).plot.bar(stacked=True)
st.pyplot()
st.info('14. Sedans have more cars with Cruise Control than SUVs')

st.write('15. City Mileage')
pd.crosstab(df['Body_Type'],df['City_Mileage']).plot.bar(stacked=True)
st.pyplot()
st.info('15. Most widely-found Mileage: City Mileage- 12 Km/Litres for 194 cars, highest in Sedans ')

st.write('16. Highway Mileage')
pd.crosstab(df['Body_Type'],df['Highway_Mileage']).plot.bar(stacked=True)
st.pyplot()
st.info('16. Most widely-found Mileage: Highway Mileage- 23 Km/Litre for 300 cars, highest in Suvs.  Sedan, coupe shares similar mileage for city and highway at 9 and 9.8 Km/L')


st.markdown('#### **C. with Hue parameters:**')
st.write('1. Make v/s Price with Body type as hue parameter')
g=sns.catplot(data=df, x="Make", y="Ex-Showroom_Price (in Rupees)", hue="Body_Type" ,kind="point")
g.fig.set_figwidth(30)
g.fig.set_figheight(6)
st.pyplot()
st.info(' Aston Martin sedans are the most expensive cars, folllowed by Bentley sedans and Lamborghini coupes.')
st.info(' Tata Hatchbacks are the most afodable starting from Rs 5 Lakh. SUVs vary greatly in prices, depending on the make.')
st.info(' Porsche Cayenne being the most expensive and Premier Rio the least.')

st.write('2. Type v/s Fuel tank capacity with City Mileage as hue parameter')
g=sns.catplot(data=df, x="Type", y="Fuel_Tank_Capacity(in Litres)", hue="City_Mileage" ,kind="point")
g.fig.set_figwidth(5)
g.fig.set_figheight(15)
st.pyplot()
st.info(' Automatic cars have the highest variation in fuel tank capacity from 35 to 90 Litres.')
st.info(' All DCTs have 50L capacity.')


st.write('3. Price v/s Seating Capacity with Model as hue parameter')
sns.catplot(data=df, y="Ex-Showroom_Price (in Rupees)", x="Seating_Capacity" , hue="Model" ,kind="point")
st.pyplot()
st.info('Hyundai provides the highest seating capacity(8) at the least price. On the opposite end is a Lamborghini 2-seater.')

st.write('4. Price v/s Seating capacity with Make as hue parameter')
sns.catplot(data=df, y="Ex-Showroom_Price (in Rupees)", x="Seating_Capacity" , hue="Make" ,kind="point")
st.pyplot()
st.info(' 7 seaters are available across a variety of Makers.')
st.info(' 4 seaters are primarily by BMW')

st.write('5. Price v/s Body Type with City Make as hue parameter')
g5=sns.catplot(data=df, y="Ex-Showroom_Price (in Rupees)", x="Body_Type" , hue="Make" ,kind="point")
g5.fig.set_figwidth(20)
g5.fig.set_figheight(5)
st.pyplot()
st.info(' Jaguar, Audi, Volvo, BMW are the only ones that have ventured into the Convertible, Crossover+SUV/Sedan and Sedan coupe segment')

st.markdown('#### D. A concluding Graph')
g = sns.pairplot(df[["Ex-Showroom_Price (in Rupees)", "Height(in mm)", "Length(in mm)", "Width(in mm)", "City_Mileage",
                     "Highway_Mileage",
                     'Extended_Warranty', 'Number_of_Airbags', 'Type']], hue="Type", diag_kind="hist")
st.pyplot()
st.info(' Length increases with width')
st.info(' Number of airbags>5 for most Automatic type cars. It also does not vary with increase in Price, i.e, even the cars with highest number of airbags are available in the mid-range.')
st.info(' Manual and Automatic cars share similarities in terms of Width and Height')


st.markdown('#### E. A concluding table')
st.write('Body type V/s Make with respect to Price')
st.image('table.png')


