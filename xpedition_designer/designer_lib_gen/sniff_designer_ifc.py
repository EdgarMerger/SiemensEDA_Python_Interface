import shlex
import subprocess
from typing import TextIO
import re

all_cls = []

import sys, os
WHERE_AM_I, WHO_AM_I=os.path.split(os.path.realpath(__file__))
path = WHERE_AM_I
print("path = " + path)
sys.path.append(path)

t_bool = ['Selected', 'Highlighted', 'Visible', 'IsConstant'] 
t_int = ['Count', 'Length', 'Distance'] 

def process_file(input_file: TextIO, output_file: TextIO) -> None:
    in_class: bool = False
    map_get: bool = False
    map_put: bool = False
    props = {}
    t: str = ''
    
    # Read the input file line by line
    for line in input_file:
        # Write the processed line to the output file
        output_file.write(line)

        if (in_class):
            # print('in:' + line)
            
            if (map_get or map_put):
                if ('#' in line):
                    # hint, extract type for the next line
                    hints = line.split('\'')
                    # print('hints({}) = '.format(len(hints)) + str(hints))
                    if (len(hints) > 1):
                        # t = hints[3]
                        t = ' # ' + hints[3]
                else:
                    members = line.split('"')
                    # print('members({}) = '.format(len(members)) + str(members))                   
                    if (len(members) > 1):
                        # gather additional info
                        delimiter: str = '; ' if len(t) > 0 else ' # ' 
                        ac: str = 'read_only'
                        if (map_put):
                            if (props[members[1]] != None):
                                ac = 'read/write'
                            else:
                                # highly unlikely, but still
                                ac = 'write_only'
                        t += delimiter + ac

                        if (members[1] in t_bool):
                            t = 'bool' + t
                        elif (members[1] in t_int):
                            t = 'int' + t
                        else:
                            t = 'str' + t
                        # memb = "{}: {}".format(members[1], t)
                        # print("member -> " + memb)
                        
                        props[members[1]] = t
                        t = ''
        
            if ('_prop_map_get_' in line):
                # print("map_get:" + line)
                map_get = True

            if ('_prop_map_put_' in line):
                # print("map_put:" + line)
                map_get = False
                map_put = True
                
            if (not map_get and map_put and '}' in line):
                map_put = False
                in_class = False
                # append types
                if (len(props) > 0):
                    nl = "\n"
                    output_file.write(nl)
                    for key in props:
                        output_file.write("\t{}: {}{}".format(key, props[key], nl))
                    output_file.write(nl)
                    props.clear()
                
        # collect all the classes to append at the end for import
        if (line.startswith('class') and 'DispatchBaseClass' in line):
            words = re.split(' |\(|\)|:', line)
            # print("words = " + str(words))
            all_cls.append('\'' + words[1] + '\'')
            
            in_class = True
            # print("in-class, line '" + line + "'")
        
    # join all the classes for import *
    output_file.write("__all__ = [" + ','.join(all_cls) + "]\n")

    # print("all_classes: " + ','.join(all_cls))

def generate_input() -> None:
    # first generate some input starting point
    cmd: str = 'python makepy.py -o designer_orig.py -v ViewDraw'
    result = subprocess.run(shlex.split(cmd), shell=True, capture_output=True, text=True)
    #result = subprocess.run('python makepy.py -o designer_orig.py -v ViewDraw', shell=True, capture_output=True, text=True)
    #result = subprocess.run(['python', 'makepy.py', '-o', 'designer_orig.py', '-v', 'ViewDraw'], capture_output=True, text=True)
    print(result)

def generate_output() -> None:
    with open('./designer_orig.py', 'r') as in_file:
        with open('./designer_ifc.py', 'w') as out_file:
            process_file(in_file, out_file)

def copy_result():
    cmd: str = 'move designer_ifc.py ../designer_ifc.py'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result)
    # cmd: str = 'move designer_orig.py ../designer_orig.py'
    # result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    # print(result)
    # result = subprocess.run(shlex.split(cmd), shell=True, capture_output=True, text=True)
    # result = subprocess.run(['python', 'makepy.py', '-o', 'designer_orig.py', '-v', 'ViewDraw'], capture_output=True, text=True)
    
def cleanup():
    cmd: str = 'del designer_orig.py'
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(result)
    
        
def run() -> None:
    generate_input()
    generate_output()
    copy_result()
    cleanup()

def main():
    run()
    print("Done!")

if __name__ == "__main__":
    main()