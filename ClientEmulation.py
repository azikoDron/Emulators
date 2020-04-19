import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

data = '''<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tran="Capitalize">
            <soapenv:Header/>
                <soapenv:Body>
                    <tran:Insoap>
                        <tran:words>cAP FIRST LATTER</tran:words>
                    </tran:Insoap>
                </soapenv:Body>
            </soapenv:Envelope>'''

session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

ff = session.post('http://localhost:8002', data=data, json='lxml')
ff = ff.text
print(ff)