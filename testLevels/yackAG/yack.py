### Basic preperation stuff
import json
import Hamen
from hamenNoodle import *
from hamenChroma import *
import pixArt
import math
import random as rand
from copy import deepcopy



#FUCK
envData = open('env.dat','r')
envJson = json.loads(envData.read())
envData.close()

### Noodle fuckery
# Add arrays
exData['customData'] = {}
exData['customData']['fakeColorNotes'] = []
exData['customData']['fakeBombNotes'] = []
exData['customData']['customEvents'] = []
exData['customData']['materials'] = {}
exData['customData']['environment'] = envJson['environment']

## paragraph
'''
I used to keep the scripts for modcharts in one file but it leads to it being horribly organized so 
I'm storing it in megaScript.py since it keeps this project a lot more organized and makes me able 
to use the same script for multiple modcharts without retweaking.
This dumb change will probably be in future charts that I make.

*** WARNING ***
Map source comments may contain naughty language.
'''

### do note scripts here
## init
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[10]BasicGameHUD', 'hud', 'Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[19]FrontLights', 'frontLights', 'Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[3]Floor', 'floor1','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[5]Construction','floor2','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[7]NearBuildingLeft','leftB','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[8]NearBuildingRight','rightB','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[11]Spectrograms','spectro','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment','mainEnv','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[10]BasicGameHUD.[1]LeftPanel','panel','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[10]BasicGameHUD.[2]RightPanel','panel','Exact')
assignEnvironmentToTrack('BigMirrorEnvironment.[0]Environment.[10]BasicGameHUD.[0]EnergyPanel','energyPanel','Exact')

## do funny point assignmnet

# heck.dll can suck my dick
for i in range(50):
    posTween(i/2,'arrowRot0',1,'easeLinear',[0,0,10000,0],[0,0,10000,1])
    posTween(i/2,'arrowRot2',1,'easeLinear',[0,0,10000,0],[0,0,10000,1])

tmpArray = []
twist = []
for index in range(240):
    tmpArray.append([0,0,15*round(math.sin(index/3),3)*(1-(index/240)),index/240])

for index in range(100):
    geg = round((index/100)*360,2)
    geg2 = round((index/100)*-30,2)
    twist.append([geg,geg2,0,index/100])

rotationFly(0,77,3.5)

# region into the light

#bounce
for i in range(4):
    assignNoteLaneToTrack(82,146,'b'+str(i%2),i)

# setup
dissolve(78,'b2',4,0,0)
dissolveArrow(78,'b2',4,0,0)

# animate fake lanes
moveIt2 = 0.25
for i in range(29):
    if i%2 == 0:
        posTweenObjekt(81.75+i,'b0',0.25,'easeInExpo',[0,0,0,0],[-moveIt2,0,0,1])
        posTweenObjekt(81.75+i,'b1',0.25,'easeInExpo',[0,0,0,0],[moveIt2,0,0,1])
        posTweenObjekt(82+i,'b0',0.75,'easeOutExpo',[-moveIt2,0,0,0],[0,0,0,1])
        posTweenObjekt(82+i,'b1',0.75,'easeOutExpo',[moveIt2,0,0,0],[0,0,0,1])
    else:
        posTweenObjekt(81.75+i,'b0',0.25,'easeInExpo',[0,0,0,0],[moveIt2,0,0,1])
        posTweenObjekt(81.75+i,'b1',0.25,'easeInExpo',[0,0,0,0],[-moveIt2,0,0,1])
        posTweenObjekt(82+i,'b0',0.75,'easeOutExpo',[moveIt2,0,0,0],[0,0,0,1])
        posTweenObjekt(82+i,'b1',0.75,'easeOutExpo',[-moveIt2,0,0,0],[0,0,0,1])

for i in range(32):
    if i%2 == 0:
        posTweenObjekt(113.75+i,'b0',0.75,'easeInExpo',[0,0,0,0],[0,moveIt2,0,1])
        posTweenObjekt(113.75+i,'b1',0.75,'easeInExpo',[0,-moveIt2,0,0],[0,0,0,1])
        posTweenObjekt(114+i,'b0',0.75,'easeOutExpo',[0,moveIt2,0,0],[0,0,0,1])
        posTweenObjekt(114+i,'b1',0.75,'easeOutExpo',[0,-moveIt2,0,0],[0,0,0,1])
    else:
        posTweenObjekt(113.75+i,'b0',0.75,'easeInExpo',[0,0,0,0],[0,-moveIt2,0,1])
        posTweenObjekt(113.75+i,'b1',0.75,'easeInExpo',[0,moveIt2,0,0],[0,0,0,1])
        posTweenObjekt(114+i,'b0',0.75,'easeOutExpo',[0,-moveIt2,0,0],[0,0,0,1])
        posTweenObjekt(114+i,'b1',0.75,'easeOutExpo',[0,moveIt2,0,0],[0,0,0,1])
del(moveIt2)


for i in range(14):
    #scale notes every 4 beats
    if i >= 7:
        scaleTween(82+(i*4),'b0',2,'easeOutExpo',[2/(i+2),i+1,1,0],[1,1,1,1])
        scaleTween(82+(i*4),'b1',2,'easeOutExpo',[2/(i+2),i+1,1,0],[1,1,1,1])
    else:
        scaleTween(82+(i*4),'b0',2,'easeOutExpo',[i+1,2/(i+2),1,0],[1,1,1,1])
        scaleTween(82+(i*4),'b1',2,'easeOutExpo',[i+1,2/(i+2),1,0],[1,1,1,1])
        
    #dissolve notes with this too
    dissolveBoth(82+(i*4),'b0',1,3/(i+3.5),1)
    dissolveBoth(82+(i*4),'b1',1,3/(i+3.5),1)

    


# push to fake notes and make real ones transparent
spawnFakeNotesWithTrackAt(82,145.5,True,0)
assignNotesToTrack(82,145.5,'b2',False)

# region kit catalina
# line 119 repeat
assignNotesToTrack(146,193,'shakeyBois',False)
spawnFakeNotesWithTrackAt(146,193,True,0)
assignNotesToTrack(146,193,'c2',False)

dissolveBoth(142,'c2',4,0,0)

# loop for shakey rotation part for beats
for i in range(63):
    initialRotate = [rand.randint(-5,5),rand.randint(-5,5),rand.randint(-5,5),0]
    localRotate(146+i,'shakeyBois',1,'easeOutExpo',initialRotate,
           [initialRotate[0]+rand.randint(-20,20),initialRotate[1]+rand.randint(-20,20),initialRotate[2]+rand.randint(-20,20),1])
    posTweenObjekt(146+i,'shakeyBois',1,'easeOutBack',[((i%2)-0.5)*0.5,0,0,0],[0,0,0,1])

# loop for bounce
for i in range(4):
    scaleTween(185+i/4,'shakeyBois',1,'easeOutElastic',[2,2,2,0],[1,1,1,1])

# wat donezo party (bad mistranslation)
scalePointDef(189,'shakeyBois',1,[[1,1,1,0],[-3,1,1,0.5,'easeOutQuad'],[1,1,1,1,'easeInQuad']])
scalePointDef(191,'shakeyBois',1,[[1,1,1,0],[1,-3,1,0.5,'easeOutQuad'],[1,1,1,1,'easeInQuad']])


# region stuff before 1 minute
assignNotesToTrack(211,269.9,'g1',False)
spawnFakeNotesWithTrackAt(194,210, True, -0.015,'FakeGlitch')
spawnFakeNotesWithTrackAt(211,218, True, 0,'deathNotes')
assignNotesToTrack(194,210,'noArrowTrack',False)
removeGravity(194,210,False)
spawnFakeNotesWithTrackAt(270, 274,True,-0.015,'d3')
removeGravity(194,269,False)
spawnFakeNotesWithTrackAt(211,269, True, -0.015,'g2')
spawnFakeNotesWithTrackAt(211,269, True, 0,'g3')
lazyOffset(210,274,1)

# track parenting funny
childrenTracks(200,'g1',['g2','g3','hud','energyPanel','frontLights'])


# what in the world
childrenTracks(0,'arrowRot0',['leftArrow'])
childrenTracks(0,'arrowRot2',['rightArrow'])
childrenTracks(0,'fack',['arrowRot0','arrowRot2'])
#childrenTracks(200,'rot3',['jimmy'])
#childrenTracks(200,'rot4',['face'])


## make notes before drop shake
#setup dissolve
dissolve(191,'FakeGlitch',4,0,0)
dissolveArrow(191,'noArrowTrack',4,0,0)


# Note Anims

#Pos Effects
posTweenObjekt(192,'FakeGlitch',2,'easeInExpo',[1,1,0,0],[-0.02,-0.02,0,1])
posTweenObjekt(194,'FakeGlitch',2,'easeOutElastic',[-0.1,-0.1,0,0],[0.0,0.0,0,1])

#dissolve chuckel nuts
dissolve(200,'noArrowTrack',0.2,1,0)
dissolve(201,'noArrowTrack',0.2,0,1)
dissolveArrow(201,'FakeGlitch',0.2,1,0)
dissolveArrow(202,'FakeGlitch',0.2,0,1)

#Shake thing
shakeOutObjekt(202,'FakeGlitch',2,0.5,10)
shakeOutObjekt(204,'FakeGlitch',2,0.5,10)

posTweenObjekt(206,'FakeGlitch',0.5,'easeOutQuad',[0,0,0,0],[0,0,0,1])

for ps in range(2):
    scaleTween(206+ps,'FakeGlitch',1,'easeOutExpo',[10,1,1,0],[1,1,1,1])
    posTweenObjekt(208+ps,'FakeGlitch',0.5,'easeOutQuad',[0,0,0,0],[0,0.5*(ps*2-1),0,1])
    posTweenObjekt(208.5+ps,'FakeGlitch',0.5,'easeInQuad',[0,0.5*(ps*2-1),0,0],[0,0,0,1])

dissolve(209,'noArrowTrack',1,1,0)


## init 2
# assign arrows to track and make them have dissolve turned off
fridgeTrack(pixArt.arrow_right, 'rightArrow',distanceFromPlayer=0)
fridgeTrack(pixArt.left_arrow, 'leftArrow',distanceFromPlayer=0)

##scalePointDef(0,'jimmy',4,[[0,0,0,0]])
##scalePointDef(0,'face',4,[[0,0,0,0]])

# region one minute mark

# Move floor
posTween(210,'floor2',1,'easeOutQuad',[0,0,0,0],[0,0,60,1])
posTween(210,'floor2',1,'easeInOutSine',[0,0,0,0],[0,0,50,1])

# Move floor 2
posTween(210,'floor1',2,'easeOutQuint',[0,0,7.5,0],[0,0,-69,1])
scaleTween(210,'floor1',2,'easeOutQuint',[1,1,1,0],[10,1,1.5,1])

# Move Towers
posTween(210,'rightB',2,'easeInExpo',[20,3,15,0],[20,-50,15,1])
posTween(210,'leftB',2,'easeInExpo',[-20,3,15,0],[-20,-50,15,1])
posTween(210,'spectro',2,'easeInExpo',[0,7,0,0],[0,-20,0,1])

# move energy panel to top
posTween(210,'energyPanel',6,'easeOutElastic',[0,-0.64,7.75,0],[0,3,7.75,1])

# shake environment with trig
rotatePointDef(210,'mainEnv',8,tmpArray)

# spin hud
rotatePointDef(210,'panel',2,twist,'easeOutExpo')

# death to og notes
dissolve(210,'deathNotes',6,0.5,0)
dissolveArrow(210,'deathNotes',6,1,0)

# note explode
newKablooey(210, 8)

# g2 and g3 my beloved
dissolveArrow(205,'g3',6,0,0)
dissolve(205,'g2',4,0,0)

# make g1 invisible
dissolveArrow(205,'g1',6,0,0)
dissolve(205,'g1',6,0,0)

#reduce code
flashbangList = [210,218,226,234,242,250,258,266]
dirList = [-30,60,-30,15,0,30,0]
for i in flashbangList:
    noteBloom(i,2,50,2.5)
    scaleTween(i,'g2',2,'easeOutCubic',[10,0.1,1,0],[1,1,1,1])
    scaleTween(i,'g3',0.5,'easeOutExpo',[10,1,1,0],[1,1,1,1])
    posTween(i,'g3',0.5,'easeOutExpo',[2.5,0,0,0],[0,0,0,1])

    if not(i == 266):
        dissolve(i,'g3',2,0.5,1)

## Animations im gonna define before the rotatey part even though they happen after it
# makes the notes do funny
posTween(216,'g2',1,'easeOutExpo',[0,0,0,0],[0,1,0,1])
posTween(217,'g2',1,'easeOutExpo',[0,1,0,0],[1,1,0,1])
posTween(218,'g2',1.5,'easeOutElastic',[1,1,0,0],[0,0,0,1])

#to be less redundant
posPointDef(222,'g2',4,[[0,0,0,0],[1,0,0,0.125,'easeOutQuad'],[2,0,0,0.25,'easeOutQuad'],[3,0,0,0.375,'easeOutQuad'],[4,0,0,0.5,'easeOutQuad'],[0,0,0,1,'easeOutElastic']])

rotate(232,'g2',1,'easeOutElastic',[0,0,0,0],[30,0,0,1])
rotate(233,'g2',1,'easeOutElastic',[30,0,0,0],[-30,0,0,1])
rotate(234,'g2',2,'easeOutElastic',[-30,0,0,0],[0,0,0,1])

posPointDef(254,'g2',4,[[0,0,0,0],[0,0.5,0,0.125,'easeOutQuad'],[0,-0.5,0,0.25,'easeOutQuad'],[0,1,0,0.375,'easeOutQuad'],[0,-1,0,0.5,'easeOutQuad'],[0,0,0,1,'easeOutElastic']])
dissolve(256,'g3',2,1,0)
dissolve(258,'g3',0.5,0,1)

# new assignment :D
tmpArray = []
s1 = []

for i in range(60):
    tmpArray.append([round(math.tan(i/3),3),0,0,i/60])
    s1.append([abs(round(1*math.tan(i/3),3))+1,1,1,i/60])

tmpArray.append([0,0,0,1])
s1.append([1,1,1,1])


posPointDef(240,'g2',2,tmpArray)
scalePointDef(240,'g2',2,s1)
scalePointDef(240,'g3',2,s1)

del(tmpArray,s1)

#real trolling hours
for i in range(8):
    rotate(244+i*0.5,'g2',0.5,'easeOutExpo',[rand.randint(-5,5),rand.randint(-5,5),rand.randint(-180,180),0],[0,0,0,1])
    scaleTween(244+i*0.5,'g2',0.5,'easeOutExpo',[100,1,1,0],[1,1,1,1])
    rotate(244+i*0.5,'g3',0.5,'easeOutExpo',[rand.randint(-5,5),rand.randint(-5,5),rand.randint(-10,10),0],[0,0,0,1])
    scaleTween(244+i*0.5,'g3',0.5,'easeOutExpo',[2,0.5,1,0],[1,1,1,1])

dissolveArrow(244,'g2',2,0.25,1)
dissolveArrow(248,'g2',2,0.25,0)
dissolveArrow(250,'g2',0.1,0,1)


# Rotatey thing and trail thing
outBackTurn(210,'g1',0,-30)
headsUpTurn(210,'leftArrow','arrowRot0',10,0)

outBackTurn(218,'g1',-30,-60)
headsUpTurn(218,'leftArrow','arrowRot0',-20,-30)
staticTrail(218,32,2,-30)

outBackTurn(226,'g1',-60,-30)
headsUpTurn(226,'rightArrow','arrowRot2',-70,-60)

outBackTurn(234,'g1',-30,-15)
headsUpTurn(234,'rightArrow','arrowRot2',-40,-30)

outBackTurn(242,'g1',-15,0)
headsUpTurn(242,'rightArrow','arrowRot2',-25,-15)

outBackTurn(250,'g1',0,30)
headsUpTurn(250,'rightArrow','arrowRot2',-10,0)

outBackTurn(256,'g1',30,0)
headsUpTurn(256,'leftArrow','arrowRot0',40,30)


# Move environment shit back
posTween(258,'floor2',1,'easeOutQuad',[0,0,50,0],[0,0,-5,1])
posTween(259,'floor2',1,'easeInOutSine',[0,0,-5,0],[0,0,0,1])

posTween(258,'floor1',1,'easeOutQuint',[0,0,-69,0],[0,0,9.5,1])
scaleTween(258,'floor1',1,'easeOutSine',[10,1,1.5,0],[1,1,1,1])
posTween(258,'floor1',1,'easeInQuint',[0,0,9.5,0],[0,0,7.5,1])


# Move Towers Back
posTween(258,'rightB',2,'easeOutExpo',[20,-50,15,0],[20,3,15,1])
posTween(258,'leftB',2,'easeOutExpo',[-20,-50,15,0],[-20,3,15,1])
posTween(258,'spectro',2,'easeOutExpo',[0,0,0,0],[0,7,0,1])

# move energy bar back
posTween(258,'energyPanel',3,'easeOutBack',[0,3,7.75,0],[0,-.64,7.75,1])

'''
# jimmy
fridgeTrack(pixArt.one, 'jimmy')
fridgeTrack(pixArt.two,'face')
#fridgeTrack(264, pixArt.troll_face, 'troll')
dissolve(260,'jimmy',4,0,0)
dissolve(260,'face',4,0,0)
'''

# polyriddm oh mah gahd 
polyrid = [262,262.5,262.75,263,263.5]
for i in polyrid:
    posTween(i,'g3',0.5,'easeOutExpo',[round(rand.uniform(-1,1),3),round(rand.uniform(-1,1),3),0,0],[0,0,0,1])
    rotate(i,'g2',0.5,'easeOutExpo',[rand.randint(-5,5),rand.randint(-180,180),rand.randint(-5,5),0],[0,0,0,1])
    scaleTween(i,'g2',0.5,'easeOutExpo',[100,0.01,1,0],[1,1,1,1])
    scaleTween(i,'g3',0.5,'easeOutCubic',[2,1,1,0],[1,1,1,1])
    dissolve(i,'g3',1,0.75,1)
    dissolveArrow(i,'g2',1,0.25,1)


bX = 5
bY = 1
bOffset = 5

#posTween(264,'rot3',0.5,'easeOutQuad',[bX,bY,bOffset,0],[bX,bY,bOffset,1])
#posTween(264,'rot4',0.5,'easeOutQuad',[-bX,bY,bOffset,0],[-bX,bY,bOffset,1])

'''
#animate numbers
scaleTween(264,'jimmy',1,'easeOutExpo',[0,0,0,0],[0.5,0.5,0.5,1])
scaleTween(266,'jimmy',1,'easeInExpo',[0.5,0.5,0.5,0],[0,0,0,1])
scaleTween(264,'face',1,'easeOutExpo',[0,0,0,0],[0.5,0.5,0.5,1])
scaleTween(266,'face',1,'easeInExpo',[0.5,0.5,0.5,0],[0,0,0,1])


rotate(264,'rot3',1,'easeOutExpo',[rand.randint(-30,30),rand.randint(-30,30),rand.randint(-10,10),0],[0,0,0,1])
rotate(266,'rot3',1,'easeInExpo',[0,0,0,0],[rand.randint(-30,30),rand.randint(-30,30),rand.randint(-10,10),1])
rotate(264,'rot4',1,'easeOutExpo',[rand.randint(-30,30),rand.randint(-30,30),rand.randint(-10,10),0],[0,0,0,1])
rotate(266,'rot4',1,'easeInExpo',[0,0,0,0],[rand.randint(-30,30),rand.randint(-30,30),rand.randint(-10,10),1])
'''

rotate(264,'panel',1,'easeOutBack',[0,0,0,0],[0,0,30,1])
rotate(265,'panel',1,'easeOutBack',[0,0,30,0],[0,0,-30,1])
rotate(266,'panel',2,'easeOutBack',[0,0,-30,0],[0,0,0,1])



# do funny
for i in range(16):
    noteBloom(266+i/2,1,2)

space(266,274,2,'balls grip',2,50)

# Finest Color Fuckery
assignNotesToTrack(270,274,'d',True)
removeGravity(270,274,False)

#init
dissolve(268,'d3',2,0,0)
dissolveArrow(268,'d2',2,0,0)
dissolveArrow(268,'d1',2,0,0)

# stuff
for i in range(4):
    localRotate(270+i/2,'d3',0.25,'easeOutQuad',[0,0,i*90,0],[0,0,(i+1)*90,1])

for i in range(8):
    clrTween(270+i/2,'d1',0,[0,0,0,1,0],[rand.uniform(0,1),rand.uniform(0,1),rand.uniform(0,1),1,0])
    clrTween(270+i/2,'d2',0,[0,0,0,1,0],[rand.uniform(0,1),rand.uniform(0,1),rand.uniform(0,1),1,0])

posTweenObjekt(272,'d3',2,'easeInExpo',[0,0,0,0],[0,10,0,1])

# region curve nockiness
staticTrail(274,32,4,shakeSteps=64)
curveNock(276,290,posEasing='easeInQuad',rotationEasing='easeInQuad')

# do note assigning
spawnFakeNotesWithTrackAt(292,305.5,True,0,'bounci')
assignNotesToTrack(292,305.5,'e1',False)

dissolveBoth(278,'e1',4,0,0)

# first bounce part which is 2 beats long
for i in range(4):
    posTweenObjekt(290+(i*2),'bounci',2,'easeOutElastic',[0,((i%2)-0.5),0,0],[0,0,0,1])

# second bounce part
for i in range(4):
    posTweenObjekt(298+i,'bounci',1,'easeInOutExpo',[0,0,1,0],[0,0,0,1])

# final bounce part
for i in range(8):
    if i%2 == 1:
        scaleTween(302+(i/2),'bounci',1,'easeOutElastic',[-2,-2,2,0],[-1,-1,1,1])
    else:
        scaleTween(302+(i/2),'bounci',1,'easeOutElastic',[2,2,2,0],[1,1,1,1])

# color part
assignNotesToTrack(306,310,'c18beloved',True)

for i in range(16):
    if i%2 == 0:
        clrTween(306+(i/4),'c18beloved1',0.25,[0.249,0.249,0.249,1,0],[1,0,0,1,1])
        clrTween(306+(i/4),'c18beloved2',0.25,[0.249,0.572,1,1,0],[0.249,0.249,0.249,1,1])
    else:
        clrTween(306+(i/4),'c18beloved1',0.25,[1,0,0,1,0],[0.249,0.249,0.249,1,1])
        clrTween(306+(i/4),'c18beloved2',0.25,[0.249,0.249,0.249,1,0],[0.249,0.572,1,1,1])


# region panel animations for one minute mark and beyond
rotate(216,'panel',1,'easeOutExpo',[0,0,0,0],[-30,0,0,1])
rotate(217,'panel',1,'easeOutExpo',[-30,0,0,0],[-30,45,0,1])
rotate(218,'panel',4,'easeOutElastic',[-30,45,0,0],[0,-60,0,1])

#cowgirl sex
for i in range(2):
    posTween(232+i,'hud',0.5,'easeOutQuad',[0,0,0,0],[0,2,0,1])
    posTween(232.5+i,'hud',0.5,'easeInQuad',[0,2,0,0],[0,0,0,1])



posTween(240,'hud',2,'easeLinear',[0,0,0,0],[0,0,30,1])
scaleTween(240,'hud',2,'easeLinear',[1,1,1,0],[0,0,0,1])
scalePointDef(242,'hud',0.1,[[1,1,1,1]])
posTween(242,'hud',2,'easeOutExpo',[0,-50,0,0],[0,0,0,1])

rotate(248,'panel',1,'easeOutExpo',[0,0,0,0],[30,10,0,1])
rotate(249,'panel',1,'easeOutExpo',[30,10,0,0],[30,10,30,1])
rotate(250,'panel',4,'easeOutElastic',[30,10,30,0],[0,30,0,1])

#cowgirl sex (again)
for i in range(8):
    posTween(266+i,'hud',0.25,'easeOutQuad',[0,0,0,0],[0,i,0,1])
    posTween(266.25+i,'hud',0.25,'easeInQuad',[0,i,0,0],[0,0,0,1])
    posTween(266.5+i,'hud',0.25,'easeOutQuad',[0,0,0,0],[0,i,0,1])
    posTween(266.75+i,'hud',0.25,'easeInQuad',[0,i,0,0],[0,0,0,1])

# i wanted to be funny with the scream
for i in range(52):
    initialRotate = [rand.randint(-5,5),rand.randint(-5,5),rand.randint(-5,5),0]
    localRotate(318+i,'panel',1,'easeOutExpo',initialRotate,
           [initialRotate[0]+rand.randint(-20,20),initialRotate[1]+rand.randint(-20,20),initialRotate[2]+rand.randint(-20,20),1])

for i in range(16):
    initialRotate = [rand.randint(-5,5),rand.randint(-5,5),rand.randint(-5,5),0]
    localRotate(370+i/2,'panel',0.5,'easeOutExpo',initialRotate,
           [initialRotate[0]+rand.randint(-20,20),initialRotate[1]+rand.randint(-20,20),initialRotate[2]+rand.randint(-20,20),1])

# region screaming lololololololol

# funny spin shithfkajshkjas
for i in range(8):
    newKablooey(310+i/64,8)

# spin hud again
twist = []
for i in range(360):
    twist.append([0,round((i/360)*1080,2),0,i/360])
twist.append([0,0,1080,1])

rotatePointDef(310,'frontLights',6,twist,'easeOutCirc')
localRotatePointDef(310,'panel',6,twist,'easeOutCirc')
localRotatePointDef(378,'panel',6,twist,'easeOutCirc')


# the fucking
assignNotesToTrack(318,378,'bounce',False)
fakeryRing(318,378,4)
moveIt(318,378,'easeInOutExpo',4,1,4)

for i in range(52):
    scaleTween(318+i,'bounce',1,'easeOutCubic',[4,0.25,1,0],[1,1,1,1])
for i in range(16):
    scaleTween(370+i/2,'bounce',0.5,'easeOutCubic',[4,0.25,1,0],[1,1,1,1])

# region end stuff
removeGravity(378,406,False)
rotationFly(379,403,5)
ghostArrows(386,409,16,3,1)

newKablooey(406, 8)

thinkFastChucklenuts(406,406,10)

### Save json to Ex+ file
diPlusFile = open('ExpertPlusStandard.dat', 'w')
diPlusFile.write(json.dumps(exData,indent=2))
diPlusFile.close()