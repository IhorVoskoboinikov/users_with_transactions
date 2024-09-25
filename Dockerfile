# Используем образ с Python
FROM python:3.11-slim

# Устанавливаем переменную окружения для более чистого вывода логов в консоль
ENV PYTHONUNBUFFERED=1

# Устанавливаем директорию приложения в контейнере
WORKDIR /app

# Копируем файлы зависимостей и устанавливаем их
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем все файлы приложения в контейнер
COPY . .

# Открываем порт, который будет использоваться для взаимодействия с приложением
EXPOSE 7000

# Команда для запуска приложения
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7000"]
