#!/usr/bin/env python3

# This script has been built has an helper for shellcoding challenges. It compiles the assembly code
# and checks for restricted chars. It prints the shellcode and its length.

import sys
import subprocess

def main():
    ## Get command lines args
    if len(sys.argv) != 3:
        print(f'Compile the given assembly file, print the shellcode and check for restricted chars\n\nUsage: {sys.argv[0]} restrictionsFile assemblyFile')
        return;

    restrictions = readRestrictions(sys.argv[1])
    print('Restrictions: {}\n'.format(restrictions))

    shellcode = getShellcode(sys.argv[2])
    print('Compiled shellcode:\n{}\n'.format(shellcode))
    splittedShellCode = splitChars(shellcode)
    print('Shellcode is {} bytes\n'.format(len(splittedShellCode)))

    badCharsFound = list(set(splittedShellCode)&set(restrictions))

    if len(badCharsFound) > 0:
        print('Found {} bad chars:\n{}\n'.format(len(badCharsFound), badCharsFound))
    else:
        print('No bad chars found in the shellcode')


def readRestrictions(restrictionsFile):
    file = open(restrictionsFile, 'r')
    content = file.read()
    return splitChars(content)

def getShellcode(assemblyFile):
    objectFile = assemblyFile.replace('.asm', '.o')

    compilationCommand = ['nasm', '-felf64', assemblyFile, '-o', objectFile]

    proc = subprocess.Popen(compilationCommand, stdout=subprocess.PIPE)
    result,errors = proc.communicate()
    exitCode = proc.wait()

    if 0 != exitCode:
        print("Failed to compile the assembly file")
        print(result)
        print(errors)
        return ''

    dumpShellcodeCommand = "for i in $(objdump -d {} -M intel |grep \"^ \" |cut -f2); do echo -n '\\\\x'$i; done;echo".format(objectFile)
    return subprocess.getoutput(dumpShellcodeCommand)

def splitChars(charsString):
    charsString = charsString.strip().split('\\x')

    return [char for char in charsString if char]

if __name__ == "__main__":
    main()

