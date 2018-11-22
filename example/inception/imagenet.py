# Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
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
# ==============================================================================
"""Provides data for the ImageNet ILSVRC 2012 Dataset plus some bounding boxes.

Some images have one or more bounding boxes associated with the label of the
image. See details here: http://image-net.org/download-bboxes

ImageNet is based upon WordNet 3.0. To uniquely identify a synset, we use
"WordNet ID" (wnid), which is a concatenation of POS ( i.e. part of speech )
and SYNSET OFFSET of WordNet. For more information, please refer to the
WordNet documentation[http://wordnet.princeton.edu/wordnet/documentation/].

"There are bounding boxes for over 3000 popular synsets available.
For each synset, there are on average 150 images with bounding boxes."

WARNING: Don't use for object detection, in this case all the bounding boxes
of the image belong to just one class.
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import os

_NUM_CLASSES = 1001

# If set to false, will not try to set label_to_names in dataset
# by reading them from labels.txt or github.
LOAD_READABLE_NAMES = True


def create_readable_names_for_imagenet_labels():
    """Create a dict mapping label id to human readable string.

    Returns:
        labels_to_names: dictionary where keys are integers from to 1000
        and values are human-readable names.

    We retrieve a synset file, which contains a list of valid synset labels used
    by ILSVRC competition. There is one synset one per line, eg.
            #   n01440764
            #   n01443537
    We also retrieve a synset_to_human_file, which contains a mapping from synsets
    to human-readable names for every synset in Imagenet. These are stored in a
    tsv format, as follows:
            #   n02119247    black fox
            #   n02119359    silver fox
    We assign each synset (in alphabetical order) an integer, starting from 1
    (since 0 is reserved for the background class).

    Code is based on
    https://github.com/tensorflow/models/blob/master/research/inception/inception/data/build_imagenet_data.py#L463
    """

    # pylint: disable=g-line-too-long
 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    filename = dir_path + "\\imagenet_lsvrc_2015_synsets.txt"
    synset_list = [s.strip() for s in open(filename).readlines()]
    num_synsets_in_ilsvrc = len(synset_list)
    assert num_synsets_in_ilsvrc == 1000
    
    filename = dir_path + "\\imagenet_metadata.txt"
    synset_to_human_list = open(filename).readlines()
    num_synsets_in_all_imagenet = len(synset_to_human_list)
    assert num_synsets_in_all_imagenet == 21842
    
    synset_to_human = {}
    for s in synset_to_human_list:
        parts = s.strip().split('\t')
        assert len(parts) == 2
        synset = parts[0]
        human = parts[1]
        synset_to_human[synset] = human
    
    label_index = 1
    labels_to_names = {0: 'background'}
    for synset in synset_list:
        name = synset_to_human[synset]
        labels_to_names[label_index] = name
        label_index += 1
    
    return labels_to_names
