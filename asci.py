from ascii_magic import AsciiArt

def print_ascii_art(image_path):
    my_art = AsciiArt.from_image(image_path)
    print(r(my_art.to_ascii()) )

# Example usage:
print_ascii_art('Beamer.png')
