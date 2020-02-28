# Mgateway Project
Mgateway driver (based on the latest SX1301 driver lora_gateway v5.0.1) and applications to handle data packet then forward to server

1. Core library: libloragw

This directory contains the sources of the library to build a gateway based on a Semtech LoRa multi-channel RF receiver (a.k.a. concentrator). Once compiled all the code is contained in the libloragw.a file that will be statically linked (ie. integrated in the final executable).

The library also comes with a bunch of basic tests programs that are used to test the different sub-modules of the library.

2. Applications

### 2.1. util_pkt_logger

This software is used to set up a LoRa concentrator using a JSON configuration file and then record all the packets received in the file `rawData.csv`, indefinitely, until the user stops the application. We use this file as a buffer contain the receive raw data (the data form in this file is hex)

### 2.2. DataHandle.py

This software is used to parse the raw data in the file above and then log it in the file `parsedData.csv`