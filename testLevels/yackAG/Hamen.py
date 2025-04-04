### Main Hamen library for heck related maps.
### Use this library for heck modules
### TODO add info.dat support

import random as rand
import math
from copy import deepcopy
import json, os

# initial stuffs
infDat = {}

# Map to apply scripts to
fileName = 'ExpertPlusLawless.dat' 

# Export filename
exportName = 'ExpertPlusStandard.dat'

# open files
exFile = open(fileName, 'r')
exData = json.loads(exFile.read())
exFile.close()

infFile = open('Info.dat', 'r')
infDat = json.loads(infFile.read())
infFile.close()



#region functions
# for final exporting
def export_diff():
    """Exports map
    """
    # remove old backup
    if os.path.exists(exportName):
        os.remove(exportName + '.bak')
    
    # rename old diff file incase accidental overwrites
    os.rename(exportName, exportName + '.bak')

    diPlusFile = open(exportName, 'w')
    diPlusFile.write(json.dumps(exData,indent=2))
    diPlusFile.close()

#region info.dat part

def export_infoDat():
    """Exports info.dat and backs it up
    """
    # remove old backup
    if os.path.exists('Info.dat.bak'):
        os.remove('Info.dat.bak')

    # rename old info.dat
    os.rename('Info.dat', 'Info.dat.bak')

    # export info
    infFile = open('Info.dat', 'w')
    infFile.write(json.dumps(infDat,indent=2))
    infFile.close()

# inject requirements
def infoDat_addRequirement(requirement):
    """Adds a mod requirement to exported difficulty

    Args:
        requirement (string[]): Map requirements
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == exportName:
                indexes = [index, index2]

    # customData check
    if not('_customData' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'] = {}
    
    # set requirements to array argument
    # blank out requirements if empty
    if requirement == []:
        if ('_requirements' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
            infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'].pop('_requirements')
    else:
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData']['_requirements'] = requirement
    
# inject requirements
def infoDat_addSuggestion(suggestion):
    """Adds a mod suggestion to exported difficulty

    Args:
        suggestion (string[]): Map suggestions
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == exportName:
                indexes = [index, index2]

    # customData check
    if not('_customData' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'] = {}
    
    # set requirements to array argument
    # blank out suggestions if empty
    if suggestion == []:
        if ('_suggestions' in infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]):
            infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData'].pop('_suggestions')
    else:
        infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'][indexes[1]]['_customData']['_suggestion'] = suggestion

def infoDat_removeBaseMap():
    """Removes base map from Info.dat
    Use this if you've finished mapping your base difficulty!
    """
    indexes = []
    # find correct diff
    for index in range(len(infDat['_difficultyBeatmapSets'])):
        for index2 in range(len(infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'])):
            if infDat['_difficultyBeatmapSets'][index]['_difficultyBeatmaps'][index2]['_beatmapFilename'] == fileName:
                indexes = [index, index2]
    
    #pops base map
    infDat['_difficultyBeatmapSets'][indexes[0]]['_difficultyBeatmaps'].pop(indexes[1])