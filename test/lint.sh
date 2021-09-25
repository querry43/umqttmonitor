#!/bin/bash

cd "$(dirname "$0")"
pylint --disable=import-error ../umqttmonitor.py
