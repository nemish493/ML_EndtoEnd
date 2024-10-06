FROM python:3.12
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# Expose port 5000 (or any port you'd like)
EXPOSE 5000

# Use a static port for gunicorn
CMD gunicorn --workers=4 --bind 0.0.0.0:5000 app:app
