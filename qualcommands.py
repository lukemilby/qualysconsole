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

vmopt = ['asset', 'scan', 'report', 'compliance' , 'IPv6 Asset', 'scan authentication','network']
wasopt = ['web application','authentication','scan','schedule','report', 'report creation', 'option profile', 'finding', 'progressive']
amopt = ['tag', 'host asset', 'asset', 'host instance vulnerability', 'asset data connector', 'AWS Asset Data Connector', 'AWS Authentication Record']
qopt = ['vm', 'was', 'am']


class qConsole(cmd.Cmd):
    """ Drop in to Q shell """

    level = ''
    mods = ''

    prompt = colored("Qconsole:> ", 'green')

    def emptyline(self):
        pass

    # Creating a use command to set the mod you want to select
    def do_use(self, line):
        if str(line).lower() in qopt:
            qConsole.level = str(line).upper()
            self.prompt = qConsole.prompt + colored('{} > ', 'yellow').format(str(line).upper())
        elif str(line).lower() in vmopt and qConsole.level == "VM":
            qConsole.level = str(line).upper()
            qConsole.mods = str(line).lower()
            self.prompt = qConsole.prompt + colored('{} > ', 'yellow').format(str(line).upper())
        elif str(line).lower() in wasopt and qConsole.level == "VM":
            qConsole.level = str(line).upper()
            qConsole.mods = str(line).lower()
            self.prompt = qConsole.prompt + colored('{} > ', 'yellow').format(str(line).upper())
        elif str(line).lower() in amopt and qConsole.level == "VM":
            qConsole.level = str(line).upper()
            qConsole.mods = str(line).lower()
            self.prompt = qConsole.prompt + colored('{} > ', 'yellow').format(str(line).upper())

    def complete_use(self, text, line, begidx, endidx):
        if qConsole.level == "VM":
            return [i for i in vmopt if i.startswith(text)]
        elif qConsole.level == "WAS":
            return [i for i in wasopt if i.startswith(text)]
        elif qConsole.level == "AM":
            return [i for i in amopt if i.startswith(text)]
        else:
            return [i for i in qopt if i.startswith(text)]


    # Runs listHosts form VMapi
    def do_hosts(self,line):
        if qConsole.level == "Asset":
            VMapi.listHosts()

    # VM:Asset
    # Moves user in to Asset level of Vuln Management
    def do_asset(self,line):
        if qConsole.level == "VM":
            qConsole.level = "Asset"
            self.prompt = qConsole.prompt + colored('Asset > ', 'yellow')


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


