#!/usr/bin/env python
import subprocess

def _get_output(command:str):
  output = subprocess.run(command.split(' '), capture_output=True, text=True)
  return output.stdout

def get_processor():
  processor_info = _get_output('lscpu')
