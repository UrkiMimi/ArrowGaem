# temporary way on how to place camera events without the map editor
import json
import zipfile
import random as rand

fileName = 'ExpertPlusLawless'


# import
with open(fileName + '.bak', 'r') as f:
    jsn = json.loads(f.read())

jsn['cameraEvents'] = []


#region functions
def posTween(beat, duration, eType, eCurve, init, final):
    """Spawns a position event

    Args:
        beat (float): Time in beats
        duration (float): Animation duration
        eType (string): Easing type [out, in, inout]
        eCurve (string): Easing curve [refer to scratch easings]
        init (array): Initial position
        final (array): Final position
    """
    jsn['cameraEvents'].append(dict(
        b = beat,
        eType = eType,
        eCurve = eCurve,
        t = "pos",
        d = duration,
        init = init,
        final = final
    ))

def rotTween(beat, duration, eType, eCurve, init, final):
    """Spawns a rotation event

    Args:
        beat (float): Time in beats
        duration (float): Animation duration
        eType (string): Easing type [out, in, inout]
        eCurve (string): Easing curve [refer to scratch easings]
        init (array): Initial rotation
        final (array): Final rotation
    """
    jsn['cameraEvents'].append(dict(
        b = beat,
        eType = eType,
        eCurve = eCurve,
        t = "rot",
        d = duration,
        init = init,
        final = final
    ))

def sinTween(beat, duration, eType, eCurve, init, final):
    """Spawns a trig sin tween

    Args:
        beat (float): Time in beats
        duration (float): Animation duration
        eType (string): Easing type [out, in, inout]
        eCurve (string): Easing curve [refer to scratch easings]
        init (array): Initial sine multiplier
        final (array): Final sin multiplier
    """
    jsn['cameraEvents'].append(dict(
        b = beat,
        eType = eType,
        eCurve = eCurve,
        t = "sin",
        d = duration,
        init = init,
        final = final
    ))

def sortCamEvents(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j]['b'] > key['b']:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    
    return array

def addToZip(fileName, contents):
    with zipfile.ZipFile(fileName, 'w') as zip:
        for i in contents:
            zip.write(i)

#region map
#region beginning
posTween(0,14,'out','expo',[0,100,0],[0,0,0])
posTween(14,4,'out','quint',[0,0,5],[0,0,0])
posTween(46,4,'out','quint',[0,0,5],[0,0,0])

oldT = [0,0,0]
for i in range(4):
    newT = [0,0,((i%2)-0.5)*20]
    posTween(70+i,1,'in out','quad',oldT,newT)

    oldT = newT
posTween(74,1,'in out','quad',oldT,[0,0,0])

rotTween(74,1,'out','quad',[0,0,0],[180,0,0])
rotTween(77,1,'out','quad',[180,0,0],[360,0,0])

#region part 1
for i in range(112-82):
    posTween(82+i,1,'out','quint',[((i%2)-0.5)*4,0,0],[0,0,0])
rotTween(112,2,'in','expo',[0,0,0],[0,720,0])

for i in range(128-114):
    rotTween(114+i,1,'out','quint',[((i%2)-0.5)*30,0,0],[0,0,0])

posTween(128,1,'out','cubic',[0,0,0],[0,0,-50])
posTween(129,1,'in','cubic',[0,0,-50],[0,0,0])

for i in [130,134,138,140,142,143,144,145]:
    posTween(i,1,'out','quad',[0,0,5],[0,0,0])


posTween(0,1,'out','quad',[0,0,0],[0,0,0])


#region part 2
posTween(146,4,'out','elastic',[0,0,10],[0,0,0])

# loop setup
oldT = [0,0,0]
for i in range(4):
    newT = [i*2.5,i*2.5,i*2.5]
    rotTween(162+i/2,0.5,'out','quad',oldT,newT)
    oldT = newT

# reset
rotTween(164,1,'out','quint',newT,[0,0,0])

for i in range(2):
    posTween(176+i,0.5,'out','quad',[0,0,0],[0,10,0])
    posTween(176.5+i,0.5,'in','quad',[0,10,0],[0,0,0])

posTween(208,2,'in','expo',[0,0,0],[0,0,50])
posTween(210,1,'out','expo',[0,0,-200],[0,0,0])

#region part 3

oldT = [0,0,0]
# first pos part
for i in range(4):
    newT = [(i+1)*2,0,0]
    posTween(212+i/2,0.5,'out','quad',oldT,newT)
    oldT = newT

for i in range(4):
    newT = [8,(i+1)*2,0]
    posTween(214+i/2,0.5,'out','quad',oldT,newT)
    oldT = newT
posTween(216,2,'out','back',[8,8,0],[0,0,0])


# first rotate part
oldT = [0,0,0]
for i in range(4):
    newT = [0,(i+1)*11.25,0]
    rotTween(220+i/2,0.5,'out','cubic',oldT,newT)
    oldT = newT

for i in range(4):
    newT = [0,i*-22.5,0]
    rotTween(222+i/2,0.5,'out','cubic',oldT,newT)
    oldT = newT

rotTween(224,1.5,'out','quad',newT,[0,0,0])

# third rotate
rotTween(232,1,'out','elastic',[0,0,0],[45,0,0])
rotTween(233,1,'out','elastic',[45,0,0],[-45,0,0])
rotTween(234,2,'out','elastic',[-45,0,0],[0,0,0])

# the funny itg
oldT = [0,0,0]
for i in range(8):
    newT = [0,((i%2)-0.5)*i*2,0]
    posTween(234+i/2,0.5,'in out','quart',oldT,newT)
    oldT = newT

posTween(238,2,'out','quad',oldT,[0,-8,0])
posTween(240,1,'out','cubic',[0,-8,0],[0,0,-50])
posTween(241,1,'in','cubic',[0,0,-50],[0,0,0])


rotTween(240,1,'out','cubic',[0,0,0],[0,-45,0])
rotTween(241,1,'in','cubic',[0,-45,0],[0,0,0])

# sin 4
for i in range(8):
    sinTween(244+i/2,0.5,'out','expo',[0,125,125],[0,0,0])

rotTween(248,1,'out','back',[0,0,0],[0,0,45])
rotTween(249,1,'out','back',[0,0,45],[0,0,-45])
rotTween(250,1,'out','back',[0,0,-45],[0,0,0])

# the funny itg2
oldT = [0,0,0]
for i in range(4):
    newT = [((i%2)-0.5)*i*5,0,0]
    posTween(254+i/2,0.5,'out','quart',oldT,newT)
    oldT = newT

posTween(256,2,'out','elastic',[7.5,0,0],[0,0,0])

# random rotations 
oldT = [0,0,0]
for i in range(8):
    sinTween(258+i,0.5,'in out','quad',[0,0,100],[0,0,0])

for i in range(16):
    sinTween(266+i/2,0.5,'out','expo',[0,300,0],[0,0,0])


for i in [210,218,226,242]:
    rotTween(i,2,'out','cubic',[0,0,0],[0,360,0])
    sinTween(i,3,'out','expo',[0,250,250],[0,0,0])


#region save
jsn['cameraEvents'] = sortCamEvents(jsn['cameraEvents'])

with open(fileName + '.dat', 'w') as f:
    f.write(json.dumps(jsn,indent=2))

# save to zip
addToZip('c18.zip', ['ExpertPlusLawless.dat','Info.dat','yack.egg','c18.png'])