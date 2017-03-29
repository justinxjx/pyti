import unittest
import numpy as np

from sample_data import SampleData
from technical_indicators import simple_moving_average


class TestSimpleMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.sma_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        804.55166666666673, 807.84333333333336, 809.89666666666665,
        811.21833333333325, 811.20333333333338, 812.51166666666666,
        813.88000000000011, 814.40333333333331, 813.18666666666661,
        812.6783333333334, 810.23333333333346, 806.20333333333338,
        799.25166666666667, 793.06499999999994, 785.82499999999993,
        778.30499999999995, 775.09000000000003, 774.75166666666667,
        776.35333333333347, 776.68333333333339, 779.10666666666668,
        782.55166666666673, 784.03833333333341, 781.79333333333341,
        781.85500000000002, 781.81833333333327, 781.17833333333328,
        775.88166666666666, 773.70666666666659, 774.42666666666662,
        777.66499999999996, 782.99833333333333, 787.4766666666668,
        792.12333333333345, 793.86333333333334, 795.21833333333336,
        795.20000000000016, 794.85333333333335, 797.77499999999998,
        803.81666666666672, 810.46833333333336, 817.15666666666664,
        822.19999999999993, 824.55999999999983, 824.90499999999986,
        826.52833333333331, 826.42666666666662, 822.80833333333339,
        817.61833333333345, 814.28833333333341, 812.64499999999998,
        809.72499999999991, 808.505, 807.48333333333323, 807.23000000000002,
        806.75500000000011, 805.25833333333321, 803.72666666666657,
        802.04166666666663, 802.36333333333334, 803.52666666666664,
        805.11000000000001, 805.08666666666659, 807.51666666666677,
        809.49833333333333, 809.89666666666665, 808.18333333333328,
        805.62666666666667, 804.84666666666669, 802.55833333333339,
        798.31000000000006, 795.5916666666667, 795.43166666666673,
        794.28000000000009, 795.0916666666667, 796.21833333333336,
        799.1450000000001, 800.50333333333344, 799.26666666666677, 799.495,
        797.67500000000007, 795.64666666666665, 793.17999999999995,
        792.25166666666667, 792.61833333333345, 793.74166666666667,
        794.58000000000004, 795.21833333333325, 796.80666666666673,
        799.15999999999997, 800.42500000000007, 801.98666666666668,
        803.67000000000007, 805.09499999999991, 806.05166666666662,
        806.39499999999987, 807.06833333333327, 807.23000000000002,
        805.59666666666669, 804.04999999999984, 802.65500000000009,
        801.56499999999994, 799.25, 792.40166666666664, 786.52166666666665,
        779.64333333333332, 772.54333333333341, 765.60000000000002,
        759.44500000000005, 757.98500000000001, 756.55833333333328,
        755.81666666666661, 752.16833333333341, 748.25500000000011,
        744.10000000000002, 740.005, 735.63666666666666, 729.73333333333323,
        725.005, 720.53333333333342, 716.43500000000006, 712.72500000000002]

        self.sma_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, 806.83875, 809.34500000000003, 810.21500000000003,
        811.60000000000002, 812.59500000000003, 813.53750000000002,
        813.31500000000005, 812.97125000000005, 810.46749999999997, 807.83875,
        803.63124999999991, 798.95249999999999, 792.27374999999995,
        785.89750000000004, 781.89499999999998, 779.39374999999995,
        778.22125000000005, 776.8125, 777.16500000000008, 778.01250000000005,
        780.55500000000006, 782.00999999999999, 783.29500000000007,
        782.11249999999995, 780.78375000000005, 777.41125, 776.505,
        775.91624999999999, 778.5150000000001, 783.01625000000001, 785.0,
        785.1400000000001, 786.01875000000007, 790.41875000000005,
        794.63499999999999, 798.33625000000006, 800.08249999999998,
        800.75375000000008, 803.26250000000005, 809.19375000000002,
        815.88750000000005, 820.34249999999997, 822.36124999999993,
        824.50999999999999, 824.75125000000003, 823.4375, 821.25,
        818.19125000000008, 815.19499999999994, 813.38375000000008,
        812.45125000000007, 809.15375000000006, 806.85249999999996,
        806.15125000000012, 805.92499999999995, 805.46250000000009,
        804.49874999999997, 803.63249999999994, 803.11874999999998,
        804.37124999999992, 804.3175, 806.03375000000005, 807.67875000000004,
        808.25999999999999, 807.72500000000002, 806.81875000000002, 805.3075,
        804.12, 802.59625000000005, 799.31625000000008, 797.17499999999995,
        795.10625000000005, 795.48874999999998, 797.06375000000003,
        798.31999999999994, 797.77500000000009, 797.89249999999993,
        798.03375000000005, 797.17124999999999, 798.08874999999989,
        796.88625000000002, 794.79999999999995, 792.99749999999995,
        792.96249999999998, 793.65625, 794.88125000000002, 796.23500000000001,
        797.43499999999995, 798.43125000000009, 800.26375000000007,
        801.94499999999994, 803.39625000000001, 804.83875, 805.81750000000011,
        806.12750000000005, 806.31625000000008, 805.82375000000002,
        804.94375000000002, 804.07749999999999, 803.17000000000007, 801.02625,
        795.82124999999996, 790.41374999999994, 784.25375000000008,
        779.28750000000002, 774.33249999999998, 768.61875000000009,
        763.13625000000002, 758.39499999999998, 756.81500000000005,
        753.52250000000004, 750.79124999999999, 747.28625, 743.94000000000005,
        740.53874999999994, 735.62625000000003, 729.85749999999996,
        724.32875000000001, 720.48624999999993, 717.29250000000002]

        self.sma_perio_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, 807.70500000000004, 810.02499999999998,
        811.52600000000007, 812.60300000000007, 812.39999999999998,
        812.56499999999994, 811.11400000000003, 809.04100000000005,
        805.13900000000001, 801.71100000000001, 797.173, 792.04099999999994,
        787.83999999999992, 785.25, 783.03899999999999, 780.11399999999992,
        778.49700000000007, 777.85000000000002, 778.7120000000001,
        778.48700000000008, 780.65700000000004, 782.22199999999998,
        782.14999999999998, 778.52800000000002, 777.12400000000002,
        777.13300000000004, 779.79200000000003, 782.49000000000001,
        784.21299999999997, 784.726, 784.32900000000006, 785.17300000000012,
        788.20500000000015, 793.87299999999993, 798.65399999999988,
        802.36000000000001, 804.01100000000008, 805.66800000000012,
        809.03899999999999, 813.33500000000004, 817.279, 821.14599999999996,
        822.74699999999996, 822.44100000000003, 820.94500000000005,
        819.61800000000005, 818.58500000000004, 816.68700000000013,
        814.52999999999997, 812.19500000000005, 810.34000000000003,
        807.75400000000013, 805.8839999999999, 805.23800000000006,
        805.18399999999997, 805.04000000000008, 804.86900000000003,
        804.9849999999999, 803.83299999999997, 805.25799999999992,
        806.54499999999996, 806.92499999999995, 806.62400000000002, 806.125,
        805.51600000000008, 805.375, 803.41500000000008, 801.21400000000006,
        800.83100000000002, 798.18299999999999, 796.87199999999996,
        797.16800000000001, 797.99199999999996, 798.1400000000001,
        797.48299999999995, 796.34500000000003, 796.49099999999999,
        797.20100000000002, 796.64099999999996, 796.923, 795.99900000000002,
        794.85900000000004, 793.75199999999995, 794.02999999999997,
        795.16499999999996, 796.72199999999998, 797.649, 798.66300000000001,
        800.04600000000005, 801.7360000000001, 803.22499999999991,
        804.31399999999996, 805.14200000000005, 805.87000000000012,
        805.32000000000005, 804.67000000000007, 804.56299999999999,
        804.06100000000004, 802.49000000000001, 798.25400000000013,
        793.60200000000009, 788.61899999999991, 783.84799999999996,
        779.08300000000008, 774.79899999999998, 770.61500000000001,
        765.94400000000007, 761.16999999999996, 755.59899999999993,
        752.59500000000003, 749.34600000000012, 746.83199999999999,
        743.79999999999995, 739.64999999999998, 734.93499999999995,
        730.12400000000002, 725.27200000000005, 720.97700000000009]

    def test_simple_moving_average_period_6(self):
        period = 6
        sma = simple_moving_average.simple_moving_average(self.data, period)
        np.testing.assert_array_equal(sma, self.sma_period_6_expected)

    def test_simple_moving_average_period_8(self):
        period = 8
        sma = simple_moving_average.simple_moving_average(self.data, period)
        np.testing.assert_array_equal(sma, self.sma_period_8_expected)

    def test_simple_moving_average_period_10(self):
        period = 10
        sma = simple_moving_average.simple_moving_average(self.data, period)
        np.testing.assert_array_equal(sma, self.sma_perio_10_expected)

    def test_simple_moving_average_invalid_period(self):
        period = 128
        # a period greater than the data length should raise an exception
        with self.assertRaises(Exception):
            simple_moving_average.simple_moving_average(self.data, period)
