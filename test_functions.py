import math

eps = 0.05

class Restrictions:
    def restr1(self, x):
        if x[0] + x[1] + x[2] + x[3] + x[4] >= 1 - eps and x[0] + x[1] + x[2] + x[3] + x[4] <= 1 + eps :
            "TRUE"
            return True
        else:
            "FALSE"
            return False

    #pass

def SphereF(x):
    return -x[0]**2 -x[1]**2

rSphereF = Restrictions()
rSphereF.x = [[-5, 5], [-5, 5]]

def AckleyF(x):
    return 20 * math.exp(-0.2 * math.sqrt(0.5 * (x[0]**2 + x[1]**2))) + math.exp(0.5 * (math.cos(2 * math.pi * x[0]) + math.cos(2 * math.pi * x[1]))) - math.e - 20

rAckleyF = Restrictions()
rAckleyF.x = [[-2, 2], [-2, 2]]

def RosenbrockF(x):
    return - 100 * (x[1] - x[0]**2)**2 - (x[0] - 1)**2

rRosenbrockF = Restrictions()
rRosenbrockF.x = [[-2, 2], [-2, 2]]

def BealeF(x):
    return - ((1.5 - x[0] + x[0] * x[1])**2 + (2.25 - x[0] + x[0] * x[1]**2)**2 + (2.625 - x[0] + x[0] * x[1]**3)**2)

rBealeF = Restrictions()
rBealeF.x = [[-4.5, 4.5], [-4.5, 4.5]]

def GoldsteinPriceF(x):
    return - (1 + (x[0] + x[1] + 1)**2 * (19 - 14 * x[0] + 3 * x[0]**2 - 14 * x[1] + 6 * x[0] * x[1] + 3 * x[1]**2)) * \
             (30 + (2 * x[0] - 3 * x[1])**2 * (18 - 32 * x[0] + 12 * x[0]**2 + 48 * x[0] - 36 * x[0] * x[1] + 27 * x[1]**2))

rGoldsteinPriceF = Restrictions()
rGoldsteinPriceF.x = [[-2, 2], [-2, 2]]

def BoothF(x):
    return - (x[0] + 2 * x[1] - 7)**2 - (2 * x[0] + x[1] - 5)**2

rBoothF = Restrictions()
rBoothF.x = [[-10, 10], [-10, 10]]

def Bukin6F(x):
    return - 100 * math.sqrt(math.fabs(x[1] - 0.01 * x[0]**2)) - 0.01 * math.fabs(x[0] + 10)

rBukin6F = Restrictions()
rBukin6F.x = [[-15, -5], [-3, 3]]

def Levi13F(x):
    return - math.sin(3 * math.pi * x[0])**2 - (x[0]-1)**2 * (1 + math.sin(3 * math.pi * x[1])**2) - (x[1] - 1)**2 * (1 + math.sin(2 * math.pi * x[1])**2)

rLevi13F = Restrictions()
rLevi13F.x = [[-10, 10], [-10, 10]]

def ThreeHumpCamelF(x):
    return - 2 * x[0]**2 + 1.05 * x[0]**4 - x[0]**6 / 6.0 - x[0] * x[1] -x[1]**2

rThreeHumpCamelF = Restrictions()
rThreeHumpCamelF.x = [[-5, 5], [-5, 5]]

def Easom(x):
    return math.cos(x[0]) * math.cos(x[1]) * math.exp(-((x[0] - math.pi)**2 + (x[1] - math.pi)**2))

rEasom = Restrictions()
rEasom.x = [[-100, 100], [-100, 100]]

functions_names = [SphereF.__name__,
                   #AckleyF.__name__,
                   #RosenbrockF.__name__,
                   #BealeF.__name__,
                   #GoldsteinPriceF.__name__,
                   #BoothF.__name__,
                   #Levi13F.__name__,
                   #ThreeHumpCamelF.__name__,
                   #Easom.__name__
                ]


#--------------------------------------------
aaalpha = [0.39, 0.34, 0.27]
#Goole
ccconst = [0.144, 0.877, 0.945, 0.893, 0.8, 0.9, 0.54, 0.7, 0.1]

def f0(x):
    return ccconst[4] * (1-ccconst[1]) * ccconst[5] * ccconst[6] * math.log(x[0]) + \
           ccconst[4] * (1-ccconst[0]) * (1-ccconst[1]) * ccconst[3] * (1-ccconst[6]) * math.log(x[1])

def f1(x):
    return ccconst[4] * ccconst[1] * ccconst[2] * ccconst[5] * math.log(x[2])

def f2(x):
    return ccconst[4] * (1-ccconst[0]) * (1-ccconst[7]) * (1-ccconst[8]) * math.log(x[3]) + \
           ccconst[4] * ccconst[1] * ccconst[3] * ccconst[5] * (1-ccconst[8]) * math.log(x[4])

def fff(x):
    return aaalpha[0] * f0(x) + aaalpha[1] * f1(x) + aaalpha[2] * f2(x)

rrrestr = Restrictions()
#Google
rrrestr.x = [[0.1, 0.2], [0.07, 1.], [0.65, 1.], [0.03, 1.], [0.03, 1.]]

dddddddim = 8
#-------------------