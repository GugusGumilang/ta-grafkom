from ursina import *
from ursina.prefabs.platformer_controller_2d import PlatformerController2d
from ursina import Ursina


game = Ursina()


# Membuat entitas pemain
class Player(Entity):

    def update(self):
        self.direction = Vec3(
            self.up * (held_keys['w'] - held_keys['s'])
            + self.right * (held_keys['d'] - held_keys['a'])
            ).normalized()  # get the direction we're trying to walk in.

        origin = self.world_position + (self.up*.5) # the ray should start slightly up from the ground so we can walk up slopes or walk over small objects.
        hit_info = raycast(origin , self.direction, ignore=(self,), distance=.5, debug=False)
        if not hit_info.hit:
            self.position += self.direction * 2 * time.dt

               

player = Player(model='quad', origin_y=-.5,texture='diam.png', z=-3, scale=(.8,.8))

def update():
    if held_keys['a']:
        player.texture = 'kiri_kakikiri.png'
    elif held_keys['d']:
        player.texture = 'kanan_kakikanan.png'
    elif held_keys['w']:
        player.texture = 'atas_kakikiri.png'
    elif held_keys['s']:
        player.texture = 'bawah_kakikiri.png'
    elif held_keys[None]:
        player.texture='diam.png' 
        
batas_atasgoa = Entity(model='quad', collider='box', scale=(6,0.5), origin_y=-.5, color=color.rgb(0, 0, 255, 0),y=-.8, x=-4, z=-3)
batas = duplicate(batas_atasgoa, y= -1.2,color=color.rgb(0, 0, 1, 0))
batas = duplicate(batas_atasgoa, x=-1,y= -2.5, scale=(0.2,2))
batas = duplicate(batas_atasgoa, x=0,y= -2.4, scale=(2,.2))
batas = duplicate(batas_atasgoa, y= -1.7, scale_x=2, x=-6)
batas = duplicate(batas_atasgoa, y= -3.7, scale_x=13.5)
batas = duplicate(batas_atasgoa,x=-0.2, y= -1.5, scale_x=1.5)
batas = duplicate(batas_atasgoa,x=1, y= -2, scale_x=1.5)
batas = duplicate(batas_atasgoa,x=1.6, y= -2.5, scale=(.5,2.2))
batas = duplicate(batas_atasgoa,x=3, y= -3.5, scale=(.5,1.2))
batas = duplicate(batas_atasgoa,x=4.6, y= -2.8, scale=(3.4,.2))
batas = duplicate(batas_atasgoa,x=3.3, y= 1, scale=(1,.2))
batas = duplicate(batas_atasgoa,x=2, y= 1, scale=(4,.2))
batas = duplicate(batas_atasgoa,x=-1, y= .8, scale=(3.5,.2))
batas = duplicate(batas_atasgoa,x=-3, y= 1, scale=(1,.2))
batas = duplicate(batas_atasgoa,x=-3.5, y= 1, scale=(.2,2))
batas = duplicate(batas_atasgoa,x=-4, y= 2, scale=(2,.2),rotation=(0,0,-45))
batas = duplicate(batas_atasgoa,x=-5, y= 1.2, scale=(1,.2))
batas = duplicate(batas_atasgoa,x=-6.3, y= -3, scale=(.2,6))
batas = duplicate(batas_atasgoa,x=6, y= -3, scale=(.2,2))
batas = duplicate(batas_atasgoa,x=-6, y= 2, scale=(2,.2),rotation=(0,0,45))
batas = duplicate(batas_atasgoa,x=0.5, y= -0.4, scale=(2,.2))
batas = duplicate(batas_atasgoa,x=4.8, y= -1.2, scale=(2.9,.2))
batas = duplicate(batas_atasgoa,x=3.3, y= -1, scale=(.2,2))
batas = duplicate(batas_atasgoa,x=-0.4, y= -1.7, scale=(0.5,1.6))



#bagian tengah
rumput=Entity(model='quad', texture='rumput.png', scale=(1,1),z=-1.1,x=-2.5,y=2.7)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1.1,x=-2.5,y=3.5)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1,x=-3.3,y=3.5)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1,x=-3.3,y=2.5)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.2,2),x=-3.1,y=2.2,z=-3)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1,x=-3.3,y=3)
tebing=Entity(model='quad', texture='tebing_atas.png', scale=(1,1),z=-2,x=-3.3,y=1.5)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1,x=-4,y=2)
rumput=Entity(model='quad', texture='rumput.png', scale=(1.5,1),x=-3,y=1,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-3,y=0.2,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-2,y=1.2,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-2,y=0.2,z=-1)
rumah=Entity(model='quad', texture='rumah.png',scale=(2,2),x=-2,y=1.8,z=-2.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.8,1),x=-1,y=1.23,z=0)
bunga=Entity(model='quad', texture='bunga1.png',scale=(1.2,.8),x=-.61,y=1.2,z=-1.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.2,1),x=-.61,y=2,z=-1)
tebing=Entity(model='quad', texture='tebing_atas.png', scale=(1,1),z=-1,x=-1,y=2.3)
tebing=Entity(model='quad', texture='tebing_atas.png', scale=(1,1),z=-1.1,x=-.3,y=2.2)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-1,y=0.2,z=-1)
tangga3=Entity(model='quad', texture='tangga3.JPEG',scale=(.3,1),x=-.15,y=.2,z=-1.3)
tangga2=Entity(model='quad', texture='tangga_tengah.png',scale=(.3,1),x=.1,y=.1,z=-1.2)
tangga1=Entity(model='quad', texture='tangga1.JPEG',scale=(.3,1),x=.4,z=-1)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),x=1,y=0,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.2,2),x=1,y=1,z=-2)
tanah=Entity(model='quad', texture='tanah.png', scale=(1,1),z=-1,x=2)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=-1,x=1,y=2)
rumput=Entity(model='quad', texture='rumput.png', scale=(1.5,1),x=0.6,y=1.6,z=-1)
batu=Entity(model='quad', texture='batu.png', scale=(.5,.5),x=0.28,y=2.2,z=-1.11)
sudut=Entity(model='quad', texture='tebing_kekanan2.png', scale=(1,1.3),z=-1,x=.4,y=1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(1,1.3),z=-1,x=1.5,y=1.1)
sudut=Entity(model='quad', texture='sudut_kiri_atas.png', scale=(1,1.3),z=-1,x=1.5,y=2.1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(1,1.3),z=-1,x=2.5,y=1.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),z=-1,x=2.3,y=2)
tanah=Entity(model='quad', texture='tanah.png', scale=(1.5,1.1),x=3,y=0.32,z=-0.1)
tebing=Entity(model='quad', texture='sudut_kanan_atas.png',scale=(1,1),z=-1,x=2.8,y=2.4)
tebing=Entity(model='quad', texture='sudut_kanan_atas.png',scale=(1,1),z=-0.8,x=2.4,y=2.4)
tebing=Entity(model='quad', texture='tebing_kanan.png',scale=(0.5,1.5),z=-0.8,x=3.2,y=1.6)
goa=Entity(model='quad', texture='goa.png', scale=(2,2),x=-5,y=-1.3,z=-1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(2,1.8),x=-7,y=-1.8,z=-1)
rumput=Entity(model='quad', texture='rumput.png', scale=(1.5,1),x=-6.4,y=-0.45,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.25,2.5),x=-2,y=-2.2,z=-4)

#bagian kiri
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4,y=0.2,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-5,y=0.2,z=-1)
sudut=Entity(model='quad', texture='tebing_atas.png',scale=(1.5,1),x=-5.8,y=.8,z=-1.3)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4.2,y=1,z=-1)
sudut=Entity(model='quad', texture='sudut_kiri_atas.png',scale=(1.5,1),x=-4.5,y=1.3,z=-1.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-6.3,y=0.2,z=-1.1)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png',scale=(1.5,1.5),x=-6.5,y=1.6,z=-1.4)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-6.5,y=.8,z=-1.3)
sudut=Entity(model='quad', texture='tebing_kekanan1.png',scale=(1,1.3),x=-6.5,y=2.3,z=-1.3)
sudut=Entity(model='quad', texture='tebing_kekanan2.png',scale=(1,1.3),x=-5.5,y=2.8,z=-1.3)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-5.5,y=1.7,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.2,2),x=-5.5,y=1.7,z=-2)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-6.2,y=3.5,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.2,2),x=-6.2,y=3.9,z=-2)
tanah=Entity(model='quad', texture='tanah.png', scale=(1.5,1),x=-6.2,y=4,z=-1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png',scale=(1,1.3),x=-4.5,y=2.8,z=-1.3)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4.5,y=2,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4.9,y=3.9,z=-1)
sudut=Entity(model='quad', texture='tebing_kekanan2.png',scale=(1.6,1.3),x=-3.9,y=3.3,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-6.5,y=-3.3,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-5.5,y=-3.1,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-5.5,y=-4.1,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4.5,y=-4,z=-1)
bunga=Entity(model='quad', texture='bunga1.png',scale=(1,0.8),x=-5.5,y=-2.2,z=-1.1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-4.5,y=-3,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-4.5,y=-2.8,z=0)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-3.5,y=-3.1,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-3.5,y=-4,z=-1)

tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-2.5,y=-3.1,z=-1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(2,1.8),x=-3.1,y=-1.15,z=-1.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-3.3,y=-2,z=-1)
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(2,1.8),x=-1.9,y=-1.15,z=-1.1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.3,2.5),x=-0.6,y=-1,z=-4)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-1.5,y=-3.3,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-1.5,y=-2.3,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=-0.5,y=-3.3,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-0.5,y=-2.2,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-0.5,y=-1.5,z=-1)
bunga=Entity(model='quad', texture='bunga1.png',scale=(1,0.8),x=0.1,y=-0.6,z=-1.1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=1.5,y=-3.3,z=-1)
tanah=Entity(model='quad', texture='tanah.png',scale=(1.1,1.2),x=0.7,y=-2.2,z=-1)
tanah=Entity(model='quad', texture='tanah.png',scale=(1.1,1.9),x=0.7,y=-1.4,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=.5,y=-3.3,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=3.7,y=-3.4,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=5,y=-3.4,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1,2),x=.7,y=-1,z=-4.1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=1.7,y=-1.9,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=1.4,y=-2.2,z=-1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.3,2.6),x=1.4,y=-1,z=-4.2)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=2.6,y=-3.3,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=2.7,y=-2.3,z=-1)
tanah=Entity(model='quad', texture='tanah_petak.png',scale=(1.1,1.2),x=2.7,y=-1.3,z=-1)
tanah=Entity(model='quad', texture='tanah.png',scale=(1.1,1.2),x=2.7,y=-0.8,z=-1)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=0,x=1.2,y=3)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=0.6,y=2.3,z=-1) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=0.3,y=2.8,z=-1) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=0 ,y=3.1,z=-1) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-1.3 ,y=3.1,z=-1) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=-1.3 ,y=3.7,z=-1) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=0 ,y=3.7,z=-1) 
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=0,x=.7,y=3.8)
air=Entity(model='quad', texture='air.png', scale=(1,1),z=1,x=1.3,y=3.8)
air=Entity(model='quad', texture='air.png', scale=(1,1),z=1,x=2.2,y=3.8)
air=Entity(model='quad', texture='air.png', scale=(1,1),z=1,x=4.5,y=2)


#bagian kanan

rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=5.1,y=-2.4,z=-2)           #pohon paling bawah kanan
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=4.3,y=-2.3,z=-2)           #pohon paling bawah kanan
pohon=Entity(model='quad', texture='pohon.png', scale=(1.3,2.5),x=5,y=-2.2,z=-4.1)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.3,2.5),x=4,y=-1.8,z=-4)
pohon=Entity(model='quad', texture='pohon.png', scale=(1.5,2.7),x=3.1,y=-2,z=-4.1)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.JPEG',scale=(1,1),x=6.5,y=1.3,z=-1.1)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.JPEG',scale=(1,1),x=6,y=1.7,z=-1)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.png',scale=(1,1),x=4.1,y=2.6,z=-1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=4,y=2,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=4.6,y=1.3,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=4,y=2.5,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=3.2,y=2.9,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=2.7,y=3.4,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=1.7,y=3.3,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=2,y=4,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=4.4,y=2.5,z=1)
air=Entity(model='quad', texture='air.png',scale=(1,1),x=3.6,y=1.5,z=1)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.png',scale=(1,1),x=3.2,y=3.2,z=-1)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.png',scale=(1,1),x=2.8,y=3.6,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=4.7,y=3.2,z=0) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=4.3,y=3.7,z=0) 
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=3.8,y=3.7,z=0) 
sudut=Entity(model='quad', texture='tebing_bawah_tengah.png', scale=(1,1),x=6.5,y=2.2,z=-1.1)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=-1,x=3.7,y=.8)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=-1,x=4.3,y=.3)
sudut=Entity(model='quad', texture='sudut_kanan_atas.png', scale=(1,1),z=-1,x=5.2,y=-0.5)
sudut=Entity(model='quad', texture='tebing_atas.png', scale=(1,0.6),z=-1,x=6.1,y=-0.9)
sudut=Entity(model='quad', texture='tebing_atas.png', scale=(1,0.6),z=-1,x=7.1,y=-0.9)
pohon=Entity(model='quad', texture='pohon.png',scale=(1.2,2.5),x=3.3,y=0,z=-4)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=3.8,y=-.7,z=0)    
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=4.7,y=-.7,z=0)    
tanah=Entity(model='quad', texture='tanah.png',scale=(1.5,1),x=4.1,y=-1,z=0)    
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=5,y=-1,z=0)  
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6,y=-1.4,z=0)  
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6.8,y=-1.4,z=0)  
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6.8,y=-2,z=0)  
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6.8,y=-2.9,z=0)  
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6.8,y=-3.3,z=0)  
bunga=Entity(model='quad', texture='bunga1.png',scale=(1.5,1),x=6.8,y=-3.6,z=0)  
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=6.8,y=-0.4,z=1)  
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=5.8,y=-0.4,z=1)  
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=5.8,y=0.5,z=1)  
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=5.9,y=1,z=1)  
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=6.8,y=0.5,z=1)  
sudut=Entity(model='quad', texture='tebing_kiri.png',scale=(0.4,1.2),x=5.5,y=2.5,z=-2)
pohon=Entity(model='quad', texture='pohon.png',scale=(1.5,2.5),x=6.1,y=3.8,z=-2)
pohon=Entity(model='quad', texture='pohon.png',scale=(1.5,2.5),x=6.1,y=3.8,z=-2)
sudut=Entity(model='quad', texture='pantai_bawah_kiri.png',scale=(1,1),x=5,y=2.1,z=-1)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=6,y=2.8,z=0)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=5.7,y=3.2,z=0)
rumput=Entity(model='quad', texture='rumput.png',scale=(1.5,1),x=5.7,y=3.8,z=0)
tebing=Entity(model='quad', texture='tebing_atas.png', scale=(1,.8),z=-1,x=6.8,y=3)
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=5.5,y=1.7,z=1) 
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=7,y=.6,z=1) 
air=Entity(model='quad', texture='air.png',scale=(1.5,1),x=7,y=-.2,z=1) 



game.run()