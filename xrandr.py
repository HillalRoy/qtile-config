import subprocess
import re



def list_monitor() -> int:
    output = subprocess.check_output(['xrandr', '--listmonitors'])
    print(output.decode())
    x = re.search("Monitors:\s*(\d+)", output.decode())
    return int(x.groups()[0])



if __name__ == '__main__':
    list_monitor()
    # print('hel')