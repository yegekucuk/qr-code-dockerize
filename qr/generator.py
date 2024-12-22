def show_qr_code(name):
    from PIL import Image
    im = Image.open("{filename}.{ext}".format(filename = name, ext = "png"))
    im.show()

def generate_qr(name, data):
    from segno import make_qr
    """
    name : The name of your file without any file extension!
    data : The data inside your QR code.
    """
    qrcode = make_qr(data, version=10, error='M')
    qrcode.save("{filename}.{ext}".format(filename = name, ext = "png"), scale=10)
