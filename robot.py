'''In this program inital coordinate are x1=0 and y1=0 so we are at starting point if we go up or down the value of y will
   be increse or decrese accordingly and if move left or right the value of x will be increse or decrese accordingly
   and finally we will get the new coordinate values of x and y'''

import math as m
def countstep(line):
    x1,y1=0,0          #initial values of x and y coordinates
    if line==" ":
        return None
    else:
        l=line.split(" ") #split the values and stored it into list here notice poistion 0th=UP 1th=DOWN 2nd=LEFT 3rd=RIGHT
        y1+=int(l[0])     #UP MEANS INCRESE THE VALUE OF Y COORIDNATE hence y1=y1+l[0] wehre l[0]=UP
        y1-=int(l[1])     #DOWN MEANS DECREASE THE VALUE OF Y COORIDNATE hence y1=y1-l[1] wehre l[1]=DOWN
        x1-=int(l[2])     #LEFT MEANS MOVE THE X axix in negative direction hence x1=x1-l[2] wehre l[2]=LEFT
        x1+=int(l[3])     #RIGHT MEANS MOVE THE X axix in POSITIVE direction hence x1=x1-l[2] wehre l[2]=LEFT
                          #IF x is already in negative suppose -5 and right move is 3 so new x will be x=-5+3
    return (round(m.sqrt(x1**2+y1**2)))
line=input('Enter UP DOWN LEFT RIGHT:') #get the input values in space seperated format
steps=countstep(line)
print('Number of Steps:{0}'.format(steps))