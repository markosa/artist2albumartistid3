#
# artist2albumartist ID3 copier
#
# Scans given directory for mp3 and m4a files. Copies artist tag to album artist.
# Why: Some Digital DJ softwares use album artist tag for tracks instead of artist and it makes things complicated.
#
# Requirements:
# - Python
# - mutagen library (pip install mutagen)
#
# Usage:
# python artist2albumartist [-r] [-m 24] -d /music/mp3/ 
#
# -r recursive
# -d directory
# -m last modified in hours. ie if you want to scan files added in few hours you can use -m 6 for 6 hours files modified before it will be skipped
#
#
#
# Version 1.2
# - Added last modified argument
#
# Version 1.1
# - Added recursive option
# Version 1.0¨
# - Initial version
#
#
# 24/11/2016 Marko Sahlman (marko.sahlman@gmail.com)
#
