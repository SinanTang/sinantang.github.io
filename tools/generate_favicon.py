#!/usr/bin/env python3
"""
Generate favicon files from text character
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_favicon(text, size, filename, bg_color=(37, 99, 235), text_color=(255, 255, 255)):
    """Create a favicon with text character"""
    # Create image with rounded rectangle background
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw rounded rectangle background
    margin = 2
    draw.rounded_rectangle(
        [margin, margin, size-margin, size-margin],
        radius=4,
        fill=bg_color
    )

    # Try to use a system font, fallback to default
    try:
        # Try different font sizes based on image size
        font_size = int(size * 0.6)
        try:
            font = ImageFont.truetype("/System/Library/Fonts/Arial.ttf", font_size)
        except:
            try:
                font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", font_size)
            except:
                font = ImageFont.load_default()
    except:
        font = ImageFont.load_default()

    # Get text size and center it
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    x = (size - text_width) // 2
    y = (size - text_height) // 2 - 2  # Slight adjustment for better centering

    # Draw text
    draw.text((x, y), text, fill=text_color, font=font)

    return img

def main():
    os.makedirs('assets/img/favicons', exist_ok=True)

    # Create different sizes
    sizes = [
        (16, 'favicon-16x16.png'),
        (32, 'favicon-32x32.png'),
        (192, 'android-chrome-192x192.png'),
        (512, 'android-chrome-512x512.png'),
        (180, 'apple-touch-icon.png'),
        (150, 'mstile-150x150.png')
    ]

    for size, filename in sizes:
        img = create_favicon('S', size, filename)
        img.save(f'assets/img/favicons/{filename}', 'PNG')
        print(f'Created {filename}')

    # Create ICO file (16x16 and 32x32)
    img16 = create_favicon('S', 16, 'favicon-16x16.png')
    img32 = create_favicon('S', 32, 'favicon-32x32.png')
    img16.save('assets/img/favicons/favicon.ico', format='ICO', sizes=[(16, 16), (32, 32)])
    print('Created favicon.ico')

    # Create site.webmanifest
    manifest = '''{
    "name": "SinansNotes",
    "short_name": "SinansNotes",
    "icons": [
        {
            "src": "/assets/img/favicons/android-chrome-192x192.png",
            "sizes": "192x192",
            "type": "image/png"
        },
        {
            "src": "/assets/img/favicons/android-chrome-512x512.png",
            "sizes": "512x512",
            "type": "image/png"
        }
    ],
    "theme_color": "#2563eb",
    "background_color": "#ffffff",
    "display": "standalone"
}'''

    with open('assets/img/favicons/site.webmanifest', 'w') as f:
        f.write(manifest)
    print('Created site.webmanifest')

    # Create browserconfig.xml
    browserconfig = '''<?xml version="1.0" encoding="utf-8"?>
<browserconfig>
    <msapplication>
        <tile>
            <square150x150logo src="/assets/img/favicons/mstile-150x150.png"/>
            <TileColor>#2563eb</TileColor>
        </tile>
    </msapplication>
</browserconfig>'''

    with open('assets/img/favicons/browserconfig.xml', 'w') as f:
        f.write(browserconfig)
    print('Created browserconfig.xml')

if __name__ == '__main__':
    main()