import sys
import math

class Scanner:
	# script_pt, k1, k2, k3, k4

	def __init__(self):
		self.script_pt = self.k1 = self.k2 = self.k3 = self.k4 = 0

	def scan(self):
		self.script_pt = input("How Many ScriptPoints to generate? ")
		self.k1 = input("K1? ")
		self.k2 = input("K2? ")
		self.k3 = input("K3? ")
		self.k4 = input("K4? ")

	def getInputs(self):
		return [self.script_pt, self.k1, self.k2, self.k3, self.k4]

class Printer:
	def __init__(self):
		pass

	def createWorldFile(self,filename):
		self.file = open(filename, 'w')

	def closeWorldFile(self):
		self.file.close()

	def writeWorldFile(self, lst, offset=[0,0,0]):
		# write header
		self.printHeader(len(lst)+5)
		# write script point
		for i in range(1,len(lst)+1):
			self.file.write(self.printOrigin(i,lst[i-1]));
		# write footer
		self.printFooter(offset)

	def printOrigin(self,i,loc):
		message = 'CEntity\neStyle 0\neOrigin %d %d %d 2\n' % (loc[0], loc[1], loc[2])
		message += '''eFlags 0
eGroup 0
ePairCount 7
Key Angle Value "0 0 0"
Key classname Value "ScriptPoint"
Key NextOrder Value ""'''
		message += '\nKey NextPoint Value "campt%d"''' % (i+1)
		message += '\nKey origin Value "%d %d %d"' % (loc[0], loc[1], loc[2])
		message += '\nKey szEntityName Value "campt%d"' % (i)
		message += '\nKey %%name%% Value "ScriptPoint%d"\n' % (i)
		message += """End CEntity"""
		message += '\n'
		return message

	def printHeader(self, count):
		message = '''3dtVersion 1.34
TextureLib "L:\\\\RealityFactory076\\\\media\\\\levels\\\\default.txl"
HeadersDir "L:\\\\RealityFactory076\\\\source;"
ActorsDir "L:\\\\RealityFactory076\\\\media\\\\Actors"
PawnIni "L:\\\\RealityFactory076\\\\install\\\\Pawn.ini"
'''
		message += "NumEntities %d" % (count)
		message += '''
NumModels 0
NumGroups 1
Brushlist 1
Brush "ALCHEM3"
	Flags 1025
	ModelId 0
	GroupId 0
	HullSize 16.000000
	Type 1
Brushlist 2
Brush "ALCHEM3"
	Flags 1025
	ModelId 0
	GroupId 0
	HullSize 16.000000
	Type 2
	BrushFaces 6
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 512.000000 448.000000 -512.000000
			Vec3d 512.000000 448.000000 512.000000
			Vec3d -512.000000 448.000000 512.000000
			Vec3d -512.000000 448.000000 -512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d -512.000000 -256.000000 512.000000
			Vec3d 512.000000 -256.000000 512.000000
			Vec3d 512.000000 -256.000000 -512.000000
			Vec3d -512.000000 -256.000000 -512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 512.000000 448.000000 512.000000
			Vec3d 512.000000 -256.000000 512.000000
			Vec3d -512.000000 -256.000000 512.000000
			Vec3d -512.000000 448.000000 512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d -512.000000 -256.000000 -512.000000
			Vec3d 512.000000 -256.000000 -512.000000
			Vec3d 512.000000 448.000000 -512.000000
			Vec3d -512.000000 448.000000 -512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d -512.000000 448.000000 512.000000
			Vec3d -512.000000 -256.000000 512.000000
			Vec3d -512.000000 -256.000000 -512.000000
			Vec3d -512.000000 448.000000 -512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	0.000000 0.000000 1.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 512.000000 -256.000000 -512.000000
			Vec3d 512.000000 -256.000000 512.000000
			Vec3d 512.000000 448.000000 512.000000
			Vec3d 512.000000 448.000000 -512.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	0.000000 0.000000 1.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
Brush "ALCHEM3"
	Flags 145
	ModelId 0
	GroupId 0
	HullSize 16.000000
	Type 2
	BrushFaces 6
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d -496.000000 432.000000 -496.000000
			Vec3d 496.000000 432.000000 -496.000000
			Vec3d 496.000000 432.000000 496.000000
			Vec3d -496.000000 432.000000 496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 496.000000 -240.000000 -496.000000
			Vec3d -496.000000 -240.000000 -496.000000
			Vec3d -496.000000 -240.000000 496.000000
			Vec3d 496.000000 -240.000000 496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "florbrwn"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 496.000000 -240.000000 496.000000
			Vec3d -496.000000 -240.000000 496.000000
			Vec3d -496.000000 432.000000 496.000000
			Vec3d 496.000000 432.000000 496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 496.000000 432.000000 -496.000000
			Vec3d -496.000000 432.000000 -496.000000
			Vec3d -496.000000 -240.000000 -496.000000
			Vec3d 496.000000 -240.000000 -496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d -496.000000 -240.000000 496.000000
			Vec3d -496.000000 -240.000000 -496.000000
			Vec3d -496.000000 432.000000 -496.000000
			Vec3d -496.000000 432.000000 496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	0.000000 0.000000 1.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
		NumPoints 4
		Flags 512
		Light 300
		MipMapBias 1.000000
		Translucency 255.000000
		Reflectivity 1.000000
			Vec3d 496.000000 432.000000 496.000000
			Vec3d 496.000000 432.000000 -496.000000
			Vec3d 496.000000 -240.000000 -496.000000
			Vec3d 496.000000 -240.000000 496.000000
			TexInfo Rotate 0.000000 Shift 0 0 Scale 1.000000 1.000000 Name "ALCHEM3"
		LightScale 2.000000 2.000000
	Transform	0.000000 0.000000 1.000000 0.000000 1.000000 0.000000 -1.000000 0.000000 0.000000 0.000000 0.000000 0.000000 
	Pos	0.000000 0.000000 0.000000 
Class CEntList
'''
		message += "EntCount %d" % (count)
		message += '''
CurEnt 0
CEntity
eStyle 0
eOrigin -8 -224 -72 2
eFlags 0
eGroup 0
ePairCount 28
Key ActorName Value ""
Key ActorRotation Value "0 180 0"
Key ActorScaleFactor Value "4"
Key AttributeInfoFile Value "player.ini"
Key classname Value "PlayerSetup"
Key DeathFogColor Value "255 0 0"
Key DeathFontSize Value "0"
Key Deathlevel Value ""
Key DeathMessage Value ""
Key HeadBobbing Value "False"
Key HeadBobLimit Value "8.0"
Key HeadBobSpeed Value "1.0"
Key HUDInfoFile Value "hud.ini"
Key KeepAttrAtDeath Value "False"
Key LevelViewPoint Value "3"
Key LockView Value "False"
Key MovieMode Value "False"
Key OpeningCutScene Value ""
Key origin Value "-8 -224 -72"
Key PlayerScaleFactor Value "1.0"
Key ShadowAlpha Value "0.0"
Key ShadowAlphamap Value ""
Key ShadowBitmap Value ""
Key ShadowSize Value "0"
Key UseDeathFog Value "False"
Key UseProjectedShadows Value "False"
Key UseStencilShadows Value "False"
Key %name% Value "PlayerSetup1"
End CEntity
CEntity
eStyle 0
eOrigin -96 -216 -40 2
eFlags 0
eGroup 0
ePairCount 9
Key Angle Value "0 0 0"
Key bSoundtrackLoops Value "False"
Key classname Value "PlayerStart"
Key origin Value "-96 -216 -40"
Key szCDTrack Value ""
Key szEntityName Value ""
Key szMIDIFile Value ""
Key szStreamingAudio Value ""
Key %name% Value "PlayerStart1"
End CEntity
CEntity
eStyle 0
eOrigin -360 -184 376 2
eFlags 0
eGroup 0
ePairCount 16
Key Angle Value "0 0 0"
Key AngleRotation Value "False"
Key BoneName Value ""
Key classname Value "FixedCamera"
Key EntityName Value "movcam1"
Key FieldofView Value "2"
Key ForceTrigger Value ""
Key FOVCheckRange Value "100"
Key Model Value "<null>"
Key origin Value "-360 -184 376"
Key OriginOffset Value "0 0 0"
Key RealAngle Value "0 0 0"
Key Rotation Value "0 0 0"
Key TriggerName Value ""
Key UseFirst Value "True"
Key %name% Value "FixedCamera1"
End CEntity
CEntity
eStyle 0
eOrigin -368 -184 408 2
eFlags 0
eGroup 0
ePairCount 16
Key Angle Value "0 0 0"
Key ChangeMaterial Value ""
Key classname Value "Pawn"
Key Converse Value "<null>"
Key ConvOrder Value ""
Key ConvScriptName Value ""
Key Data Value "<null>"
Key HideFromRadar Value "False"
Key origin Value "-368 -184 408"
Key PawnType Value "MovCam"
Key ScriptName Value "movcam.s"
Key SpawnOrder Value "Spawn"
Key SpawnPoint Value "campt1"
Key SpawnTrigger Value ""
Key szEntityName Value "movcam1"
Key %name% Value "Pawn1"
End CEntity
'''
		self.file.write(message)

	def printFooter(self, offset):
		message = '''CEntity
eStyle 0
eOrigin 0 0 0 2
eFlags 0
eGroup 0
ePairCount 4
Key angles Value "180 0 0"
Key classname Value "Camera"
Key origin Value "0 0 0"
Key %name% Value "Camera1"
End CEntity
Group "Default"
	GroupId 0
	Visible 1
	Locked 0
Color 255.000000 255.000000 255.000000
Sky
0 ""
0 ""
0 ""
0 ""
0 ""
0 ""
Axis 1.000000 0.000000 0.000000
Speed 10.000000
Scale 1.000000
CompileInfo
Filename "L:\\\\RealityFactory076\\\\media\\\\levels\\\\1040_2014_0.map"
Vis 1
Light 1
Bsp 1
Preview 1
MinLight 1
SuppressHidden 0
EntitiesOnly 0
VisDetail 0
Verbose 0
ExtraSamples 0
LightScale 1.000000
Radiosity 0
NumBounce 10
PatchSize 128.000000
FastPatch 0
ReflectScale 1.000000
MinLight 128.000000 128.000000 128.000000
VisVerbose 0
FullVis 0
SortPortals 1
BspVerbose 0
EntityVerbose 0
ShowGroups 1
EntityVis 74
"WindGenerator" 1
"CurvedSurfaceEnt" 1
"CurvePatchEnt" 1
"CurveEnt" 1
"CurvePointEnt" 1
"DSpotLight" 1
"LiftBelt" 1
"SkyDome" 1
"ActMaterial" 1
"CutScene" 1
"EM_Morph" 1
"ActorSpout" 1
"Overlay" 1
"ChangeAttribute" 1
"CountDownTimer" 1
"Pawn" 1
"ScriptPoint" 1
"ModifyAttribute" 1
"Liquid" 1
"ViewSwitch" 1
"FixedCamera" 1
"ScreenShake" 1
"Explosion" 1
"FlipBook" 1
"Attribute" 1
"ModelAttributes" 1
"ModelStateModifier" 1
"DestroyableModel" 1
"FirePoint" 1
"WallDecal" 1
"DecalDefine" 1
"Message" 1
"LogicGate" 1
"Trigger" 1
"Flame" 1
"Spout" 1
"Rain" 1
"EChaos" 1
"FloatingParticles" 1
"PlayerSetup" 1
"PathFollower" 1
"PathPoint" 1
"TextureProc" 1
"ElectricBolt" 1
"ElectricBoltTerminus" 1
"DynamicLight" 1
"Corona" 1
"EnvironmentSetup" 1
"VideoTextureReplacer" 1
"StreamingAudioProxy" 1
"SoundtrackToggle" 1
"ChangeLevel" 1
"ParticleSystemProxy" 1
"StaticMesh" 1
"Foliage" 1
"StaticEntityProxy" 1
"AudioSource3D" 1
"MorphingField" 1
"PlayerStart" 1
"TeleportTarget" 1
"Teleporter" 1
"LevelController" 1
"MovingPlatform" 1
"Door" 1
"FogLight" 1
"SunLight" 1
"AreaSwitch" 1
"FlipTree" 1
"Sun" 1
"Camera" 1
"ModelOrigin" 1
"Sunlight" 1
"spotlight" 1
"light" 1
Grid 1
Type 1
Snap 1
Metric 10
Texel 8
Rotation 15
BspRebuild 1
TexturedView 1
Zoom 0.681250
PitchRollYaw 3.141433 0.000000 0.000000
'''
		message += "CamPos %.6f %.6f %.6f" % (offset[0], offset[1], offset[2])
		message +='''
TopView 1
Zoom 1.543750
PitchRollYaw 3.141593 0.000000 0.000000
CamPos 0.000000 0.000000 0.000000
FrontView 1
Zoom 0.975000
PitchRollYaw 3.141593 0.000000 0.000000
CamPos 0.000000 0.000000 0.000000
SideView 1
Zoom 1.543750
PitchRollYaw 3.141593 0.000000 0.000000
CamPos 0.000000 0.000000 0.000000
ArchTemplate
NumSlits 3
Thickness 150.000000
Width 100.000000
Radius 200.000000
WallSize 16.000000
Style 1
EndAngle 180.000000
StartAngle 0.000000
TCut 0
Sides 3
CW 0
Shape 0
Radius2 64.000000
Height 0.000000
Massive 0
Steps 0
BoxTemplate
Solid 1
TCut 0
TSheet 0
Thickness 16.000000
XSizeBot 1024.000000
XSizeTop 1024.000000
YSize 512.000000
ZSizeBot 1024.000000
ZSizeTop 1024.000000
ConeTemplate
Style 1
Width 200.000000
Height 300.000000
VerticalStrips 8
Thickness 16.000000
TCut 0
CylinderTemplate
BotXOffset 0.000000
BotXSize 128.000000
BotZOffset 0.000000
BotZSize 128.000000
Solid 1
Thickness 16.000000
TopXOffset 0.000000
TopXSize 128.000000
TopZOffset 0.000000
TopZSize 128.000000
VerticalStripes 8
YSize 512.000000
RingLength 3.000000
TCut 0
SpheroidTemplate
HorizontalBands 4
VerticalBands 8
YSize 256.000000
Solid 1
Thickness 16.000000
TCut 0
StaircaseTemplate
Height 128.000000
Length 128.000000
NumberOfStairs 8
Width 64.000000
MakeRamp 0
TCut 0
TemplatePos 0.000000 0.000000 0.000000
DrawScale 1.000000
LightmapScale 2.000000
'''
		self.file.write(message)

class OriginGenerator:

	def __init__(self,inputs):
		if(len(inputs)!=5):
			print 'incorrect list len'
			sys.exit()
		else:
			self.count = inputs[0]
			self.k = inputs[1:]
			self.originList = []

	def calOrigin(self,t,offset):
		x = self.k[0] * math.exp(-0.05*self.k[1]*t) * math.sin(self.k[2]*t)
		y = self.k[0] * math.exp(-0.05*self.k[1]*t) * math.cos(self.k[2]*t)
		z = t*self.k[3]
		return [int(x)+offset[0],int(z)+offset[1],int(y)+offset[2]]

	def setPoints(self,offset=[0,0,0]):
		for i in range(0,self.count):
			self.originList.append(self.calOrigin(i,offset))
			print self.calOrigin(i,offset)
		# print self.originList

	def getPoints(self):
		return self.originList

def main():
	sc = Scanner()
	sc.scan()
	og = OriginGenerator(sc.getInputs())
	offset = [0,0,0]
	og.setPoints(offset);
	printer = Printer()
	printer.createWorldFile("dummy.txt");
	printer.writeWorldFile(og.getPoints(),offset);
	printer.closeWorldFile();


if __name__ == "__main__":
    main()