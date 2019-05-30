# sed.py - simple sed by python

## install
```
git clone https://github.com/hshmtkzhr/sed_py.git
cd sed_py
cp sed.py /path/to/tool # and set add envrinment variable PATH
```

## help
```
$ ./sed.py -h
usage: sed.py [-h] [-f FILE] [-ow] before after

positional arguments:
  before                origin string for replacement.
  after                 a replacement string. you cat set multiline with
                        return code.

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  /path/to/file
  -ow, --overwrite      overwrite file
```
