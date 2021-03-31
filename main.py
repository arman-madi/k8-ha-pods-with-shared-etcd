import os
import time
import socket
from random import uniform

import etcd3


def main():
    node_name = os.environ.get("MY_NODE_NAME")
    node_ip = os.environ.get("MY_NODE_IP")
    pod_ip = os.environ.get("MY_POD_IP")
    print(f'STARTING DISTRIBUTED COUNTER on pod {pod_ip}')
    etcd = etcd3.client(host=node_ip, port=2379,
                        ca_cert="/etc/ssl/etcd-connect/ca.crt",
                        cert_cert="/etc/ssl/etcd-connect/server.crt",
                        cert_key="/etc/ssl/etcd-connect/server.key")
    opened_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        start = time.time()

        with etcd.lock('dcounter_lock') as lock:
            value, metadata = etcd.get('dcounter')
            if value is None:
                counter = 0
            else:
                counter = int(value.decode('utf-8'))
            counter += 1
            byte_message = bytes(f'\n#{counter} - {node_name} - {pod_ip}', " utf-8")
            opened_socket.sendto(byte_message, ("192.168.111.1", 9393))
            etcd.put('dcounter', str(counter))

        end = time.time()
        print(f'Pod {pod_ip} took {(end-start)*1000} milliseconds to send message')
        time.sleep(uniform(0, 0.3))


if __name__ == '__main__':
    main()
