# import pywhatkit as img

# img.image_to_ascii_art("joker.jpg","new")

import ascii_magic

# output = ascii_magic.from_image_file("rk.jpg", columns=100, char="#")

# ascii_magic.to_terminal(output)

my_art = ascii_magic.from_image_file(
    'roshan.jpg',
    columns=200,
    width_ratio=2,
    mode=ascii_magic.Modes.HTML
)
ascii_magic.to_html_file('roshan.html', my_art)
