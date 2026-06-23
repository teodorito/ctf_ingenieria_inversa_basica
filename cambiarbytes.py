python3 -c"
f=bytearray(open('hola_fix','rb').read())
f[5]=1
open('hola_fix', 'wb').write(f)