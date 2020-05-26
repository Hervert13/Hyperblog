MFRC522-python
==============
A small class to interface with the NFC reader Module MFRC522 on the Raspberry Pi.
This is a Python port of the example code for the NFC module MF522-AN.

**Important notice:** This library has been confirmed to work with the Pi Zero W, Pi 3 B +, and Pi 3 A+. It uses an updated version of [SPI-Py](https://github.com/naleefer/SPI-Py) that fixes a memory leak in the original SPI-Py code. The fix modifies the spi interface slightly, and this repository reflects that change. Additional changes are in progress to improve performance.

## Requirements
This code requires you to have SPI-Py installed from the following repository:
[https://github.com/naleefer/SPI-Py](https://github.com/naleefer/SPI-Py)

## Examples
This repository includes a couple of examples showing how to read, write, and dump data from a chip. They are thoroughly commented, and should be easy to understand.

## Pins
You can use [this](http://i.imgur.com/y7Fnvhq.png) image for reference.

| Name | Pin # | Pin name   |
|:------:|:-------:|:------------:|
| SDA  | 24    | GPIO8      |
| SCK  | 23    | GPIO11     |
| MOSI | 19    | GPIO10     |
| MISO | 21    | GPIO9      |
| IRQ  | None  | None       |
| GND  | Any   | Any Ground |
| RST  | 22    | GPIO25     |
| 3.3V | 1     | 3V3        |

## Usage
Import the class by importing MFRC522 in the top of your script. For more info see the examples.

## License
This code and examples are licensed under the GNU Lesser General Public License 3.0.
