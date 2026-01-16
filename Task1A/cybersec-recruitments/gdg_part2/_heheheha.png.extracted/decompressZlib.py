#import zlib
#with open('29.zlib', 'rb') as f:
#   data = f.read()
#decompressed = zlib.decompress(data)
#print(decompressed.decode('utf-8', errors='ignore'))

import zlib

with open('29.zlib', 'rb') as f:
    data = f.read()

try:
    # Try standard decompression
    print(zlib.decompress(data).decode('utf-8', errors='ignore'))
except zlib.error:
    # Try raw DEFLATE decompression (common in CTFs)
    print(zlib.decompress(data, -15).decode('utf-8', errors='ignore'))
