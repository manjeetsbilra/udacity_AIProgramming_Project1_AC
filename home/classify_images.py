#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Manjeet Singh
# DATE CREATED: 25/07/2025                              
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the functin call within main.
#            -The CNN model architecture as model wihtin classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 

# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function. Be sure to
    format the classifier labels so that they will match your pet image labels.
    The format will include putting the classifier labels in all lower case 
    letters and strip the leading and trailing whitespace characters from them.
    For example, the Classifier function returns = 'Maltese dog, Maltese terrier, Maltese' 
    so the classifier label = 'maltese dog, maltese terrier, maltese'.
    Recall that dog names from the classifier function can be a string of dog 
    names separated by commas when a particular breed of dog has multiple dog 
    names associated with that breed. For example, you will find pet images of
    a 'dalmatian'(pet label) and it will match to the classifier label 
    'dalmatian, coach dog, carriage dog' if the classifier function correctly 
    classified the pet images of dalmatians.
     PLEASE NOTE: This function uses the classifier() function defined in 
     classifier.py within this function. The proper use of this function is
     in test_classifier.py Please refer to this program prior to using the 
     classifier() function to classify images within this function 
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    for key in results_dic:          #results_dic = {'Boston_terrier_02250.jpg': ['boston terrier'], 'ZTxer_01120.jpg': ['ztxer'], 'Alex_5656.jpg': ['alex']}
        # get classifier labels
        classifier_label = classifier(images_dir+key, model) # images_dir+key = 'pet_images/Boston_terrier_02250.jpg'
        # images_dir = 'pet_images/' # folder where all images are stored
        # key = 'Boston_terrier_02250.jpg'

        #lowercase and remove white spaces
        classifier_label = classifier_label.lower().strip()  # string.lower() converts all characters to lowercase, strip() removes leading and trailing whitespace      
        
        key_image_label = results_dic[key][0] # Key = 'Boston_terrier_02250.jpg' and results_dic[key][0] = 'boston terrier'
        # key_image_label = results_dic[key][0]
        if key_image_label in classifier_label:
            results_dic[key].extend([classifier_label, 1]) # extends --> (['boston terrier',1])
          # results_dic[key] = ['boston terrier', 'boston terrier', 1]
           # results_dic[key] = ['boston terrier', 'boston terrier', 1]
           # my_list = [1, 2]
           # my_list.extend([3, 4])  # Result: [1, 2, 3, 4]
           # my_list.append([3, 4])  # Would result: [1, 2, [3, 4]]
        else:
            #results_dic[[key][0]].extend([classifier_label, 0])
            results_dic[key].extend([classifier_label, 0])
        
'''
      MSB --> Logic:

# Initialize with some parameters for dictionary
# Defining lists to populate dictionary
filenames = ["Beagle_01141.jpg", "Beagle_01125.jpg", "skunk_029.jpg"] # key as filename of results_dic
pet_labels = ["beagle", "beagle", "skunk"] # [0] of results_dic
classifier_labels = ["walker hound, walker foxhound", "beagle",
                     "skunk, polecat, wood pussy"] # [1] of results_dic
pet_label_classifier_label_match = [0, 1, 1] # [2] of results_dic
pet_label_is_dog = [1, 1, 0] # [3] of results_dic
classifier_label_is_dog = [0, 1, 1] # [4] of results_dic

# Create empty dictionary
results_dic = {}

# Populate dictionary with both labels & indicates if they match (idx 2)
for idx in range(len(filenames)):
    if filenames[idx] not in results_dic:
        results_dic[filenames[idx]] = [
            pet_labels[idx],
            classifier_labels[idx],
            pet_label_classifier_label_match[idx],
            pet_label_is_dog[idx],
            classifier_label_is_dog[idx]
        ]

print(f"This is results_dic = {results_dic}", "\n")

# Print details for each key
for key in results_dic:
    print(f"Analyzing {key}: {results_dic[key]}")
    print(f"  [2] Breed match: {results_dic[key][2]}")
    print(f"  [3] Pet is dog: {results_dic[key][3]}")
    print(f"  [4] Classifier is dog: {results_dic[key][4]}")
    print(f"  Sum [2:]: {sum(results_dic[key][2:])}")
    print(f"  Sum [3:]: {sum(results_dic[key][3:])}")
    print()

print("=" * 60)
print("CLASSIFICATION RESULTS:")
print("=" * 60)

for key in results_dic:
    # Use elif to ensure only one condition is met per key
    if sum(results_dic[key][2:]) == 3:
        print(f"{key}: *Breed Match* *IS dog* - Perfect match!")

    elif (sum(results_dic[key][3:]) == 0) and (results_dic[key][2] == 1):
        print(f"{key}: *Breed Match* *NOT a Dog* - Correct non-dog classification")

    elif sum(results_dic[key][3:]) == 2 and (results_dic[key][2] == 0):
        print(f"{key}: *Breed Mis-match* *IS Dog* - Wrong breed classification by classifier!")

    elif sum(results_dic[key][2:4]) == 0 and results_dic[key][4] == 1:
        print(f"{key}: *Breed Mis-match* *Wrong Classification* - Classifier error")

    else:
        print(f"{key}: Other classification case")
        print(f"  Details: breed_match={results_dic[key][2]}, pet_is_dog={results_dic[key][3]}, classifier_is_dog={results_dic[key][4]}")

    print()
       
         '''
    
    
        
    