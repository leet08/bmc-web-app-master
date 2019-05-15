from bible import bible
from random_chooser import random_book_chapter

def main():
    # for name, chapter_titles in bible.items():
    #     print('Book of {}'.format(name))
    #     for chapter, title in chapter_titles.items():
    #         print('Chapter {}: {}'.format(chapter, title))
    #     print('')
    print('BMC QUIZ: (enter q to quit the program)')
    stop = False

    while stop == False:
        random_book, random_chapter = random_book_chapter(bible)
        answer = bible[random_book][random_chapter]
        user_response = input("Please enter chapter title for %s chapter %s: " %(random_book, random_chapter))
        if user_response == 'q':
            stop = True
        elif user_response == answer:
            print('correct!')
        else:
            print('wrong! The correct answer is %s' %(answer))

if __name__ == "__main__":
    main()