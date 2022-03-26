FROM python:3.7.9
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt
COPY . .
CMD [ "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "15400" ]