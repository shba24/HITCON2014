.global _start

.text

_start:
adr x0,pc
add x0,x0,24
sub x1,x1,x1
sub x2,x2,x2
mov x8,0xdd
svc 0

