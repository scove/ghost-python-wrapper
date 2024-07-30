class GhostWrapper:
    def __init__(self, host: str, version: str, username:str, password:str):
        self.host = host
        self.version = version
        self.username = username
        self.password = password

        self.basic_auth()
    
    def basic_auth(self):
        return