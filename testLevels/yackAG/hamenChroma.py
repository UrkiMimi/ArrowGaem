## Chroma based library for heck related maps.
## Some animation events are staying in heckNoodle cause some of this shit relies on noodle as well
## Specifically, most of the transformation tweens
## Refer to https://heck.aeroluna.dev/ when using this 
from Hamen import *

def addPrimitiveModel(type, material, position, localRotation, scale):
    """Creates a primitive model using Heck Geometry

    Args:
        type (string): Model Type
        material (string): Model material
        position (array): Position
        localRotation (array): Rotation
        scale (array): Object Scale
    """
    exData['customData']['environment'].append(dict(
        scale=scale,
        position=position,
        localRotation=localRotation,
        geometry={'type':type,'material':material}
        ))


def addPrimitiveModelTrack(type, material, position, localRotation, scale, track):
    """Creates a primitive and assigns it to a track

    Args:
        type (string): Model type
        material (string): Model material
        position (array): Position
        localRotation (array): Rotation
        scale (array): Object Scale
        track (string): Track
    """
    exData['customData']['customData']['environment'].append(dict(
        scale=scale,
        position=position,
        localRotation=localRotation,
        track=track,
        geometry={'type':type,'material':material}
        ))

# adds geometry
def addMaterial(shader, color, unlit, matName):
    """Makes a new material for geometry 
    (Unlit materials will not work on 1.39+)

    Args:
        shader (string): Shader
        color (array): Color
        unlit (bool): Use unlit shader (May not work on 1.39+)
        matName (string): Material name
    """
    if not(unlit):
        exData['customData']['materials'][matName] = dict(shader=shader,color=color)
    else:
        exData['customData']['materials'][matName] = dict(shader=shader,color=color,shaderKeywords=[])


def customRingRotation(time, rotation, step=15, prop=None, speed=1, namefilter=None, direction=None):
    """Custom ring rotation for V2 environments

    Args:
        time (float): Time
        rotation (float): Rotation value
        step (float, optional): Ring step. Defaults to 15.
        prop (float, optional): dont know what the fuck this does. Defaults to None.
        speed (float, optional): Ring speed. Defaults to 1.
        namefilter (string, optional): dont know what the fuck this does. Defaults to None.
        direction (int, optional): Makes the ring go clockwise or counter-clockwise Defaults to None.
    """
    dat = {}
    # add essential stuff for ring rotation
    dat['rotation'] = rotation
    dat['step'] = step
    dat['speed'] = speed

    # optional shit
    if (prop != None):
        dat['prop'] = prop
    if (namefilter != None):
        dat['nameFilter'] = prop
    if (direction != None):
        dat['direction'] = prop

    exData['basicBeatmapEvents'].append(dict(
        b=time,
        et=8,
        i=5,
        f=1,
        customData = dat
    ))


def customRingStep(time, step=15, speed=1):
    """Custom ring step for V2 Environments

    Args:
        time (float): Time
        step (float, optional): Ring step. Defaults to 15.
        speed (float, optional): Ring speed. Defaults to 1.
    """
    dat = {}
    # add essential stuff for ring zoom
    dat['step'] = step
    dat['speed'] = speed

    exData['basicBeatmapEvents'].append(dict(
        b=time,
        et=9,
        i=5,
        f=1,
        customData = dat
    ))

def assignEnvironmentToTrack(envName, trackName, lkMethod):
    """Assigns a part of the environment to a track

    Args:
        envName (float): Environment ID
        trackName (string): Track
        lkMethod (string): LookUp Method [Regex, Exact, Contains, StartsWith, EndsWith]
    """
    exData['customData']['environment'].append(dict(id=envName, lookupMethod=lkMethod, track=trackName))

def disableObject(envId, lookupMe):
    """Disables object in environment

    Args:
        envId (string): Environment ID
        lookupMe (string): Lookup method
    """
    exData['customData']['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False))

def dupe(envId, lookupMe, dupe):
    """Duplicates object in environment

    Args:
        envId (string): Environment ID
        lookupMe (string): Lookup method
        dupe (int): Amount of objects to duplicate
    """
    exData['customData']['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False,duplicate=dupe))

def fogging(envId, lookupMe, atten, offset, startY, height):
    """Adjusts environment fog

    Args:
        envId (string): Environment ID
        lookupMe (string): Lookup method
        atten (float): Attenuation
        offset (float): Fog offset
        startY (float): Fog start Y
        height (float): Fog height offset
    """
    exData['customData']['environment'].append(dict(
        id=envId,
        lookupMethod=lookupMe,
        components={'BloomFogEnvironment':{'attenuation':atten,'offset':offset,'startY':startY,'height':height}}
    ))

# Customization for objects
def editer(envId, lookupMe, pos, sc, rotation, enabled):
    """Environment params

    Args:
        envId (string): Environment ID
        lookupMe (string): Lookup method
        pos (array): Position
        sc (array): Scale
        rotation (array): Rotation
        enabled (bool): Enabled
    """
    exData['customData']['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled
        ))
    
# Customization for tubelights you want to do hacky shit with
def tubeEditer(envId, lookupMe, pos, sc, rotation, enabled, id, multi, fogMulti):
    """Editer but for tube lights

    Args:
        envId (string): Environment ID
        lookupMe (string): Lookup method
        pos (array): Position
        sc (array): Scale
        rotation (array): Rotation
        enabled (bool): Object enabled
        id (int): Tube ID
        multi (float): Tube multiplier
        fogMulti (float): Object multiplier
    """
    exData['customData']['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled,
        components={'ILightWithId':{'lightID':id},'TubeBloomPrePassLight':{'colorAlphaMultiplier':multi,'bloomFogIntensityMultiplier':fogMulti}}
        ))

def fridgeTrack(pix, trackName, distanceFromPlayer = 12, color=[1,1,1,0]):
    """Converts a B&W fridge image into geometry and assigns it to a track

    Args:
        pix (array): Fridge Image
        trackName (string): Track
        distanceFromPlayer (float, optional): Distance from player. Defaults to 12.
        color (array, optional): Color. Defaults to [1,1,1,0].
    """
    xLen = (len(pix[0])/2)-1
    yLen = (len(pix)/2)-1

    #Add material with name unique to spawned fridge
    matName = str(rand.randint(0,9999999))
    exData['customData']['materials'][matName] = {'color':color,'shader':'Standard'}

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

def clrTween(nTime, trackName, duration, clr0, clr1, easing='easeLinear'):
    exData['customData']['customEvents'].append(dict(b=nTime, t='AnimateTrack', d={'duration':duration, 'repeat':0}))
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['track'] = trackName
    clr1.append(easing)
    exData['customData']['customEvents'][len(exData['customData']['customEvents']) - 1]['d']['color'] = [
        clr0,
        clr1
    ]   
