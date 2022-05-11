#!/usr/bin/python3

import sys
import pexpect as px

def main():
    print("I am a marker.")
    ch = px.spawn('ssh root@10.100.32.150')
    ch.logfile = sys.stdout.buffer  #must-have after spawn() or you see nothing print out
    ch.expect('~#')
    ch.sendline('version.sh')
    ch.sendline('roboctrl -p')
    ch.sendline('exit')
    ch.expect(px.EOF)  //need this cmd at end, otherwise the scrip would immediately exit and no ouput shown
    

if __name__ == '__main__':
    main()