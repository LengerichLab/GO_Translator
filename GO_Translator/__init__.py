import numpy as np
import os

class Term:
    def __init__(self, id, name, namespace, defn, synonym, is_a):
        self.id = id
        self.name = name
        self.namespace = namespace
        self.defn = defn
        self.synonym = synonym
        self.is_a = is_a

def create_terms(my_path):
    by_id = {}
    by_name = {}

    n_parsed = 0

    cur_id = None
    cur_name = None
    cur_namespace = None
    cur_defn = None
    cur_synonym = None
    cur_isa = None
    cur_alt_id = []

    with open(os.path.join(my_path, "go.obo"), 'r') as term_file:
        for line in term_file:
            if '[Term]' in line:
                # New term
                n_parsed += 1
                new_term = Term(cur_id, cur_name, cur_namespace, cur_defn, cur_synonym, cur_isa)
                by_id[cur_id] = new_term
                by_name[cur_name] = new_term
                cur_id = None
                cur_name = None
                cur_namespace = None
                cur_defn = None
                cur_synonym = None
                cur_isa = None
            if 'alt_id: ' in line:
                cur_alt_id.append(line.split("alt_id")[1].strip())
            elif 'id: ' in line:
                cur_id = line.split('id: ')[1].strip()
            elif 'name: ' in line:
                cur_name = line.split('name: ')[1].strip()
            elif 'namespace: ' in line:
                cur_namespace = line.split('namespace: ')[1].strip()
            elif 'def: ' in line:
                cur_defn = line.split('def: ')[1].strip()
            elif 'synonym: ' in line:
                cur_synonym = line.split('synonym: ')[1].strip()
            elif 'is_a: ' in line:
                cur_isa = line.split('is_a: ')[1].strip()

    print("Parsed {} terms.".format(n_parsed))
    print("{} Indexed by ID".format(len(by_id)))
    print("{} Indexed by name".format(len(by_name)))
    np.save(os.path.join(my_path, "go_terms_by_id.npy"), by_id)
    np.save(os.path.join(my_path, "go_terms_by_name.npy"), by_name)

my_path = '/' + os.path.join(*os.path.realpath(__file__).split("/")[:-1])
if not os.path.exists(os.path.join(my_path, "./go_terms_by_id.npy")):
    create_terms(my_path)

go_terms_by_id   = np.load(os.path.join(my_path, "go_terms_by_id.npy"), allow_pickle=True).flat[0]
go_terms_by_name = np.load(os.path.join(my_path, "go_terms_by_name.npy"), allow_pickle=True).flat[0]
