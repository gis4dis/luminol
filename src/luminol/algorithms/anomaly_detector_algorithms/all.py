# coding=utf-8
"""
© 2015 LinkedIn Corp. All rights reserved.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
"""
from luminol.algorithms.anomaly_detector_algorithms import (bitmap_detector,
                                                            bitmap_mod,
                                                            bitmap_diminishing,
                                                            bitmap_mod_shift,
                                                            default_detector,
                                                            derivative_detector,
                                                            exp_avg_detector,
                                                            absolute_threshold,
                                                            diff_percent_threshold,
                                                            sign_test)

anomaly_detector_algorithms = {
    'bitmap_detector': bitmap_detector.BitmapDetector,
    'bitmap_mod': bitmap_mod.BitmapMod,
    'bitmap_diminishing': bitmap_diminishing.BitmapModDiminishing,
    'bitmap_mod_shift': bitmap_mod_shift.BitmapModShift,
    'default_detector': default_detector.DefaultDetector,
    'derivative_detector': derivative_detector.DerivativeDetector,
    'exp_avg_detector': exp_avg_detector.ExpAvgDetector,
    'absolute_threshold': absolute_threshold.AbsoluteThreshold,
    'diff_percent_threshold': diff_percent_threshold.DiffPercentThreshold,
    'sign_test': sign_test.SignTest
}
