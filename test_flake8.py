"""
Prototype to test flake8 api.
"""
#!/usr/bin/python3

import os
import sys
from flake8.api import legacy as flake8

def colorPrint(string, color):
    print("\033[%sm%s\033[0m" % (color, string))

def get_resource(name):
    """
    Get a file path from resource folder.
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resource', name)


def analyze(path):
    """
    Analyze given Python script using Flake8.
    """
    print("Analyze %s" % path)
    style_guide = flake8.get_style_guide(quiet=2)
    report = style_guide.check_files([path])
    for x in report.get_statistics('E'):
        colorPrint(x, "31")
    for x in report.get_statistics('W'):
        colorPrint(x, "35")
    for x in report.get_statistics('F'):
        colorPrint(x, "34")
    print("\n")


if __name__ == "__main__":
    analyze(get_resource('plugin.audio.detektorfm/addon.py'))
    analyze(get_resource('bad.py'))
