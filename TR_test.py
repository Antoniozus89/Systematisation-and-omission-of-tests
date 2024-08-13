import unittest

from Module12.HW3.test_12_3 import Runner, Tournament


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
       res = {place: runner.name for place, runner in cls.all_results.items()}
       print(res)

    # @unittest.skipIf(is_frozen, "Пропуск")
    def test_first_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last = max(results.keys())
        self.assertTrue(results[last].name == "Ник")
        self.tearDownClass()

    # @unittest.skipIf(is_frozen, "Пропуск")
    def test_second_tournament(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last = max(results.keys())
        self.assertTrue(results[last].name == "Ник")
        self.tearDownClass()

    # @unittest.skipIf(is_frozen, "Пропуск")
    def test_third_tournament(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        last = max(results.keys())
        self.assertTrue(results[last].name == "Ник")




if __name__ == "__main__":
    unittest.main()

# def skip_if_frozen(test_func):
#     def wrapper(*args, **kwargs):
#         if args[0].is_frozen:
#             print(f"Тесты в этом кейсе заморожены: {test_func.__name__}")
#             raise unittest.SkipTest("Тесты в этом кейсе заморожены")
#         return test_func(*args, **kwargs)
#     return wrapper





# runnerST = unittest.TestSuite()
# runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
# is_frozen = False




    # if __name__ == '__main__':
    #     suite = unittest.TestSuite()
    #     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_1.RunnerTest))
    #     suite.addTest(unittest.TestLoader().loadTestsFromTestCase(test_12_3.TournamentTest))
    #
    #     runner = unittest.TextTestRunner(verbosity=2)
    #     runner.run(suite)`
