#
# artist2albumartist ID3 copier
#
# Scans given directory for mp3 and m4a files. Copies artist tag to album artist.
# Why: Some Digital DJ softwares use album artist tag for tracks instead of artist and it makes things complicated.
#
# See README.md
#
# 24/11/2016 Marko Sahlman (marko.sahlman@gmail.com)
#


from os.path import isfile, join
import mutagen
import sys, getopt, os
import fnmatch
import time

def printUsageAndExit():
    print 'Usage: [-r] -d <dir> -m <last modified in hours>'
    sys.exit(1)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def main(argv):
    dir_opt = False
    recursive_opt = False
    last_modified = None
    last_modified_in_ms = 0

    try:
        opts,args = getopt.getopt(argv, "rd:m:")
    except getopt.GetoptError:
        printUsageAndExit()

    for opt,arg in opts:
        if opt == '-d':
            directory = arg
            dir_opt = True
        if opt == '-r':
            recursive_opt = True
        if opt == '-m':
            last_modified=arg

    if not dir_opt:
        printUsageAndExit()

    if not directory:
        printUsageAndExit()

    if not os.path.isdir(directory):
        print "Error: Directory not found"
        printUsageAndExit()

    if last_modified != None:
        if not is_number(last_modified):
            print "Error: Last modified -m must be positive number"
            printUsageAndExit()

        last_modified_in_ms=3600*int(last_modified)

    now = time.time()

    files = []

    if recursive_opt:
        for root, dirnames, filenames in os.walk(directory):
            for filename in fnmatch.filter(filenames, '*'):
                files.append(os.path.join(root, filename))
    else:
        files = [f for f in os.listdir(directory) if isfile(join(directory,f)) ]

    for f in files:

        audiofile = join(directory,f)
        audiofile_last_modified=os.path.getmtime(audiofile)

        if last_modified != None:
            if now - last_modified_in_ms > audiofile_last_modified:
                continue

        if (audiofile.endswith(".mp3") or audiofile.endswith(".m4a")):
            try:
                audio = mutagen.File(audiofile, easy=True)
                artist=None
                albumartist=None
                if audio.get('artist'):
                    artist=audio['artist'][0]
                if audio.get('albumartist'):
                    albumartist=audio['albumartist'][0]

                if (artist != None and albumartist != artist):
                    print audiofile+": "+str(albumartist)+"=>"+str(artist)
                    audio['albumartist']=artist
                    audio.save()
                else:
                    print audiofile+": Artist does not exist"
            except Exception as e:
                print audiofile+": Failed to read/change file "
                print "Error: "+str(e)

if __name__ == "__main__":
   main(sys.argv[1:])
