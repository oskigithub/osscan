#!/usr/bin/python
import subprocess,re,sys

def return_ttl(address):
    proc = subprocess.Popen(["ping -c 1 %s" %address, ""], stdout=subprocess.PIPE, shell=True)
    (out,err) = proc.communicate()
    out = out.split()
    out = re.findall(r"\d{1,3}",out[12])

    return out[0]

def retun_ttl_os_name(ttl_number):
    if ttl_number >= 0 and ttl_number <= 64:
        return "Linux"
    elif ttl_number >= 65 and ttl_number <= 128:
        return "Windows"
    else:
        return "Unknown"
    
if len(sys.argv) != 2:
    print ("\n[*] Uso: python osscan.py <ip-address>\n")
    sys.exit(1)

if __name__ == '__main__':
    addr = sys.argv[1]
    ttl = return_ttl(addr)

    try:
        print ("\n%s -> %s" %(addr, retun_ttl_os_name(int(ttl))))
    except:
        pass