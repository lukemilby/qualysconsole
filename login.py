#import logging
import qualysapi
from lxml import objectify
from termcolor import colored
from lxml.builder import E

# set logging level
#logging.basicConfig(level=logging.DEBUG)
# Auth
a = qualysapi.connect("config")
#logger = logging.getLogger('qualysapi.connector')
#logger.setLevel(logging.DEBUG)
#print a.request('about.php')
#print a.request('api/2.0/fo/asset/host/', {'action': 'list', 'ips':'64.41.200.231'})


def logout():
    print "Logging out"
    print a.request('api/2.0/fo/session/', {'action':'logout'})

#print a.request('api/2.0/fo/report', {'action': 'launch', 'output_format':'xml', 'template_id':'','report_id':'Scan'})


def resourceList():
    print  a.request('api/2.0/fo/report/', {'action':'list'})


def vmScan(peram):
    if peram == 'list':
        print a.request('api/2.0/fo/scan', {'action':'list'})

def hosts():
    call = '/api/2.0/fo/asset/host'
    parameters = {'action':'list'}
    xml_output = a.request(call, parameters)
    #print xml_output
    root = objectify.fromstring(xml_output)
    for host in root.RESPONSE.HOST_LIST.HOST:
        print colored("[+]IP - ", 'green', attrs=['bold']) + colored(host.IP.text, 'yellow') + colored(" DNS - ", 'blue',attrs=['bold']) + colored(host.DNS.text, 'yellow') + colored(" OS - ", 'cyan', attrs=['bold']) + colored(host.OS.text, 'yellow')


hosts()
#vmScan('list')