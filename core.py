import nmap
import threading

def run_scan(target, callback):
    def task():
        try:
            scan = nmap.PortScanner()
            result = scan.scan(target, '21-443')
        except Exception as e:
            result = e
        callback(result)

    threading.Thread(target=task).start()