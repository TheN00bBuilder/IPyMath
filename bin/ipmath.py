#!/usr/bin/env python3

import argparse
import ipaddress

def domath(bip, verbose):
    """The whole thing is contained in one math class, I didn't feel the need to split it up. Calls builtin ipaddress function to do the math."""

    if bip == None:
        print("Add an IP!")
        pass
    else:
        try:
            address = ipaddress.IPv4Network(bip, strict = False)
            edgecase = 'Usable Range: %s - %s' % (address[0], address[-1])
            normalp = 'Usable Range: %s - %s' % (address[0]+1, address[-1]-1)
        except ValueError as e:
            print("This is not a valid IP range: %s" % e)
        else:
            if verbose == True:
                for ip in address:
                    print(ip)
                if bip[-2:] == '32' or '31':
                    print(edgecase)
                else:
                    print(normalp)
            else:
                if bip[-2:] == '32' or '31':
                    print(edgecase)
                else:
                    print(normalp)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("bip", type = str, help = "Put in your beginning IP with subnet here.")
    parser.add_argument("--v", action = 'store_true', help = "Set verbose to print all possible IP addresses with specified subnet. No flag will only print a range value.")
    args = parser.parse_args()

    bip = args.bip
    verbose = args.v
    
    domath(bip, verbose)