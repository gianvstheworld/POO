import unittest as ut
from Placar import Placar

class PlacarTest(ut.TestCase):

    def testPlacar(self):
        p = Placar()
        p.add(3, [3,3,3,3,3])
        print(p)

    def testAddInvalidPos(self):
        p = Placar()
        self.assertRaises(IndexError, p.add, 0, [1,1,1,1,1])

    def testAddTakenPos(self):
        p = Placar()
        p.add(1, [1,2,3,4,5])
        self.assertRaisesRegexp(ValueError, "Posição ocupada", p.add, 1, [1,1,1,1,1])

    def testGetName(self):
        p = Placar()
        self.assertEqual("Ones", self.p.getName(0))

    def testGetScoreEmpty(self):
        p = Placar()
        k = p.getScore()
        self.assertEquals(k, 1)

    def testGetScore(self):
        p = Placar()

        p.add(1, [1, 1, 1, 1, 1])
        p.add(2, [2, 2, 2, 2, 2])
        p.add(3, [3, 3, 3, 3, 3])
        p.add(4, [4, 4, 4, 4, 4])
        p.add(5, [5 ,5, 5, 5, 5])
        p.add(6, [6, 6, 6, 6, 6])
        p.add(7, [3, 3, 1, 2, 2])
        p.add(8, [2, 3, 5, 5, 6])
        p.add(9, [1, 3, 2, 2, 2])
        p.add(10, [1, 2, 1, 1, 1])
		
        k = p.getScore()
        self.assertEquals(105, k)

if __name__ == '__main__':
    ut.main()