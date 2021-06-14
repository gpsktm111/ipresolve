import re
import requests
from requests.exceptions import ConnectionError
f = open("tracking.txt","r")
lines = (line.strip() for line in f)
for line in lines:
    aa=re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b",line)
    r1=requests.get('https://tools.keycdn.com/geo.json?host={}'.format(aa[0]))
    res = r1.json()
    for k, v in res.items():
        if k == 'data':
            for a1, v1 in v.items():
                if a1 == "geo":
                    for a2, v2 in v1.items():
                        if a2 == "isp":
                            f1=open("ip.txt","w")
                            # print(aa[0],"=>",v2)
                            try:
                                r = requests.get("http://{}/".format(aa[0]))
                            except ConnectionError:
                                status = "No Connection"
                            else:
                                check = ['mikrotik','proxy','fortigate','router']
                                res = any(ele in r.text for ele in check)
                                if res:
                                    status = "Router"
                                else:
                                    status = "Not Router"
                            f1.write('{} => {},{}\n'.format(aa[0], v2,status))
f.close()
