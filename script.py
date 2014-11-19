import os

def screenToAxis(sx,sy,frame):
  left_x = frame['left_x']
  right_x = frame['right_x']
  top_y = frame['top_y']
  bottom_y = frame['bottom_y']
  width = right_x - left_x
  height = bottom_y - top_y
  origin_x = left_x + width/2.0
  origin_y = top_y + height/2.0
  ax = (sx - origin_x) * (50.0/width)
  ay = (sy - origin_y) * (-30.0/height)
  return ax,ay

def makeFunct(coords):
  px,py = map(float,coords[0])
  x1,y1 = map(float,coords[1])
  x1 -= px
  y1 -= py
  y1_x1 = str(y1/x1)
  out = 'x*'+y1_x1+'-(abs(x-x1)+(x-x1))/2*'.replace('x1',str(x1))+y1_x1
  i = 2
  while i < len(coords):
    x2,y2 = map(float,coords[i])
    x2 -= px
    y2 -= py
    dxdy = str((y2-y1)/(x2-x1))
    chunk = dxdy+'-'+dxdy
    piece = '+((abs(x-x1)+(x-x1))/2)*'+chunk+'*((abs(x-x2)+(x-x2))/2)'
    out += piece.replace('x1',str(x1)).replace('x2',str(x2))
    x1,y1 = x2,y2
    i+=1
  return out

if __name__ == '__main__':
  while True:
    os.system('clear')
    print 'Type this JS into your console:'
    print "document.onmousemove = function(e){console.log(e.pageX.toString() + ',' + e.pageY.toString())}"
    print ''
    print 'Move your cursor to top left, and type in coords from console.'
    left_x, top_y = map(float, str(raw_input('left,top: ')).split(','))
    print 'Move your cursor to bottom right, and type in coords.'
    right_x, bottom_y = map(float, str(raw_input('right,bottom: ')).split(','))
    frame = {'left_x':left_x, 'right_x':right_x, 'top_y':top_y, 'bottom_y':bottom_y}
    print 'Move your cursor over player, and type in coords.'
    psx, psy = map(float, str(raw_input('px,py: ')).split(','))
    pax,pay = screenToAxis(psx, psy, frame)
    coords = [(pax,pay)]
    print 'For each point you want the function to go through, type its coords.'
    print '(x to end)'
    s = str(raw_input('x,y: '))
    while s!='x':
      try:
        sx,sy = map(float, s.split(','))
      except:
        print 'Could not parse that input.'
        continue
      ax,ay = screenToAxis(sx, sy, frame)
      coords.append([ax,ay])
      s = str(raw_input('x,y: '))
    print ''
    os.system('clear')
    print '\n\n\n'
    print makeFunct(coords)
    print '\n'
    str(raw_input('Press enter to continue...'))
