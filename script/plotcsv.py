#!/usr/bin/python
"""
read csv file and plot it easily
"""

import numpy as np
import sys
import os
import argparse
import matplotlib.pyplot as plt
import pandas as pd
from io import StringIO

def run_old():
    parser = argparse.ArgumentParser(description=
                                     "read csv files and plot them")
    parser.add_argument("specifiers", action='store', nargs='+')
    parser.add_argument("-s", "--path-root-dst",
                        action='store', nargs='?', default=".")
    parser.add_argument("-d", "--delimiter", default=",")
    parser.add_argument("-i", "--ignore-header", type=bool, default=False, nargs='?')
    parser.add_argument("-x", "--xlim", default="all")
    parser.add_argument("-y", "--ylim", default="all")
    args = parser.parse_args()
    
    for spec in args.specifiers:
        splitted = spec.split(":")

        ## -- read csv as pandas --
        fpath = splitted[0]
        droot = "."
        print "delimiter:", args.delimiter
        if(args.ignore_header):
            df = pd.read_csv(droot + "/" + fpath, header=None, delimiter=args.delimiter)
        else:
            df = pd.read_csv(droot + "/" + fpath, delimiter=args.delimiter)

        ## -- determine x label --
        if(len(splitted)==1):
            xlabel = df.columns[0]
            ylabels = [df.columns[i] for i in range(1,len(df.columns))]
            if(len(args.specifiers)==1):
                labels = ylabels
            else:
                labels = [fpath+":"+y for y in ylabels]
        elif(len(splitted) == 3):
            xlabel = splitted[1]
            ylabels = [splitted[2]]
            labels = [spec]
        else:
            raise Exception("bad combination")

        ## -- xlim -- 
        if(args.xlim!="all"):
            (x0,x1) = map(float, args.xlim.split(":"))
            plt.xlim(x0, x1)

            ## -- ylim -- 
        if(args.ylim!="all"):
            (y0,y1) = map(float, args.ylim.split(":"))
            plt.ylim(y0, y1)

        for (y, lbl) in zip(ylabels, labels):
            plt.plot(df[xlabel], df[y], label=lbl)
        
    plt.legend()
    plt.show()

def run():
    parser = argparse.ArgumentParser(description=
                                     "read csv files and plot them")
    parser.add_argument("specifiers", action='store', nargs='+')
    parser.add_argument("-s", "--path-root-dst",
                        action='store', nargs='?', default=".")
    parser.add_argument("-o", "--out", nargs='?', default="")
    parser.add_argument("-d", "--delimiter", default=",")
    parser.add_argument("-i", "--ignore-header", type=bool, default=False, nargs='?')
    parser.add_argument("-x", "--xlim", default="all")
    parser.add_argument("-y", "--ylim", default="all")
    
    args = parser.parse_args()

    define_x = False
    for spec in args.specifiers:

        if(spec=="_"):
            define_x = False
            continue
        
        splitted = spec.split(":")

        ## -- read csv as pandas --
        relpath = splitted[0]
        droot = args.path_root_dst
        fpath = droot + "/" + relpath
        if(fpath[-4:]!=".csv"):
            fpath = fpath+".csv"
        try:
            if(args.ignore_header):
                df = pd.read_csv(fpath, header=None, delimiter=args.delimiter)
            else:
                df = pd.read_csv(fpath, delimiter=args.delimiter)
        except:
            print "Failed to open csv file"
            print "file path:", fpath
            print "exit plotcsv...."
            return 
            
        ## -- determine labels --
        if(len(splitted)==1):
            label_list = df.columns
        else:
            label_list = splitted[1:]


        ## -- label check --
        for label in label_list:
            if(label not in df):
                print "Failed to find label key in csv file"
                print "file path:", fpath
                print "key:", label
                print "exit plotcsv...."
                return
            
        ## -- plot --
        if(define_x):
            ylbls = label_list
        else:
            x = df[label_list[0]]
            define_x = True
            ylbls = label_list[1:]

        for lbl in ylbls:
            plt.plot(x, df[lbl], label=relpath+":"+lbl)

    ## -- xlim -- 
    if(args.xlim!="all"):
        (x0,x1) = map(float, args.xlim.split(":"))
        plt.xlim(x0, x1)

    ## -- ylim -- 
    if(args.ylim!="all"):
        (y0,y1) = map(float, args.ylim.split(":"))
        plt.ylim(y0, y1)
        
    plt.legend()
    if(args.out==""):
        plt.show()
    else:
        plt.savefig(args.out)

if __name__ == "__main__":
    run()




