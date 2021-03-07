(1) how to setup and run your program:
	First, filter the row whose 'TEMP' is '-99.000' or '-999.000'. Use list(filter()) to do this. Then, filter the row whose 'station_id' is 'C0A880' or 'C0F9A0'..., separately. And we get 5 lists. Next, we use 'max()' to calculate the maximum if the 'TEMP' of each weather station and use 'append()' to add these values into a list called 'result'. After using 'sort()' to sort the result, we print the output.

(2) what are the results:
In the terminal:
ee2405@ubuntu:~/ee2405/hw1$ python3 main.py
[('C0A880', 27.1), ('C0F9A0', 31.0), ('C0G640', 29.5), ('C0R190', 31.2), ('C0X260', 31.6)]s

