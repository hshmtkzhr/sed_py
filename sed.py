#!/usr/bin/env python

import sys
import re
import codecs
from argparse import ArgumentParser

def get_opt():
  argparser = ArgumentParser()
  argparser.add_argument('before', help='origin string for replacement.')
  argparser.add_argument('after', help='a replacement string. you cat set multiline with return code.')
  argparser.add_argument('-f', '--file', default="", help='/path/to/file')
  argparser.add_argument('-ow', '--overwrite',action="store_true", help='overwrite file')
  return argparser.parse_args()

if __name__ == '__main__':
  args = get_opt()
  if args.before == "" or args.after == "":
    args.print_help()
    exit

  r = open(args.file, 'r')
  data = r.read()
  replaced = re.sub(args.before, args.after, data, flags=re.DOTALL)

  if args.overwrite:
    w = open(args.file, 'w')
    w.write(replaced)
    w.close()
    r.close()
  else:
    print replaced
