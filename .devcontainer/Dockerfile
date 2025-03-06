FROM ubuntu:22.04
SHELL ["/bin/bash", "-c"]
WORKDIR /workspaces

### TIMEZONE SETUP ###
RUN echo 'Etc/UTC' > /etc/timezone && \
    ln -s /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    apt-get update && \
    apt-get install -q -y --no-install-recommends tzdata && \
    rm -rf /var/lib/apt/lists/*

# packages
RUN apt-get update
RUN apt-get upgrade -y 
RUN apt-get install -y \
    sudo \
    curl \
    wget \
    git \
    htop \
    vim \
    python3 \
    python3-pip \
    python3-dev

RUN pip3 install --upgrade pip
RUN pip3 install \
    numpy==2.0.2 \
    pydantic==2.8.2 \
    requests==2.32.3 \
    bs4==0.0.2 \
    colorlog==6.9.0 \
    pandas==2.2.3

### KRONOS USER AND ROOT PASSWD###
RUN useradd -ms /bin/bash kronos && \
    usermod -aG sudo kronos && \
    echo "root:root" | chpasswd && \
    echo "kronos:kronos" | chpasswd