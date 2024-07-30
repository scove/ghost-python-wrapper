import requests

class GhostWrapper:
    def __init__(self, host: str, version: str, username:str, password:str):
        self.host = host
        self.version = version
        self.username = username
        self.password = password

        self.session_token = self.basic_auth()
    
    def basic_auth(self):
        r = requests.post(self.host, data={"username" : self.username, "password" : self.password})
        if r.status_code != 201:
            raise Exception("Could not establish a session.")
        
        cookies = requests.utils.dict_from_cookiejar(r.cookies)
        
        return cookies['ghost-admin-api-session']