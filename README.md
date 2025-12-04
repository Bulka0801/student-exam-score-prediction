# Прогнозування екзаменаційної оцінки студента

Невеликий проєкт з машинного навчання:
- `student_habits_performance.csv` – дані про навчальні звички студентів;
- `notebook.ipynb` – тренування моделей та вибір найкращої;
- `best_model.pkl` – збережена модель;
- `app.py` – веб-інтерфейс на Streamlit для прогнозу підсумкової екзаменаційної оцінки.

## Як запустити

```bash
pip install -r requirements.txt
python3 -m streamlit run app.py