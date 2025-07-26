#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#                                                                             
# PROGRAMMER: Manjeet Singh
# DATE CREATED: 26/07/2025                                 
# REVISED DATE: 
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results 
#          dictionary to indicate whether or not the pet image label is of-a-dog, 
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the 
#          dog name (from dognames.txt) and the 'value' is one. If a label is 
#          found to exist within this dictionary of dog names then the label 
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one 
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog. 
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog 
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the 
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 
    Demonstrates if model architecture correctly classifies dog images even if
    it gets dog breed wrong (not a match).
    Parameters:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
                    List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                  index 1 = classifier label (string)
                  index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
                ------ where index 3 & index 4 are added by this function -----
                 NEW - index 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                 NEW - index 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
     dogfile - A text file that contains names of all dogs from the classifier
               function and dog names from the pet image files. This file has 
               one dog name per line dog names are all in lowercase with 
               spaces separating the distinct words of the dog name. Dog names
               from the classifier function can be a string of dog names separated
               by commas when a particular breed of dog has multiple dog names 
               associated with that breed (ex. maltese dog, maltese terrier, 
               maltese) (string - indicates text file's filename)
    Returns:
           None - results_dic is mutable data type so no return needed.
    """           
    #dogname_dic = dict() 
    dogname_dic = {} # Will store dog names as keys in form of strings and 1 as values
    with open(dogfile, "r") as file:
        for line in file:
            line = line.lower().strip() # Removes leading and trailing whitespace characters
            if line and line not in dogname_dic:
                dogname_dic[line] = 1 # Add dog name to dictionary with value 1
            else:
                print("Duplicate names found in 'dognames.txt' : ", line) # Increment the count for the dog name

    '''
        line = file.readline()
  
    #with open (dogfile, "r") as f:
        #line = f.readline()
        
        while line != "":
        #   line = line.strip()  # Removes leading and trailing whitespace characters
            line = line.lower().rstrip()
            if line not in dogname_dic:
                dogname_dic[line] = 1            
            #line = f.readline()
            line = file.readline() # Read the next line in the file; if not while loop will only read the first line
    '''    
    
    ''' 
    for key in results_dic: # You write this when you want to iterate through the keys in results_dic. 
        if results_dic[key][0] in dogname_dic:        # results_dic[key][0] is value of 'image label' = 'boston terrier' 
            if results_dic[key][1] in dogname_dic:    # results_dic[key][1] is value of 'classifier label' = 'boston terrier'
                results_dic[key].extend([1, 1])       # Perfect match, both labels are dogs
            else:
                results_dic[key].extend([1, 0])       # As this is else from main if considering that Image/pet label is a dog but classifier label is not a dog       
        else:
            if results_dic[key][1] in dogname_dic:    # results_dic[key][1] is value of 'classifier label' = 'boston terrier'
                results_dic[key].extend([0, 1])       # As this is else from main if considering that Image/pet label is not a dog
            else:
                results_dic[key].extend([0, 0])       # Neither label is a dog, so both are 0
    '''            
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        if pet_label in dogname_dic:
            if classifier_label in dogname_dic:
                results_dic[key].extend([1, 1])     # Perfect match, both labels are dogs
            else: 
                results_dic[key].extend([1, 0])     # Only Image label is dog
        else:
            if classifier_label in dogname_dic:
                results_dic[key].extend([0, 1])     # Only classifier label is dog
            else:
                results_dic[key].extend([0, 0])     # neither are dogs 