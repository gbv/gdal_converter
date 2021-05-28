FROM osgeo/gdal

WORKDIR /usr/opt/app
RUN apt update
RUN apt -y install python3-pip git
RUN pip3 install pipenv

RUN git clone https://github.com/chris-jan-trapp/gdal_converter.git /usr/opt/app
RUN pipenv install --system

CMD [ "python3", "./converter.py" ]

