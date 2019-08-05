import network, socket


def connect(id,pswd):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(id, pswd)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())
    return wlan


def connect_socket(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = (ip,23)
    addr_port = (ip, 23)
    print('connecting to %s port %s' % addr_port)
    sock.connect(addr_port)
    return sock

# try:
    
#     # Send data
#     message = 'This is the message.  It will be repeated.'
#     print('sending "%s"' % message)
#     sock.sendall(message.encode())

#     # Look for the response
#     amount_received = 0
#     amount_expected = len(message)
    
#     while amount_received < amount_expected:
#         data = sock.recv(200)
#         amount_received += len(data)
#         print('received "%s"' % data)

# finally:
#     print('closing socket')
#     sock.close()