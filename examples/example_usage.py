from PIL import Image
import py_qoi as qoi

def main():
    # Load an image via Pillow
    img = Image.open("ILTQq.png").convert("RGBA")
    width, height = img.size
    pixels = list(img.getdata())  # RGBA tuples

    # Or use the convenience function
    qoi.save_qoi("output.qoi", pixels, width, height, channel=4, colorspace=0)

    # Decode a QOI file from disk
    w, h, c, decoded_pixels = qoi.load_qoi("output.qoi")

    # Convert the decoded pixels back to a Pillow image and save to PNG
    decoded_img = Image.new("RGBA", (w, h))
    decoded_img.putdata(decoded_pixels)
    decoded_img.save("decoded.png")

if __name__ == "__main__":
    main()