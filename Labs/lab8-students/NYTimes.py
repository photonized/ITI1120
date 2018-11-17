def create_books_2Dlist(file_name):

    books=open(file_name).read().splitlines()


    table=[]

    for book in books:
        book=book.rsplit("\t")
        book.insert(0, book[3])
        book.pop(4)
        table.append(book)

    return table


def search_by_year(books, year1, year2):
    l=[]
    for i in range(len(books)):
        bookdate=books[i][0]
        l.append(bookdate.split("/"))
    l2=[]
    for i in range(len(l)):
        a = ""
        for j in range(len(l[i])):
            a += l[i][-1 - j]
        l2.append(a)
    return l2

