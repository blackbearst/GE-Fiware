FROM python:3.5

MAINTAINER gusbgtk

# Install Firefox
RUN \
    curl 'https://download-installer.cdn.mozilla.net/pub/firefox/releases/35.0/linux-x86_64/en-US/firefox-35.0.tar.bz2' \
        -o firefox.tar.bz2 &&\
    bunzip2 firefox.tar.bz2 &&\
    tar xf firefox.tar &&\
    rm firefox.tar

RUN apt-get update && apt-get install -y \
    # Headless browser support
    xvfb \
    # Needed to launch firefox
    libasound2 \
    libgtk2.0-0 \
    libdbus-glib-1-2 \
    libxcomposite1

#install pip and numpy
RUN pip install selenium numpy 

WORKDIR /usr/src/app

#CMD ["python", "-u", "/index.py"]

COPY ge_fiware ./
