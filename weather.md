weather stantion


# esp32c3_supermini
    Pin     | ADC | func |
GPIO_NUM_0  | A0  |      |bat
GPIO_NUM_1  | A1  |      |service switch
GPIO_NUM_2  | A2  |      |
GPIO_NUM_3  | A3  |      |
GPIO_NUM_4  | A4  | SCK  | 
3V3
GND
5V
-------------------------------------
GPIO_NUM_5  | A5  | MISO |
GPIO_NUM_6  |     | MOSI | bme680 SDA
GPIO_NUM_7  |     | SS   | bme680 SDL
GPIO_NUM_8  |     | SDA  | LED           
GPIO_NUM_9  |     | SDL  | BOOT_BUTTON   
GPIO_NUM_10 |     |      |
GPIO_NUM_20 |     | RX   |
GPIO_NUM_21 |     | TX   |


# bme680
adress 0x77
https://github.com/DiegoPaezA/ESP32-freeRTOS/blob/master/i2c_scanner/main/i2c_scanner.c
https://github.com/espressif/esp-iot-solution/tree/dd15770d0f8c5fedea78809737f04b63d3765c83/examples/sensors/sensor_hub_monitor


# button
todo boot btn to go provision mode?


# esp-idf-lib
https://esp-idf-lib.readthedocs.io/en/latest/index.html
git clone git@github.com:UncleRus/esp-idf-lib.git

# dependency
https://github.com/olemin7/esp32_idf_libs

# TP4056  li ion charger
max 4.2
min 2.5
## li ion
max 4.2
min 3.0

## attenuation
ADC_ATTEN_DB_0   100 mV ~ 950 mV
ADC_ATTEN_DB_2_5 100 mV ~ 1250 mV
ADC_ATTEN_DB_6   150 mV ~ 1750 mV
ADC_ATTEN_DB_12  150 mV ~ 2450 mV

https://docs.espressif.com/projects/esp-idf/en/v4.4.8/esp32/api-reference/peripherals/adc.html

# LiIon
max 4.2
min 3.0

(GND ) -resistor 10k-- (A0) -resistor 10k- (BAT)
ADC_ATTEN_DB_12 and mult 2