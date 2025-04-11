# temporary way on how to place camera events without the map editor
import json

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

def sortCamEvents(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1

        while j >= 0 and array[j]['b'] > key['b']:
            array[j + 1] = array[j]
            j -= 1

        array[j + 1] = key
    
    return array

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

jsn['cameraEvents'] = sortCamEvents(jsn['cameraEvents'])


# save
with open(fileName + '.dat', 'w') as f:
    f.write(json.dumps(jsn,indent=2))