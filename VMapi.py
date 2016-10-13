# Vuln Management Mod
# API Documentation => https://www.qualys.com/docs/version/8.8/qualys-api-v2-user-guide.pdf

import qualysapi
from lxml import objectify
from termcolor import colored
from tabulate import tabulate


req = qualysapi.connect('config')

# TODO:
#   Def each function in the API docs
#       List Data
#           List information in to objects?
#       Format Date
#


def listHosts():
    call = '/api/2.0/fo/asset/host'
    parameters = {'action':'list'}
    xml_output = req.request(call, parameters)
    #print xml_output
    # Tabulate Perams
    headers = [colored('IP', 'green'), colored('DNS', 'blue'),colored('OS','red')]
    table = []
    root = objectify.fromstring(xml_output)
    for host in root.RESPONSE.HOST_LIST.HOST:
        table.append([colored(host.IP.text, 'yellow'), colored(host.DNS.text, 'yellow'), colored(host.OS.text, 'yellow')])
    print tabulate(table, headers, tablefmt='fancy_grid')


def