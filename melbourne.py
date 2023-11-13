from random import choice


def pickfunfact():
    funfacts = ["Until 1966, all pubs in Melbourne had to close at 6pm.",
                "Melbourne is home to the world's fourth-largest tram system!",
                "It is Australia's cultural melting pot"]
    index = choice('012')
    print(funfacts[int(index)])


print(__name__)
if __name__ == '__main__':
    pickfunfact()
