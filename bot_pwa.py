import pywinauto as pwa

def main():
    app = pwa.Application().connect(path='C:\\Users\\diego\\AppData\\Local\\Discord')
    print(dir(app))

if __name__ == '__main__':
    main()