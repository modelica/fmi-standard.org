import argparse
import csv
import sys
import os

parser = argparse.ArgumentParser(description="Validate the tools.csv file")

parser.add_argument('filename', nargs='?', help="Path to the tools.csv file from the fmi-standard.org repository")

args = parser.parse_args()

if args.filename:
    filename = args.filename
else:
    filename = os.path.dirname(__file__)
    filename = os.path.dirname(filename)
    filename = os.path.join(filename, '_data', 'tools.csv')

problems = []

column_names = ['name', 'id', 'homepage', 'description', 'license', 'platforms', 'export_cs_fmi1', 'export_cs_fmi2', 'export_me_fmi1', 'export_me_fmi2', 'import_cs_fmi1', 'import_cs_fmi2', 'import_me_fmi1', 'import_me_fmi2']
tool_names = []
tool_ids = []

with open(filename, 'r') as csvfile:

    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    header = next(reader)

    if header != column_names:
        problems.append("Column names must be: " + ', '.join(column_names))

    for line, row in enumerate(reader):

        if len(row) != len(column_names):
            problems.append('line %d: all rows must have %d fields. Make sure text with commas is enclosed in double quotes (").' % (line + 2, len(column_names)))
            break

        tool_name, tool_id, vendor_id = row[:3]

        if tool_name in tool_names:
            problems.append("tool_name '%s' is not unique" % tool_name)
        elif tool_names and tool_name.lower() < tool_names[-1].lower():
            problems.append("tool_name '%s' is not in alphabetical order" % tool_name)

        tool_names.append(tool_name)

        if tool_id in tool_ids:
            problems.append("tool_id '%s' is not unique" % tool_id)

        tool_ids.append(tool_id)

        if row[4] not in ['commercial', 'osi']:
            problems.append("%s: license must be commercial or osi" % tool_id)

        for field in row[7:]:
            if field not in ['', 'available', 'planned']:
                problems.append("%s: Capabilities must be planned, available or empty" % tool_id)

print("%d problems found in %s" % (len(problems), filename))

for problem in problems:
    print()
    print(problem)

sys.exit(len(problems))
