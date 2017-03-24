import ctypes
import struct
import socket
from ryu.lib.packet import ipv4
from ryu.lib.packet import icmp
from ryu.lib.packet import tcp
from ryu.lib.packet import udp
from ryu.lib.packet import ethernet
from ryu.lib import addrconv


def nf_log(nfa):
    # prefix
    print 'prefix', nfa.prefix
    # dump ethernet packet
    hw_type = socket.htons(nfa.msg_packet_hdr[0].hw_protocol)
    data = nfa.msg_packet_hwhdr
    dst, src = struct.unpack_from('!6s6s', data)
    eth = ethernet.ethernet(addrconv.mac.bin_to_text(dst),
                            addrconv.mac.bin_to_text(src),
                            ethertype=hw_type)
    print "eth: ", str(eth)
    # dump ipv4 packet
    pkt = nfa.payload
    buf = (ctypes.c_char * ctypes.sizeof(pkt)).from_buffer_copy(pkt)
    ipv4_pkt, proto, buf1 = ipv4.ipv4().parser(buf)
    print str(ipv4_pkt)
    if ipv4_pkt.proto == socket.IPPROTO_ICMP:
        icmp_pkt, a, b = icmp.icmp().parser(buf1)
        print "icmp_pkt", str(icmp_pkt)

    elif ipv4_pkt.proto == socket.IPPROTO_TCP:
        tcp_pkt, a, b = tcp.tcp().parser(buf1)
        print "tcp_pkt", str(tcp_pkt)
    elif ipv4_pkt.proto == socket.IPPROTO_UDP:
        udp_pkt, a, b = udp.udp().parser(buf1)
        print "udp_pkt", str(udp_pkt)

    elif ipv4_pkt.proto == socket.IPPROTO_AH:
        print 'proto = AH'

    elif ipv4_pkt.proto == socket.IPPROTO_ESP:
        print 'proto = ESP'

