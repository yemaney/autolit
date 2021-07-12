FROM python:3.8
EXPOSE 8501
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD streamlit run main.py
# to build container run:   docker build -f Dockerfile -t autolit:latest .
# to run it:    docker run -p 8501:8501 autolit:latest
# container now available on:   http://localhost:8501/