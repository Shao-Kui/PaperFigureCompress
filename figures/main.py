import cv2 as cv
import os
F = 3
def compressDirectory(root):
    filenames = os.listdir(root)
    for filename in filenames:
        if '.jpg' in filename or '.png' in filename:
            img = cv.imread(os.path.join(root, filename), cv.IMREAD_UNCHANGED)
            img = cv.resize(img, dsize=(int(img.shape[1]/F), int(img.shape[0]/F)))
            if not os.path.exists(os.path.join('../figures_reduce/', root)):
                os.makedirs(os.path.join('../figures_reduce/', root))
            cv.imwrite(os.path.join('../figures_reduce/', root, filename), img)
        elif os.path.isdir(filename):
            compressDirectory(os.path.join(root, filename))

if __name__ == '__main__':
    compressDirectory('./')
