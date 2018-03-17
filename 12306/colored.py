import colorama
from colorama import init
init(autoreset=True)
from colorama import Fore, Back, Style

def cs(color,text,brightness=None):
	if brightness and brightness.upper()=='BRIGHT':
		if color.upper()=='BLACK':
			return Fore.BLACK+Style.BRIGHT +text
		elif color.upper()=='RED':
			return Fore.RED+Style.BRIGHT +text
		elif color.upper()=='GREEN':
			return Fore.GREEN+Style.BRIGHT +text
		elif color.upper()=='YELLOW':
			return Fore.YELLOW+Style.BRIGHT +text
		elif color.upper()=='BLUE':
			return Fore.BLUE+Style.BRIGHT +text
		elif color.upper()=='MAGENTA':
			return Fore.MAGENTA+Style.BRIGHT +text
		elif color.upper()=='CYAN':
			return Fore.CYAN+Style.BRIGHT +text
		elif color.upper()=='WHITE':
			return Fore.WHITE+Style.BRIGHT +text
	else:
		if color.upper()=='BLACK':
			return Fore.BLACK+text
		elif color.upper()=='RED':
			return Fore.RED+text
		elif color.upper()=='GREEN':
			return Fore.GREEN+text
		elif color.upper()=='YELLOW':
			return Fore.YELLOW+text
		elif color.upper()=='BLUE':
			return Fore.BLUE+text
		elif color.upper()=='MAGENTA':
			return Fore.MAGENTA+text
		elif color.upper()=='CYAN':
			return Fore.CYAN+text
		elif color.upper()=='WHITE':
			return Fore.WHITE+text

# print colored('red','haha','bright')

