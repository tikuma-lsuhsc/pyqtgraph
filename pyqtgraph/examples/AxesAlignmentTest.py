"""
Demonstrates a way to put multiple axes around a single plot. 

(This will eventually become a built-in feature of PlotItem)
"""


import pyqtgraph as pg

app = pg.mkQApp("Arrow Example")

view = pg.GraphicsView()
l = pg.GraphicsLayout(border='r')
view.setCentralItem(l)
view.show()
view.setWindowTitle('pyqtgraph example: GraphicsLayout')
view.resize(800,600)

p00 = l.addPlot(row=0, col=0)
p01 = l.addPlot(row=0,col=1,title='top right')
p10 = l.addPlot(row=1, col=0)
p11 = l.addPlot(row=1,col=1)

for p in (p10,p11):
    p.hideAxis('left')
    p.showAxis('right')

for p in (p01,p11):
    p.hideAxis('bottom')
    p.showAxis('top')

print(p00.margins(),p00.tightMargins())
print(p01.margins())
print(p10.margins())
print(p11.margins())

l.alignPlotAxes()

# pg.PlotItem

# ## create a new ViewBox, link the right axis to its coordinate system
# p2 = pg.ViewBox()
# p1.showAxis('right')
# p1.scene().addItem(p2)
# p1.getAxis('right').linkToView(p2)
# p2.setXLink(p1)
# p1.getAxis('right').setLabel('axis2', color='#0000ff')

# ## create third ViewBox. 
# ## this time we need to create a new axis as well.
# p3 = pg.ViewBox()
# ax3 = pg.AxisItem('right')
# p1.layout.addItem(ax3, 2, 3)
# p1.scene().addItem(p3)
# ax3.linkToView(p3)
# p3.setXLink(p1)
# ax3.setZValue(-10000)
# ax3.setLabel('axis 3', color='#ff0000')


# ## Handle view resizing 
# def updateViews():
#     ## view has resized; update auxiliary views to match
#     global p1, p2, p3
#     p2.setGeometry(p1.vb.sceneBoundingRect())
#     p3.setGeometry(p1.vb.sceneBoundingRect())
    
#     ## need to re-update linked axes since this was called
#     ## incorrectly while views had different shapes.
#     ## (probably this should be handled in ViewBox.resizeEvent)
#     p2.linkedViewChanged(p1.vb, p2.XAxis)
#     p3.linkedViewChanged(p1.vb, p3.XAxis)

# updateViews()
# p1.vb.sigResized.connect(updateViews)


# p1.plot([1,2,4,8,16,32])
# p2.addItem(pg.PlotCurveItem([10,20,40,80,40,20], pen='b'))
# p3.addItem(pg.PlotCurveItem([3200,1600,800,400,200,100], pen='r'))

if __name__ == '__main__':
    pg.exec()
