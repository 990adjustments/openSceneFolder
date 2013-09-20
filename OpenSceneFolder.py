"""
OpenSceneFolder

Copyright: Erwin Santacruz 2013 (www.990adjustments.com)

Written for CINEMA 4D R14

Name-US: OpenSceneFolder

Description-US: Opens the current document's containing folder.

Creation Date: 09/07/13
"""


import c4d
from c4d import documents

import subprocess
import os


def open_scene_folder(activeDoc):
    activeDocPath = activeDoc.GetDocumentPath()
    if not activeDocPath:
        c4d.gui.MessageDialog("Unable to locate the scene file. Please make sure your scene is saved.")
        return False

    activeDocName = activeDoc.GetDocumentName()

    fullPath = os.path.join(activeDocPath, activeDocName)

    if c4d.GeGetCurrentOS() is c4d.OPERATINGSYSTEM_OSX:
        subprocess.Popen('open -R "{0}"'.format(fullPath.replace(" ", "\ ")), shell=True)
    else:
        subprocess.Popen('Explorer /select, {0}'.format(fullPath), shell=True)

if __name__=='__main__':
    activeDoc = documents.GetActiveDocument()
    open_scene_folder(activeDoc)
