import random
import string

letters = string.ascii_lowercase

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

def _gen_field_map(int_fields=2, 
                    str_fields=1, 
                    float_fields=1,
                    field_key_size=10,
                    int_value_size=4,
                    str_value_size=10,
                    float_value_size=4):
        
    field_map = {}
    # Creates integer field mappings --> number of requested keys to number of values needed to satisfy
    if int_fields:
        int_field_keys = ['int_' + _gen_string(field_key_size-4) for field_key in range(int_fields)]
        int_field_values = [_gen_int(int_value_size) for int_value in range(num_lines)]

        # Map keys to values
        int_fields_map = {k: [v for v in int_field_values] for k in int_field_keys}
        field_map.update(int_fields_map)

    # Creates string field mappings --> number of requested keys to number of values needed to satisfy
    if str_fields:
        str_field_keys = ['str_' + _gen_string(field_key_size-4) for field_key in range(str_fields)]
        str_field_values = [_gen_string(str_value_size) for field_value in range(num_lines)]
        
        str_fields_map = {k: [v for v in str_field_values] for k in str_field_keys}

        field_map.update(str_fields_map)
    # Creates float field mappings --> number of requested keys to number of values needed to satisfy
    if float_fields:
        float_field_keys = ['fl_' + _gen_string(field_key_size-3) for field_key in range(float_fields)]
        float_field_values = [round(random.uniform(10,99), float_value_size-2) for field_value in range(num_lines)]
        float_fields_map = {k: [v for v in float_field_values] for k in str_field_keys}

        field_map.update(float_fields_map)
        print(float_fields_map)
    return field_map

print(_gen_field_map())