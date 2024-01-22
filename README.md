# bw_auto_confirm
A simple python script and docker container to auto confirm users into bitwarden organisation 

Uses the Bitwarden CLI to interface with vault, and a python wrapper to control

https://hub.docker.com/r/qubered/bw_auto_confirm

To get started make a env file with the following values
* BW_CLIENTID: Your Bitwarden user API ID
* BW_CLIENTSECRET: Your Bitwarden user API secret
* BW_CONFIGSERVER: Your Bitwarden host URL (https://bitwarden.com if unsure)
* BW_ORGID: Your Bitwarden Org ID
* BW_PASSWORD: Your Bitwarden Master Password
And create a folder to access the logs

Then run:
```docker run --env-file ./env-file -v (YOUR-LOGS-FOLDER):/logs qubered/bw_auto_confirm```