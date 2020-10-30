import random
import string

letters = string.ascii_lowercase

# Generates random string of length equal to `num`
def _gen_string(num):
    result_str = ''.join(random.choice(letters) for i in range(num))
    return(result_str)

def _gen_int(num):
    lower_bound = 10 ** (num - 1)
    upper_bound = 10 ** num - 1
    return(random.randint(lower_bound,upper_bound))


num_tags = 2
num_tag_values = 11
tag_value_size=10
tag_key_size=10
int_fields = 2
str_fields = 1
float_fields = 1
field_key_size = 10
int_value_size = 4
str_value_size = 10
float_value_size = 8

num_lines = num_tag_values/num_tags

# Tag and Field key-value maps (dicts) are classes to make it easier to work with multiple of them.
# If it makes sense to later split up workloads into different logical groupings, this will help.

# Maps Tag keys to all Tag values (may consider having each Tag key get values/keys at a later date)
class TagMap():
    def __init__(self, 
                num_tags=2,
                num_tag_values=11,
                tag_value_size=10,
                tag_key_size=10)

        self.num_tags = num_tags
        self.num_tag_values = 11
        self.tag_value_size = 10
        self.tag_key_size = 10
        # Use abbove vars to create lists of keys and values to be iterated through later
        self.tag_keys = ['tag_' + _gen_string(self.tag_key_size-4) for tag_key in range(self.num_tags)]
        self.tag_values = [_gen_string(tag_value_size) for tag_value in range(num_tag_values/num_tags)]
        # Use above lists to create key-value mappings in a dictionary to be used later
        self.tags_map = {k:[v for v in tag_values] for k in tag_keys}
        print(tags_map)
        return(tags_map)
    
# Maps Field keys to all Tag values (may consider having each Field key get values/keys at a later date)
class FieldMap():
    def __init__(self, 
                int_fields=2, 
                str_fields=1, 
                float_fields=1,
                field_key_size=10,
                int_value_size=4,
                str_value_size=10,
                float_value_size=4)

        self.int_fields=int_fields
        self.str_fields = str_fields
        self.float_fields = float_fields
        self.field_key_size = field_key_size
        self.int_value_size = int_value_size
        self.str_value_size = str_value_size
        self.float_value_size = float_value_size
        
        self.field_map = {}
        # Creates integer field mappings --> number of requested keys to number of values needed to satisfy
        if self.int_fields:
            self.int_field_keys = ['int_' + _gen_string(field_key_size-4) for field_key in range(int_fields)]
            self.int_field_values = [_gen_int(int_value_size) for int_value in range(num_lines)]

            # Map keys to values
            self.int_fields_map = {k: [v for v in int_field_values] for k in int_field_keys}
            self.field_map.update(self.int_fields_map)

        # Creates string field mappings --> number of requested keys to number of values needed to satisfy
        if self.str_fields:
            self.str_field_keys = ['str_' + _gen_string(self.field_key_size-4) for field_key in range(self.str_fields)]
            self.str_field_values = [_gen_string(self.str_value_size) for field_value in range(self.num_lines)]
            
            self.str_fields_map = {k: [v for v in self.str_field_values] for k in self.str_field_keys}

            self.field_map.update(self.str_fields_map)
        # Creates float field mappings --> number of requested keys to number of values needed to satisfy
        if self.float_fields:
            self.float_field_keys = ['fl_' + _gen_string(self.field_key_size-3) for field_key in range(self.float_fields)]
            self.float_field_values = [round(random.uniform(10,99), self.float_value_size-2) for field_value in range(num_lines)]
            self.float_fields_map = {k: [v for v in float_field_values] for k in str_field_keys}

            self.field_map.update(self.float_fields_map)
        
        print(str_fields_map, int_fields_map, float_fields_map)

        return(int_fields_map, str_fields_map, float_fields_map)

_gen_tag_map()

_gen_field_map()