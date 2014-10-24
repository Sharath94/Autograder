#Completely uncommented, fragile, build code.
#Works is you provide the input format file as inp.txt and output format file
#as output.txt
#the result of the gradation process will be available in results.txt
import sys, io, traceback, os

def createNew():
    f = open("new.py","w")
    l = []
    indent = 0
    #com = False
    with open(sys.argv[1]) as fp:
        for line in fp:
            if indent > 0:
                if line[0]!='\n' and line[0]!=' ' and line[0]!='\t':
                    indent = 0
                else:
                    f.write(line)
                    continue
            if line.find("def") == 0 or line.find("class") ==0:
                f.write(line)
                indent = 1
            elif line.find("import") == 0:
                f.write(line)
            else:
                l.append(line)
 #           print("Normal: ",line,end='')
    f.write("def main(args):\n")
    f.write("    sys.argv = args")
    f.write("    ".join(l))
    f.close()


def closeFiles():
    out.close()
    res.close()
    output.close()

def checkOut():
    out = open("out.txt")
    res = open("result.txt","w")
    mod = __import__("new")
    res.write("Submit to evalutation successful\n")
    output = io.StringIO()
    temp = sys.stdout
    sys.stdout = output
    f = open(os.devnull, "w")
    sys.stderr = f
    with open("inp.txt") as inp:
        for line in inp:
            l = line.split(" ")
            l.insert(0, "")
            try:
                mod.main(l)
            except Exception:
                traceback.print_exc(file=res)
                closeFiles()                
            print("h\n"+str(e))
            ans = output.getvalue()
            count = ans.count("\n")
            exp = ""
            for i in range(count):
                exp += out.readline()
            if ans != exp:
                res.write("Error: expected output for "+line+" is "+exp)
                res.write("But output obtained is "+ans)
                closeFiles()
                sys.exit(2)
            output.truncate(0)
            output.seek(0)
#sys.stdout = temp
    res.write("Successful Completion!\n")
    closeFiles()
#print(l)

createNew()
checkOut()
