from http.server import BaseHTTPRequestHandler, HTTPServer
import os
import time
import configparser

host_name = '192.168.0.193'
host_port = 8000

conf = configparser.ConfigParser()
conf.read('tradfri.cfg')
gateway_ip = conf.get('tradfri','gateway_ip')
identity = conf.get('tradfri', 'identity')
pre_shared_key = conf.get('tradfri', 'pre_shared_key')
bulb = conf.get('tradfri', 'bulb')

def flash():
    cmd_start = f'coap-client -m put -u "{identity}" -k "{pre_shared_key}"'
    cmd_end = f'"coaps://{gateway_ip}:5684/15001/{bulb}"'
    cmd0 = f'{cmd_start} -e \'{{ "3311": [{{ "5850": 0 }}] }}\' {cmd_end}'
    print('cmd0')
    print(cmd0)
    os.system(cmd0)
    time.sleep(0.5)
    cmd1 = f'{cmd_start} -e \'{{ "3311": [{{ "5850": 1 }}] }}\' {cmd_end}'
    os.system(cmd1)
    time.sleep(0.5)
    os.system(cmd0)
    time.sleep(0.5)
    os.system(cmd1)
    time.sleep(0.5)
    os.system(cmd0)
    time.sleep(0.5)
    os.system(cmd1)

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.end_headers()
    def do_GET(self):
        self.do_HEAD()
        self.wfile.write("alert triggered successfully".encode("utf-8"))
        flash()

    def do_POST(self):
        self.do_GET()

if __name__ == '__main__':
    http_server = HTTPServer((host_name, host_port), MyServer)
    print("Server Starts - %s:%s" % (host_name, host_port))

    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        http_server.server_close()
