# Below code would club same type of files into a single file which would make loading process quite easy
import glob

files = glob.glob("/Users/xyxz/abc/*.csv")

header_saved = False

with open('/Users/xyxz/abc/sales_csv.csv','w') as fout:
    for filename in files:
        with open(filename) as fin:
            header = next(fin)
            if not header_saved:
                fout.write(header)
                header_saved = True
            for line in fin:
                fout.write(line)
