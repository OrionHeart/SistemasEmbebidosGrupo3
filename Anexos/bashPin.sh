#!/bin/bash

echo "17" > /sys/class/gpio/export
echo "out" > /sys/class/gpio/gpio17/direction # BCM17
while true; do
	echo "0" > /sys/class/gpio/gpio17/value
	echo "1" > /sys/class/gpio/gpio17/value
done
echo "17" > /sys/class/gpio/unexport