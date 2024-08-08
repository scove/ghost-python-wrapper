import requests

from ghost_session import GhostSession


class Endpoint():
    def __init__(self, host: str, end_point: str, session: GhostSession):
        self.end_point = end_point
        self.full_path = host + end_point
        self.session = session.session_cookie
        self.version = session.version
    
    def get(self):
        r = requests.get(self.full_path, cookies=self.session)
        print(r.status_code)
        print(r.content)
