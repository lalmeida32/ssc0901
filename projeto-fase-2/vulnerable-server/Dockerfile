FROM ubuntu

RUN apt update 
RUN apt install -y openssh-server rsync
RUN mkdir -p /var/run/sshd
RUN useradd -m -d /home/sftpuser -s /bin/bash sftpuser

RUN mkdir -p /home/sftpuser/.ssh
RUN chmod 700 /home/sftpuser/.ssh

COPY ssh_host_rsa_key /etc/ssh/ssh_host_rsa_key
COPY ssh_host_rsa_key.pub /etc/ssh/ssh_host_rsa_key.pub
COPY id_rsa.pub /home/sftpuser/.ssh/authorized_keys

RUN chmod 600 /etc/ssh/ssh_host_rsa_key
RUN chmod 600 /home/sftpuser/.ssh/authorized_keys
RUN chown -R sftpuser:sftpuser /home/sftpuser/.ssh

RUN mkdir /data
RUN chown sftpuser:sftpuser /data

RUN sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]