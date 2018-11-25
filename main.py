#!/usr/bin/python3
import argparse
import modules.utils as utils

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("Set", type=str, help="Set to be read.")
    args = parser.parse_args()

    SET = args.Set

    setImages = utils.readSet(SET)

    for image in setImages:
        image.displayImage()
