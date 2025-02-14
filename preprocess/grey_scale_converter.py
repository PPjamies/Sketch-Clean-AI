import cv2


def preprocess(path: str):
    image = cv2.imread(path, cv2.IMREAD_COLOR)
    assert image is not None

    # convert image to greyscale
    grey_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    assert grey_image is not None

    # use bilateral filtering to blur image except dark edges
    blurr_image = cv2.bilateralFilter(grey_image, 7, 75, 75)

    # extract background and merge lines that are similar to background from image
    _, threshold_image = cv2.threshold(blurr_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    show(blurr_image, threshold_image)


def show(original_image, after_image):
    cv2.imshow("Original Image", original_image)
    cv2.imshow("After Image", after_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


preprocess("/Users/pazuzujindrich/IdeaProjects/Sketch-Clean-AI/images/rough-sketch-girl-colored.png")
