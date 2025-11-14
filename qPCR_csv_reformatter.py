#!/usr/bin/env python3

"""Reformats a CSV to be heatmap-compatible."""

keyword_search = {"mhv":5,"yHV68":6,"ccr3":7}

reformat_dict = {}

curr_search = "yHV68"

with open("combined_qPCR_kn_rep.csv","r",encoding="utf-8") as f:
    for idx, lines in enumerate(f):
        line = lines.strip().split(",")
        if idx != 0:
            if line[1] not in reformat_dict:
                reformat_dict[line[1]] = [line[keyword_search[curr_search]]]
            else:
                reformat_dict[line[1]].append(line[keyword_search[curr_search]])

f.close()

with open("outfile_yHV68.csv","w",encoding="utf-8") as g:
    write_list = []
    for keys,values in reformat_dict.items():
        counter = 0
        for idx, vals in enumerate(values):
            if (idx % 20 == 0) and (idx != 0):
                if counter == 3:
                    counter = 0
                counter += 1
                title = keys + "_" + str(counter)
                g.write(title + ",")
                g.write(",".join(write_list))
                g.write("\n")
                write_list = []
            else:
                write_list.append(vals)
        if counter == 3:
            counter = 0
        counter += 1
        title = keys + "_" + str(counter)
        g.write(title + ",")
        g.write(",".join(write_list))
        g.write("\n")
        write_list = []
g.close()
