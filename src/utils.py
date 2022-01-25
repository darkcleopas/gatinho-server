from skimage import io, transform


def reshape_image(image):
    return transform.resize(image,(50, 50, 3)) 