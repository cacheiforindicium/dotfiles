#!/usr/bin/env python3
import argparse
import logging
import sys
import signal
import gi
import json
gi.require_version('Playerctl', '2.0')
from gi.repository import Playerctl, GLib

toggle = open("toggle", "r+")
print(toggle.read())
print("Above")
def output():
    if(str(toggle.read()) == "0"):
        toggle.truncate(1)
        toggle.write("1")
        output = {'text': ""}
        sys.stdout.write(json.dumps(output) + '\n')
        sys.stdout.flush()

    else:
        toggle.truncate(0)
        toggle.write("0")
        output = {'text': ""}
        sys.stdout.write(json.dumps(output) + '\n')
        sys.stdout.flush()
output()