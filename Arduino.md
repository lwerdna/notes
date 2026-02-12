---
title: Arduino.md
date_created: 2025-11-24
tags:
typora-copy-images-to: ./assets
---

# Speed

## Old

## New

```C
// toggles the pin marked "D2" on the board
// produces 440ns
void setup() {
  	pinMode(2, OUTPUT);
}
void loop() {
  PORTD ^= (1 << PD2);
}
```

Produces 880ns period pulse on my knockoff nano.

To sample a 50mhz signal... 50mhz is 20e-9 or 20ns period, so we need twice as fast as that, or 10ns period.

https://www.reddit.com/r/esp32/comments/f529hf/results_comparing_the_speeds_of_different_gpio/

Getting 100ns periods (set pin high, set pin low) on ESP32. That's 10mhz period.



# Particular Boards

## Old Knockoff Nano's

**sold as**: Gikfun USB Nano V3.0 ATmega328 CH340G 5V 16M

**board choice in Arduino IDE**: Arduino Nano

**processor**: ATmega328P (Old Bootloader)

**programmer**: "AVR ISP"

VID: 1A86, PID: 7523

## ESP32

**sold as**: "38Pin-ESP32S-Type C"

**marked as**: NodeMCU ESP32-S

**chip type**: ESP32-D0WD-V3 (revision v3.1)

**board choice in Arduino IDE**: ESP32 Dev Module

VID: 10C4 PID: EA60

Better than, maybe a successor to, the ESP8266

# Unsorted Notes

Shortcut to inverting: write the number backwards, place decimal 1 inside

| input | backward | fully inverted |
| ----- | -------- | -------------- |
| 1     | 1        | 1.0            |
| 10    | 01       | 0.1            |
| 100   | 001      | 0.01           |
| 123   | 321      | 3.21           |

