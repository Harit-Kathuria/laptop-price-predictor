import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('pipe.pkl','rb'))
data = pickle.load(open('data.pkl','rb'))

st.title('Laptop Price Predictor')

company = st.selectbox('Brand',data['Manufacturer'].unique())
type = st.selectbox('Type',data['Category'].unique())
weight = st.number_input('Weight')
touchscreen = st.selectbox('Touchscreen',['No','Yes'])
ips = st.selectbox('IPS',['No','Yes'])
ss = st.number_input('Screen Size')
reso = st.selectbox('Resolution',['1920x1080','1366x768','1600x900','3840x2160',
'3200x1080','2880x1800','2560x1600','2560x1440','2304x1440'])
cpu = st.selectbox('CPU',data['Cpu brand'].unique())

ram = st.selectbox('RAM',[2,4,6,8,12,16,24,32,64])
hdd = st.selectbox('HDD(in GB',[0,32,128,500,1000,2000])
ssd = st.selectbox('SSD(in GB',[0,32,64,128,256,512,1024])

gpu = st.selectbox('GPU',data['gpu'].unique())
os = st.selectbox('OS',data['OS'].unique())

if st.button('Predict Price'):
    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips == 'Yes':
        ips = 1
    else: ips = 0

    xr = int(reso.split('x')[0])
    yr = int(reso.split('x')[1])
    ppi = (xr**2 + yr**2)**0.5/ss

    query = np.array([company,type,weight,ram,touchscreen,ips,ppi,cpu,hdd,ssd,gpu,os])
    query = query.reshape((1,12))

    price = int(np.exp(pipe.predict(query)[0]))
    st.title(price)