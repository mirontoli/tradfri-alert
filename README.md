# Trådfri Alert
This simple web application serves as a webhook and flashes an IKEA Smart bulb. Use the webhook for any alert. This application is mainly designed for Raspberry Pi Zero W.

I'll provide the link to a blog post about it.

# Prerequisites
* IKEA Smart Bulb, remote and a gateway
* Raspberry Pi (or a computer)
* [Installed libcoap](https://learn.pimoroni.com/tutorial/sandyj/controlling-ikea-tradfri-lights-from-your-pi)
* ngrok
* python3


# Setup
```bash
cp tradfri-sample.cfg tradfri.cfg
``` 
Update the values in the `tradfri.cfg` for your home environment. 

Configure ngrok web interface to be accessible from other computers in your network:
```bash
echo "web_addr: 192.168.0.193:4040" >> ~/.ngrok2/ngrok.yml
```

Run the server and ngrok
```bash
python3 server.py &
~/ngrok http 192.168.0.193:8000 -region eu > /dev/null &
```
On your computer navigate to ngrok web interface (`192.168.0.193:4040` in my case), copy the public https address, try it with curl:
```bash
curl -d '' https://0ec6f40b50a6.eu.ngrok.io/
```
When done, register that webhook url in your alert setup.
