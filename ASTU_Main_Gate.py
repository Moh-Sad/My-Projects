
#GROUP 1
#GROUP MEMBERS
# 1 Hussein Beshir -----UGR/30697/15
# 2 Mohammed Sadik -----UGR/30960/15
# 3 Hanif Esmail  ------UGR/30629/15
# 4 Bikila Denino ------UGR/30306/15
# 5 Efrata Anteneh -----UGR/30439/15
# 6 Yamrout Kifle-------UGR/31360/15


from cs1graphics import *
import time
p=Point
dooor=Layer()
c=Canvas(1300,800)
c.setTitle("ASTU View From The Main Gate")
c.setBackgroundColor("darkgreen")

r=Rectangle(1300,427,Point(650,525))
r.setFillColor("darkgreen")
c.add(r)

#road

road=Rectangle(450,540)
road.moveTo(600,500)
road.setFillColor("black")
c.add(road)

road2=Rectangle(10000,180,p(0,220))
road2.setFillColor("black")

c.add(road2)


#door

doorb=Ellipse(700,450,p(600,600))
doorb.setBorderColor("white")
doorb.setFillColor("blue")
doorb.setBorderWidth(5)
dooor.add(doorb)

doora=Ellipse(600,450,p(600,600))
doora.setBorderColor("white")
doora.setFillColor("white")
doora.setBorderWidth(5)
dooor.add(doora)

doorh=Ellipse(800,400,p(600,730))
doorh.setFillColor("black")
doorh.setBorderColor('darkorange')
dooor.add(doorh)

door1=Ellipse(100,200,p(400,600))
door1.setFillColor("black")
dooor.add(door1)

door2=Ellipse(100,200,p(800,600))
door2.setFillColor("black")
door2.rotate(-10)
dooor.add(door2)

door3=Ellipse(130,300,p(523,600))
door3.setFillColor("black")
dooor.add(door3)

door4=Ellipse(130,300,p(676,600))
door4.setFillColor("black")
dooor.add(door4)


doora=Ellipse(600,450,p(600,600))
doora.setBorderColor("white")
doora.setBorderWidth(5)
dooor.add(doora)

doorcut=Ellipse(800,400,p(600,730))
doorcut.setFillColor("black")
dooor.add(doorcut)
dooor.setDepth(-5)

# ASTU

m=Text("A")
m.setFontColor("blue")
m.scale(3)
m.moveTo(440,460)
dooor.add(m)

m2=Text("S")
m2.setFontColor("blue")
m2.setDepth(-100)
m2.scale(3)
m2.moveTo(540,425)
c.add(m2)

m3=Text("T")
m3.setFontColor("blue")
m3.scale(3)
m3.moveTo(640,425)
dooor.add(m3)

m4=Text("U")
m4.setFontColor("blue")
m4.scale(3)
m4.moveTo(740,440)
dooor.add(m4)

##LOGO

ca=Layer()

dd=Circle(415, Point(450,450))
dd.setFillColor("brown")
ca.add(dd)

cc=Circle(370, Point(450,450))
cc.setFillColor("white")
ca.add(cc)

h=Circle(90, Point(450,240))
h.setFillColor("darkgreen")
ca.add(h)
h=Circle(90, Point(305,295))
h.setFillColor("darkgreen")
ca.add(h)
h=Circle(90, Point(595,295))
h.setFillColor("darkgreen")
ca.add(h)
h=Circle(90, Point(245,435))
h.setFillColor("darkgreen")
ca.add(h)
h=Circle(90, Point(655,435))
h.setFillColor("darkgreen")
ca.add(h)

bb=Circle(245, Point(450,450))
bb.setFillColor("white")
ca.add(bb)

aa=Circle(195, Point(450,450))
aa.setFillColor("darkgreen")
ca.add(aa)

one=Ellipse(80,360, Point(450,450))
one.setBorderColor("white")
ca.add(one)

two=Ellipse(80,360, Point(450,450))
two.setBorderColor("white")
two.rotate(45)
ca.add(two)

three=Ellipse(80,360, Point(450,450))
three.setBorderColor("white")
three.rotate(135)
ca.add(three)

four=Ellipse(80,360, Point(450,450))
four.setBorderColor("white")
four.rotate(90)
ca.add(four)

center=Circle(20, Point(450,450))
center.setFillColor("white")
center.setBorderColor("white")
ca.add(center)

bottomline=Path(Point(83,500), Point(817,500))
bottomline.setBorderWidth(5)
bottomline.setBorderColor('darkblue')
ca.add(bottomline)

cutter=Polygon(Point(817,500),Point(83,500),Point(150,658),Point(450,820),Point(750,658))
cutter.setFillColor("blue")
cutter.setBorderColor("blue")
ca.add(cutter)

dooor.add(ca)
ca.scale(0.075)
ca.move(560,400)
c.add(dooor)
# OutFront

green1=Polygon (p(0,600), p(300,600), p(380,800), p(0,800))
green1.setFillColor("black")
c.add(green1)

green2=Polygon (p(900,600), p(1300,600), p(1380,800), p(1000,800))
green2.setFillColor("black")
c.add(green2)
green3=Polygon (p(0,700), p(340,700), p(450,800), p(0,800))
green3.setFillColor("black")
c.add(green3)

green4=Polygon (p(870,700), p(1300,700), p(1380,800), p(1000,800))
green4.setFillColor("black")
c.add(green4)
hide1=Rectangle(50,30)
hide1.setDepth(-10)
hide1.moveTo(270,618)
hide1.setFillColor("black")
c.add(hide1)
hide2=Rectangle(50,30)
hide2.setDepth(-10)
hide2.moveTo(930,618)
hide2.setFillColor("black")
c.add(hide2)


#fence
above=Path(Point(0,540),Point(40,540))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(70,540),Point(120,540))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(150,540),Point(200,540))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(220,540),Point(260,540))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)

above=Path(Point(0,525),Point(40,525))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(70,525),Point(120,525))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(150,525),Point(200,525))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)
above=Path(Point(220,525),Point(260,525))
above.setBorderWidth(2)
above.setBorderColor('black')
c.add(above)

mid=Rectangle(25,50, Point(55,530))
mid.setBorderWidth(5)
mid.setBorderColor('grey')
c.add(mid)
mid=Rectangle(25,50, Point(135,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
c.add(mid)
mid=Rectangle(25,50, Point(210,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
c.add(mid)


fence=Polygon (p(0,550),p(310,550),p(300,600),p(0,600))
fence.setFillColor("brown")
fence.setDepth(46)
fence.setBorderWidth(4)
fence.setBorderColor("gray")
c.add(fence)


fence2=Layer()

above=Path(Point(-10,540),Point(40,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(70,540),Point(120,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(150,540),Point(200,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(220,540),Point(260,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(290,540),Point(340,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(360,540),Point(420,540))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)

above=Path(Point(-15,525),Point(40,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(70,525),Point(120,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(150,525),Point(200,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(220,525),Point(260,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(290,525),Point(340,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)
above=Path(Point(360,525),Point(420,525))
above.setBorderWidth(2)
above.setBorderColor('black')
fence2.add(above)



mid=Rectangle(25,50, Point(55,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
fence2.add(mid)
mid=Rectangle(25,50, Point(135,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
fence2.add(mid)
mid=Rectangle(25,50, Point(210,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
fence2.add(mid)
mid=Rectangle(25,50, Point(275,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
fence2.add(mid)
mid=Rectangle(25,50, Point(350,530))
mid.setBorderWidth(5)
mid.setBorderColor('gray')
fence2.add(mid)

c.add(fence2)
fence2.move(900,0)


fen=Polygon (p(895,550),p(1300,550),p(1300,600),p(905,600))
fen.setFillColor("brown")
fen.setDepth(46)
c.add(fen)


##horizontal road


roadline=Layer()


l6=Path(p(600,245),p(700,245))
l6.setBorderColor("white")
l6.setBorderWidth(3)
roadline.add(l6)

per=l6.clone()
per.moveTo(395,380)
per.rotate(-90)
per.scale(0.5)
per.setBorderWidth(3)
roadline.add(per)
per1=per.clone()
per1.setDepth(-96)
per1.moveTo(595,600)
c.add(per1)



l7=l6.clone()
l7.moveTo(780,245)
roadline.add(l7)

rr1=l6.clone()
rr1.moveTo(400,245)
roadline.add(rr1)

rr2=l6.clone()
rr2.moveTo(200,245)
roadline.add(rr2)

rr3=l6.clone()
rr3.moveTo(20,245)
roadline.add(rr3)

rr4=l6.clone()
rr4.moveTo(-180,245)
roadline.add(rr4)



l8=l6.clone()
l8.moveTo(950,245)
roadline.add(l8)

l9=l6.clone()
l9.moveTo(1120,245)
roadline.add(l9)
roadline.setDepth(-93)
roadline.moveTo(200,-20)
c.add(roadline)


roadline2=roadline.clone()
roadline2.moveTo(200,420)
roadline2.setDepth(-10)
c.add(roadline2)




#lighpole

lightpole = Layer()


lig3 = Layer()
bul3 = Circle(25, Point(100, 80))
bul3.setFillColor("yellow")
lig3.add(bul3)
re3 = Rectangle(15, 100, Point(100, 150))
re3.setFillColor("brown")
lig3.add(re3)

lig3.moveTo(640, 668)
lightpole.add(lig3)
lightpole.scale(0.5)
c.add(lightpole)

lightpole1 = Layer()


lig1 = Layer()
bul1 = Circle(25, Point(100, 80))
bul1.setFillColor("yellow")
lig1.add(bul1)
re1 = Rectangle(15, 100, Point(100, 150))
re1.setFillColor("brown")
lig1.add(re1)

lig1.moveTo(640, 430)
lightpole1.add(lig1)
lightpole1.scale(0.5)
c.add(lightpole1)

lightpole2= Layer()


lig2 = Layer()
bul2 = Circle(25, Point(100, 80))
bul2.setFillColor("yellow")
lig2.add(bul1)
re2 = Rectangle(15, 100, Point(100, 150))
re2.setFillColor("brown")
lig2.add(re2)

lig2.moveTo(300,427)
lightpole2.add(lig2)
lightpole2.scale(0.5)
c.add(lightpole2)

lightpole3= Layer()


lig3 = Layer()
bul3 = Circle(25, Point(100, 80))
bul3.setFillColor("yellow")
lig3.add(bul3)
re3 = Rectangle(15, 100, Point(100, 150))
re3.setFillColor("brown")
lig3.add(re3)

lig3.moveTo(20, 427)
lightpole3.add(lig3)
lightpole3.scale(0.5)
c.add(lightpole3)

lightpolea= Layer()


liga = Layer()
bula= Circle(25, Point(100, 80))
bula.setFillColor("yellow")
liga.add(bula)
rea = Rectangle(15, 100, Point(100, 150))
rea.setFillColor("brown")
liga.add(rea)

liga.moveTo(1560, 427)
lightpolea.add(liga)
lightpolea.scale(0.5)
c.add(lightpolea)




lightpoleb = Layer()


ligb= Layer()
bulb = Circle(25, Point(100, 80))
bulb.setFillColor("yellow")
ligb.add(bulb)
reb = Rectangle(15, 100, Point(100, 150))
reb.setFillColor("brown")
ligb.add(reb)

ligb.moveTo(1560, 660)
lightpoleb.add(ligb)
lightpoleb.scale(0.5)
c.add(lightpoleb)


lightpolec = Layer()


ligc = Layer()
bulc = Circle(25, Point(100, 80))
bulc.setFillColor("yellow")
ligc.add(bulc)
rec = Rectangle(15, 100, Point(100, 150))
rec.setFillColor("brown")
ligc.add(rec)

ligc.moveTo(1900, 427)
lightpolec.add(ligc)
lightpolec.scale(0.5)
c.add(lightpolec)

lightpoled = Layer()


ligd = Layer()
buld = Circle(25, Point(100, 80))
buld.setFillColor("yellow")

ligd.add(buld)
red = Rectangle(15, 100, Point(100, 150))
red.setFillColor("brown")
ligd.add(red)

ligd.moveTo(2300, 427)
lightpoled.add(ligd)
lightpoled.scale(0.5)
c.add(lightpoled)

#Buildings

Building=Layer()
h=Polygon(Point(700,180) ,Point(700,0) ,Point(650,40) ,Point(650,160))
h.setBorderColor("black")
h.setFillColor(" dark grey")
h.setDepth(25)

h1=Polygon(Point(700,0) ,Point(740,20) ,Point(740,180) ,Point(700,180))
h1.setBorderColor("black")
h1.setFillColor("grey")
h1.setDepth(25)

h2=Polygon(Point(740,20) ,Point(860,20) ,Point(860,180) ,Point(740,180))
h2.setBorderColor("grey")
h2.setFillColor("grey")
h2.setDepth(25)

h3=Polygon(Point(700,0) ,Point(820,0) ,Point(860,20) ,Point(740,20))
h3.setBorderColor("yellow")
h3.setFillColor("darkred")
h3.setDepth(25)
##window
h4=Rectangle(25,35,p(760,50))
h4.setBorderColor("yellow")
h4.setFillColor("brown")
h4.setDepth(25)


h5=h4.clone()
h5.moveTo(800,50)

h6=h4.clone()
h6.moveTo(840,50)

h7=h4.clone()
h7.moveTo(800,100)

h8=h4.clone()
h8.moveTo(840,100)

h9=h4.clone()
h9.moveTo(760,100)

h10=h4.clone()
h10.moveTo(760,150)

h11=h4.clone()
h11.moveTo(800,150)

h12=h4.clone()
h12.moveTo(840,150)





Building.add(h)
Building.add(h1)
Building.add(h2)
Building.add(h3)
Building.add(h4)
Building.add(h5)
Building.add(h6)
Building.add(h7)
Building.add(h8)
Building.add(h9)
Building.add(h10)
Building.add(h11)
Building.add(h12)
Building.setDepth(25)
Building.moveTo(-140,-55)
c.add(Building)

Building2=Building.clone()
Building2.moveTo(450,-50)
c.add(Building2)

Building3=Building.clone()
Building3.moveTo(150,-50)
c.add(Building3)
Building4=Building.clone()
Building4.moveTo(-700 ,-50)
c.add(Building4)
Building5=Building.clone()
Building5.moveTo(-400,-55)
c.add(Building5)
#TREE

Tree=Layer()

tree=Polygon(Point(250,275),Point(210,375),Point(290,375))
tree.setFillColor("green")
bark=Rectangle(10,30,Point(250,390))
bark.setFillColor("darkgoldenrod")

Tree.setDepth(-95)
Tree.add(tree)
Tree.add(bark)
Tree.moveTo(650,50)

c.add(Tree)
Tree2=Tree.clone()
Tree2.moveTo(930,80)
c.add(Tree2)
Tree3=Tree.clone()
Tree3.moveTo(800,80)
c.add(Tree3)
Tree4=Tree.clone()
Tree4.moveTo(1000,-10)
c.add(Tree4)


#car


car=Layer()

body=Rectangle(60,100)
body.setFillColor('white')
body.moveTo(500,600)
body.setBorderColor("white")
car.add(body)

body1=Rectangle(55,50)
body1.setFillColor('white')
body1.setBorderColor("white")
body1.moveTo(500,525)
car.add(body1)

lite=Rectangle(10,10)
lite.setFillColor('white')
lite.setBorderColor("white")
lite.moveTo(480,500)
lite.setDepth(51)
car.add(lite)

lite1=lite.clone()
lite1.moveTo(520,500)
car.add(lite1)

car.scale(1.1)
car.setDepth(-90)
car.moveTo(-30,150)
c.add(car)




#car 2
husso=Layer()
c1=Rectangle(150,60)
c1.moveTo(250,250)
c1.setFillColor("blue")
husso.add(c1)
c2=Rectangle(200,36)
c2.setFillColor("red")
c2.moveTo(274,290)
husso.add(c2)
c3=Spline(Point(325,220),Point(375,275))
c3.setBorderWidth(1.3)
c3.setBorderColor("blue")
husso.add(c3)
ci=Circle(10)
ci.setFillColor("white")
ci.moveTo(205,310)
husso.add(ci)
cl=ci.clone()
cl.moveTo(320,310)
husso.add(cl)
husso.moveTo(-400,-90)
husso.setDepth(-90)
c.add(husso)

#man
people=Layer()

man3=Layer()
ment=Ellipse(26,20,Point(460,465))
ment.setFillColor("chocolate")
man3.add(ment)

men20=Rectangle(20,30,Point(460,496))
men20.setFillColor("yellow")
man3.add(men20)

men3=Path(Point(455,515),Point(455,535))
men3.setBorderWidth(5)
men3.setBorderColor("white")
man3.add(men3)

men4=Path(Point(465,515),Point(465,535))
men4.setBorderWidth(5)
men4.setBorderColor("white")
man3.add(men4)

men5=Path(Point(445,485),Point(440,495),Point(445,505))
men5.setBorderWidth(3)
man3.add(men5)

men6=Path(Point(475,485),Point(480,495),Point(475,505))
men6.setBorderWidth(3)
man3.add(men6)
man3.moveTo(0,-250)
people.add(man3)

man15=man3.clone()
man15.moveTo(-100,-250)
men20.setFillColor("red")
people.add(man15)

man16=man3.clone()
man16.moveTo(-150,-250)
men20.setFillColor("blue")
people.add(man16)
people.scale(0.4)
people.moveTo(380,100)
people.setDepth(-50)


# motor
all = Layer()
motor = Layer()

tire1 = Layer()

c1 = Circle(20)
c1.setFillColor("black")
c1.setBorderColor("white")
c1.setBorderWidth(4)
c1.setDepth(60)
tire1.add(c1)

c2 = Circle(5)
c2.setFillColor("darkgrey")
tire1.add(c2)

tire1.moveTo(250, 250)

r1 = Rectangle(43, 3)
r1.setFillColor("darkgrey")
tire1.add(r1)

r2 = Rectangle(3, 43)
r2.setFillColor("darkgrey")
tire1.add(r2)

motor.add(tire1)

tire2 = Layer()

c3 = Circle(20)
c3.setFillColor("black")
c3.setBorderColor("white")
c3.setBorderWidth(4)
c3.setDepth(60)
tire2.add(c3)

c4 = Circle(5)
c4.setFillColor("darkgrey")
tire2.add(c4)

tire2.moveTo(350, 250)

r2 = Rectangle(43, 3)
r2.setFillColor("darkgrey")
tire2.add(r2)

r2 = Rectangle(3, 43)
r2.setFillColor("darkgrey")
tire2.add(r2)

motor.add(tire2)

body1 = Layer()
r3 = Rectangle(80, 10)
r3.setFillColor("orange")
r3.setBorderColor("black")
r3.rotate(-30)
r3.moveTo(280, 230)
body1.add(r3)

motor.add(body1)

body2 = Layer()
r4 = Rectangle(70, 10)
r4.setFillColor("purple")
r4.setBorderColor("black")
r4.rotate(50)
r4.setDepth(60)
r4.moveTo(330, 222)
body2.add(r4)

motor.add(body2)

body3 = Layer()
r5 = Rectangle(110, 15)
r5.setFillColor("red")
r5.setBorderColor("black")
r5.moveTo(300, 250)
body3.add(r5)

motor.add(body3)

body4 = Layer()
r6 = Rectangle(25, 5)
r6.setFillColor("orange")
r6.setBorderColor("black")
r6.rotate(45)
r6.moveTo(275, 215)
body4.add(r6)
body4.setDepth(70)

motor.add(body4)

sit = Layer()
t1 = Polygon()
t1.addPoint(Point(40, 30))
t1.addPoint(Point(40, 40))
t1.addPoint(Point(50, 35))
t1.setFillColor("gray")
t1.setBorderColor("black")
t1.scale(2)
t1.rotate(-15)
t1.moveTo(260, 200)
sit.add(t1)
motor.add(sit)

body5 = Layer()
r7 = Rectangle(8, 20)
r7.setFillColor("black")
r7.setBorderColor("white")
r7.moveTo(308, 190)
body5.add(r7)
body5.setDepth(100)

motor.add(body5)

body6 = Layer()
r8 = Rectangle(20, 8)
r8.setFillColor("black")
r8.setBorderColor("white")
r8.rotate(-30)
r8.moveTo(308, 180)
body6.add(r8)

motor.add(body6)

body7 = Layer()
t1 = Polygon()
t1.addPoint(Point(10, 40))
t1.addPoint(Point(40, 15))
t1.addPoint(Point(50, 40))
t1.setFillColor("light green")
t1.setBorderColor("black")
t1.scale(2)
t1.rotate(5)
t1.moveTo(260, 249)
body7.add(t1)
body7.setDepth(60)

motor.add(body7)

body8 = Layer()
r9 = Rectangle(8, 15)
r9.setFillColor("gray")
r9.setBorderColor("white")
r9.moveTo(280, 258)
body8.add(r9)
body8.setDepth(60)

motor.add(body8)

body9 = Layer()
r10 = Rectangle(40, 10)
r10.setFillColor("gray")
r10.setBorderColor("white")
r10.moveTo(266, 268)
body9.add(r10)

motor.add(body9)

# biker

biker = Layer()

abdomin = Ellipse(20, 45)
abdomin.setFillColor("white")
abdomin.moveTo(270, 190)
biker.add(abdomin)

head1 = Circle(10)
head1.setFillColor("white")
head1.moveTo(270, 155)
biker.add(head1)

hand1 = Rectangle(23, 5)
hand1.setFillColor("white")
hand1.moveTo(290, 190)
hand1.rotate(-14)
biker.add(hand1)

hand2 = Rectangle(45, 5)
hand2.setFillColor("white")
hand2.moveTo(290, 178)
hand2.rotate(-10)
biker.add(hand2)

leg1 = Rectangle(5, 40)
leg1.setFillColor("white")
leg1.moveTo(280, 225)
leg1.rotate(-30)
biker.add(leg1)

smoke = Layer()

e1 = Ellipse(40, 8)
e1.setFillColor("gray")
e1.setBorderColor("gray")
e1.moveTo(220, 270)
smoke.add(e1)

e2 = Ellipse(40, 8)
e2.setFillColor("gray")
e2.moveTo(220, 270)
e2.rotate(45)
e2.setDepth(90)
e2.setBorderColor("gray")
smoke.add(e2)

e3 = Ellipse(40, 8)
e3.setFillColor("gray")
e3.moveTo(220, 270)
e3.rotate(-45)
e3.setDepth(90)
e3.setBorderColor("gray")
smoke.add(e3)

e4 = Ellipse(40, 8)
e4.setFillColor("gray")
e4.moveTo(220, 270)
e4.rotate(90)
e4.setDepth(90)
e4.setBorderColor("gray")
smoke.add(e4)
smoke.scale(0.5)
smoke.moveTo(120, 135)

smoke2 = smoke.clone()
smoke2.moveTo(20, 60)
smoke2.scale(1.5)

smoke3 = smoke.clone()
smoke3.moveTo(-100, -30)
smoke3.scale(2)

biker2 = Layer()

abdomin1 = Ellipse(20, 45)
abdomin1.setFillColor("white")
abdomin1.moveTo(300, 85)
biker2.add(abdomin1)

head2 = Circle(10)
head2.setFillColor("white")
head2.moveTo(300, 50)
biker2.add(head2)

hand3 = Rectangle(30, 5)
hand3.setFillColor("white")
hand3.moveTo(285, 85)
hand3.rotate(-60)
biker2.add(hand3)

hand4 = Rectangle(30, 5)
hand4.setFillColor("white")
hand4.moveTo(315, 85)
hand4.rotate(60)
biker2.add(hand4)

leg2 = Rectangle(5, 30)
leg2.setFillColor("white")
leg2.moveTo(295, 120)
biker2.add(leg2)

leg3 = Rectangle(5, 30)
leg3.setFillColor("white")
leg3.moveTo(305, 120)
biker2.add(leg3)

biker2.setDepth(40)
biker2.moveTo(-30, 330)

all.add(biker2)
all.add(motor)
all.setDepth(-10)
c.add(biker2)
biker2.moveTo(-340,530)
biker2.setDepth(40)
biker.setDepth(-10)
all.moveTo(-100,400)
c.add(all)
#cycle

all=Layer()
motor1=Layer()

tire11=Layer()

c1=Circle(20)
c1.setFillColor("white")
c1.setBorderColor("grey")
c1.setBorderWidth(4)
c1.setDepth(60)
tire11.add(c1)

c2=Circle(5)
c2.setFillColor("black")
tire11.add(c2)

tire11.moveTo(250,250)

r1=Rectangle(43,3)
r1.setFillColor("black")
tire11.add(r1)

r2=Rectangle(3,43)
r2.setFillColor("black")
tire11.add(r2)

motor1.add(tire11)

tire22=Layer()

c3=Circle(20)
c3.setFillColor("white")
c3.setBorderColor("grey")
c3.setBorderWidth(4)
c3.setDepth(60)
tire22.add(c3)

c4=Circle(5)
c4.setFillColor("black")
tire22.add(c4)

tire22.moveTo(350,250)

r2=Rectangle(43,3)
r2.setFillColor("black")
tire22.add(r2)

r2=Rectangle(3,43)
r2.setFillColor("black")
tire22.add(r2)

motor1.add(tire22)

body1=Layer()
r3=Rectangle(80,10)
r3.setFillColor("orange")
r3.setBorderColor("black")
r3.rotate(-30)
r3.moveTo(280,230)
body1.add(r3)

motor1.add(body1)

body2=Layer()
r4=Rectangle(70,10)
r4.setFillColor("pink")
r4.setBorderColor("black")
r4.rotate(50)
r4.setDepth(60)
r4.moveTo(330,222)
body2.add(r4)

motor1.add(body2)

body3=Layer()
r5=Rectangle(110,5)
r5.setFillColor("chocolate")
r5.setBorderColor("black")
r5.moveTo(300,250)
body3.add(r5)

motor1.add(body3)

body4=Layer()
r6=Rectangle(25,5)
r6.setFillColor("orange")
r6.setBorderColor("black")
r6.rotate(45)
r6.moveTo(275,215)
body4.add(r6)
body4.setDepth(70)

motor1.add(body4)

sit=Layer()
t1=Polygon()
t1.addPoint(Point(40,30))
t1.addPoint(Point(40,40))
t1.addPoint(Point(50,35))
t1.setFillColor("gray")
t1.setBorderColor("black")
t1.scale(2)
t1.rotate(-15)
t1.moveTo(260,200)
sit.add(t1)
motor1.add(sit)

body5=Layer()
r7=Rectangle(8,20)
r7.setFillColor("black")
r7.setBorderColor("white")
r7.moveTo(308,190)
body5.add(r7)
body5.setDepth(100)

motor1.add(body5)

body6=Layer()
r8=Rectangle(20,8)
r8.setFillColor("black")
r8.setBorderColor("white")
r8.rotate(-30)
r8.moveTo(308,180)
body6.add(r8)
motor1.add(body6)

body7=Layer()
k=tire1.clone()
k.scale(0.5)
body7.add(k)
motor1.add(body7)

body8=Layer()
o=tire1.clone()
body8.add(k)
body8.scale(1.5)
body8.moveTo(-80,-125)
motor1.add(body8)

body9=Layer()
u=Rectangle(35,3)
u.setFillColor("blue")
body9.add(u)
body9.setDepth(10)
body9.rotate(-15)
body9.moveTo(270,240)
motor1.add(body9)

body10=Layer()
u=Rectangle(35,3)
u.setFillColor("blue")
body10.add(u)
body10.setDepth(10)
body10.rotate(15)
body10.moveTo(270,260)
motor1.add(body10)

#biker

biker=Layer()

abdomin=Ellipse(20,45)
abdomin.setFillColor("white")
abdomin.moveTo(270,190)
biker.add(abdomin)



head1=Circle(10)
head1.setFillColor("white")
head1.moveTo(270,155)
biker.add(head1)

hand1=Rectangle(23,5)
hand1.setFillColor("white")
hand1.moveTo(290,190)
hand1.rotate(-14)
biker.add(hand1)

hand2=Rectangle(45,5)
hand2.setFillColor("white")
hand2.moveTo(290,178)
hand2.rotate(-10)
biker.add(hand2)

leg1=Rectangle(5,48)
leg1.setFillColor("white")
leg1.moveTo(280,225)
leg1.rotate(-30)
leg1.setDepth(5)
biker.add(leg1)

motor1.add(biker)
all.add(motor1)
all.moveTo(-350,-100)
all.setDepth(-99)
c.add(all)


for i in range(350):
    motor1.move(5,0)
    leg1.rotate(-5)
    tire11.rotate(19)
    tire22.rotate(19)
    leg1.rotate(5)
for i in range(1000):
    husso.move(1,0)
for i in range(555):
    car.move(0,-1)
c.add(people)
for i in range(300):
    people.move(1,0)
for i in range(15):
    people.move(0,-1)
for i in range(69):
    people.move(1,0)
for i in range(550):
    husso.move(1,0)
    people.move(1,0)

#movement2
for i in range(220):
    biker2.move(1,0)
c.remove(biker2)
motor.add(biker)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)


for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)



for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.add(smoke3)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke3)

for i in range(10):
    motor.move(1, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke2)

for i in range(10):
    motor.move(3, 0)
    tire1.rotate(10)
    tire2.rotate(10)
motor.remove(smoke)



#GROUP MEMBERS
group=Layer()
hh=Rectangle(500,300,Point(120,400))
hh.setFillColor((55,77,99))
hh.setBorderColor("red")
group.add(hh)
gr=Text('GROUP 1',16,Point(100,260))
gr.setFontColor("white")
group.add(gr)


gr2=Text('GROUP MEMBERS',16,Point(110,295))
gr2.setFontColor("white")
group.add(gr2)
muk=Text('1 Hussein Beshir  UGR/30697/15 ',18,Point(165,335))
muk.setFontColor("white")
group.add(muk)


mub=Text('2 Mohammed Sadik  UGR/30960/15 ',18,Point(180,365))
mub.setFontColor("white")
group.add(mub)


mud=Text('3 Hanif Esmail    UGR/30629/15',18,Point(157,395))
mud.setFontColor("white")
group.add(mud)

mul=Text('4 Bikila Denino   UGR/30306/15 ',18,Point(160,423))
mul.setFontColor("white")
group.add(mul)



mut=Text('5 Efrata Anteneh  UGR/30439/15 ',18,Point(165,450))
mut.setFontColor("white")
group.add(mut)

mul2=Text('6 Yamrout Kifle UGR/31360/15 ',18,Point(155,480))
mul2.setFontColor("white")
group.add(mul2)



su=Text(" Submitted to Mr. Megersa Daraja and Mr. Malda Motuma",22,Point(180,508))
su.setFontColor("white")
su.scale(0.6)
group.add(su)


date=Text('Submitted date: May 23,2023 G.C.',23,Point(160,535))
date.setFontColor("white")
date.scale(0.6)
group.add(date)
group.setDepth(-90)
c.add(group)
