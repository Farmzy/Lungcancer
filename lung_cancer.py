import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('lung_cancer.sav','rb'))

st.title('Prediksi Terkena Penyakit Paru-Paru')
col1, col2, col3 = st.columns(3)

with col1:
   GENDER = st.number_input('Jenis Kelamin Pasien')
   AGE	= st.number_input('Umur Pasien')
   SMOKING = st.number_input('Pasien yang merokok')
   YELLOW_FINGERS = st.number_input('Pasien yang tangannya kuning')
   ANXIETY = st.number_input('Pasien yang cemas')
   
   
with col2:
   PEER_PRESSURE	= st.number_input('Pasien yang mendapatkan tekanan')
   CHRONIC_DISEASE = st.number_input('Pasien yang mempunyai penyakit kronis')
   FATIGUE = st.number_input('Pasien yang kelelahan')
   ALLERGY = st.number_input('Pasien yang memiliki alergi')
   WHEEZING = st.number_input('Pasien yang nafasnya menciut ciut')

with col3:
   ALCOHOL_CONSUMING	= st.number_input('Pasien yang mengkonsumsi alkohol')
   COUGHING = st.number_input('Pasien yang mengalami batuk')
   SHORTNESS_OF_BREATH = st.number_input('Pasien yang memiliki nafas pendek')
   SWALLOWING_DIFFICULTY = st.number_input('Pasien yang kesulitan menelan')
   CHEST_PAIN = st.number_input('Pasien yang memiliki nyeri dada')

predik = ''
if st.button('Hasil Prediksi'):
    predik = model.predict([[GENDER,AGE,SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE ,ALLERGY ,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]])

    if(predik[0] == 1):
        predik = 'Kemungkinan Pasien yang terkena Penyakit Paru-Paru'
    else:
        predik = 'Kemungkinan Pasien yang tidak terkena Penyakit Paru-Paru'
st.success(predik)