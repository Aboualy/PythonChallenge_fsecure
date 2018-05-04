import codecs
import os
import shutil
import subprocess
import urllib.request

p_url = "ftp://ftp.f-secure.com/support/tools/fsdiag/fsdiag_standalone.exe"

# Get the tool name out of the url
p_name = p_url.split('/')[-1]


def download_install_program():
    with urllib.request.urlopen(p_url) as req, open(p_name, 'wb') as result:
        shutil.copyfileobj(req, result)
    #Install and wait for the installation using subprocess.check_call
    with codecs.open(os.devnull, 'wb', encoding='utf8') as std:
        subprocess.check_call(p_name,
                         stdout=std,
                         shell=True,
                         stderr=subprocess.STDOUT
                         )


def execute_another_tool(fs_path, another_path):
    while True:

        if another_path == fs_path or not another_path:
            print("Error! Please provide another path!")
            break
        elif another_path != fs_path:
            execute_program(another_path)
            break
        else:
            break

#execute a tool/program using exsubprocess.Popen


def execute_program(program):
    # subprocess.check_call(program_name, shell=True)
    with codecs.open(os.devnull, 'wb', encoding='utf8') as std:
        subprocess.Popen(program,
                         stdout=std,
                         shell=True,
                         stderr=subprocess.STDOUT
                         )


def check_fsecure_file_existence():
    try:
        file = os.path.expanduser("~/Desktop/fsdiag.7z")
        # A test with a text file on my desktop and it works
        # file = os.path.expanduser("~/Desktop/txt.txt")
    except IOError:
        file = False
    if os.path.isfile(file):
        print("The file exists on your desktop")
    else:
        print("The file doesn't exist on your desktop")


def main():
    #download and install f-esure tool
    download_install_program()


    tool_path = input("Please enter the path of the installed F-Secure tool (copy/paste ):\n \n")
    #execute fsecure tool
    execute_program(tool_path)
    #"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    another_tool_path = input("Please enter a path of another tool/program to be executed (copy/paste ):\n\n")
    #execute any other tool
    execute_another_tool(tool_path, another_tool_path)

    #check that fsdiag.7z exists on the user´s desktop
    check_fsecure_file_existence()

if __name__ == "__main__":
    # execute only if run as a script
    main()