# flake8: noqa

from cereal import car
from selfdrive.car import dbc_dict
Ecu = car.CarParams.Ecu

class CarControllerParams():

  STEER_STEP = 2  # control frames per command
  MIN_STEER_SPEED = 3.  # m/s
  NEAR_STOP_BRAKE_PHASE = 0.5  # m/s

  # Heartbeat for dash "Service Adaptive Cruise" and "Service Front Camera"
  ADAS_KEEPALIVE_STEP = 100
  CAMERA_KEEPALIVE_STEP = 100

  # pedal lookups, only for Volt
  MAX_GAS = 3072  # Only a safety limit
  ZERO_GAS = 2048
  MAX_BRAKE = 350  # Should be around 3.5m/s^2, including regen

  # Allow small margin below -3.5 m/s^2 from ISO 15622:2018 since we
  # perform the closed loop control, and might need some

  # Our controller should still keep the 2 second average above
  # -3.5 m/s^2 as per planner limits
  ACCEL_MAX = 2.0
  ACCEL_MIN = -3.5
  # ACCEL_SCALE = 3.5  # max(ACCEL_MAX, -ACCEL_MIN)

  # MAX_ACC_REGEN = 1404  # ACC Regen braking is slightly less powerful than max regen paddle
  # GAS_LOOKUP_BP = [-1, 0., ACCEL_MAX]
  # GAS_LOOKUP_V = [MAX_ACC_REGEN, ZERO_GAS, MAX_GAS]
  # BRAKE_LOOKUP_BP = [ACCEL_MIN, -1]
  # BRAKE_LOOKUP_V = [MAX_BRAKE, 0]
  # ACCEL_HYST_GAP = 0.02
  def __init__(self, CP):
    self.STEER_MAX = 300   # 409 is the max, 255 is stock
    self.STEER_DELTA_UP = 7
    self.STEER_DELTA_DOWN = 17
    self.STEER_DRIVER_ALLOWANCE = 50
    self.STEER_DRIVER_MULTIPLIER = 4
    self.STEER_DRIVER_FACTOR = 100

STEER_THRESHOLD = 1.0

class CAR:
  BOLT_EV = "CHEVROLET BOLT EV"


class CruiseButtons:
  INIT = 0
  UNPRESS = 1
  RES_ACCEL = 2
  DECEL_SET = 3
  MAIN = 5
  CANCEL = 6

class AccState:
  OFF = 0
  ACTIVE = 1
  FAULTED = 3
  STANDSTILL = 4

class CanBus:
  POWERTRAIN = 0
  OBSTACLE = 1
  CHASSIS = 2
  SW_GMLAN = 3
  LOOPBACK = 128

FINGERPRINTS = {

  CAR.BOLT_EV: [
  # Bolt Premier w/o ACC 2017
  {
    170: 8, 188: 8, 189: 7, 190: 6, 192: 5, 193: 8, 197: 8, 201: 6, 209: 7, 211: 2, 241: 6, 289: 1, 290: 1, 298: 8, 304: 8, 309: 8, 311: 8, 313: 8, 320: 8, 322: 7, 328: 1, 352: 5, 353: 3, 368: 8, 381: 6, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 458: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 5, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 1, 508: 8, 512: 3, 514: 2, 516: 4, 519: 2, 521: 3, 528: 5, 530: 8, 532: 7, 537: 5, 539: 8, 542: 7, 546: 7, 550: 8, 554: 3, 558: 8, 560: 6, 562: 4, 563: 5, 564: 5, 565: 8, 566: 6, 567: 5, 568: 1, 569: 3, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 832: 8, 840: 6, 842: 6, 844: 8, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 5, 1003: 5, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1601: 8, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2020: 8, 2024: 8, 2028: 8
  },
  # Bolt Premier no ACC 2019
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 381: 8, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 2, 508: 8, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 7, 567: 5, 568: 2, 569: 3, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 975: 2, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1037: 5, 1105: 5, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1236: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1268: 2, 1275: 3, 1279: 4, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2024: 8
  },
  # Bolt Premier no ACC 2019 + Pedal
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 381: 8, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 2, 508: 8, 512: 6, 513: 6, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 7, 567: 5, 568: 2, 569: 3, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 975: 2, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1037: 5, 1105: 5, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1236: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1268: 2, 1275: 3, 1279: 4, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2024: 8
  },
  # Bolt Premier no ACC 2020
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 381: 8, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 2, 508: 8, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 7, 567: 5, 568: 2, 569: 3, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 975: 2, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1037: 5, 1105: 5, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1236: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1268: 2, 1275: 3, 1279: 4, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2024: 8
  },
  # Bolt Premier no ACC 2020 2
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 368: 3, 381: 8, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 2, 508: 8, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 7, 567: 5, 568: 2, 569: 3, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 866: 4, 872: 1, 961: 8, 967: 4, 969: 8, 975: 2, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1037: 5, 1105: 5, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1236: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1279: 4, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1922: 7, 1927: 7
  },
  # Bolt Premier no ACC 2020 w pedal
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 288: 5, 298: 8, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 368: 3, 381: 8, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 2, 508: 8, 512: 6, 513: 6, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 7, 567: 5, 568: 2, 569: 3, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 753: 5, 761: 7, 810: 8, 840: 5, 842: 5, 844: 8, 848: 4, 866: 4, 872: 1, 961: 8, 967: 4, 969: 8, 975: 2, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1037: 5, 1105: 5, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1236: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1279: 4, 1280: 4, 1300: 8, 1322: 6, 1323: 4, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1922: 7, 1927: 7
  },
  # Bolt EV Premier 2017
  {
    170: 8, 188: 8, 189: 7, 190: 6, 192: 5, 193: 8, 197: 8, 201: 6, 209: 7, 211: 2, 241: 6, 289: 1, 290: 1, 298: 8, 304: 8, 309: 8, 311: 8, 313: 8, 320: 8, 322: 7, 328: 1, 352: 5, 353: 3, 368: 8, 381: 6, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 458: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 5, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 1, 508: 8, 512: 3, 514: 2, 516: 4, 519: 2, 521: 3, 528: 5, 530: 8, 532: 7, 537: 5, 539: 8, 542: 7, 546: 7, 550: 8, 554: 3, 558: 8, 560: 6, 562: 4, 563: 5, 564: 5, 565: 8, 566: 6, 567: 5, 568: 1, 569: 3, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 832: 8, 840: 6, 842: 6, 844: 8, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 5, 1003: 5, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1601: 8, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2020: 8, 2024: 8, 2028: 8
  },
  # Bolt EV Premier 2017 w Pedal
  {
    170: 8, 188: 8, 189: 7, 190: 6, 192: 5, 193: 8, 197: 8, 201: 6, 209: 7, 211: 2, 241: 6, 289: 1, 290: 1, 298: 8, 304: 8, 309: 8, 311: 8, 313: 8, 320: 8, 322: 7, 328: 1, 352: 5, 353: 3, 368: 8, 381: 6, 384: 4, 386: 8, 388: 8, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 458: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 5, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 1, 508: 8, 512: 3, 512: 6, 513: 6, 514: 2, 516: 4, 519: 2, 521: 3, 528: 5, 530: 8, 532: 7, 537: 5, 539: 8, 542: 7, 546: 7, 550: 8, 554: 3, 558: 8, 560: 6, 562: 4, 563: 5, 564: 5, 565: 8, 566: 6, 567: 5, 568: 1, 569: 3, 573: 1, 577: 8, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 832: 8, 840: 6, 842: 6, 844: 8, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 5, 1003: 5, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1601: 8, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1927: 7, 2016: 8, 2020: 8, 2024: 8, 2028: 8
  },
  # Bolt EV Premier 2017 2 w Pedal
  {
    170: 8, 188: 8, 189: 7, 190: 6, 193: 8, 197: 8, 201: 8, 209: 7, 211: 2, 241: 6, 298: 8, 304: 1, 308: 4, 309: 8, 311: 8, 313: 8, 320: 3, 322: 7, 328: 1, 352: 5, 353: 3, 381: 6, 384: 8, 386: 8, 388: 4, 390: 7, 407: 7, 417: 7, 419: 1, 451: 8, 452: 8, 453: 6, 454: 8, 456: 8, 463: 3, 479: 3, 481: 7, 485: 8, 489: 8, 493: 8, 495: 4, 497: 8, 499: 3, 500: 6, 501: 8, 503: 1, 508: 8, 513: 6, 528: 5, 532: 6, 546: 7, 550: 8, 554: 3, 558: 8, 560: 8, 562: 8, 563: 5, 564: 5, 565: 5, 566: 6, 567: 5, 568: 1, 573: 1, 608: 8, 609: 6, 610: 6, 611: 6, 612: 8, 613: 8, 647: 3, 707: 8, 711: 6, 717: 5, 753: 5, 761: 7, 800: 6, 810: 8, 840: 5, 842: 5, 844: 8, 866: 4, 869: 4, 872: 1, 961: 8, 967: 4, 969: 8, 977: 8, 979: 7, 985: 5, 988: 6, 989: 8, 995: 7, 1001: 8, 1005: 6, 1009: 8, 1013: 3, 1017: 8, 1019: 2, 1020: 8, 1022: 1, 1105: 6, 1187: 4, 1217: 8, 1221: 5, 1223: 3, 1225: 7, 1227: 4, 1233: 8, 1243: 3, 1249: 8, 1257: 6, 1265: 8, 1275: 3, 1280: 4, 1300: 8, 1322: 6, 1328: 4, 1904: 7, 1905: 7, 1906: 7, 1907: 7, 1912: 7, 1913: 7, 1922: 7, 1927: 7
  }],

}

DBC = {
  CAR.BOLT_EV: dbc_dict('gm_global_a_powertrain', 'gm_global_a_object', chassis_dbc='gm_global_a_chassis'),

}




def main():
  for member, value in vars(CAR).items():
    if not member.startswith("_"):
      print(value)


if __name__ == "__main__":
  main()

