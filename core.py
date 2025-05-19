import nmap
import threading

def run_scan(target,args, callback):
    def task():
        try:
            scan = nmap.PortScanner()
            result = scan.scan(target, '21-443' ,arguments=args)
        except Exception as e:
            result = e
        callback(result)

    threading.Thread(target=task).start()