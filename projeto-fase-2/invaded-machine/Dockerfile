FROM ubuntu

RUN apt-get update
RUN apt-get install -y openssh-client cron rsync

COPY id_rsa /root/.ssh/id_rsa
COPY id_rsa.pub /root/.ssh/id_rsa.pub

RUN mkdir -p /root/to_sync

COPY sync.sh /root/sync.sh

RUN chmod 600 /root/.ssh/id_rsa
RUN chmod 700 /root/sync.sh

RUN (crontab -l ; echo "* * * * * /root/sync.sh >> /var/log/sync.log 2>&1") | crontab

CMD ["cron", "-f"]