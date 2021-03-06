# Copyright 2014 Allen Institute for Brain Science
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Nicholas Cain
# Allen Institute for Brain Science
# June 11 2014
# nicholasc@alleninstitute.org

'''
Created on Dec 6, 2012

@author: nicholasc
'''

class Structure( object ):
    '''
    classdocs
    '''

    @staticmethod
    def from_json(region_dict):
        import_dict = {}
        import_dict['structure_id'] = int(region_dict['id'])
        acronym = str(region_dict['acronym']).strip()
        import_dict['acronym'] = acronym
        import_dict['graph_order'] = int(region_dict['graph_order'])
        import_dict['rgb'] = hex_to_rgb(region_dict['color_hex_triplet'])
        import_dict['path_to_root'] = map(int,region_dict['structure_id_path'][1:-1].split('/'))
        import_dict['name'] = str(region_dict['name'])        

        return Structure(**import_dict)

    '''
    Constructor
    '''
    def __init__(self, **kwargs):
        
        for key, val in kwargs.iteritems():
            setattr(self, key, val)

        self.child_list = None

    def __str__(self):
        return self.acronym

    def is_child_of(self, parent_structure):
        return parent_structure.structure_id in self.path_to_root
    

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv/3], 16) for i in range(0, lv, lv/3))


    


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



