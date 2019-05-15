from bible import bible


def main():
    for name, chapter_titles in bible.items():
        print('Book of {}'.format(name))
        for chapter, title in chapter_titles.items():
            print('Chapter {}: {}'.format(chapter, title))
        print('')


if __name__ == "__main__":
    main()