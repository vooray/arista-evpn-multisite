containerlab based Arista EVPN multisite LAB

to start LAB:
```
clab dep --timeout 15m -t arista-evpn-multisite.yml
```
wait to start
```
cd nnr-arista-evpn-multisite/
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python deploy.py
```
to stop LAB:
```
clab des -t arista-evpn-multisite.yml
```
MGMT network: 10.10.0.0/24

To access hosts from windows add route: 
```
route ADD 10.10.0.0 MASK 255.255.255.0 10.0.0.20
```

Explore topology by running:
```
clab graph -s "0.0.0.0:80" -t  arista-evpn-multisite.yml
```
![IMAGE_DESCRIPTION](https://github.com/vooray/arista-evpn-multisite/blob/main/topology.jpg)
