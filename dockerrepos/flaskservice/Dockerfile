FROM ubuntu

RUN apt-get update
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install git
RUN mkdir rakesh
RUN git clone https://github.com/rakeshkedar181/ga-1209.git
WORKDIR ga-1209
RUN pip3 install -r ga-1209/requirements.txt
copy dummy.txt rakesh/dummy.txt
WORKDIR ga-1209/bin

CMD ["python3" , "summaryService.py"]