from os import listdir
from os.path import isfile, join
from mutagen.easyid3 import EasyID3
import mutagen
import sys, getopt, os

def printUsageAndExit():
    print 'Usage: -d <dir>'
    sys.exit(1)

def main(argv):
    dir_opt = False
    try:
        opts,args = getopt.getopt(argv, "d:")
    except getopt.GetoptError:
        printUsageAndExit()

    for opt,arg in opts:
        if opt == '-d':
            directory = arg
            dir_opt = True

    if not dir_opt:
        printUsageAndExit()

    if not directory:
        printUsageAndExit()

    if not os.path.isdir(directory):
        print "Error: Directory not found"
        printUsageAndExit()

    files = [f for f in listdir(directory) if isfile(join(directory,f)) ]

    for f in files:
        audiofile = join(directory,f)
        if (audiofile.endswith(".mp3") or audiofile.endswith(".m4a")):
            try:
                audio = mutagen.File(audiofile, easy=True)
                artist=audio['artist'][0]
                albumartist=audio['albumartist'][0]
                if (albumartist != artist):
                    print audiofile+": "+albumartist+"=>"+artist
                    audio['albumartist']=artist
                    audio.save()
            except Exception as e:
                print audiofile+": Failed to read/change file "
                print "Error: "+str(e)

if __name__ == "__main__":
   main(sys.argv[1:])
