from register8 import Register8
from procgen_name import ProcgenName

msg = "Hello World"
print(msg)

r = Register8(0xFF)
r.add(0x01)

print(r)
