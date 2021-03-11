# flake8: noqa

from selfdrive.car import dbc_dict
from cereal import car
Ecu = car.CarParams.Ecu

class CarControllerParams:
  STEER_MAX = 261         # 262 faults
  STEER_DELTA_UP = 2      # 3 is stock. 100 is fine. 200 is too much it seems
  STEER_DELTA_DOWN = 2    # no faults on the way down it seems
  STEER_ERROR_MAX = 80


class CAR:
  PACIFICA_2017_HYBRID = "CHRYSLER PACIFICA HYBRID 2017"
  PACIFICA_2018_HYBRID = "CHRYSLER PACIFICA HYBRID 2018"
  PACIFICA_2019_HYBRID = "CHRYSLER PACIFICA HYBRID 2019"
  PACIFICA_2018 = "CHRYSLER PACIFICA 2018"  # includes 2017 Pacifica
  PACIFICA_2020 = "CHRYSLER PACIFICA 2020"
  JEEP_CHEROKEE = "JEEP GRAND CHEROKEE V6 2018"  # includes 2017 Trailhawk
  JEEP_CHEROKEE_2019 = "JEEP GRAND CHEROKEE 2019" # includes 2020 Trailhawk

# Unique can messages:
# Only the hybrids have 270: 8
# Only the gas have 55: 8, 416: 7
# For 564, All 2017 have length 4, whereas 2018-19 have length 8.
# For 924, Pacifica 2017 has length 3, whereas all 2018-19 have length 8.
# For 560, All 2019 have length 8, whereas all 2017-18 have length 4.

# Jeep Grand Cherokee unique messages:
# 2017 Trailhawk: 618: 8
# For 924, Trailhawk 2017 has length 3, whereas 2018 V6 has length 8.

FINGERPRINTS = {
  CAR.PACIFICA_2017_HYBRID: [
    {168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 515: 7, 516: 7, 517: 7, 518: 7, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 4, 571: 3, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 701: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 788:3, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 908: 8, 924: 3, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 956: 8, 958: 8, 959: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1225: 8, 1235: 8, 1242: 8, 1246: 8, 1250: 8, 1284: 8, 1537: 8, 1538: 8, 1562: 8, 1568: 8, 1856: 8, 1858: 8, 1860: 8, 1865: 8, 1875: 8, 1882: 8, 1886: 8, 1890: 8, 1892: 8, 2016: 8, 2024: 8},
  ],
  CAR.PACIFICA_2018: [
    {55: 8, 257: 5, 258: 8, 264: 8, 268: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 516: 7, 517: 7, 520: 8, 524: 8, 526: 6, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 656: 4, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 746: 5, 752: 2, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 924: 8, 926: 3, 937: 8, 947: 8, 948: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1098: 8, 1100: 8, 1537: 8, 1538: 8, 1562: 8},
    {55: 8, 257: 5, 258: 8, 264: 8, 268: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 516: 7, 517: 7, 520: 8, 524: 8, 526: 6, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 4, 571: 3, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 656: 4, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 746: 5, 752: 2, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 924: 3, 926: 3, 937: 8, 947: 8, 948: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1098: 8, 1100: 8, 1537: 8, 1538: 8, 1562: 8},
  ],
  CAR.PACIFICA_2020: [
    {
      55: 8, 179: 8, 181: 8, 257: 5, 258: 8, 264: 8, 268: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 650: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 676: 8, 678: 8, 680: 8, 683: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 847: 1, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 906: 8, 924: 8, 926: 3, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1223: 7, 1225: 8, 1235: 8, 1242: 8, 1246: 8, 1250: 8, 1251: 8, 1252: 8, 1284: 8, 1568: 8, 1570: 8, 1856: 8, 1858: 8, 1860: 8, 1863: 8, 1865: 8, 1875: 8, 1882: 8, 1886: 8, 1890: 8, 1891: 8, 1892: 8, 2016: 8, 2017:8, 2024: 8, 2025: 8
    }
  ],
  CAR.PACIFICA_2018_HYBRID: [
    {68: 8, 168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 680: 8, 701: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 736: 8, 737: 8, 746: 5, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8},
    # based on 9ae7821dc4e92455|2019-07-01--16-42-55
    {168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 515: 7, 516: 7, 517: 7, 518: 7, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 701: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 969: 4, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1225: 8, 1235: 8, 1242: 8, 1246: 8, 1250: 8, 1251: 8, 1252: 8, 1258: 8, 1259: 8, 1260: 8, 1262: 8, 1284: 8, 1537: 8, 1538: 8, 1562: 8, 1568: 8, 1856: 8, 1858: 8, 1860: 8, 1865: 8, 1875: 8, 1882: 8, 1886: 8, 1890: 8, 1891: 8, 1892: 8, 1898: 8, 1899: 8, 1900: 8, 1902: 8, 2016: 8, 2018: 8, 2019: 8, 2020: 8, 2023: 8, 2024: 8, 2026: 8, 2027: 8, 2028: 8, 2031: 8},
  ],
  CAR.PACIFICA_2019_HYBRID: [
    {168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 515: 7, 516: 7, 517: 7, 518: 7, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 680: 8, 701: 8, 703: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 736: 8, 737: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 906: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1538: 8},
    # Based on 0607d2516fc2148f|2019-02-13--23-03-16
    {
      168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 701: 8, 703: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 906: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1537: 8
    },
    # Based on 3c7ce223e3571b54|2019-05-11--20-16-14
    {
      168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 701: 8, 703: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 906: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1562: 8, 1570: 8
    },
    {
      168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 515: 7, 516: 7, 517: 7, 518: 7, 520: 8, 524: 8, 526: 6, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 650: 8, 653: 8, 654: 8, 655: 8, 656: 4, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 683: 8, 701: 8, 703: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 738: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 897: 8, 906: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 2015: 8, 2016: 8, 2024: 8
    },
    # Based on "8190c7275a24557b|2020-02-24--09-57-23"
    {
      168: 8, 257: 5, 258: 8, 264: 8, 268: 8, 270: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 291: 8, 292: 8, 294: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 368: 8, 376: 3, 384: 8, 388: 4, 448: 6, 456: 4, 464: 8, 469: 8, 480: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 528: 8, 532: 8, 542: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 624: 8, 625: 8, 632: 8, 639: 8, 650: 8, 656: 4, 653: 8, 654: 8, 655: 8, 658: 6, 660: 8, 669: 3, 671: 8, 672: 8, 678: 8, 680: 8, 683: 8, 701: 8, 703: 8, 704: 8, 705: 8, 706: 8, 709: 8, 710: 8, 711: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 738: 8, 746: 5, 752: 2, 754: 8, 760: 8, 764: 8, 766: 8, 770: 8, 773: 8, 779: 8, 782: 8, 784: 8, 792: 8, 793: 8, 794: 8, 795: 8, 796: 8, 797: 8, 798: 8, 799: 8, 800: 8, 801: 8, 802: 8, 803: 8, 804: 8, 805: 8, 807: 8, 808: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 832: 8, 838: 2, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 878: 8, 882: 8, 886: 8, 897: 8, 906: 8, 908: 8, 924: 8, 926: 3, 929: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 958: 8, 959: 8, 962: 8, 969: 4, 973: 8, 974: 5, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1082: 8, 1083: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1225: 8, 1235: 8, 1242: 8, 1246: 8, 1250: 8, 1251: 8, 1252: 8, 1258: 8, 1259: 8, 1260: 8, 1262: 8, 1284: 8, 1568: 8, 1570: 8, 1856: 8, 1858: 8, 1860: 8, 1863: 8, 1865: 8, 1875: 8, 1882: 8, 1886: 8, 1890: 8, 1891: 8, 1892: 8, 1898: 8, 1899: 8, 1900: 8, 1902: 8, 2015: 8, 2016: 8, 2017: 8, 2018: 8, 2019: 8, 2020: 8, 2023: 8, 2024: 8, 2026: 8, 2027: 8, 2028: 8, 2031: 8
    }
  ],
  CAR.JEEP_CHEROKEE: [
    # JEEP GRAND CHEROKEE V6 2018
    {55: 8, 168: 8, 181: 8, 256: 4, 257: 5, 258: 8, 264: 8, 268: 8, 272: 6, 273: 6, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 352: 8, 362: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 4, 571: 3, 579: 8, 584: 8, 608: 8, 618: 8, 624: 8, 625: 8, 632: 8, 639: 8, 656: 4, 658: 6, 660: 8, 671: 8, 672: 8, 676: 8, 678: 8, 680: 8, 683: 8, 684: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 738: 8, 746: 5, 752: 2, 754: 8, 760: 8, 761: 8, 764: 8, 766: 8, 773: 8, 776: 8, 779: 8, 782: 8, 783: 8, 784: 8, 785: 8, 788: 3, 792: 8, 799: 8, 800: 8, 804: 8, 806: 2, 808: 8, 810: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 831: 6, 832: 8, 838: 2, 844: 5, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 906: 8, 924: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 956: 8, 968: 8, 969: 4, 970: 8, 973: 8, 974: 5, 976: 8, 977: 4, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1062: 8, 1098: 8, 1100: 8},
    # Jeep Grand Cherokee 2017 Trailhawk
    {257: 5, 258: 8, 264: 8, 268: 8, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 344: 8, 352: 8, 362: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 4, 564: 4, 571: 3, 584: 8, 608: 8, 618: 8, 624: 8, 625: 8, 632: 8, 639: 8, 658: 6, 660: 8, 671: 8, 672: 8, 680: 8, 684: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 736: 8, 737: 8, 746: 5, 752: 2, 760: 8, 761: 8, 764: 8, 766: 8, 773: 8, 776: 8, 779: 8, 783: 8, 784: 8, 792: 8, 799: 8, 800: 8, 804: 8, 806: 2, 808: 8, 810: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 831: 6, 832: 8, 838: 2, 844: 5, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 924: 3, 937: 8, 947: 8, 948: 8, 969: 4, 974: 5, 977: 4, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1062: 8, 1098: 8, 1100: 8},
  ],
  CAR.JEEP_CHEROKEE_2019: [
    # Jeep Grand Cherokee 2019, including most 2020 models
    {55: 8, 168: 8, 179: 8, 181: 8, 256: 4, 257: 5, 258: 8, 264: 8, 268: 8, 272: 6, 273: 6, 274: 2, 280: 8, 284: 8, 288: 7, 290: 6, 292: 8, 300: 8, 308: 8, 320: 8, 324: 8, 331: 8, 332: 8, 341: 8, 344: 8, 352: 8, 362: 8, 368: 8, 376: 3, 384: 8, 388: 4, 416: 7, 448: 6, 456: 4, 464: 8, 500: 8, 501: 8, 512: 8, 514: 8, 520: 8, 530: 8, 532: 8, 544: 8, 557: 8, 559: 8, 560: 8, 564: 8, 571: 3, 579: 8, 584: 8, 608: 8, 618: 8, 624: 8, 625: 8, 632: 8, 639: 8, 640: 1, 656: 4, 658: 6, 660: 8, 671: 8, 672: 8, 676: 8, 678: 8, 680: 8, 683: 8, 684: 8, 703: 8, 705: 8, 706: 8, 709: 8, 710: 8, 719: 8, 720: 6, 729: 5, 736: 8, 737: 8, 738: 8, 746: 5, 752: 2, 754: 8, 760: 8, 761: 8, 764: 8, 766: 8, 773: 8, 776: 8, 779: 8, 782: 8, 783: 8, 784: 8, 785: 8, 792: 8, 799: 8, 800: 8, 804: 8, 806: 2, 808: 8, 810: 8, 816: 8, 817: 8, 820: 8, 825: 2, 826: 8, 831: 6, 832: 8, 838: 2, 840: 8, 844: 5, 847: 1, 848: 8, 853: 8, 856: 4, 860: 6, 863: 8, 882: 8, 897: 8, 906: 8, 924: 8, 937: 8, 938: 8, 939: 8, 940: 8, 941: 8, 942: 8, 943: 8, 947: 8, 948: 8, 960: 4, 968: 8, 969: 4, 970: 8, 973: 8, 974: 5, 976: 8, 977: 4, 979: 8, 980: 8, 981: 8, 982: 8, 983: 8, 984: 8, 992: 8, 993: 7, 995: 8, 996: 8, 1000: 8, 1001: 8, 1002: 8, 1003: 8, 1008: 8, 1009: 8, 1010: 8, 1011: 8, 1012: 8, 1013: 8, 1014: 8, 1015: 8, 1024: 8, 1025: 8, 1026: 8, 1031: 8, 1033: 8, 1050: 8, 1059: 8, 1062: 8, 1098: 8, 1100: 8, 1216: 8, 1218: 8, 1220: 8, 1223: 8, 1225: 8, 1227: 8, 1235: 8, 1242: 8, 1250: 8, 1251: 8, 1252: 8, 1254: 8, 1264: 8, 1284: 8, 1536: 8, 1537: 8, 1543: 8, 1545: 8, 1562: 8, 1568: 8, 1570: 8, 1572: 8, 1593: 8, 1856: 8, 1858: 8, 1860: 8, 1863: 8, 1865: 8, 1867: 8, 1875: 8, 1882: 8, 1890: 8, 1891: 8, 1892: 8, 1894: 8, 1896: 8, 1904: 8, 2015: 8, 2016: 8, 2017: 8, 2024: 8, 2025: 8},
  ],
}


DBC = {
  CAR.PACIFICA_2017_HYBRID: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.PACIFICA_2018: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.PACIFICA_2020: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.PACIFICA_2018_HYBRID: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.PACIFICA_2019_HYBRID: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.JEEP_CHEROKEE: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
  CAR.JEEP_CHEROKEE_2019: dbc_dict('chrysler_pacifica_2017_hybrid', 'chrysler_pacifica_2017_hybrid_private_fusion'),
}

STEER_THRESHOLD = 120
