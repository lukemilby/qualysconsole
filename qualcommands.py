# Commands for qualconsole
# Load CMD
import cmd
# Load Qualys Mods
import VMapi
from termcolor import colored

# TODO:
#   Move from CMD to CMD2
#   Boiler for commands
#

vmopt = ['Asset', 'Scan', 'Report', 'Compliance' , 'IPv6 Asset', 'Scan Authentication','Network']
wasopt = ['Web Application','Authentication','Scan','Schedule','Report', 'Report Creation', 'Option Profile', 'Finding', 'Progressive']
amopt = ['Tag', 'Host Asset', 'Asset', 'Host Instance Vulnerability', 'Asset Data Connector', 'AWS Asset Data Connector', 'AWS Authentication Record']

class qConsole(cmd.Cmd):
    """ Drop in to Q shell """

    level = ''

    prompt = colored("Qconsole:> ", 'green')


    # Creating a use command to set the mod you want to select
    def do_use(self, line):
        #if mod == "vm":
        pass

    # Workaround till I get do_use working
    def do_vm(self, line):
        qConsole.level = "VM"
        self.prompt = qConsole.prompt + colored('VM > ', 'yellow')

    # Runs listHosts form VMapi
    def do_hosts(self,line):
        if qConsole.level == "Asset":
            VMapi.listHosts()


    def do_scan(self,line):
        if qConsole.level == "VM":
            qConsole.level = "VM Scan"
            self.prompt = qConsole.prompt + colored('VM Scan > ', 'yellow')


    def do_asset(self,line):
        if qConsole.level == "VM":
            qConsole.level = "Asset"
            self.prompt = qConsole.prompt + colored('Assets > ', 'yellow')


    def do_help(self, line):
        pass

    def do_options(self,line):
        #if qConsole.level == '':
        pass

    def do_quit(self,line):
        pass


