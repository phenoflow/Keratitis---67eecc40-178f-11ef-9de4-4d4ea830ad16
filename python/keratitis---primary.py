# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"F4A2400","system":"readv2"},{"code":"F4A2500","system":"readv2"},{"code":"F4A2200","system":"readv2"},{"code":"F4Az.00","system":"readv2"},{"code":"A984300","system":"readv2"},{"code":"F4A2300","system":"readv2"},{"code":"F4A5400","system":"readv2"},{"code":"AD67000","system":"readv2"},{"code":"F4A..00","system":"readv2"},{"code":"F4A5200","system":"readv2"},{"code":"F4A5500","system":"readv2"},{"code":"20491.0","system":"readv2"},{"code":"39445.0","system":"readv2"},{"code":"6749.0","system":"readv2"},{"code":"53785.0","system":"readv2"},{"code":"27546.0","system":"readv2"},{"code":"56042.0","system":"readv2"},{"code":"30358.0","system":"readv2"},{"code":"10408.0","system":"readv2"},{"code":"90575.0","system":"readv2"},{"code":"94249.0","system":"readv2"},{"code":"1082.0","system":"readv2"},{"code":"72172.0","system":"readv2"},{"code":"15686.0","system":"readv2"},{"code":"35865.0","system":"readv2"},{"code":"44620.0","system":"readv2"},{"code":"48197.0","system":"readv2"},{"code":"5176.0","system":"readv2"},{"code":"55629.0","system":"readv2"},{"code":"45610.0","system":"readv2"},{"code":"24948.0","system":"readv2"},{"code":"27900.0","system":"readv2"},{"code":"72913.0","system":"readv2"},{"code":"12131.0","system":"readv2"},{"code":"94899.0","system":"readv2"},{"code":"20305.0","system":"readv2"},{"code":"27749.0","system":"readv2"},{"code":"9279.0","system":"readv2"},{"code":"40792.0","system":"readv2"},{"code":"50273.0","system":"readv2"},{"code":"35193.0","system":"readv2"},{"code":"72393.0","system":"readv2"},{"code":"49802.0","system":"readv2"},{"code":"16413.0","system":"readv2"},{"code":"27797.0","system":"readv2"},{"code":"44027.0","system":"readv2"},{"code":"107617.0","system":"readv2"},{"code":"11319.0","system":"readv2"},{"code":"27545.0","system":"readv2"},{"code":"101578.0","system":"readv2"},{"code":"29763.0","system":"readv2"},{"code":"45168.0","system":"readv2"},{"code":"3581.0","system":"readv2"},{"code":"7287.0","system":"readv2"},{"code":"515.0","system":"readv2"},{"code":"H16","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('keratitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["keratitis---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["keratitis---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["keratitis---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
