wall clock
https://github.com/voed/esphome_max7219_clock/blob/main/esp32clock.yaml
https://ha1tch.github.io/bdf-fonts/font_catalogue.html
https://github.com/trip5/Matrix-Fonts/tree/main

# esp32c3_supermini
    Pin     | ADC | func |
GPIO_NUM_0  | A0  |      |photoresistor
GPIO_NUM_1  | A1  |      |
GPIO_NUM_2  | A2  |      |
GPIO_NUM_3  | A3  |      |
GPIO_NUM_4  | A4  | SCK  | max7219 CLK
3V3
GND
5V
-------------------------------------
GPIO_NUM_5  | A5  | MISO | max7219 CS
GPIO_NUM_6  |     | MOSI | max7219 DIN
GPIO_NUM_7  |     | SS   | 
GPIO_NUM_8  |     | SDA  | LED           |HTU2x SDA
GPIO_NUM_9  |     | SDL  | BOOT_BUTTON   |HTU2x SDL
GPIO_NUM_10 |     |      |
GPIO_NUM_20 |     | RX   |
GPIO_NUM_21 |     | TX   |

# Display MAX7219 
https://fonts2u.com/pixelmix-regular.font?ptext=12%3A33&size=

si7021 (htu2x)

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

(GND ) -photo resistor-- (A0) -resistor 10k- +3.3
ADC_ATTEN_DB_12 and mult 2