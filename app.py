import streamlit as st
import numpy as np
import joblib
import warnings
warnings.filterwarnings("ignore")

# Завантажуємо навчений модель
model = joblib.load("best_model.pkl")

st.title("Прогнозувач екзаменаційної оцінки студента")

study_hours = st.slider("Кількість годин навчання на день", 0.0, 12.0, 2.0)
attendence = st.slider("Відвідуваність (%)", 0, 100, 80)
mental_health = st.slider("Оцінка психічного стану (1–10)", 1, 10, 5)
sleep_hours = st.slider("Кількість годин сну за ніч", 0.0, 12.0, 7.0)
part_time_job = st.selectbox("Чи має студент підробіток?", ["Ні", "Так"])

# Кодування 'part_time_job' у 0/1
ptj_encoded = 1 if part_time_job == "Так" else 0

if st.button("Прогнозувати підсумкову оцінку"):
    input_data = np.array([[study_hours, attendence, mental_health, sleep_hours, ptj_encoded]])
    prediction = model.predict(input_data)[0]

    # Обмеження прогнозу в діапазоні 0–100
    prediction = max(0, min(100, prediction))
    st.success(f"Прогнозована екзаменаційна оцінка: {prediction:.2f} балів")
