#!/usr/bin/python3
import re;

# Indicator
ip_address = input("IP Address: ");
success = re.match("^[A-Za-z,-]*$", ip_address);
error_count = 0;

# Wait for valid input
while not success == None:
	print("Invalid input! IP format XXX.XXX.XXX");
	error_count += 1;
	
	# Check error count
	if (error_count > 2):
		break
	
	ip_address = input("IP Address: ");
	success = re.match("^[A-Za-z,-]*$", ip_address);
	
# Check error count
if (error_count > 2):
	print("Too many failures please excute and try again!")
else:	
	# Indicator
	error_count = 0;
	subnet_mask = input("Subnet Mask: ");
	success = re.match("^[A-Za-z,-]*$", subnet_mask);

	# Wait for valid input
	while not success == None:
		print("Invalid input! Mask format XXX.XXX.XXX");
		error_count += 1;

		# Check error count
		if (error_count > 2):
			break;

		subnet_mask = input("IP Address: ");
		success = re.match("^[A-Za-z,-]*$", subnet_mask);


	# Check error count
	if (error_count > 2):
		print("Too many failures please excute and try again!");
	else:
		print(f"Applying IP {ip_address} and Mask {subnet_mask} to device!");


	