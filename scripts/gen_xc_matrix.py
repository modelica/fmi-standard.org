import yaml
import os

combinations = []

for fmi_version in ['FMI_1.0', 'FMI_2.0']:
    for fmi_type in ['CoSimulation', 'ModelExchange']:
        for platform in ['c-code', 'darwin64', 'linux32', 'linux64', 'win32', 'win64']:
            combinations.append((fmi_version, fmi_type, platform))

data_dir = os.path.dirname(__file__)
data_dir = os.path.dirname(data_dir)
data_dir = os.path.join(data_dir, '_data')

repo_dir = os.path.dirname(__file__)
repo_dir = os.path.dirname(repo_dir)
repo_dir = os.path.dirname(repo_dir)
repo_dir = os.path.join(repo_dir, 'fmi-xc')

vendors = set()
tools = []

with open(os.path.join(data_dir, 'tools.yml'), 'r') as f:
    y = yaml.load(f)
    for tool in y:
        if tool['vendor'].startswith('Dass'):
            vendors.add('3DS')
        else:
            vendors.add(tool['vendor'])
        tools.append(tool['name'])


def split_path(path):

    segments = []

    while True:
        path, segment = os.path.split(path)
        if not segment:
            break
        segments.insert(0, segment)

    return segments


def collect_results():

    results = []

    for vendor in vendors:  # ['3DS', 'QTronic']:

        vendor_repo = os.path.join(repo_dir, vendor, 'CrossCheck_Results')

        for root, dirs, files in os.walk(vendor_repo):

            if 'passed' not in files:
                continue

            segments = split_path(root)

            results.append(segments[-8:])

    return results


def build_matrix(results, fmi_version, fmi_type, platform):

    importing_tools = set()
    exporting_tools = set()

    filtered = []

    # get the tools
    for fmi_version_, fmi_type_, platform_, importing_tool_name, importing_tool_version, exporting_tool_name, exporting_tool_version, model_name in results:

        if fmi_version_ != fmi_version or fmi_type_ != fmi_type or platform_ != platform:
            continue

        importing_tools.add(importing_tool_name)
        exporting_tools.add(exporting_tool_name)

        filtered.append((importing_tool_name, importing_tool_version, exporting_tool_name, exporting_tool_version, model_name))

    # build matrix
    importing_tools = sorted(importing_tools)
    exporting_tools = sorted(exporting_tools)

    matrix = []

    for importing_tool in importing_tools:
        row = []
        for exporting_tool in exporting_tools:
            count = 0
            for r in filtered:
                if r[0] == importing_tool and r[2] == exporting_tool:
                    count += 1
            row.append(count)
        matrix.append(row)

    return importing_tools, exporting_tools, matrix


results = collect_results()

matrices = {}

for combination in combinations:
    matrices[combination] = build_matrix(results, *combination)

for fmi_version, fmi_type, platform in combinations:

    importing_tools, exporting_tools, matrix = matrices[(fmi_version, fmi_type, platform)]

    csv_filename = 'fmi1' if fmi_version == 'FMI_1.0' else 'fmi2'
    csv_filename += '-'
    csv_filename += 'cs' if fmi_type == 'CoSimulation' else 'me'
    csv_filename += '-'
    csv_filename += platform + '.csv'

    with open(os.path.join(data_dir, csv_filename), 'w') as f:
        f.write(','.join([''] + exporting_tools) + '\n')
        for importing_tool, row in zip(importing_tools, matrix):
            f.write(','.join([importing_tool] + list(map(str, row))) + '\n')

print("Done.")
