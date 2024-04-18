FROM python:alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

RUN python -m nltk.downloader stopwords

CMD ["python", "assignment2.py"]