import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(target, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        if s.connect_ex((target, port)) == 0:
            s.close()
            return port
        s.close()
    except:
        pass
    return None


def scan_range(target, start, end):
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        results = executor.map(lambda p: scan_port(target, p), range(start, end + 1))

    for r in results:
        if r:
            open_ports.append(r)

    return open_ports
