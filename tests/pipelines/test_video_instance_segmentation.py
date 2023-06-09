# Copyright (c) Alibaba, Inc. and its affiliates.
import unittest

from modelscope.pipelines import pipeline
from modelscope.utils.constant import Tasks
from modelscope.utils.demo_utils import DemoCompatibilityCheck
from modelscope.utils.test_utils import test_level


class VideoInstanceSegmentationTest(unittest.TestCase, DemoCompatibilityCheck):

    def setUp(self) -> None:
        self.task = Tasks.video_panoptic_segmentation
        self.model_id = 'damo/cv_swinb_video-instance-segmentation'

    @unittest.skipUnless(test_level() >= 0, 'skip test in current test level')
    def test_run_modelhub(self):
        video_path = 'data/test/videos/kitti-step_testing_image_02_0000.mp4'
        seg_pipeline = pipeline(
            Tasks.video_instance_segmentation,
            model=self.model_id,
            max_video_frames=20)
        result = seg_pipeline(video_path)

        print(f'video instance segmentation output: \n{result}.')

    @unittest.skipUnless(test_level() >= 1, 'skip test in current test level')
    def test_run_modelhub_default_model(self):
        video_path = 'data/test/videos/kitti-step_testing_image_02_0000.mp4'
        seg_pipeline = pipeline(
            Tasks.video_instance_segmentation, max_video_frames=20)
        result = seg_pipeline(video_path)

        print(f'video instance segmentation output:\n {result}.')

    @unittest.skip('demo compatibility test is only enabled on a needed-basis')
    def test_demo_compatibility(self):
        self.compatibility_check()


if __name__ == '__main__':
    unittest.main()
