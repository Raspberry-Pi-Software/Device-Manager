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
