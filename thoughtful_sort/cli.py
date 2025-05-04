#!/usr/bin/env python3
"""Command-line interface for the thoughtful_sort package.

This module provides a command-line interface for categorizing packages based on their
dimensions and mass. It uses the sort function from the thoughtful_sort package to
determine the category of a package.

Example:
    To categorize a package with dimensions 10x10x10 and mass 10:
        $ python -m thoughtful_sort.cli 10 10 10 10
        Package category: STANDARD
"""

import argparse
from thoughtful_sort.sort import sort

def main():
    """Main entry point for the command-line interface.

    Parses command-line arguments for package dimensions and mass, then uses the sort
    function to determine the package category. Prints the result to stdout.

    Returns:
        int: Exit code (0 for success, 1 for error)

    Raises:
        SystemExit: If argument parsing fails or if the sort function raises a ValueError
    """
    parser = argparse.ArgumentParser(description='Sort a package based on its dimensions and mass')
    parser.add_argument('width', type=float, help='Width of the package')
    parser.add_argument('height', type=float, help='Height of the package')
    parser.add_argument('length', type=float, help='Length of the package')
    parser.add_argument('mass', type=float, help='Mass of the package')
    
    args = parser.parse_args()
    
    try:
        result = sort(args.width, args.height, args.length, args.mass)
        print(f"Package category: {result}")
    except ValueError as e:
        print(f"Error: {e}")
        return 1
    
    return 0

if __name__ == '__main__':
    exit(main()) 