#!/usr/bin/python3

import os
import sys
import argparse

from jinja2 import Environment

from yaml import load
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper


parser = argparse.ArgumentParser(description='Pretxt, render a template with provided values')
parser.add_argument('-c', '--config', help='config file (YAML)', type=str)
parser.add_argument("input", help="input file (Jinja2 template)", type=str)
args = parser.parse_args()

sys.stderr.write(str(args))
sys.stderr.write('\n')

def read_file(fname):
  res = None
  if os.path.isfile(fname):
    try:
      with open(fname, 'r') as f:
        res = f.read()
    except Exception as e:
      print('File read error {}: {}'.format(fname, e))
      sys.exit(2)
  else:
    print('File not found: {}'.format(fname))
    sys.exit(2)

  return  res

def main():
  input_f = read_file(args.input)
  config_f = read_file(args.config)

  # Read YAML
  config = load(config_f, Loader=Loader)

  sys.stderr.write(str(config))
  sys.stderr.write('\n')

  # Read template
  env = Environment()
  templ = env.from_string(source=input_f)
  # print(env)
  # print(templ)
  print(templ.render(config))

if __name__ == '__main__':
  main()
