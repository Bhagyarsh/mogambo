import base64
import json
img = json.dumps(base64.b64encode(open('inkscape.jpg', 'rb').read()))
print(img)