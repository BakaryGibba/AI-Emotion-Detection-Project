import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_emotion_detection(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear")
        ]

        for text, expected_dominant_emotion in test_cases:
            with self.subTest(text=text):
                result = emotion_detector(text)
                if result is not None:
                    self.assertEqual(result['dominant_emotion'], expected_dominant_emotion)
                else:
                    self.fail("emotion_detector returned None")

if __name__ == '__main__':
    unittest.main()
