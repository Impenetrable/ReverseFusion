# ReverseFusion
A quick Python3 script to generate Coldfusion reverse powershell *.cfm pages.

When run it will ask for your IP, your port and a filename to name the cfm page.

It will then generate a .cfm page in the same folder that it is run, the payload will use a base64 encoded powershell reverse shell. Upload this to a ColdFusion instance that you have access to execute and voila!
