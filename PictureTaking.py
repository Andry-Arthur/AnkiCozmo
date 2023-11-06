#!/usr/bin/env python3
# Copyright (c) 2016 Anki, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License in the file LICENSE.txt or at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
'''Hello World
Make Cozmo say 'Hello World' in this simple Cozmo SDK example program.
'''
# implementation of montecarlo locolization
from PIL import Image
import cozmo
import cv2
from cozmo.util import degrees, distance_mm, speed_mmps
import Stitching
import random
import Localize2
import MotionUpdate
import Histogram


# spins the cozmo 360 degrees to get a panorama image of its current environment
def cozmo_program(robot: cozmo.robot.Robot):
    robot.say_text("Okay Here we goooooooo").wait_for_completed()
    move_arms = robot.set_lift_height(0)
    move_arms.wait_for_completed()
    set_head = robot.set_head_angle((cozmo.robot.MAX_HEAD_ANGLE) / 3, in_parallel=True)
    set_head.wait_for_completed()
    # Enabling Cozmo Camera
    robot.camera.image_stream_enabled = True

    degree = 0

    while (degree < 360):
        fileName = "/Users/Veysel Guney Yilmaz/Desktop/Cozmo/Former Group/Cozmopics/takingpics" + str(degree)

        robot.turn_in_place(degrees(10)).wait_for_completed()

        latest_image = robot.world.latest_image
        annotated = latest_image.annotate_image()
        if latest_image is not None:
            print("image = %s" % latest_image)
            converted = annotated.convert()
            converted.save(fileName, "JPEG", resolution=10)
        degree += 10


# turns the robot a random amount simulating a kidnapping robot problem
def randomTurn(robot: cozmo.robot.Robot):
    # Enabling Cozmo Camera
    robot.camera.image_stream_enabled = True
    # rotate a random degree
    deg = random.randint(0, 60)
    robot.turn_in_place(degrees(deg + 20)).wait_for_completed()

    # take a picture and write it out
    latest_image = robot.world.latest_image
    annotated = latest_image.annotate_image()
    if latest_image is not None:
        converted = annotated.convert()
        converted.save("latestImage", "JPEG", resolution=10)
    robot.say_text("Oh Noooooooo they kidnapped me").wait_for_completed()
    return deg


def madeItHome(robot: cozmo.robot.Robot):
    robot.say_text("Im hoooooooome").wait_for_completed()


# rotates the robot in 5 degree intervals as it gathers data to try and localize
def rotato(robot: cozmo.robot.Robot):
    # Enabling Cozmo Camera
    robot.camera.image_stream_enabled = True
    # rotate a random degree
    robot.turn_in_place(degrees(5 * - 1)).wait_for_completed()

    # take a picture and write it out
    latest_image = robot.world.latest_image
    annotated = latest_image.annotate_image()
    if latest_image is not None:
        converted = annotated.convert()
        converted.save("latestImage", "JPEG", resolution=10)


# initial set up for the panorama
# cozmo.run_program(cozmo_program)
# runs the stitching alrgorithm
# Stitching.run()
# turns the cozmo a random direction
# degree = cozmo.run_program(randomTurn)
# calls the initial localizing algorithm
#Localize.localize()
turnDegrees = Localize2.localize()
print(turnDegrees)
# runs the algorithm until it believes it is localized
for i in range(25):
    cozmo.run_program(rotato)
    #MotionUpdate.motionUpdate()
    #Localize.localize2()
#Histogram.makeHistogram()
cozmo.robot.Robot.turn_in_place(turnDegrees).wait_for_completed()
cozmo.run_program(madeItHome)