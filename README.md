# MDP-Motor-Function-Generator

This repo will let the robot run at various various setSpeeds intervals, then use Linear Regression to produce a mapping function for setSpeeds value to the physical RPM of the robot.

### Usage:
1) If python environment has not been set up, run `pip install -r requirements.txt`
2) (Optional) Modify the `startValue` and `increment` of `PieceWiseGenerator.ino` if you'd like. End value = 400, so `startValue` of 70 and `increment` of 30 will result in (400-70)/30 = 11 sample points.
3) Upload `PieceWiseGenerator.ino`. While you're on Arduino IDE, take note of the COM Port your Arduino is on. 
4) Place robot on even surface, ideally on your respective lab's board. Clear the board from any obstacle.
5) Run main.py by calling `python main.py`
6) Copy the 2 functions generated into your main Arduino code, and you're good to go!



Note: This code is written by three frustrated seniors who took MDP (CE3004/CZ3004) in AY2021 Semester 1, in the midst of the pandemic. All three of us worked on Arduino component for our teams, and we couldn't stand repetitive works, hence we produced this repo, along with [MDP-Sensor-Piecewise-Function-Generator](https://github.com/yongshanjie/MDP-Sensor-Piecewise-Function-Generator). 

This methodology is not guaranteed to make your robot run straight 10/10 times. It is meant to speed up the process of calibration and tuning. How well your robot performs is ultimately still dependent on your hardware. If you have a faulty hardware, GET IT REPLACED, don't waste your time calibrating it. Good luck (you really need it) :)))))