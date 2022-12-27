
user = ['test', 'test2', 'test3', 'amdin']
host = ['gmail', 'yahoo', 'pentest', 'edge-inc']
domain_list = ['com', 'net', 'jp', 'kr', 'co.jp']

def gen():
    with open("./output_email_gen.txt", "w+") as f:
        for u in user:
            for h in host:
                for d in domain_list:
                    for i in range(0, 200):
                        if i == 0:
                            f.write(f"{u}@{h}.{d}\n")
                            f.write(f"{u}{str(i).zfill(3)}@{h}.{d}\n")
                        else:
                            f.write(f"{u}{str(i).zfill(3)}@{h}.{d}\n")
gen()
