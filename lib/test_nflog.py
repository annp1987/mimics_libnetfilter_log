import socket

from lib.log.nflog_wrapper import nflog_handle

import nflog_decode


def main():
    import select
    import time

    n = nflog_handle.open()
    r = n.unbind_pf(socket.AF_INET)
    r = n.bind_pf(socket.AF_INET)
    qh = n.bind_group(0)
    qh.set_mode(0x02, 0xffff)

    def cb(gh, nfmsg, nfa, data):
        nflog_decode.nf_log(nfa)
        return 0

    qh.callback_register(cb, None)

    fd = n.fd

    while True:
        r, w, x = select.select([fd], [], [], 1.0)
        if len(r) == 0:
            # timeout
            print("timeout")
            continue
        if fd in r:
            n.handle_io()


if __name__ == '__main__':
    main()
