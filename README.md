containerlab based Arista EVPN multisite LAB

to start LAB:
```
clab dep -t arista-evpn-multisite.yml
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
