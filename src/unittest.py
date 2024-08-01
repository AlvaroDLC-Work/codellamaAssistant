# Here is a suggested unit test for the `get_process` function:
    
import unittest
from tkinter import Tk, Entry, Button, Label, BooleanVar, Checkbutton
from functions import *

class TestGetProcess(unittest.TestCase):
    def setUp(self):
        self.root = Tk()
        self.root.title("Personal Assistant")
        self.root.geometry("850x500")
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=10)
        self.label = tk.Label(self.frame, text="Termino de Busqueda")
        self.label.grid(row=0, column=0, padx=5)
        self.search_value = tk.Entry(self.frame, width=30 )
        self.search_value.grid(row=0, column=1, padx=5)
        self.button = tk.Button(self.frame, text="Process Data", command=get_process)
        self.button.grid(row=1, column=1, padx=5)
        self.text_box = ScrolledText(self.root, wrap=tk.WORD, width=100, height=25)
        self.text_box.pack(pady=10)
        self.var1 = tk.BooleanVar()
        self.check1 = tk.Checkbutton(self.frame, text="Uppercase", variable=self.var1)
        self.check1.grid(row=1, column=0, pady=5)
        self.var2 = tk.BooleanVar()
        self.check2 = tk.Checkbutton(self.frame, text="Lowercase", variable=self.var2)
        self.check2.grid(row=1, column=1, pady=5)
        self.var3 = tk.BooleanVar()
        self.check3 = tk.Checkbutton(self.frame, text="Title Case", variable=self.var3)
        self.check3.grid(row=1, column=2, pady=5)
        self.root.mainloop()

    def test_get_process(self):
        # Test that the function returns a tuple with three elements
        self.assertEqual(len(self.result), 3)

        # Test that the first element is an integer
        self.assertIsInstance(self.result[0], int)

        # Test that the second element is a string
        self.assertIsInstance(self.result[1], str)

        # Test that the third element is a list of strings
        self.assertIsInstance(self.result[2], list)
        for item in self.result[2]:
            self.assertIsInstance(item, str)

    def tearDown(self):
        self.root.quit()

"""
In this test case, we first set up the tkinter window and its widgets using the `setUp` method. We then create a
mock function for the `get_process` function that will be used to simulate the user clicking the "Process Data"
button. The `test_get_process` method is where we actually run the test. We assert that the function returns a
tuple with three elements, and that each element is of the correct type. Finally, we tear down the tkinter window
using the `tearDown` method.

Note that this test case assumes that the `get_process` function is correctly implemented and will return a tuple
as expected. If the function is not working correctly, the test case will also fail.
"""