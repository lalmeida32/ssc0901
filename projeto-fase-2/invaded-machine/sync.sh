#!/bin/bash

rsync -e "ssh -o StrictHostKeyChecking=no -i /root/.ssh/id_rsa" -avz /root/to_sync/ sftpuser@vulnerable-server:/data/