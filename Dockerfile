FROM python:3
ENV PYTHONUNBUFFERED=1
RUN mkdir /sparta_accounts_manager
WORKDIR /sparta_accounts_manager
COPY requirements.txt /sparta_accounts_manager/
RUN pip install -r requirements.txt
COPY . /sparta_accounts_manager/
