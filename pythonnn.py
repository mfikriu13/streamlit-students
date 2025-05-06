import pickle
import streamlit as st

model = pickle.load(open('model.sav', 'rb'))

st.title('Prediksi ststus kelulusan siswa')

Admission_grade = st.number_input('Input nilai awal masuk')
Debtor = st.number_input('Input status hutang 1/0')
Tuition = st.number_input('Input sudah bayar uang pendidikan 1/0')
Sem1_approved = st.number_input('Input sks selesai semester_1')
Sem2_approved = st.number_input('Input sks selesai semester_2')

pred = ''

if st.button('Prediksi'):
    pred = model.predict(
        [[Admission_grade, Debtor, Tuition, Sem1_approved, Sem2_approved]]
    )
    st.write ('Prediksi kelulusan : ', pred)
