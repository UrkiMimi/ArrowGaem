# temporary way on how to place camera events without the map editor
import json

fileName = 'ExpertPlusStandard.dat'


# import
with open(fileName, 'r') as f:
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

