import json


def get_file_info(filename: str) -> tuple[int, bytes]:
    with open(filename, 'rb') as file:
        content = file.read()
        size = len(content)
        return size, content


def number_to_bytes(number: int) -> bytes:
    data = []
    while number > 0:
        number, mod = divmod(number, 256)
        data.append(chr(mod).encode('utf-8'))
    return b''.join(data)


def main():
    files_to_compress = [
        'test/Fraktal_3.jpg',
        'test/fraktal_3.py',
        'test/Fraktal_3_1.jpg',
        'test/Fraktal_3_2.jpg',
        'test/Fraktal_3_2.png',
        'test/fraktal_4.py',
        'test/Fraktal_4_2.jpg',
        'test/fraktal_5.jpg',
        'test/fraktal_5.py',
        'test/Fraktal_5_1.jpg',
    ]

    file_infos = [get_file_info(name) for name in files_to_compress]
    names_to_size = {name: file_infos[idx][0] for idx, name in enumerate(files_to_compress)}
    header = json.dumps(names_to_size).encode('utf-8')
    size = str(len(header)).encode('utf-8')
    if len(size) > 255:
        raise ValueError

    compressed = chr(len(size)).encode('utf-8') + size + header + b''.join(file for _, file in file_infos)

    with open('out.pack', 'wb') as file:
        file.write(compressed)


if __name__ == '__main__':
    main()

