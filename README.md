# Panda Excel 🐼
This code aims to read excel files with names of months (january, february, etc) and check if any seller had sales above 55000. If found, the seller and the sales value are printed and a message is sent via Twilio to a specified cell phone number.

# Requirements

* Pandas package
* Twilio package


# Usage
Insert your Twilio credentials (Account SID and Auth Token) in the corresponding variables.
Insert the cell phone number to receive the message in the code.
Make sure the excel files are in the same folder as the code with the month names specified in the "list_mounth" list.
Run the code and check that the messages were sent correctly.


# Notes

The excel file names must be in lowercase and without accentuation.
Make sure the excel files have the "Seller" and "Sales" columns.
Make sure the phone number is in international format (ex: +1xxxxxxxxxx for US)
