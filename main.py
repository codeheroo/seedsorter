def main():

    with open('seeds.txt', 'r', encoding='utf-8') as seeds_file:
        lines = seeds_file.readlines()


    file_names = {
        12: '12words.txt',
        18: '18words.txt',
        24: '24words.txt',
    }


    files = {num_words: open(file_name, 'w', encoding='utf-8') for num_words, file_name in file_names.items()}

    try:

        for line in lines:
            words = line.strip().split()
            num_words = len(words)

            if num_words in files:
                files[num_words].write(line)
    finally:

        for f in files.values():
            f.close()

if __name__ == '__main__':
    main()
