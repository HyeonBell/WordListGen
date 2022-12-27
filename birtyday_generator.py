import random
import sys
import getopt

birtyday_list = []

def year_random(year_first, year_final):
    #print("{}_{}_{}_{}".format(year_first[0],year_first[1], year_final[0],year_final[1])) 
    while True:
        #ret = "{}{}".format(random.randint(int(year_first[0]),int(year_final[0])), random.randint(int(year_first[1]),int(year_final[1])))
        ret = "{}{}".format(random.randint(7,9), random.randint(0,9)) #77 - 99
        if int(ret[0]) >= int(year_first[0]) or int(ret[0]) <= int(year_final[0]):
            if int(ret[1]) >= int(year_first[1]) or int(ret[1]) <= int(year_final[1]):
                break
    return ret

def month_random():
    ret = "{}".format(random.randint(0,1))
    if ret == "0":
        ret += str(random.randint(1,9))
    elif ret == "1":
        ret += str(random.randint(0,2))        
    return ret

def day_random():
    ret = "{}".format(random.randint(0,3)) # 01 31 
    if int(ret) <= 2 and int(ret) >= 0:
        ret += str(random.randint(1,9))
    elif ret == "3":
        ret += str(random.randint(0,1))
    return ret

if __name__ == "__main__":
    if sys.argv.__len__() > 1:
        options, args = getopt.getopt(sys.argv[1:], 'y:m:d:c:')
        for op, p in options:
            if op == "-y":
                year_first = p.split("-")[0]
                year_final = p.split("-")[1]
                if int(year_final) > int(year_first):
                    print(year_first, year_final)
                else:
                    print("-y option parse error")
                    sys.exit(1)
                    
            elif op == "-m":
                pass
            elif op == "-d":
                pass
            elif op == "-c":
                if p.isdecimal() and int(p) >= 0:
                    loop_number = int(p)   
            else:
                print("getopt error")
    else:
        print("[== Birtyday_Generator ==]")
        print("> Usage : python birtyday_generator.py -c [count]")
        print("> Example : python birtyday_generator.py 20\n")
        sys.exit(1)

    for _ in range(0, loop_number):
        birtyday_list.append("{}{}{}".format(year_random(year_first,year_final),month_random(),day_random()))
    final = list(set(birtyday_list))
    for iter_br in final:
        print(iter_br)
    print(final.__len__())


