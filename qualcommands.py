# Commands for qualconsole
# Load CMD
import cmd
# Load Qualys Mods
import VMapi
from termcolor import colored



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
        if qConsole.level == "VM":
            VMapi.listHosts()

# TODO:
#   Move from CMD to CMD2
#   Boiler for commands
#

