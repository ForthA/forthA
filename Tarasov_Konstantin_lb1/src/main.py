from tests.findHeightTest import findHeightTest
from src.input import input_data
from src.findHeight import findHeight

if __name__ == '__main__':
    findHeightTest()
    n, parent = input_data()
    print(findHeight(parent, n))


