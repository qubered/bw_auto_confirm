## BW auto approve v2

import subprocess
import json
from loguru import logger
import sys
import os
import time



bw_env_server = os.environ["BW_CONFIGSERVER"]
bw_env_orgid = os.environ["BW_ORGID"]

logger.add("logs/bw_confirm_{time}",format="{time} {level} {message}")
logger.info("LOGGER STARTED: Code v2")

server_set = subprocess.check_output("./bw config server "+bw_env_server,shell=True)
server_set = server_set.decode("utf-8")
logger.info(server_set)

try:
    logout = subprocess.check_output("./bw logout", shell=True)
    logout = logout.decode("utf-8")
    logger.info(logout)
except:
    logger.debug("LOGOUT FAILED")
try:
    login = subprocess.check_output("./bw login --apikey", shell=True)
    login = login.decode("utf-8")
    logger.info(login)
except:
    logger.debug("LOGIN FAILED")

while True:
    session_id = subprocess.check_output("./bw unlock --passwordenv BW_PASSWORD --raw", shell=True)
    session_id = session_id.decode("utf-8")
    logger.debug(session_id)

    member_list = subprocess.check_output("./bw list --session "+session_id+" org-members --organizationid "+bw_env_orgid, shell=True)
    member_list = member_list.decode("utf-8")

    members = json.loads(member_list)
    approval = False

    for member in members:
        if member['status'] == 1:
            try:
                res = subprocess.check_output("./bw confirm --session "+session_id+" org-member "+member['id']+" --organizationid "+bw_env_orgid, shell=True)
                logger.info("Confirmed User: "+member['name']+" "+member['email']+" To Bitwarden")
                approval = True
            except Exception as error:
                logger.DEBUG("ERROR APPROVING: "+member['name']+"Error: "+error)
    if not approval:
        logger.info("Script Finished! No users to approve")
    if approval:
        logger.info("Script Finished. Users approved")

    session_lock = subprocess.check_output("./bw lock", shell=True)
    session_lock = session_lock.decode("utf-8")
    logger.info(session_lock)
    logger.info("WAITING FOR 60 SECONDS")
    time.sleep(60)