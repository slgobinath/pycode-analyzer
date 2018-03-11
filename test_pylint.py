"""
Prototype to test pylint api.
"""
#!/usr/bin/python3

import os
import sys
import json
from pylint import epylint as lint
from pylint import lint
from pylint.reporters.text import TextReporter
from pylint.reporters.json import JSONReporter


class JSONReport(object):
    def __init__(self):
        self.contents = []

    def write(self, txt):
        txt = txt.strip()
        if txt:
            self.contents.append(txt)

    def read(self):
        return self.contents

    def toJson(self):
        json_array = []
        for content in self.contents:
            json_array.extend(json.loads(content))
        return json_array

    def getReports(self, report_type=None):
        json_report = self.toJson()
        if report_type is None:
            return json_report
        else:
            filtered_reports = []
            for report in json_report:
                if report_type == report['type']:
                    filtered_reports.append(report)
            return filtered_reports

    @staticmethod
    def format_report(report):
        return '[%d:%d] %s %s' % (report['line'], report['column'], report['message-id'], report['message'])


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
    # Disable import error: E0401
    # We can allow import error and filter KODI modules in JSONReport
    args = ["-r", "n", "--disable=E0401", path]
    report = JSONReport()
    lint.Run(args, reporter=JSONReporter(report), exit=False)

    for r in report.getReports('error'):
        colorPrint(JSONReport.format_report(r), "31")

    # for r in report.getReports('convention'):
    #     colorPrint(JSONReport.format_report(r), "34")

    # for r in report.getReports('warning'):
    #     colorPrint(JSONReport.format_report(r), "35")

    print("\n")


if __name__ == "__main__":
    analyze(get_resource('plugin.py'))
