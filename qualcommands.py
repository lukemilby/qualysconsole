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

    def emptyline(self):
        pass

    def complete_emptyline(self, text, line, begidx, endidx):
        if qConsole.level == "VM":
            return [i for i in vmopt if i.startswith(text)]
        elif qConsole.level == "WAS":
            return [i for i in wasopt if i.startswith(text)]
        elif qConsole.level == "AM":
            return [i for i in amopt if i.startswith(text)]



    # Creating a use command to set the mod you want to select
    def do_use(self, line):
        #if mod == "vm":
        pass

    # Workaround till I get do_use working
    # Key to move in the Vulnerability Managment
    def do_vm(self, line):
        qConsole.level = "VM"
        self.prompt = qConsole.prompt + colored('VM > ', 'yellow')

    # Key to move in to Web Application Scanning
    def do_was(self,line):
        qConsole.level = "WAS"
        self.prompt = qConsole.prompt + colored('WAS > ', 'yellow')

    # Key to move in to Asset Management
    def do_am(self,line):
        qConsole.level = "AM"
        self.prompt = qConsole.prompt + colored('AM > ', 'yellow')

    # Runs listHosts form VMapi
    def do_hosts(self,line):
        if qConsole.level == "Asset":
            VMapi.listHosts()


    # VM:VM Scan
    # Move user in to Scan level of Vuln Management
    def do_scan(self,line):
        if qConsole.level == "VM":
            qConsole.level = "VM Scan"
            self.prompt = qConsole.prompt + colored('VM Scan > ', 'yellow')

    # VM:Asset
    # Moves user in to Asset level of Vuln Management
    def do_asset(self,line):
        if qConsole.level == "VM":
            qConsole.level = "Asset"
            self.prompt = qConsole.prompt + colored('Assets > ', 'yellow')


    def do_help(self, line):
        if line == '':
            print "VM"
            print "{}".format(vmopt)
            print "WAS"
            print "{}".format(wasopt)
            print "AM"
            print "{}".format(amopt)

    def do_options(self,line):
        if qConsole.level == '':
            print 'VM => ' + str(vmopt)
            print 'WAS => ' + str(wasopt)
            print 'AM => ' + str(amopt)
        elif qConsole.level == 'VM':
            print vmopt
        elif qConsole.level == 'WAS':
            print wasopt
        elif qConsole.level == 'AM':
            print amopt


    def do_quit(self,line):
        pass


