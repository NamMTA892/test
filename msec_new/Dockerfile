FROM python:3.8-slim


WORKDIR /app
COPY . /app
RUN pip install --trusted-host pypi.python.org Flask
EXPOSE 5001
ENV FLASK_APP app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
