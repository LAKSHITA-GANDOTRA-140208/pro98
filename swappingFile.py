import os
import shutil

def swapping():
  source = input("enter source folder name:- ")
  destination = input('enter destination folder name:- ')

  source = source + '/'
  destination = destination + '/'
  f = open(source, 'r')
  data_a=f
  f2=  open(destination, 'r')
  data_b=f2


  list_of_files = os.listdir(source)
  for file in list_of_files:
    if file == "sample1.txt":
      shutil.move((source+file), "sample2.txt")
swapping()