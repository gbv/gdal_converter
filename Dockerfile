FROM osgeo/gdal

WORKDIR /usr/opt/app
RUN apt update
RUN apt install python3-pip
RUN pip3 install pipenv

RUN git clone https://github.com/chris-jan-trapp/geodummy.git ./usr/opt/app
RUN pipenv install --system

CMD [ "python3", "./converter.py" ]

