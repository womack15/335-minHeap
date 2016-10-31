from HeapInt import *
import math

'''
Joshua Womack
CPSC 335
Project #2
Summer 2016
'''

'''*
 * An implementation of a minimum heap with handles
 '''

class Heap:

    '''
    #########################################################
    The constructor has been set up with an initial array of size 4
    so that your doubleHeap() method will be tested.  Don't change
    this!
    #########################################################
    '''
    def __init__(self):
        self.array = [0]*4
        self.heapsize = 0
        self.arraysize = 4






    '''
    #########################################################
    Exchanges that values at positions pos1 and pos2 in the heap array.
    Handles must be exchanged correctly as well.

    Running time = O(n)
    #########################################################
    '''
    def exchange(self, pos1, pos2):
        temp = self.array[pos1]                         # swap
        self.array[pos1] = self.array[pos2]             #
        self.array[pos2] = temp                         #

        self.array[pos1].setHandle(pos1)                # fix handles after swap
        self.array[pos2].setHandle(pos2)                #





    '''
    #########################################################
    Doubles the size of the array.  A new array is created, the elements in
    the heap are copied to the new array, and the array data member is set
    to the new array.  Data member arraysize is set to the size of the
    new array.

    Running time = O(n)
    #########################################################
    '''
    def doubleHeap(self):
        self.array += [0]*self.arraysize    # concantinates 0s to the end of the array
        self.arraysize += self.arraysize    # updates the heap arraysize attribute






    '''
    #########################################################
    Fixes the heap if the value at position pos may be bigger than one of
    its children.  Using exchange() to swap elements will simplify your
    implementation.  HeapElts contain records, and records contain
    keys; you will need to decide how to handle comparisons.

    Running time = O(lg n)
    #########################################################
    '''
    def heapifyDown(self, pos):
        l = self.left(pos)						#assign l the left child of current position
        r = self.right(pos)						#assign r the right child of current position


	    #if value of l is <= the heapsize and the left child value is less the parent value,
		#then assign l to be smallest, else make the parent value the smallest
        if l <= self.heapsize and self.array[l].getKey() < self.array[pos].getKey():
            smallest = l
        else:
            smallest = pos


        #if value of r is < the heapsize and the right child value is less the parent value,
		#then assign r to be smallest
        if r <= self.heapsize and self.array[r].getKey() < self.array[smallest].getKey():
         smallest = r

		#if the smallest value is not equal to the passed position,
		#then call exchange function to swap the two values and
		#call heapifyDown function and pass the new smallest value
        if smallest != pos:
          self.exchange(pos, smallest)
          self.heapifyDown(smallest)






    """
    #########################################################
    Fixes the heap if the value at position pos may be smaller than its
    parent.  Using exchange() to swap elements will simplify your
    implementation.  HeapElts contain records, and records contain
    keys; you will need to decide how to handle comparisons.

    Running time = O(lg n)
    #########################################################
    """
    def heapifyUp(self, pos):
        # while pos is not root and child is less than parent
        while pos > 1 and self.array[self.parent(pos)].getKey() > self.array[pos].getKey():
            self.exchange(self.parent(pos), pos)
            pos = self.parent(pos)                  # updates pos to new swapped position





    '''
    #########################################################
    #########################################################
    '''
    def parent(self, handle):
        return int(math.floor(handle/2))




    '''
    #########################################################
    #########################################################
    '''
    def left(self, handle):
        return 2 * handle




    '''
    #########################################################
    #########################################################
    '''
    def right(self, handle):
        return 2 * handle + 1






    '''
    #########################################################
    Insert inElt into the heap.  Before doing so, make sure that there is
    an open spot in the array for doing so.  If you need more space, call
    doubleHeap() before doing the insertion.

    Running time = O(lg n) (NOTE that there are a couple of different cases
    here!)
    #########################################################
    '''
    def insert(self, inElt):
        print ("In here")
        if self.heapsize >= (self.arraysize - 1):          # check if there is room for a new element
            self.doubleHeap()

        self.heapsize = self.heapsize + 1           # increment heapsize to account for new element
        inElt.setHandle(self.heapsize)          # sets the correct handle of inElt
        self.array[self.heapsize] = inElt       # insert element into the next available position
        self.heapifyUp(self.heapsize)           # passes handle into heapifyUp
        print ("Out here")





    '''
    #########################################################
    Remove the minimum element from the heap and return it.  Restore
    the heap to heap order.  Assumes heap is not empty, and will
    cause an exception if the heap is empty.

    Running time = O(lg n)
    #########################################################
    '''
    def removeMin(self):
        if self.heapsize < 1:					#check if heap is empty and print error if it is
            print("No heap available")
        else:
            self.exchange(1, self.heapsize)	        #swap root with the last node of the heap
            self.heapsize = self.heapsize - 1	    #decrement size of heap by 1
            self.heapifyDown(1)					    #call heapifyDown and pass in top of the heap
            return (self.array[self.heapsize + 1])	#return the min value that has been removed







    '''
    #########################################################
    Return the number of elements in the heap..

    Running time = O(1)
    #########################################################
    '''
    def getHeapsize(self):
        return self.heapsize





    '''
    #########################################################
    Print out the heap for debugging purposes.  It is recommended to
    print both the key from the record and the handle.

    Running time = O(n)
    #########################################################
    '''
    def printHeap(self):
        for i in range(self.getHeapsize()):
            print self.array[i + 1]


