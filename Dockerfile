FROM python:3.10
WORKDIR /code
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY . .
# rembg model download karne ke liye permissions
RUN mkdir -p /.u2net && chmod 777 /.u2net
ENV U2NET_HOME=/.u2net
CMD ["python", "app.py"]