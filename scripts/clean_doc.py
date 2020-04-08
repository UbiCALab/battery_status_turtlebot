
if __name__ == "__main__":
    with open('pub_subs_batteryStatus.py', 'rb+') as f:
        content = f.read()
        f.seek(0)
        f.write(content.replace(b'\r', b''))
        f.truncate()