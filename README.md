# sed.py - simple sed by python

## install
```
git clone https://github.com/hshmtkzhr/sed_py.git
cd sed_py
cp sed.py /path/to/tool # and set add envrinment variable PATH
```

## help
```bash
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

## sample.txt
```bash
$ cat /tmp/sample.txt
nara
osaka
kyoto
kanagawa
tokyo
saitama
chiba
```

## replace and output to stdout
```bash
$ ./sed.py -f /tmp/sample.txt 'kyoto' 'kyoto\nkobe'
nara
osaka
kyoto
kobe
kanagawa
tokyo
saitama
chiba
```

## replace and overwrite file
```bash
$ ./sed.py -f /tmp/sample.txt 'kyoto' 'kyoto\nkobe' --overwrite

$ cat /tmp/sample.txt 
nara
osaka
kyoto
kobe
kanagawa
tokyo
saitama
chiba
```
