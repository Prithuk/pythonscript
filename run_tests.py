import unittest
import csv
from tests.test_credit_card_validation import CreditCardValidationTest

class SimplifiedTestResult(unittest.TestResult):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.testResults = []  # Store test results here

    def addSuccess(self, test):
        super().addSuccess(test)
        self.testResults.append((test.id(), 'Pass'))

    def addFailure(self, test, err):
        super().addFailure(test, err)
        self.testResults.append((test.id(), 'Fail'))

    def addError(self, test, err):
        super().addError(test, err)
        self.testResults.append((test.id(), 'Error'))

def run_tests_and_write_results():
    suite = unittest.TestLoader().loadTestsFromTestCase(CreditCardValidationTest)
    result = SimplifiedTestResult()
    suite.run(result)  
    
    with open("test_results.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Test Name", "Result"])  
        
        for testName, outcome in result.testResults:
            testName = testName.split('.')[-1]  
            writer.writerow([testName, outcome])  

if __name__ == '__main__':
    run_tests_and_write_results()
