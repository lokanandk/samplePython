

# TUBES IN A RACK
------------------
## This program performs move or remove operations and returns final positions of the tubes in the rack

## Dependencies

python v. 3.6.0+
numpy v. 1.14.0+

## Installation

No installation is required. Clone the git repository, move tubesInARack.py to a directory in your PATH or add the cloned directory to your PATH. 

## Usage:
```bash
tubesInARack.py [-h] --rack_size RACKSIZE [RACKSIZE ...]
                       --tube_positions FILE --moves FILE --remove FILE
```
Output (the final tube positions in the rack) will saved in a text file named 'finaltubepositions.txt'

## Example usage:
(*Add the cloned github directory to your PATH*)

```bash
python tubesInARack.py --rack_size 10 --tube_positions ../test/initpos.txt --moves ../test/moves.txt --remove ../test/remove.txt 

## Optional arguments:
  -h, --help            

## Required arguments:
  --rack_size RACKSIZE [RACKSIZE ...]
                        Size of the square rack: please provide the capacity
                        of the rack in a single row or column).
  --tube_positions FILE
                        Name of the tab delimited text file containing the
                        positions or (x, y) coordinates of each existing tubes, one in a row.
			
			Format (example):
			
			(0, 0)
			(9, 2)
			(5, 5)
			(2, 8)
			
  --moves FILE          Name of the tab delimited text file containing the
                        moves, one in a row. First column must consist of the
                        initial (x, y) coordinates of the tube to be moved,
                        second column should be the (x, y) coordinates of the
                        destination.
			
			Format (example):
			
			(0, 0)	(3, 2)
			
  --remove FILE         Name of the tab delimited text file containing (x, y)
                        coordinates of the tubes to be removed, one in each
                        row.
			
			Format (example):
			
			(9, 2)
			(2, 8)
```			
## Sample output

```bash

(3, 2)
(5, 5)
(9, 2)  removed
(2, 8)  removed


The output shown above has been saved in 'finaltubepositions.txt'
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
