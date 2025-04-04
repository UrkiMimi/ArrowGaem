### NE Megascript 
### Put new noodle scripts here and make sure its seperate from the main python file (yack.py in this case)

import random as rand
import math
from copy import deepcopy
import json

exFile = open('ExpertPlusLawless.dat', 'r')
exData = json.loads(exFile.read())
exFile.close()

#print('just letting you know you executed the noodle megascript dumbass.\n')

def export_json(filename):
    diPlusFile = open(filename, 'w')
    diPlusFile.write(json.dumps(exData,indent=2))
    diPlusFile.close()

# Assigns notes to a track
def assignNotesToTrack(startTime, endTime, trackName, colorCheck):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            if colorCheck:
                if (exData['colorNotes'][index]['c'] == 0):
                    exData['colorNotes'][index]['customData']['track'] = trackName + '1'
                else:
                    exData['colorNotes'][index]['customData']['track'] = trackName + '2'
            else:
                exData['colorNotes'][index]['customData']['track'] = trackName

# Assigns notes to a track
def assignObstaclesToTrack(startTime, endTime, trackName):
    for index in range(len(exData['obstacles'])):
        if (startTime <= exData['obstacles'][index]['b']) and (endTime >= exData['obstacles'][index]['b']):
            if not('customData' in exData['obstacles'][index]):
                exData['obstacles'][index]['customData'] = {}
            exData['obstacles'][index]['customData']['track'] = trackName

def assignEnvironmentToTrack(envName, trackName, lkMethod):
    exData['customData']['environment'].append(dict(id=envName, lookupMethod=lkMethod, track=trackName))

# Returns an array for all notes at a specified time
def findNoteAt(nTime):
    timeList = []
    for index in range(len(exData['colorNotes'])):
        if (nTime == exData['colorNotes'][index]['b']):
            timeList.append(index)
    return(timeList)

# Spawns a bulk of notes based on nTime
def kablooey(amount, nTime, spread):
    nBuffer = findNoteAt(nTime)
    for index2 in nBuffer:
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(amount):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][nBuffer[0]]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + 0.001
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = 3

            # Animation Fuckery
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['localRotation'] = [
                [0,0,0,0.5],
                [rand.randint(0,360),rand.randint(0,360),rand.randint(0,360),0.65,'easeOutExpo']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,0,0.5],
                [round(rand.uniform(-spread,spread),3),round(rand.uniform(-spread,spread),3),round(rand.uniform(0,spread),3),0.65,'easeOutExpo']
                ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo'],
                [0,0.75,'easeInQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [1,0.51,'easeOutExpo'],
                [0,0.75,'easeInQuad']
            ]

# Spawns fake notes at desired time (yes this uses a shitty track effect)
def noteBloom(nTime, duration, amount, distance = 1):
    trackName = str(rand.randint(0,90000000))
    for index in range(amount):
        fuck = rand.uniform(0.5,1.5)
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])

        # note vision block test
        pos = [rand.uniform(-10,10),rand.uniform(-10,10),rand.uniform(-15,5),0]
        while not((abs(pos[0]) > distance) and (abs(pos[1]) > distance) and (abs(pos[2]) > distance)):
            pos = [rand.uniform(-10,10),rand.uniform(-10,10),rand.uniform(-15,5),0]
        
        exData['customData']['fakeColorNotes'].append(dict(b=nTime,x=0,y=0,c=rand.randint(0,1),a=0,d=rand.randint(0,8),customData={}))
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['noteJumpStartBeatOffset'] = -10
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['disableNoteGravity'] = True
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['spawnEffect'] = False
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['track'] = trackName
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['color'] = [rand.uniform(0,1),rand.uniform(0,1),rand.uniform(0,1),1]  
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['animation']['offsetPosition'] = [
            pos
        ]
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['animation']['localRotation'] = [
            [rand.randint(-90,90),rand.randint(-90,90),rand.randint(-90,90),0]
        ]
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['animation']['scale'] = [
            [fuck,fuck,fuck,0]
        ]
    
    #trackpart
    dissolve(nTime-3, trackName, 0.25, 0,0)
    dissolveArrow(nTime-3, trackName, 0.25, 0,0)

    time(nTime-3,trackName,0,'easeOutQuad',0,0)
    dissolve(nTime, trackName, 0.25, 0,1)
    dissolveArrow(nTime, trackName, 0.25, 0,1)
    posTweenObjekt(nTime,trackName, 1,'easeOutExpo',[0,-5,0,0],[0,0,0,1])

    dissolve(nTime+duration, trackName, 0.5, 1,0)
    dissolveArrow(nTime+duration, trackName, 0.5, 1,0)
    time(nTime+duration+0.5,trackName,0,'easeOutQuad',1,1)
    posTweenObjekt(nTime+duration,trackName, 0.5,'easeInExpo',[0,0,0,0],[0,10,0,1])

# Makes the notes tween from random positions 
def randMovements(startTime, endTime, noteOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-4,4),rand.randint(-4,4),0,0.25],
                [0,0,0,0.45,'easeInOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(0,360),rand.randint(0,360),rand.randint(0,360),0.25],
                [0,0,0,0.45,'easeInOutExpo']
            ]

# Does a scale like trail at specified time
def scaleTrail(time, amount):
    nBuffer = findNoteAt(time)
    for index2 in nBuffer:
        t = 0
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(amount):
            # sanity check
            fakeIndex = index + fakeNoteLength

            # general customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.001
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = -1
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}

            # Note fuckery
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,index*10,0]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['scale'] = [
                [index*2,index*2,index*2,0]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [1,0.5],
                [0,0.65,'easeInExpo']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [1,0.5],
                [0,0.7,'easeInCirc']
            ]
            t+=0.02

# Does trail at specified time
def trail(time):
    nBuffer = findNoteAt(time)
    for index2 in nBuffer:
        t = 0
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        for index in range(32):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = 0
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}

            # Yippie
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [0,0,index*2,0.9],
                [0,0,100,0.95,'easeInCirc']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
                [0,0,index*10,0.75],
                [rand.randint(-10,10),rand.randint(-10,10),index*10,0.8,'easeInQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0,0.5],
                [0.5,0.51,'easeOutExpo'],
                [0,0.85,'easeInQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0,0.5],
                [0.75,0.51,'easeOutExpo'],
                [0,0.85,'easeInQuad']
            ]
            t+=0.01

# Does a knockoff 'Oh no.' effect
def ohYes(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 2
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,40,0],
                [0,0,19,0.25,'easeOutExpo'],
                [0,0,0,0.5,'easeInSine'],
                [0,0,-20,0.75,'easeOutSine']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [270,270,270,0],
                [0,0,0,0.25,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0],
                [1,0.15],
                [1,0.65],
                [0,0.75]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0],
                [1,0.15],
                [1,0.65],
                [0,0.75]
            ]

# Makes the notes act like a tangent graph
def tangent(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            # Invert xAxis tangent if note is blue
            if (exData['colorNotes'][index]['c'] == 1):
                xAxis = -25
            else:
                xAxis = 25

            # customData setup
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            
            # Animations
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,0,0.25],
                [xAxis,0,0,0.3,'easeInExpo'],
                [-xAxis,0,0,0.3],
                [0,0,0,0.35,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['scale'] = [
                [1,1,1,0.25],
                [abs(xAxis)/2,1,1,0.3,'easeInExpo'],
                [abs(xAxis)/2,1,1,0.3],
                [1,1,1,0.35,'easeOutExpo']
            ]

# Makes the notes tween from random positions 
def rotationFly(startTime, endTime, noteOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
                [0,0,0,0.45,'easeOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(-90,90),rand.randint(-90,90),rand.randint(-90,90),0.25],
                [0,0,0,0.45,'easeOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0.25],
                [0.95,0.45]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0.25,0],
                [0.75,0.25]
            ]

# Makes the notes go through a zig zag thing
def zigZagWobble(startTime, endTime, noteOffset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [10,0,0,0],
                [-8,0,0,0.05,'easeInOutQuad'],
                [6,0,0,0.1,'easeInOutQuad'],
                [-4,0,0,0.15,'easeInOutQuad'],
                [2,0,0,0.2,'easeInOutQuad'],
                [-1,0,0,0.25,'easeInOutQuad'],
                [0,0,0,0.3,'easeInOutQuad'],
            ]

# Make the notes go all over the place for the majority of their lifetime
def lordFoog(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 10
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-75,75),rand.randint(-75,75),rand.randint(-75,75),0,'easeOutQuad'],
                [rand.randint(-75,75),rand.randint(-75,75),rand.randint(-75,75),0.1,'easeOutQuad'],
                [rand.randint(-75,75),rand.randint(-75,75),rand.randint(-75,75),0.2,'easeInExpo'],
                [rand.randint(-75,75),rand.randint(-75,75),rand.randint(-75,75),0.3,'easeInExpo'],
                [rand.randint(-10,10),rand.randint(-10,10),rand.randint(-10,10),0.4,'easeInExpo'],
                [0,0,0,0.45,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['interactable'] = [
                [0,0.4],
                [1,0.45]
            ]
            exData['colorNotes'][index]['customData']['animation']['scale'] = [
                [10,10,10,0.3],
                [1,1,1,0.45,'easeOutExpo']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.1,'easeOutQuad'],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.2,'easeInExpo'],
                [rand.randint(-360,360),rand.randint(-360,360),rand.randint(-360,360),0.3,'easeInExpo'],
                [rand.randint(-90,90),rand.randint(-90,90),rand.randint(-90,90),0.4,'easeInExpo'],
                [0,0,0,0.45,'easeOutExpo']
            ]

# Similar to rotationFly but instead spawns in fake arrows around the player
def ghostArrows(startTime, endTime, amount, noteOffset, timeAdd=0.1):
    nBuffer = []

    # Add notes in the time zone to note buffer
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
            
    # real fun
    for index2 in nBuffer:
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        t = 0
        for index in range(amount):
            # to keep my sanity
            fakeIndex = index + fakeNoteLength

            # General customData setup
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = noteOffset

            # Animations
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),1,'easeInOutQuad']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-4,4),rand.randint(-50,50),5,0],
                [rand.randint(-4,4),rand.randint(-50,50),5,0,'easeOutSine']
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                [0.25,0],
                [0,0.25]
            ]
            exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                [0.25,0],
                [0.75,0.25]
            ]
            t+=timeAdd
    
# Makes the notes spin and float into the players view
def friedRoad(nTime):
    # Get notes
    nBuffer = findNoteAt(nTime)

    # Add fried road animation to selected notes
    for index in nBuffer:
        exData['colorNotes'][index]['customData'] = {}
        exData['colorNotes'][index]['customData']['animation'] = {}
        exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 1
        exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
            [rand.randint(-10,10),rand.randint(-10,10),0,0],
            [0,0,0,0.45,'easeOutBack']
        ]
        exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
            [0,0,360,0],
            [0,0,180,0.15],
            [0,0,0,0.45,'easeOutQuad']
        ]

# Makes the notes tween from random positions 
def xShift(startTime, endTime):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 1
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [rand.randint(-2,2),0,0,0],
                [0,0,0,0.4,'easeInOutExpo']
            ]

# Makes the notes on a track do a funny on each beat
def glitchTrack(startTime, endTime, trackName, duration):
    t = endTime - startTime
    exData['customData']['customEvents'].append(dict(b=startTime, t='AnimateTrack', d={'duration':duration, 'repeat':t/duration}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [0.25,0.5],
        [1,0.5],
        [1,1],
        [0.25,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [1,0.5],
        [0.25,0.5],
        [0.5,1],
        [1,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [0.1,0,0,0],
        [0,0,0,0.5,'easeOutElastic'],
        [-0.1,0,0,0.5],
        [0,0,0,1,'easeOutElastic']
    ]

# Makes the notes move back and forth on each 1/2 beat
def theFunnyBounce(startTime, endTime, trackName, x, y):
    t = endTime - startTime
    # Track Part
    exData['customData']['customEvents'].append(dict(b=startTime, t='AnimateTrack', d={'duration':1, 'repeat':t}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        [x,y,0,0],
        [-x,-y,0,0.5,'easeOutBack'],
        [x,y,0,1,'easeOutBack']
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [1,0],
        [0.5,0.5,'easeInExpo'],
        [1,0.5],
        [0.5,1,'easeInExpo']
    ]

    nBuffer = []
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            nBuffer.append(index)
            exData['colorNotes'][index]['customData'].pop('track')
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [1,0]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0]
            ]
    for index2 in nBuffer:
        fakeIndex = len(exData['customData']['fakeColorNotes'])

        exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
        exData['customData']['fakeColorNotes'][fakeIndex]['customData'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['track'] = trackName
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
            [0,0]
        ]

# Scales notes to desired size, easing is customizable
def scaleDown(startTime, endTime, scaleStart, scaleEnd, easing, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['animation']['scale'] = [
                [scaleStart,scaleStart,scaleStart,0.25],
                [scaleEnd,scaleEnd,scaleEnd,0.4,easing]
            ]
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,(scaleStart-1)/2,0,0.25],
                [0,0,0,0.4,easing]
            ]

# Makes notes spring up on desired time
def elasticRotate(time):
    nBuffer = findNoteAt(time)

    for index in nBuffer:
        exData['colorNotes'][index]['customData'] = {}
        exData['colorNotes'][index]['customData']['animation'] = {}
        exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
        exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.001
        exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 3
        exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
            [0,0,180,0],
            [0,0,0,0.25,'easeOutElastic']
        ]
        exData['colorNotes'][index]['customData']['animation']['interactable'] = [
            [0,0],
            [1,0.35]
        ]
        exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
            [0,0],
            [1,0.25],
        ]
        exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
            [0,0],
            [1,0.25],
        ]
        exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
            [0,0,12,0.25],
            [0,0,14,0.3,'easeOutSine'],
            [0,0,0,0.5,'easeInSine'],
            [0,0,-20,1]
        ]

# Bounce on track
def quagBounce(nTime, trackName, duration):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [4,0.25,1,0,'easeInOutSine'],
        [0.5,2,1,0.25,'easeInOutSine'],
        [1.5,0.67,1,0.5,'easeInOutSine'],
        [0.8,1.25,1,0.75,'easeInOutSine'],
        [1,1,1,1,'easeInOutSine']
    ]

def squish(nTime, trackName, duration, easing):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        [4,0.25,0,0],
        [1,1,1,1]
    ]

def turn(nTime, trackName, duration, easing, rot0, rot1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetWorldRotation'] = [
        [0,rot0,0,0],
        [0,rot1,0,1],
    ] 
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['rotation'] = [
        [0,rot0,0,0],
        [0,rot1,0,1],
    ]

def rotate(nTime, trackName, duration, easing, rot0, rot1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    rot1.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetWorldRotation'] = [
        rot0,
        rot1,
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['rotation'] = [
        rot0,
        rot1,
    ]

def rotatePointDef(nTime, trackName, duration, arrayPointDef,easing='easeLinear'):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetWorldRotation'] = arrayPointDef
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['rotation'] = arrayPointDef

def localRotatePointDef(nTime, trackName, duration, arrayPointDef,easing='easeLinear'):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localRotation'] = arrayPointDef

def posPointDef(nTime, trackName, duration, arrayPointDef,easing='easeLinear'):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = arrayPointDef


def lazyOffset(startTime, endTime, offset):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
    for index in range(len(exData['customData']['fakeColorNotes'])):
        if (startTime <= exData['customData']['fakeColorNotes'][index]['b']) and (endTime >= exData['customData']['fakeColorNotes'][index]['b']):
            if not('customData' in exData['customData']['fakeColorNotes'][index]):
                exData['customData']['fakeColorNotes'][index]['customData'] = {}
            exData['customData']['fakeColorNotes'][index]['customData']['noteJumpStartBeatOffset'] = offset
            exData['customData']['fakeColorNotes'][index]['customData']['disableNoteGravity'] = True

# Use only for environment tracks
def posTween(nTime, trackName, duration, easing, oldPosVector, posVector):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    posVector.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localPosition'] = [
        oldPosVector,
        posVector
    ]   

# Use only for environment tracks
def posTweenObjekt(nTime, trackName, duration, easing, oldPosVector, posVector):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    posVector.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = [
        oldPosVector,
        posVector
    ]     

def time(nTime, trackName, duration, easing, oldx,x):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['time'] = [
        [oldx,0],
        [x,1]
    ]

def dissolve(nTime, trackName, duration, oldx,x):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [oldx,0],
        [x,1]
    ]

def dissolveArrow(nTime, trackName, duration, oldx,x):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [oldx,0],
        [x,1]
    ]

def fridge(nTime, pix):
    xLen = (len(pix[0])/2)-1
    yLen = (len(pix)/2)-1
    print('==Original fridge function is deprecated. Use fridgeTrack==')
    for y in range(len(pix)):
        for x in range(len(pix[0])):
            pixlist = pix[y][x]
            if pixlist == 'x':
                exData['obstacles'].append(dict(b=nTime,x=0,y=0,d=0.05,w=1,h=5))
                index = len(exData['obstacles']) - 1
                exData['obstacles'][index]['customData'] = {}
                exData['obstacles'][index]['customData']['color'] = [10,10,10,0]
                exData['obstacles'][index]['customData']['coordinates'] = [(x-xLen)/2,(y/-2)+yLen]
                exData['obstacles'][index]['customData']['size'] = [0.5,0.5]

def fridgeTrack(pix, trackName, distanceFromPlayer = 12, color=[1,1,1,0]):
    xLen = (len(pix[0])/2)-1
    yLen = (len(pix)/2)-1

    #Add material with name unique to spawned fridge
    matName = str(rand.randint(0,9999999))
    exData['customData']['materials'][matName] = {'color':color,'shader':'Standard','shaderKeywords':[]}

    #Grid loop
    for y in range(len(pix)):
        for x in range(len(pix[0])):
            pixlist = pix[y][x]
            if pixlist == 'x':
                exData['customData']['environment'].append(dict(
                        geometry = {
                            'type':'Cube',
                            'material':matName
                    },
                    scale = [0.5, 0.5, 0.5],
                    position = [(x-xLen)/2,(y-yLen)/2,distanceFromPlayer],
                    track = trackName))

def headsUpTurn(nTime, track, parentTrack, rot0, rot1, parentParent='fack'):
    localRotate(nTime,parentTrack,1,'easeOutCubic',[90,0,0,0],[0,0,0,1])
    scalePointDef(nTime,track,0.5,[[0,0,0,0],[0.5,0.5,0.5,0.5,'easeOutQuad']])
    posTween(nTime,parentTrack,1,'easeOutCubic',[0,2,14,0],[0,2,12,1])
    turn(nTime,parentParent,1,'easeOutCubic', rot0, rot1)
    scalePointDef(nTime+4,track,1,[[0.5,0.5,0.5,0],[0,0,0,1,'easeInQuad']])
    localRotate(nTime+4,parentTrack,1,'easeInCubic',[0,0,0,0],[-90,0,0,1])
    turn(nTime+4,parentParent,1,'easeInCubic', rot1, rot1+(rot1-rot0))

def outBackTurn(nTime, track, rot0, rot1):
    bleh = rot1 - rot0
    if 0 <= bleh:
        bleh = 5
    else:
        bleh = -5
    turn(nTime, track, 1, 'easeOutQuad', rot0, rot1 + bleh)
    turn(nTime+1, track, 1, 'easeInSine', rot1 + bleh, rot1)

# dumb wall effect
def notOutThere(startTime, endTime, offset, speed):
    for index in range((endTime - startTime)*2):
        obLen = len(exData['obstacles'])
        exData['obstacles'].append(dict(b=index/2+startTime,x=0,y=0,d=1,w=1,h=5,customData={'animation':{}}))
        exData['obstacles'][obLen]['customData']['noteJumpMovementSpeed'] = speed
        exData['obstacles'][obLen]['customData']['noteJumpStartBeatOffset'] = offset
        exData['obstacles'][obLen]['customData']['coordinates'] = [-0.05,0.5]
        exData['obstacles'][obLen]['customData']['size'] = [0.1,rand.randint(1,8)]
        exData['obstacles'][obLen]['customData']['animation']['dissolve'] = [
            [0,0],
            [1,0.25],
            [1,0.45],
            [0,0.5]
        ]
        exData['obstacles'][obLen]['customData']['animation']['color'] = [
            [10,1,1,2,0],
            [0,0,0,0,0.5]
        ]
        exData['obstacles'][obLen]['customData']['animation']['offsetWorldRotation'] = [
            [rand.randint(-90,90),rand.randint(-90,90),0,0]
        ]
        exData['obstacles'][obLen]['customData']['animation']['offsetPosition'] = [
            [0,0,0,0],
            [(index%2-0.5)*20,0,0,0.5,'easeOutExpo']
        ]
        exData['obstacles'][obLen]['customData']['animation']['scale'] = [
            [1,1,1,0],
            [0.01,0.01,1,0.5]
        ]

def spawnFakeNotesWithTrackAt(startTime, endTime, disableGravity, timeOffset, track=''):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            fakeLen = len(exData['customData']['fakeColorNotes'])
            exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))
            exData['customData']['fakeColorNotes'][fakeLen]['b'] = exData['customData']['fakeColorNotes'][fakeLen]['b'] + timeOffset
            if not('customData' in exData['customData']['fakeColorNotes'][fakeLen]):
                exData['customData']['fakeColorNotes'][fakeLen]['customData'] = {}
            if not(track == ''):
                exData['customData']['fakeColorNotes'][fakeLen]['customData']['track'] = track
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['spawnEffect'] = False
            if disableGravity:
                exData['customData']['fakeColorNotes'][fakeLen]['customData']['disableNoteGravity'] = True

def removeGravity(startTime, endTime, fakeNotes):
    if fakeNotes:
        for index in range(len(exData['customData']['fakeColorNotes'])):
            if (startTime <= exData['customData']['fakeColorNotes'][index]['b']) and (endTime >= exData['customData']['fakeColorNotes'][index]['b']):
                exData['customData']['fakeColorNotes'][index]['customData']['disableNoteGravity'] = True
    else:
        for index in range(len(exData['colorNotes'])):
            if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
                if not('customData' in exData['colorNotes'][index]):
                    exData['colorNotes'][index]['customData'] = {}
                exData['colorNotes'][index]['customData']['disableNoteGravity'] = True

def shakeOutObjekt(nTime, trackName, duration, in0, steps):
    r = []
    for i in range(steps):
        oneMin = (i - steps-1) / steps
        r.append([round(rand.uniform(-in0,in0)*oneMin,3),
                  round(rand.uniform(-in0,in0)*oneMin,3),
                  0,
                  i/steps,'easeStep'])
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = r

def shakeInObjekt(nTime, trackName, duration, in0, steps):
    r = []
    for i in range(steps):
        r.append([rand.uniform(-in0,in0)*i/steps,
                  rand.uniform(-in0,in0)*i/steps,
                  0,
                  i/steps,'easeStep'])
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['offsetPosition'] = r


def scaleTween(nTime, trackName, duration, easing, st0, st1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    st1.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = [
        st0,
        st1
    ]

def colorTrack(nTime, trackName, duration, clr0, clr1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['color'] = [
        clr0,
        clr1
    ]

def staticTrail(nTime, step, duration, rotation=0, shakeSteps=10):
    noteTime = findNoteAt(nTime)

    # Note Setup
    tmpTrack = str(rand.randint(0,999999999))
    for index in range(step):
        for index2 in noteTime:
            fakeLen = len(exData['customData']['fakeColorNotes'])
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeLen]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['track'] = tmpTrack
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['interactable'] = False
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['noteJumpStartBeatOffset'] = -10
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['SpawnEffect'] = False
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['offsetPosition'] = [
                [0,0,5+index*4,0]
            ]
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['offsetWorldRotation'] = [
                [0,rotation,0,0]
            ]
    
    # Track stuff
    #init
    dissolve(nTime-4,tmpTrack,0,0,0)
    time(nTime-3,tmpTrack,0,'easeOutQuad',0.4,0.4)
    dissolveArrow(nTime-4,tmpTrack,0,0,0)

    #animations
    shakeOutObjekt(nTime,tmpTrack,duration,0.5,shakeSteps)
    dissolveArrow(nTime,tmpTrack,duration,1,0)
    time(nTime+duration,tmpTrack,0.1,'easeOutQuad',1,1)

def localRotate(nTime, trackName, duration, easing, rot0, rot1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    rot1.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['localRotation'] = [
        rot0,
        rot1,
    ]

def rotateyTrail2(nTime, step):
    noteTime = findNoteAt(nTime)

    # Note Setup
    for index in range(step):
        for index2 in noteTime:
            fakeLen = len(exData['customData']['fakeColorNotes'])
            exData['customData']['fakeColorNotes'].append(dict(exData['colorNotes'][index2]))
            exData['customData']['fakeColorNotes'][fakeLen]['customData'] = {}
            exData['customData']['fakeColorNotes'][fakeLen]['b'] += index/8
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['interactable'] = False
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['noteJumpMovementSpeed'] = 100
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['noteJumpStartBeatOffset'] = 0
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['SpawnEffect'] = False
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation'] = {}
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['offsetPosition'] = [
                [0,0,5+index*4,0]
            ]
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['offsetWorldRotation'] = [
                [0,0,index*index,0]
            ]
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['scale'] = [
                [index*2+1,index*2+1,index*2+1,0]
            ]
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['dissolve'] = [
                [0.75,0.45],
                [0,0.5]
            ]
            exData['customData']['fakeColorNotes'][fakeLen]['customData']['animation']['dissolveArrow'] = [
                [1,0.45],
                [0,0.5]
            ]

def spinnyArrows(startTime, endTime, timeOffset, noteOffset, timeAdd=0.1):
    realTime = round(endTime - startTime) * timeOffset
            
    # real fun
    fakeNoteLength = len(exData['customData']['fakeColorNotes'])
    t = 0
    for index in range(realTime):
    # to keep my sanity
        fakeIndex = index + fakeNoteLength

        # General customData setup
        exData['customData']['fakeColorNotes'].append(dict(b=t+startTime,x=0,y=0,c=rand.randint(0,1),a=0,d=rand.randint(0,8),customData={}))
        exData['customData']['fakeColorNotes'][fakeIndex]['b'] = exData['customData']['fakeColorNotes'][fakeIndex]['b'] + t
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteLook'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['spawnEffect'] = False
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = noteOffset
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 0.01

        # Animations

        # prep bullshit
        r = []
        randRot = rand.uniform(-100,100)
        for i in range(150):
            r.append([0,0,i*randRot,i/150])

        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        '''
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
            [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
            [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),1,'easeInOutQuad']
        ]'''
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['localRotation'] = r
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
            [rand.randint(-25,25),rand.randint(-25,25),30,0],
            [rand.randint(-25,25),rand.randint(-25,25),0,0.45,'easeOutSine'],
            [rand.randint(-25,25),rand.randint(-25,25),20,0.95,'easeInSine']
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
            [0.25,0],
            [0,0.25]
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
            [0.25,0],
            [0.75,0.25],
            [0.75,0.75],
            [0,0.8]
        ]
        t+=1/timeOffset/2

# Rewrite of a function that explodes notes at specified time
def newKablooey(nTime, duration, randomizationXY = 15):
    tmpNotes = findNoteAt(nTime)

    for index in tmpNotes:
        pos = [rand.uniform(-randomizationXY,randomizationXY),rand.uniform(-randomizationXY,randomizationXY),rand.uniform(5,20)]
        rot = [rand.randint(-2080,2080),rand.randint(-2080,2080),0]

        # complete programming hell
        p1 = []
        f1 = [0,0,0]
        r1 = []

        for i in range(100):
            f1[0] = (f1[0] - pos[0])*0.975 + pos[0]
            f1[1] = (f1[1] - pos[1])*0.975 + pos[1]
            f1[2] = (f1[2] - pos[2])*0.975 + pos[2]

            #rounding to reduce file size
            p1.append([round(f1[0],3),round(f1[1],3),round(f1[2],3),i/100])
            r1.append([round(rot[0]*(i/100),3),round(rot[1]*(i/100),3),round(rot[2]*(i/100),3),round(i/100,3)])

        # bleh
        trackName = str(index)
        fakeNoteLength = len(exData['customData']['fakeColorNotes'])
        # Note stuff
        exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData'] = {}
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['noteJumpStartBeatOffset'] = -100
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['noteJumpMovementSpeed'] = 0.001
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['disableNoteGravity'] = True
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['spawnEffect'] = False
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeNoteLength]['customData']['track'] = trackName

        # Track stuff
        dissolve(nTime-3,trackName,3,0,0)
        dissolveArrow(nTime-3,trackName,3,0,0)
        time(nTime-3,trackName,4,'easeLinear',0,0)

        dissolve(nTime,trackName,duration,1,0)
        dissolveArrow(nTime,trackName,duration,1,0)
        posPointDef(nTime,trackName,duration,p1)
        localRotatePointDef(nTime,trackName,duration,r1)

# spawns fake notes that are stupidly big with a high njs
def bigBois(startTime, endTime, amount, trackName):
    ti = (endTime - startTime) * amount
    for i in range(ti):
        # yippie
        
        fakeIndex = len(exData['customData']['fakeColorNotes'])
        exData['customData']['fakeColorNotes'].append(dict(b=startTime+i/amount,x=0,y=0,c=rand.randint(0,1),a=0,d=rand.randint(0,8),customData={}))
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = 50
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = 3
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['spawnEffect'] = False
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['track'] = trackName
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['scale'] = [
            [100,100,100,0]
        ]

# creates dust from dissolved notes
def space(startTime, endTime, amount, trackName, offset, njs=20):
    ti = (endTime - startTime) * amount
    for i in range(ti):
        # yippie
        
        fakeIndex = len(exData['customData']['fakeColorNotes'])
        exData['customData']['fakeColorNotes'].append(dict(b=startTime+i/amount,x=0,y=0,c=rand.randint(0,1),a=0,d=rand.randint(0,7),customData={}))
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation'] = {}
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['disableNoteGravity'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpMovementSpeed'] = njs
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['noteJumpStartBeatOffset'] = offset
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['spawnEffect'] = False
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['track'] = trackName
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
            [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),0],
            [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-45,45),1,'easeInOutQuad']
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetPosition'] = [
            [rand.randint(-4,4),rand.randint(-50,50),5,0],
            [rand.randint(-4,4),rand.randint(-50,50),5,0,'easeOutSine']
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
            [0.25,0],
            [0,0.25]
        ]
        exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
            [0.25,0],
            [0.75,0.25]
        ]

def assignPlayerToTrack(nTime, trackName):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignPlayerToTrack', d={'track':trackName}))

def childrenTracks(nTime, trackName, childrens):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignTrackParent', d={'childrenTracks':childrens, 'parentTrack':trackName}))
    
def clrTween(nTime, trackName, duration, easing, clr0, clr1):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    clr1.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['color'] = [
        clr0,
        clr1
    ]   

def scalePointDef(nTime, trackName, duration, arrayPointDef, easing='easeLinear'):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0, 'easing':easing}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['scale'] = arrayPointDef

def moveIt(startTime, endTime, easing,randomization=4, noteOffset=4, division=2):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            fakeI = len(exData['customData']['fakeColorNotes'])
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            if not('animation' in exData['colorNotes'][index]['customData']):
                exData['colorNotes'][index]['customData']['animation'] = {}

            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = noteOffset
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [round(rand.uniform(-randomization,randomization),3),
                 round(rand.uniform(-randomization,randomization),3),
                 0,
                 (1/noteOffset)/division/2],
                [0,0,0,(1/noteOffset)/division,easing]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0]
            ]
            

            exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))
            exData['customData']['fakeColorNotes'][fakeI]['b'] -= 0.005
            exData['customData']['fakeColorNotes'][fakeI]['customData']['uninteractable'] = True
            exData['customData']['fakeColorNotes'][fakeI]['customData']['disableNoteLook'] = True
            exData['customData']['fakeColorNotes'][fakeI]['customData']['disableNoteGravity'] = True
            exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['offsetPosition'] = [
                [round(rand.uniform(-randomization,randomization),3),
                 round(rand.uniform(-randomization,randomization),3),
                 0,
                 (1/noteOffset)/division/2],
                [0,0,0,(1/noteOffset)/division,easing]
            ]
            exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolveArrow'] = [
                [1,0.5],
                [0,0.5]
            ]
            exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolve'] = [
                [0,0]
            ]

def fakeryRing(startTime, endTime, randomization=4):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']):
            #reduce shitty code
            for i in range(2):
                fakeI = len(exData['customData']['fakeColorNotes'])
                exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))
                if not('customData' in exData['customData']['fakeColorNotes'][fakeI]):
                    exData['customData']['fakeColorNotes'][fakeI]['customData'] = {}
                if not('animation' in exData['customData']['fakeColorNotes'][fakeI]):
                    exData['customData']['fakeColorNotes'][fakeI]['customData']['animation'] = {}
                
                exData['customData']['fakeColorNotes'][fakeI]['customData']['disableNoteLook'] = True
                exData['customData']['fakeColorNotes'][fakeI]['customData']['disableNoteGravity'] = True

                exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['offsetPosition'] = [
                    [round(rand.uniform(-randomization,randomization),3),
                    round(rand.uniform(-randomization,randomization),3),
                    0,
                    0]
                ]

                exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['offsetWorldRotation'] = [
                    [0,round(rand.uniform(0,360),3),0,0]
                ]

                if (i == 0):
                    exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolve'] = [
                        [0,0]
                    ]
                    exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolveArrow'] = [
                        [0.25,0]
                    ]
                else:
                    exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolveArrow'] = [
                        [0,0]
                    ]
                    exData['customData']['fakeColorNotes'][fakeI]['customData']['animation']['dissolve'] = [
                        [0.25,0]
                    ]
 
def curveNock(startTime, endTime, rotationEasing='easeInExpo',posEasing='easeInQuint'):
    for index in range(len(exData['colorNotes'])):
        if (exData['colorNotes'][index]['b'] >= startTime) and (exData['colorNotes'][index]['b'] <= endTime):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            if not('animation' in exData['colorNotes'][index]['customData']):
                exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 1
            exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 5
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['spawnEffect'] = False
            #animation
            exData['colorNotes'][index]['customData']['animation']['offsetWorldRotation'] = [
                [rand.randint(-15,0),rand.randint(-20,20),rand.randint(-30,30),0],
                [0,0,0,0.5,rotationEasing]
            ]
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,15,0],
                [0,0,0,0.49,posEasing],
                [0,0,-15,1,'easeInSine']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0],
                [1,0.5]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0],
                [1,0.5]
            ]            

            #fakenote stuff
            for i in range(3):
                fakeIndex = len(exData['customData']['fakeColorNotes'])
                exData['customData']['fakeColorNotes'].append(dict(deepcopy(exData['colorNotes'][index])))
                exData['customData']['fakeColorNotes'][fakeIndex]['b'] -= 0.02
                exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['offsetWorldRotation'] = [
                    [rand.randint(-15,0),rand.randint(-20,20),rand.randint(-30,30),0],
                    [0,0,0,0.49,'easeInExpo']
                ]
                exData['customData']['fakeColorNotes'][fakeIndex]['customData']['uninteractable'] = True
                exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolveArrow'] = [
                    [1,0],
                    [0,0.5]
                ]
                exData['customData']['fakeColorNotes'][fakeIndex]['customData']['animation']['dissolve'] = [
                    [0,0]
                ]

def assignNoteLaneToTrack(startTime, endTime, trackName, lane):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']) and (exData['colorNotes'][index]['x'] == lane):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['track'] = trackName

def assignNoteColumnToTrack(startTime, endTime, trackName, column):
    for index in range(len(exData['colorNotes'])):
        if (startTime <= exData['colorNotes'][index]['b']) and (endTime >= exData['colorNotes'][index]['b']) and (exData['colorNotes'][index]['y'] == column):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            exData['colorNotes'][index]['customData']['track'] = trackName

def dissolveBoth(nTime, trackName, duration, oldx,x):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolve'] = [
        [oldx,0],
        [x,1]
    ]
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['dissolveArrow'] = [
        [oldx,0],
        [x,1]
    ]

def thinkFastChucklenuts(startTime, endTime, distance=5):
    for index in range(len(exData['colorNotes'])):
        if (exData['colorNotes'][index]['b'] >= startTime) and (exData['colorNotes'][index]['b'] <= endTime):
            if not('customData' in exData['colorNotes'][index]):
                exData['colorNotes'][index]['customData'] = {}
            if not('animation' in exData['colorNotes'][index]['customData']):
                exData['colorNotes'][index]['customData']['animation'] = {}
            exData['colorNotes'][index]['customData']['noteJumpStartBeatOffset'] = 3
            exData['colorNotes'][index]['customData']['noteJumpMovementSpeed'] = 0.01
            exData['colorNotes'][index]['customData']['disableNoteLook'] = True
            exData['colorNotes'][index]['customData']['disableNoteGravity'] = True
            exData['colorNotes'][index]['customData']['spawnEffect'] = False

            #animation
            exData['colorNotes'][index]['customData']['animation']['offsetPosition'] = [
                [0,0,20,0],
                [0,0,distance-3.5,0.15,'easeInSine'],
                [0,0,distance,0.35,'easeOutSine'],
                [0,0,0,0.499,'easeInQuad'],
                [0,0,-20,1,'easeOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['localRotation'] = [
                [rand.randint(-45,45),rand.randint(-45,45),rand.randint(-10,10),0],
                [0,0,0,0.15,'easeInSine'],
                [rand.randint(-25,25),rand.randint(-25,0),rand.randint(-10,10),0.25,'easeOutSine'],
                [0,0,0,0.4,'easeInOutQuad']
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolve'] = [
                [0,0],
                [1,0.25]
            ]
            exData['colorNotes'][index]['customData']['animation']['dissolveArrow'] = [
                [0,0],
                [1,0.25]
            ]
