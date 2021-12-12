from ChatRoom import chat_room
import unittest

class ChatRoomTest(unittest.TestCase):
    def test_1(self):
        res = chat_room('hello').lower()

        self.assertEqual(res, 'yes')

    def test_2(self):
        res = chat_room('hello').lower()
        
        self.assertEqual(res, 'yes')

    def test_3(self):
        res = chat_room('gggghgegeglglooooeeafgja').lower()
        
        self.assertEqual(res, 'yes')

    def test_4(self):
        res = chat_room('ggggggggggggggggggggggggheeeeeeeeeeeeeeeeeelggggggggggglorrrrrrr').lower()
        
        self.assertEqual(res, 'yes')

    def test_5(self):
        res = chat_room('hlelo').lower()
        
        self.assertEqual(res, 'no')

    def test_6(self):
        res = chat_room('hddlleeloooff').lower()
        
        self.assertEqual(res, 'no')

    def test_4(self):
        res = chat_room('hoolleellgg').lower()
        
        self.assertEqual(res, 'no')

if __name__ == '__main__':
    unittest.main()