# temporary way on how to place camera events without the map editor
import json
import zipfile
import random as rand

fileName = 'ExpertPlusStandard'


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

def noteScaleTween(beat, duration, eType, eCurve, init, final):
    """Spawns a note scale tween

    Args:
        beat (float): Time in beats
        duration (float): Animation duration
        eType (string): Easing type [out, in, inout]
        eCurve (string): Easing curve [refer to scratch easings]
        init (array): Initial scale multiplier
        final (array): Final scale multiplier
    """
    jsn['cameraEvents'].append(dict(
        b = beat,
        eType = eType,
        eCurve = eCurve,
        t = "note",
        d = duration,
        init = init,
        final = final
    ))

def playScaleTween(beat, duration, eType, eCurve, init, final):
    """Spawns a playfield scale tween

    Args:
        beat (float): Time in beats
        duration (float): Animation duration
        eType (string): Easing type [out, in, inout]
        eCurve (string): Easing curve [refer to scratch easings]
        init (array): Initial scale multiplier
        final (array): Final scale multiplier
    """
    jsn['cameraEvents'].append(dict(
        b = beat,
        eType = eType,
        eCurve = eCurve,
        t = "playScale",
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
for i in range(14):
    rotTween(4+i,1,'out','expo',[((i%2)-0.5)*90,0,0], [0,0,0])

rotTween(18,2,'in','expo',[0,0,0],[0,360,0])


for i in range(12):
    rotTween(20+i,1,'out','expo',[0,((i%2)-0.5)*90,0], [0,0,0])

playScaleTween(32,1,'out','quint',[1,1,1],[-1,1,1])
playScaleTween(33,1,'out','quint',[-1,1,1],[1,1,1])

playScaleTween(52,8,'in','linear',[1,1,1],[0.1,0.1,0.1])
noteScaleTween(52,8,'in','linear',[1,1,1],[0.1,0.1,0.1])

playScaleTween(60,2,'out','back',[0.1,0.1,0.1],[1,0.1,1])
playScaleTween(64,2,'out','quad',[1,0.1,1],[1,1,1])
noteScaleTween(64,2,'out','quad',[0.1,0.1,0.1],[1,1,0])

for i in range(8):
    playScaleTween(70+i,1,'out','quint',[1,-((i%2)-0.5)*2,1],[1,((i%2)-0.5)*2,1])

for i in range(4):
    playScaleTween(78+i/2,0.5,'out','quint',[-((i%2)-0.5)*2,1,1],[((i%2)-0.5)*2,1,1])
    
for i in range(8):
    noteScaleTween(84+i,1,'out','expo',[-((i%2)-0.5)*2,1,1],[((i%2)-0.5)*2,1,1])

for i in range(4):
    noteScaleTween(92+i,1,'out','expo',[-((i%2)-0.5)*2,-((i%2)-0.5)*2,1,1],[((i%2)-0.5)*2,((i%2)-0.5)*2,1])

for i in range(12):
    posTween(100+i,0.5,'out','quad',[0,0,0],[0,5,0])
    posTween(100.5+i,0.5,'in','quad',[0,5,0],[0,0,0])

rotTween(100,6,'out','quad',[0,0,0],[0,0,30])
rotTween(106,6,'in out','quad',[0,0,30],[0,0,-30])
rotTween(112,2,'out','elastic',[0,0,-30],[0,0,0])


rotTween(132,8,'out','quart',[0,0,0],[1080,0,0])
posTween(132,8,'out','quart',[0,0,0],[0,0,-200])
noteScaleTween(132,8,'out','quad',[1,1,0],[0,0,0])

#region save
jsn['cameraEvents'] = sortCamEvents(jsn['cameraEvents'])

with open(fileName + '.dat', 'w') as f:
    f.write(json.dumps(jsn,indent=2))

# save to zip
addToZip('bass.zip', ['ExpertPlusStandard.dat','Info.dat','bass.ogg','s.png'])