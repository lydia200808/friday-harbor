'''
Created on Dec 6, 2012

@author: nicholasc
'''

import os
import json
from resources.Mask import Mask
import h5py

# Settings:
json_file_save_dir = '../data/src'
json_file_name = 'structure_data.json'
structure_mask_file_name = os.path.join(os.path.dirname(__file__), '../data/src/structure_masks.hdf5')

# Get data:
f = open(os.path.join(os.path.dirname(__file__), json_file_save_dir, json_file_name))
raw_json = json.load(f)
f.close()

class Structure(object):
    '''
    classdocs
    '''

    def __init__(self, import_dict):
        '''
        Constructor
        '''
        
        for key, val in import_dict.items():
            setattr(self, key, val)
            
        self.child_list = None

    def __str__(self):
        return self.acronym

    def is_child_of(self, parent_structure):
        return parent_structure.structure_id in self.path_to_root
    
    @staticmethod
    def get_mask_from_id_nonzero(structure_id):
        curr_acronym = id_structure_dict[structure_id].acronym
        return Mask.read_from_hdf5(structure_mask_file_name, '%s_nonzero' % curr_acronym)
    
    @staticmethod
    def get_mask_from_id_right_hemisphere_nonzero(structure_id):
        curr_acronym = id_structure_dict[structure_id].acronym
        return Mask.read_from_hdf5(structure_mask_file_name, '%s_right_nonzero' % curr_acronym)
    
    @staticmethod
    def get_mask_from_id_left_hemisphere_nonzero(structure_id):
        curr_acronym = id_structure_dict[structure_id].acronym
        return Mask.read_from_hdf5(structure_mask_file_name, '%s_left_nonzero' % curr_acronym)

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))

# Create structure list:
structure_list = []
for region_dict in raw_json['msg']:
    
    import_dict = {}
    
    import_dict['structure_id'] = int(region_dict['id'])
    acronym = str(region_dict['acronym'])
    # Damn 'SUM ' typo:
    if acronym == 'SUM ':
        acronym = 'SUM'
    import_dict['acronym'] = acronym
    import_dict['graph_order'] = int(region_dict['graph_order'])
    import_dict['rgb'] = hex_to_rgb(region_dict['color_hex_triplet'])
    import_dict['path_to_root'] = map(int,region_dict['structure_id_path'][1:-1].split('/'))
    import_dict['name'] = str(region_dict['name'])
    
    structure_list.append(Structure(import_dict))
    
# Set child list:
for s in structure_list:
    s.child_list = [s2 for s2 in structure_list if s2.is_child_of(s)]
 
# Create easy_access dictionaries:
id_structure_dict = {}
acronym_structure_dict = {}
for s in structure_list:
    id_structure_dict[s.structure_id] = s
    acronym_structure_dict[s.acronym] = s



# ii = 1
# print structure_list[ii].structure_id
# L = [x.structure_id for x in structure_list[ii].child_list]
# print L
# print structure_list[ii].child_list[0].path_to_root







# # Function to return list of structures over acceptable size constraint:
# def get_analysis_id_list(voxel_threshold):
#     
#     analysis_id_list = []
#     f=open(os.path.join(path_to_this_file, rel_data_dir, structure_id_source_file_name),'r')
#     for line in f:
#         curr_id, _ = map(int,line.split(','))
#         if size > voxel_threshold:
#             analysis_id_list.append(curr_id)
#     f.close()
# 
#     return analysis_id_list
# 
# # Check to ensure compatibility of structures with size:
# 
# structure_size_dict = {}
# f=open(os.path.join(path_to_this_file, rel_data_dir, structure_id_source_file_name),'r')
# for line in f:
#      
#     curr_id, size = map(int,line.split(','))
#     s = id_structure_dict[curr_id]
#     structure_size_dict[s] = size
# f.close()
#  
# 
#  
# for ii, curr_id in enumerate(x_labels):
#     s = id_structure_dict[curr_id]
#     if s in structure_size_dict.keys():
#         print curr_id, structure_size_dict[s], structure_mask_ipsi[ii,:].sum() + structure_mask_contra[ii,:].sum() 



