FROM python:3.7.3-stretch

# Working Directory
WORKDIR /app

# Copy source code to working directory
COPY .  /app/

# Install packages from requirements.txt
RUN pip install -r requirements.txt

CMD python test.py
