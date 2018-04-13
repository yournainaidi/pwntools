from pwn import *
context(arch='i386', os='linux')

r=process("./some_challenge")

r=remote("127.0.0.1",1337)

r.sendline("This sends a string with a newline appended to the end")
r.send("This also sends a string")

write_plt = p32(binary.symbols["write"])
read_GOT = p32(binary.symbols["got.read"])
read_plt = p32(binary.symbols["read"])
bss_addr = p32(binary.symbols["__bss_start"])
pop_ret = "\x9d\x85\x04\x08"

