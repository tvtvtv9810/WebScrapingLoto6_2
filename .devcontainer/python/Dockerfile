FROM python:3.9-slim

WORKDIR /tmp/work

COPY requirements.txt ${PWD}

RUN apt-get update && apt-get install -y unzip wget vim

# google-chrome
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb && \
    apt-get install -y -f ./google-chrome-stable_current_amd64.deb 

# ChromeDriver
# ADD https://chromedriver.storage.googleapis.com/110.0.5481.30/chromedriver_linux64.zip /opt/chrome/
# RUN cd /opt/chrome/ && \
#     unzip chromedriver_linux64.zip
##
## ---> pip install chromedriver

# python package
#RUN pip install selenium && \
#    pip install bs4 && \
#    pip install oauth2client
RUN pip install -r requirements.txt

# ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/chrome

RUN rm google-chrome-stable_current_amd64.deb
