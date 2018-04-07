import nmap
ns = nmap.PortScanner()
print(ns.nmap_version())
ns.scan('172.16.63.135', '22-445', '-sV')
#print (ns.scaninfo())
#print (ns.csv())

print (ns.scanstats())
print (ns['172.16.63.135'].state())
print (ns['172.16.63.135'].all_protocols())
print (ns['172.16.63.135']['tcp'].keys())
print (ns['172.16.63.135'].has_tcp(80))
