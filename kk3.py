print("Enter'0'for exit.");
ch = input("Enter any character:");
if ch=='0':
    exit();
else:
    if((ch>='a' and ch<='z') or (ch>='A' and ch<='Z')):
    	print(character,"is an alphabet.");
    else:
    	print(character,"is not an alphabet.");
