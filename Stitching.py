# code needed to stitch images together
import cv2


def run():
    images = []
    for i in range(36):
        images.append(
            cv2.imread('/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/Cozmopics/takingpics' + str((i * 10))))
    stitcher = cv2.Stitcher.create()
    ret, pano = stitcher.stitch(images)
    cv2.imwrite('Panorama.jpeg', pano)