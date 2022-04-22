import argparse

parser = argparse.ArgumentParser()

parser.add_argument('file_name', help='image file name')
parser.add_argument('--on', type=str, help='on_color')
parser.add_argument('--off',type=str, help='off_color')

args = parser.parse_args() 

file_path = args.file_name

on_file = file_path.replace('.svg', '_on.svg')
off_file = file_path.replace('.svg', '_off.svg')

with open(file_path, 'r') as rf:
    svg_context = rf.read()

    on_svg = svg_context.replace('currentColor', args.on)
    with open(on_file, 'w') as wf:
        wf.write(on_svg)
    
    off_svg = svg_context.replace('currentColor', args.off)
    with open(off_file, 'w') as wf:
        wf.write(off_svg)


