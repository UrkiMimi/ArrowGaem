### Basic preperation stuff
import json
import random as rand
import math

envData = {}

### Use this function first
# function that creates the metadata for the environment
def metaData(na,auth,envVer,envName,desc):
    envData['version'] = '1.0.0'
    envData['name'] = na
    envData['author'] = auth
    envData['environmentVersion'] = envVer
    envData['environmentName'] = envName
    envData['description'] = desc
    envData['features'] = {}

metaData(
    'Big Mirror Chevron',
    'ojooj',
    '0.0.2',
    'BigMirrorEnvironment',
    'the fucking'
)
envData['environment'] = []
### Env Functions
# Disables object in scene
def disableObject(envId, lookupMe):
    envData['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False))

def dupe(envId, lookupMe, dupe):
    envData['environment'].append(dict(id=envId, lookupMethod=lookupMe,active=False,duplicate=dupe))

def fogging(envId, lookupMe, atten, offset, startY, height):
    envData['environment'].append(dict(
        id=envId,
        lookupMethod=lookupMe,
        components={'BloomFogEnvironment':{'attenuation':atten,'offset':offset,'startY':startY,'height':height}}
    ))

# Customization for objects
def editer(envId, lookupMe, pos, sc, rotation, enabled):
    envData['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled
        ))
    
# Customization for tubelights you want to do hacky shit with
def tubeEditer(envId, lookupMe, pos, sc, rotation, enabled, id, multi, fogMulti):
    envData['environment'].append(dict(
        id=envId, 
        lookupMethod=lookupMe,
        localPosition=pos,
        scale=sc,
        localRotation=rotation,
        active=enabled,
        components={'ILightWithId':{'lightID':id},'TubeBloomPrePassLight':{'colorAlphaMultiplier':multi,'bloomFogIntensityMultiplier':fogMulti}}
        ))
    
# fixes env errors
def sanityCheck():
    for index in range(len(envData['environment'])):
        if 'duplicate' in envData['environment'][index]:
            if envData['environment'][index]['duplicate'] == 0:
                envData['environment'][index].pop('duplicate')

### Do Env scripting here
dupe('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[0]NeonTube','Exact',4)
disableObject('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[0]NeonTube','Exact')
disableObject('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[1]NeonTube (1)','Exact')
disableObject('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[1]NeonTube (1)','Exact')
disableObject('BigMirrorEnvironment.[0]Environment.[10]BasicGameHUD.[2]RightPanel.[2]MultiplierCanvas.[0]BGCircle','Exact')

tubeEditer('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[2]NeonTube(Clone)','Exact',
           [-0.05,4.65,55],
           [0.8,2.2/1.25,0.8],
           [0,0,55],
           True,4,3,2)
tubeEditer('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[3]NeonTube(Clone)','Exact',
           [-0.05,4.65,55],
           [0.8,2.2/1.25,0.8],
           [0,0,-55],
           True,4,3,2)
tubeEditer('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[4]NeonTube(Clone)','Exact',
           [0.05,4.65,85],
           [0.8,2.2/1.25,0.8],
           [0,0,55],
           True,4,3,2)
tubeEditer('BigMirrorEnvironment.[0]Environment.[19]FrontLights.[5]NeonTube(Clone)','Exact',
           [-0.05,4.65,85],
           [0.8,2.2/1.25,0.8],
           [0,0,-55],
           True,4,3,2)
editer('BigMirrorEnvironment.[0]Environment.[19]FrontLights','Exact',
       [0,0,0],
       [1,1,1],
       [0,0,0],
       True)
fogging('BigMirrorEnvironment.[0]Environment','Exact',
        0.003,4,-20,0.1)

sanityCheck()

### Save json to Ex+ file
exPlusFile = open('env.dat', 'w')
exPlusFile.write(json.dumps(envData, indent=2))
exPlusFile.close()