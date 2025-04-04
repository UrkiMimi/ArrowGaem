## Vivify based library for heck related maps.
## Use this with asset bundle shit
## Refer to https://heck.aeroluna.dev/ when using this 

from Hamen import *
from os import path, rename, remove

## start functions here
def setUnityMaterialProperty(nTime, materialName, duration, shaderID, type, value, easing='easeLinear'):
    """Sets unity material property to specified value

    Args:
        nTime (float): Time
        materialName (string): Asset path for material
        duration (float): Animation duration
        shaderID (string): Property name on the material
        type (string): Property Type. [Texture, Float, Color, Vector, Keyword]
        value (?): Material value. Varies on property type
        easing (string, optional): Easing. Defaults to 'easeLinear'.
    """
    # customData part
    cData = {}
    cData['asset'] = materialName.lower() # lower for accidental typos for paths
    cData['duration'] = duration
    cData['easing'] = easing
    cData['properties'] = [dict(id = shaderID, type=type, value=value)]

    # inject customData into event
    exData['customData']['customEvents'].append(dict(b=nTime, t='SetMaterialProperty', d=cData))


def setUnityGlobalProperty(nTime, duration, propID, type, value, easing='easeLinear'):
    """Sets global unity property

    Args:
        nTime (float): Time
        duration (float): Animation time
        propID (string): Name of the property
        type (string): Type of property
        value (?): What to set the property to. Varies on property type
        easing (string, optional): Easing. Defaults to 'easeLinear'.
    """

    # customData part
    cData = {}
    cData['duration'] = duration
    cData['easing'] = easing
    cData['properties'] = [dict(id = propID, type=type, value=value)]

    # inject customData into event
    exData['customData']['customEvents'].append(dict(b=nTime, t='SetGlobalProperty', d=cData))

def unityBlit(nTime, duration, propID, type, value, asset=None, priority=None, cPass=None, order=None, source=None, destination=None, easing='easeLinear'):
    """Assigns material to camera

    Args:
        nTime (Float): Time in beats
        duration (float): How long the material is on the camera
        propID (string): Property ID
        type (string): Property type [See AssignMaterialProperty for explanation]
        value (?): Material value
        asset (string, optional): Asset path. Defaults to None.
        priority (int, optional): Which order to run the current active post processing effects. Defaults to None.
        cPass (int, optional): Which pass in the shader to use. Defaults to None.
        order (string, optional): Whether to use this shader before or after MainEffect [Bloom]. Defaults to None.
        source (string, optional): Source texture. Defaults to None.
        destination (string, optional): Destination texture. Defaults to None.
        easing (string, optional): Easing. Defaults to 'easeLinear'.
    """

    # customData part
    cData = {}
    cData['duration'] = duration
    cData['easing'] = easing
    cData['properties'] = [dict(id = propID, type=type, value=value)]
    
    # optional stuff
    if asset != None:
        cData['asset'] = asset.lower() # lower for accidental typos for paths
    if priority != None:
        cData['priority'] = priority
    if cPass != None:
        cData['pass'] = cPass
    if order != None:
        cData['order'] = order
    if source != None:
        cData['source'] = source
    if destination != None:
        cData['destination'] = destination

    # inject customData into event
    exData['customData']['customEvents'].append(dict(b=nTime, t='Blit', d=cData))

def createCamera(nTime, id, cullingTrack='', whitelist=True, depthMode = ['depth'], texture=None, depthTexture=None):
    """Creates a camera

    Args:
        nTime (float): Time in beats
        id (string): ID of camera
        texture (string): Will render to a new texture set to this key (Optional)
        depthTexture (string): Renders just the depth to this texture (Optional)
        cullingTrack (string, optional): Track to be culled. Defaults to ''.
        whitelist (bool, optional): Enable or disable Whitelist mode. Defaults to True.
        depthMode (list, optional): Depth texture shit i dont understand. Defaults to ['depth'].
    """

    # customData part
    cData = {}
    cData['id'] = id
    cData['properties'] = [dict(culling={'track':cullingTrack,'whitelist':whitelist}, depthTextureMode = depthMode)]

    # optional shit
    if texture != None:
        cData['texture'] = texture
    if depthTexture != None:
        cData['depthTexture'] = depthTexture

    exData['customData']['customEvents'].append(dict(b=nTime, t='CreateCamera', d=cData))

def assignObjectPrefab(nTime, loadMode, objectName, contents = {}):
    """Assigns prefab from asset bundle to an object

    Args:
        nTime (float): Time in beats
        loadMode (string): How to load the asset
        objectName (string): Name of object
        contents (dict, optional): Object properties. See vivify github documentation
    """

    cData = {}
    cData['loadMode'] = loadMode
    cData[objectName] = contents

    exData['customData']['customEvents'].append(dict(b=nTime, t='AssignObjectPrefab', d=cData))

def InstantiatePrefab(nTime, asset, id=None, track=None, position=[0,0,0], localPosition=[0,0,0], rotation=[0,0,0], localRotation=[0,0,0], scale=[1,1,1]):
    # custom data
    cData = {}
    cData['asset'] = asset
    cData['position'] = position
    cData['localPosition'] = localPosition
    cData['rotation'] = rotation
    cData['localRotation'] = localRotation
    cData['scale'] = scale

    # optional properties
    if id != None:
        cData['id'] = id
    if track != None:
        cData['track'] = track

    # inject customData into json
    exData['customData']['customEvents'].append(dict(b=nTime, t='InstantiatePrefab', d=cData))

def destroyObject(nTime, id):
    """Destroys an object in the scene. Can be a prefab, camera, or texture id.

    Args:
        nTime (float): Time in beats
        id (string or string[]): Object(s) to destroy
    """
    # customData
    cData = {}
    cData['id'] = id
    
    exData['customData']['customEvents'].append(dict(b=nTime, t='DestroyObject', d=cData))

def loadBundleInfo(jsn):
    with open(jsn, 'r') as k:
        return json.loads(k.read())