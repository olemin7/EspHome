alarm
https://esphome.io/components/light/#light-automations
https://esphome.io/components/select/template/

# ESP32-S3 DevKitC-1
    Pin     | func
GPIO_NUM_48 | onboard RGB LED (i2s_clockless_led_strip, GRB, 1 led)

# Alarm states
Set via select `select.alarm_alarm_state` (entity "Alarm State").

 Option | LED
--------|------------------------------------------
 Off    | off
 None   | steady green, 20% brightness (no alert)
 Yellow | amber pulse (red 100%, green 50%), ~2s period, 10%..100%
 Red    | red strobe, 250ms on / 250ms off

Boot: LED off (light restore_mode ALWAYS_OFF, select initial_option "Off",
restore_value false) until the ESP connects to HA.

# Alarm source: Ukraine Alarm Pro (read on the ESP)
Integration: https://github.com/ABovsh/ukraine-alarm-pro (HACS), region 31.

The ESP subscribes to `sensor.uap_31_air_alert_level` with a `homeassistant`
text_sensor (`uap_air_alert_level`, internal) and sets the select itself.
HA sends the current value on every API connect, so after an ESP reboot or
Wi-Fi drop the LED shows the current alarm state. No HA automation needed;
remove `/config/packages/alarm_led.yaml` if it was created.

 air_alert_level             | LED option
-----------------------------|-----------
 none                        | None
 yellow                      | Yellow
 red                         | Red
 unrecognized                | Red  (air alert active, level not given)
 unknown / unavailable       | Off  (no data)

The select can still be set by hand from HA; the next sensor change
overrides it.

Test without a real alert: Developer Tools -> States -> set
`sensor.uap_31_air_alert_level` to `yellow` / `red` / `none` (temporary, the
integration overwrites it on its next update). Reboot the ESP during an
alert: the LED must come back in the alert state.
