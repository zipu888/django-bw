FROM registry.cn-beijing.aliyuncs.com/vtronedu/base-python-bw:latest
WORKDIR /opt
ADD . /opt/
#RUN pip3 install -Ur requirements.txt
EXPOSE 80
CMD /opt/start.sh