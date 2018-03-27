# translate.py
This is a small program that takes two lists, zips them into a translation dictionary, and translates a file using that translation dictionary.

This is a good example of text manipulation, file manipulation, and working with unicode in Python 2.7 (using io.open() instead of the regular open(), for example)

If you want to test it, I've included testing files enDict.txt, deDict.txt, and testInput.csv.

If you run translate.py like this: "python ./translate.py enDict.txt deDict.txt testInput.csv <outputFileName.csv>" it should work.

