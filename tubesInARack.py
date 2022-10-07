#!/usr/bin/env python3

import argparse
import numpy as np

def main():
	parser = argparse.ArgumentParser(description="**This program performs move or remove operations and returns"+
			"the final positions of tubes in the rack**")
	requiredArgs = parser.add_argument_group('Required arguments')
	requiredArgs.add_argument('--rack_size', nargs='+', type=int, required=True, help="Size of the square rack:\n" +
			"please provide the capacity of the rack in a single row or column).", dest='rackSize')
	requiredArgs.add_argument('--tube_positions', metavar='FILE', type=argparse.FileType('r'), required=True, help="Name of\n"+
			"the tab delimited text file containing the positions or (x, y) coordinates of each existing tubes,\n"+
			"one in a row.\n",dest='initialPositions')
	requiredArgs.add_argument('--moves', metavar='FILE', type=argparse.FileType('r'), required=True, help="Name of the tab\n" +
			"delimited text file containing the moves, one in a row. First column must consist of the initial\n" +
			"(x, y) coordinates of the tube to be moved, second column should be the (x, y) coordinates of the\n" +
			"destination.", dest='moves')
	requiredArgs.add_argument('--remove', metavar='FILE', type=argparse.FileType('r'), required=True, help="Name of the\n" +
			"tab delimited text file containing (x, y) coordinates of the tubes to be removed, one in\n" +
			"each row." , dest='removeList')
	args = parser.parse_args()
	N = args.rackSize
	initPos = args.initialPositions.read()
	# Following lines consist of series of text processing operations to convert the input coordinates into a binary matrix
	temp1 = initPos.replace("(","").replace(")","")
	temp2 = temp1.split('\n')
	temp3 = [item for items in temp2 for item in items.split(",")]
	temp4 = list(filter(None, temp3))
	temp5 = [int(i) for i in temp4]
	list1 = ([(temp5[i],temp5[i+1]) for i in range(0,len(temp5),2)])
	array1 = np.array(list1)
	# PAM: presence-absence matrix
	PAM = np.zeros((N[0],N[0]), dtype=int)	# initializing a zero matrix of size 'N X N'
	PAM[array1[:,0], array1[:,1]] = 1	# binarizing the matrix. 1: Presence of tube, 0: Absence of tube
	moves_list = args.moves.read()
	# Following lines consist of series of text processing operations to convert the input move operations to indices of PAM
	temp1 = moves_list.replace("(","").replace(")","")
	temp2 = temp1.split('\n')
	temp3 = [item for items in temp2 for item in items.split(",")]
	temp4 = [item for items in temp3 for item in items.split("\t")]
	temp5 = list(filter(None, temp4))
	temp6 = [int(i) for i in temp5]
	list2 = ([(temp6[i],temp6[i+1]) for i in range(0,len(temp6),2)])
	array2 = np.array(list2)
	remove_list = args.removeList.read()
	# Following lines consist of series of text processing operations to convert the input remove operations to indices of PAM
	temp1 = remove_list.replace("(","").replace(")","")
	temp2 = temp1.split('\n')
	temp3 = [item for items in temp2 for item in items.split(",")]
	temp4 = list(filter(None, temp3))
	temp5 = [int(i) for i in temp4]
	list3 = ([(temp5[i],temp5[i+1]) for i in range(0,len(temp5),2)])
	array3 = np.array(list3)
	
	# Move operations
	j=0
	for i in range(int(len(array2)/2)):
		if PAM[array2[j+1][0]][array2[j+1][1]]==0:
			PAM[array2[j][0]][array2[j][1]]=0
			PAM[array2[j+1][0]][array2[j+1][1]]=1
		j=j+2
	
	# Remove operations
	j=0
	for i in range(len(array3)):
		if PAM[array3[j][0]][array3[j][1]]==1:
			PAM[array3[j][0]][array3[j][1]]=0
		j=j+1
	PAMnp = np.array(PAM)
	PAMnp_nonzero = PAMnp.nonzero()	# Obtaining to coordinates (indices) of the final positions of tubes in the rack
	# The following lines save the output to a text file
	
	k=0
	myfile = open('finaltubepositions.txt','w')
	for j in range(len(PAMnp_nonzero[0])):
		myfile.write("({0}, {1})\n" .format(PAMnp_nonzero[0][k],PAMnp_nonzero[1][k]))
	k=k+1
	array3np = np.array(array3)
	
	k=0
	for j in range(len(array3np)):
		myfile.write("({0}, {1})\tremoved\n" .format(array3np[k][0],array3np[k][1]))
		k=k+1
	myfile.close()
	outfile = open('finaltubepositions.txt','r')
	print("\n")
	print(outfile.read())
	outfile.close()
	print("\nThe output shown above has been saved in 'finaltubepositions.txt'\n")

if __name__ == '__main__':
	main()
