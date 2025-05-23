import nmap
import threading

def run_scan(target,args,port_start,port_end, speed,callback):
    def task():
        try:
          
            scan = nmap.PortScanner()
            if args=='-sn':
                result = scan.scan(target,arguments=f'{args} {speed}')
            else:
                result = scan.scan(target, f'{port_start}-{port_end}' ,arguments=f'{args} {speed}')
        except Exception as e:
            result = f'Error: {e}'
        
        callback(format_scan_result(result))
    
    threading.Thread(target=task).start()
    
    
def format_scan_result(result):
    output = []
    # This line checks if result is a string and if it is returns it.
    # this occurs when it an exeption pops up causing run_san to return the error as a string
    if isinstance(result,str):
        return result
    
    try:
        scaninfo = result['nmap'].get('scaninfo', {})
        errors = scaninfo.get('error', None)
        if errors:
            for err in errors:
                output.append(f'Error: {err.strip()}')
            return "\n".join(output)
    except Exception as e:
            return f'Error: {e}'
        
    try:
        hosts = result.get('scan', {})
    except Exception as e:
            return f'Error: {e}'
    
    for host, info in hosts.items():
        state = info.get('status', {}).get('state', 'unknown')
        output.append(f"\nHost: {host} ({state})")
        
        os_matches = info.get('osmatch', [])
        if os_matches:
            top_os = os_matches[0]
            os_name = top_os.get('name', 'Unknown OS')
            os_accuracy = top_os.get('accuracy', '?')
            output.append(f"  OS Guess: {os_name} ({os_accuracy}% accuracy)")

        # Print open ports
        for proto in ['tcp', 'udp']:
            if proto in info:
                ports = info[proto]
                for port, port_info in ports.items():
                    service = port_info.get('name', '')
                    port_state = port_info.get('state', '')
                    product = port_info.get('product', '')
                    version = port_info.get('version', '')
                    extra = f"{product} {version}".strip()
                    line = f"  {proto.upper()} Port {port}: {port_state} - {service}"
                    if extra:
                        line += f" ({extra})"
                    output.append(line)
    
    return "\n".join(output) if output else "No hosts found."