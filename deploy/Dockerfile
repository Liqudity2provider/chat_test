FROM python:3.9

WORKDIR .

COPY requirements/ requirements/
RUN pip install -r requirements/prod.txt

COPY . .

RUN pip install .

RUN chmod +x deploy/entrypoint.sh

ENTRYPOINT ["deploy/entrypoint.sh"]
