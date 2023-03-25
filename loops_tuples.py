#!/usr/bin/python3

# Data table
bits_data = [];
last_bit_value = None;

# Loop through items table
for index in range(1, 9):
	if (index == 1):
		bits_data.append(index);
		last_bit_value = index;
		continue;
		
	bit_value = (last_bit_value != None and last_bit_value or index) * 2;
	last_bit_value = bit_value;
	bits_data.append(bit_value);
	
	
print(f"Base2 values in 8 bits are {bits_data[:len(bits_data)]}");