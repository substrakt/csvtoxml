import sys, csv
from argparse import ArgumentParser
from slugify import slugify
from simplexml import XMLWriter

parser = ArgumentParser(description = 'Turn 3D CSV data into XML')
parser.add_argument(
    'commafields', type = str, nargs = '?',
    help = 'Turn these fields into multiple XML tags'
)

args = parser.parse_args()
commafields = args.commafields and args.commafields.split(',') or []

infile = csv.reader(sys.stdin)
outfile = XMLWriter(sys.stdout)
first = True
fields = {}

dom = outfile.start('document')

for row in infile:
    if first:
        fields = list([slugify(r) for r in row])
        first = False
        continue

    data = dict(
        [
            (
                fields[f],
                fields[f] in commafields and v.split(',') or v
            ) for (f, v) in enumerate(row)
        ]
    )

    outfile.start('user')
    for key, value in data.items():
        if isinstance(value, list):
            for subvalue in value:
                outfile.element(key, subvalue)
        else:
            outfile.element(key, value)

    outfile.end()

outfile.close(dom)
outfile.flush()
