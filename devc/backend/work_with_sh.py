#!/usr/bin/env python
import subprocess

def _get_output(command:str):
  output = subprocess.run(command.split(' '), capture_output=True, text=True)
  return output.stdout

def get_processor():
  processor_info = _get_output('lscpu')
  processor_name = processor_info.split('Model name:')[1].split('\n')[0]
  processor_vendor = processor_info.split('Vendor ID:')[1].split('\n')[0]
  return {
    "name": processor_name,
    "vendor": processor_vendor,
    "original": processor_info
  }
