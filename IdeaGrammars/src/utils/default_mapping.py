__author__ = 'marodrig'

def default_mapping(fileName):
    """
    Prints to screen a very default mapping out of a file with a list of words
    :param fileName: File to obtain command words from
    :return: None
    """
    with open(fileName, "r") as f:
        for line in f:
            line = line[:-1]
            print("\"" + line + "\" : Text(\"" + line + "\"),")

if __name__ == '__main__':
    default_mapping("C:/MarcelStuff/data/small_experiment.txt")