import sys
import getopt
 
def checkargs(argv):
    try:
        opts,_ = getopt.getopt(argv, "i:o:p:")
    except getopt.GetoptError as e:
        print("Error: "+str(e))
        sys.exit(2)
#    print("left: "+ str(left))
    if(len(opts)<3):
        print("Error: Too few arguments")
        sys.exit(2)

    for opt, arg in opts:
        if opt=="-i":
            inp_file = arg
        if opt=="-o":
            out_file = arg
        if opt=="-p":
            prog_file = arg

    return inp_file, out_file, prog_file
    
#print(checkargs(sys.argv[1:]))
