FROM python:3.7-slim
WORKDIR griddle
COPY __main__.py gs_*.py requirements.txt ./
RUN pip install -r requirements.txt
RUN ls -lah
CMD python .