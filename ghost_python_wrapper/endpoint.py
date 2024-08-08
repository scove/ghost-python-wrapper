import requests

from ghost_session import GhostSession


class Endpoint():
    def __init__(self, host: str, end_point: str, session: GhostSession):
        #host can likely just be grabbed from session since we are already passing that in
        self.end_point = end_point
        self.full_path = host + end_point
        self.session = session.session_cookie
        self.version = session.version
    
    def get(self):
        #TODO: if I pass in an id, grab that id only, else grab all posts
        r = requests.get(self.full_path, cookies=self.session)
        print(r.status_code)
        print(r.content)
        #TODO: return this stuff, no reason to print
    
    #TODO: add post fn
