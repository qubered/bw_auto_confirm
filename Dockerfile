FROM python:slim

ADD script.py .
ADD bw .

RUN pip install loguru
RUN chmod +x bw


CMD ["python","./script.py"]