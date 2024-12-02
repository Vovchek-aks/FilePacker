import json


def main():
    with open('out.pack', 'rb') as file:
        data = file.read()

    size_of_header_size = ord(data[0:1].decode('utf-8'))
    header_start = size_of_header_size + 1
    header_size = int(data[1:header_start].decode('utf-8'))
    next_file_start = header_start + header_size
    names_to_size: dict[str, int] = json.loads(data[header_start:next_file_start])

    for name, size in names_to_size.items():
        with open(name, 'wb') as file:
            file.write(data[next_file_start:(next_file_start := next_file_start + size)])


if __name__ == '__main__':
    main()

