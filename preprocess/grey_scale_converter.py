import cv2

def convert_to_greyscale(path: str):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # test
    cv2.imshow("Greyscale Image", grey_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



convert_to_greyscale("/Users/pazuzujindrich/IdeaProjects/Sketch-Clean-AI/images/rough-sketch-girl-colored.png")
