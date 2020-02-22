from os import listdir

def get_pet_labels(image_dir):
    results_dic = {}
    for file_name in listdir(image_dir):
        if not file_name.startswith('.'):
            patrs = file_name.split('_')
            label = ' '.join(patrs[:-1]).strip().lower()
            print (label)
            results_dic[file_name] = [label]

    return results_dic
