from Screenshot import Screenshot
from CycleTracker import CycleTracker
from Draw import Draw

screenshot = Screenshot()
screenshot["setId"]("Android Device")

cycleTracker = CycleTracker()

draw = Draw()

while True:
    img = screenshot["takeScreenshot"]()
    cycleTracker["processImg"](img)
    
    draw(cycleTracker["getCycle"]())


# royal ghost not exist 
