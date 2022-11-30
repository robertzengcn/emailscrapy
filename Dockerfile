FROM python:3.9

WORKDIR /app/emailscrapy
RUN pip3 install git+https://github.com/robertzengcn/emailscrapy.git@main

RUN apt-get update && apt-get install -y openssh-server vim
RUN mkdir /var/run/sshd

RUN echo "root:mypassword" | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
#RUN sed -i '/^#/!s/PermitRootLogin .*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
RUN service ssh restart
#download and install chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get update&&apt-get install -y ./google-chrome-stable_current_amd64.deb

#install chrome
WORKDIR /app/chromeDriver
RUN apt-get update
RUN apt-get install unzip

# RUN wget https://chromedriver.storage.googleapis.com/103.0.5060.53/chromedriver_linux64.zip
RUN CHROMEVER=$(google-chrome --product-version | grep -o "[^\.]*\.[^\.]*\.[^\.]*") && \
    DRIVERVER=$(curl -s "https://chromedriver.storage.googleapis.com/LATEST_RELEASE_$CHROMEVER") && \
    wget -q --continue "http://chromedriver.storage.googleapis.com/$DRIVERVER/chromedriver_linux64.zip" && \
    unzip chromedriver_linux64.zip
# RUN unzip chromedriver_linux64.zip
RUN apt-get remove -y unzip

RUN sed -i "/SELENIUM_DRIVER_EXECUTABLE_PATH =/c\SELENIUM_DRIVER_EXECUTABLE_PATH = '/app/chromeDriver/chromedriver'" /usr/local/lib/python3.9/site-packages/emailscrapy/emailscrapy/settings.py 

WORKDIR /app/workspace 
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
