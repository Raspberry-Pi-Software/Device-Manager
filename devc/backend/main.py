from work_with_sh import get_processor
from config import *
from flask import Flask

print("[*][DEVCMGR*] Backend is running.")
print("[*][DEVCMGR*] Hosting server...")

class WSGI(Flask):
  def __init__(self):
    super().__init__('devcmgrhost')

    @self.route('/')
    def route():
      return "HAHA"

    self.run(host='0.0.0.0', port=random.randint(1111,99999))

WSGI()
