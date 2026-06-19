channels = [
    {
        "name": "FIFA 2026 Live 4",
        "url": "http://1716770.wofer.sbs/live/1Aoen7elp5/IgMJ60tmAa/741567.ts?token=ShJcU0BbQQNHDQYOU1oFAF8EU1RQDVZWBQZTUgFRBAQDVVVUAAJXD1EbGBpEF0dcWF1vWQIXXlYFU1cBUkgRR0JVRm1aV0EDRwgDCQFUAgkbHBJED1gBQwtTVQ9UXAcCBQAFHhFDCl1HAxYBAlIMCwgSHBIDTRAEQwwDWzoAVkRYU1EQCV0WVQkVFldZPFFcVFFeVEQPRlETTkBeFhQRCF9FWF4fEQFQEUtVTFJBDxsNBAIIRBlGAl4XDEMXHREIE3JwEB8RBkERXFpLXgxbGwMSRENEGUYIQj0QUhYQQVdQXVFAEQlBCUcVFlVWG2paVl5eVQVBDQ5fEUANR1URHhNdW1xaRwxLOkldXBVZFwANBwEAVxcZ"
    }
]

with open("unite.m3u", "w", encoding="utf-8") as f:
    f.write("#EXTM3U\n\n")

    for ch in channels:
        f.write(f"#EXTINF:-1,{ch['name']}\n")
        f.write(f"{ch['url']}\n\n")

print("Updated playlist done")
