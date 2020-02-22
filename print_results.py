def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):   
    print("\n\n ** Summary for CNN Model : " + model.upper())
    print(" Number of images : " + str(results_stats_dic['n_images']))
    print(" Number of Dog Images : " + str(results_stats_dic['n_dogs_img']))
    print(' Number of "Not-a" Dog Images : ' + str(results_stats_dic['n_notdogs_img']))
    
    for key in results_stats_dic:
        if key.startswith( 'pct' ):
            key_list = str(key[4:]).split("_")
            if len(key_list) > 1:
                if key_list[1] == "notdogs":
                    key_list[1] = '"not-a" dog'
                print(" " + str(int(results_stats_dic[key])) + '% ' 
                      + key_list[0].capitalize() + " " + key_list[1].capitalize())
            else:
                if key_list[0] == "match":
                    print(" " + str(int((results_stats_dic["pct_correct_dogs"] / 100 
                                   * results_stats_dic["pct_correct_notdogs"] / 100)
                                  * 100)) + "% " + key_list[0].capitalize())
     
    if (print_incorrect_dogs and 
        ( (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
          != results_stats_dic['n_images'] ) 
       ):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results_dic:
            pet_image_is_a_dog = results_dic[key][3]
            classifier_image_as_a_dog = results_dic[key][4]
            
            if(pet_image_is_a_dog == 1 and classifier_image_as_a_dog == 0 or
               pet_image_is_a_dog == 0 and classifier_image_as_a_dog == 1):
                
                print(results_dic)
                              
    if (print_incorrect_breed and 
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']) 
       ):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results_dic:
            if ( sum(results_dic[key][3:]) == 2 and
                results_dic[key][2] == 0 ):
                print("Real: {:>26}   Classifier: {:>30}".format(results_dic[key][0],
                                                          results_dic[key][1]))
                
