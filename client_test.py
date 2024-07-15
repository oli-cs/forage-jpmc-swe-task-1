import unittest
from client3 import getDataPoint,getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    datapoint = getDataPoint(quotes[0])
    self.assertEqual(("ABC",120.48,121.2,120.84),datapoint)

    datapoint2 = getDataPoint(quotes[1])
    self.assertEqual(("DEF",117.87,121.68,119.775),datapoint2)


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    datapoint1 = getDataPoint(quotes[0])
    datapoint2 = getDataPoint(quotes[1])
    

    self.assertEqual(getRatio(0,0),None)
    self.assertEqual(getRatio(datapoint1[1],datapoint1[2]),datapoint1[1]/datapoint1[2])
    self.assertEqual(getRatio(datapoint2[1],datapoint2[2]),datapoint2[1]/datapoint2[2])
    

  """ ------------ Add more unit tests ------------ """



if __name__ == '__main__':
    unittest.main()
