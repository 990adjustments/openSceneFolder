'''
OpenSceneFolder

Copyright: Erwin Santacruz 2013 (www.990adjustments.com)
Written for CINEMA 4D R14 on Mac OS X

Name-US: OpenSceneFolder

Description-US: Opens the current document's folder.

Creation Date: 09/07/13
'''


import c4d
from c4d import documents

import subprocess


def main():
    activeDoc = documents.GetActiveDocument()
    activeDocPath = activeDoc.GetDocumentPath()
    
    folderPath = activeDocPath.replace(" ", "\ ")
    subprocess.Popen('open "{0}"'.format(folderPath), shell=True)

if __name__=='__main__':
    main()