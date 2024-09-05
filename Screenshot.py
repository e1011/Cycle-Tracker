from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import cv2 as cv
import os


def Screenshot():
    windowId = None

    def printWindows():
        windowList = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
        for window in windowList:
            print(window.get('kCGWindowName', '').lower())

    def setId(windowName):
        nonlocal windowId
        windowList = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)

        for window in windowList:
            if(windowName.lower() in window.get('kCGWindowName', '').lower()):
                windowId = window['kCGWindowNumber']

    def takeScreenshot():
        nonlocal windowId
        if windowId is None:
            raise Exception("ID is not defined")

        imageFileName = './match/screenshot.jpg'
        img = os.system('screencapture -x -t jpg -l %s %s' % (windowId, imageFileName))
        img = cv.imread(imageFileName, cv.IMREAD_REDUCED_COLOR_2)

        if img.shape[0] == 909:
            img = img[38:836, 56:483]
        elif img.shape[0] == 865:
            img = img[26:826, 34:461]
        elif img.shape[0] == 455:
            img = img[19:418, 28:242]
        else:
            img = img[13:413, 17:231]
        
        elixir = img[int(img.shape[0]*0.062):int(img.shape[0]*0.082), int(img.shape[1]*0.037):int(img.shape[1]*0.752)]
        cv.imwrite("./assets/elixir.jpg", elixir)
        
        ret = []
        step = 0.108125
        for i in range(0, 8):
            ret.append(img[int(img.shape[0]*0.105):int(img.shape[0]*0.175), int(img.shape[1]*(0.12+step*i)):int(img.shape[1]*(0.18+step*(i)))])

        return ret

    return {"takeScreenshot":takeScreenshot, "setId":setId, "printWindows":printWindows}
