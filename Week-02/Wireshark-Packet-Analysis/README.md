# Wireshark Packet Analysis

## Project Overview

A beginner-level network traffic investigation performed using Wireshark on a live Wi-Fi network.

## Objectives

- Capture and analyse real network traffic
- Identify devices and services on the local network
- Understand TCP/IP communication
- Investigate mDNS service discovery
- Analyse DNS resolution
- Examine TLS-encrypted traffic
- Correlate DNS resolution with TCP/TLS connections
- Understand protocol hierarchy and conversation statistics

## Tools

- Wireshark
- Windows
- Wi-Fi network interface

## Key Findings

- Identified a BPL Android TV at `192.168.1.4`
- Identified Google Cast service discovery through mDNS
- Established the Google Cast → TCP port `8009` relationship using an SRV record
- Analysed a TCP connection between `192.168.1.7` and `192.168.1.4:8009`
- Observed TLS 1.2 encrypted application data
- Investigated DNS resolution for `mobile.events.data.microsoft.com`
- Correlated the resolved IP `4.150.223.96` with TCP/TLS traffic on port `443`
- Examined an additional connection involving port `5228`
- Analysed the overall protocol hierarchy of the capture

## Report

The complete investigation report is included in this folder.

---

 
**Tool:** Wireshark  
**Focus:** Network Traffic Analysis
