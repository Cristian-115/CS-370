
#implementation and assumptions

Assumption 1. The program is meant to run forever when a user types --get-otp, only a keyboard interrupt will stop the otp prints

Assumption 2. The secret needed to generate otp's will be static. It will not change on every run of the program

The implementation of this TOTP algorithm was based of the rfc link provided. Two functions are needed to generate a TOTP one that creates a HOTP and the other one gets the TOTP
When tokens are generated the program calculates the time left until a google authenticator refresh. It then sleeps for the appropriate amount of time in order to sync the authenticator
and the program. Any questions regarding implementation can be forwarded to garibcri@oregonstate.edu


In order to  compile the following program a virtual inviorment is needed to install the the following packages qrcode and others not installed on the server
this can be done using the following steps:

Create a virtual environment in your current directory for a project with the command: python3 -m venv my_project

Start the virtual environment by activating with the command: source my_project/bin/activate

once the venv is set up you can now PIP install the necessary libraries with

pip3 install qrcode[pil]

Finally to run the program type:

python3 TOTP.py --generate-qr    #this generates a qrcode that can be scanned with google authenticator

or 

python3 TOTP.py --get-otp        #This command will generate the current TOTP and print it to the console. 
				#this will run forever until the user hits CNTRL+ C to trigger a keyboard interrupt


type "deactivate" to stop the enviorment