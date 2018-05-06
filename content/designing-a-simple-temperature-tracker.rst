Designing a simple temperature tracker
######################################

:date: 2018-05-05 14:01
:category: programming
:tags: python
:slug: designing-a-simple-temperature-tracker

What we are going to build
--------------------------

On this post, we well build a temperature tracker together!

A temperature tracker is a device that keeps track of all monitored temperatures that have been collected.
Our temperature tracker is responsible from:

- Insert a temperature
- Return the maximum temperature we have seen so far
- Return the minimum temperature we have seen so far
- Return the mean temperature we have seen so far

We also have some constraints:

- A temperature must be an integer number
- It must be between 0 and 100 Fahrenheit scale
- Minimum and maximum must return integer results
- Mean must return a float

Coding
------

All the code listed here can be found at: https://github.com/mauricioabreu/temperature_tracker

Okay, let's build some code, starting with the tests:

.. code-block:: python

    import unittest

    class TestTemperatureTracker(unittest.TestCase):

        def test_insert(self):
            temperature_tracker = TemperatureTracker()
            temperature_tracker.insert(22)

    if __name__ == '__main__':
        unittest.main()

We can run our tests by executing the file using the Python interpreter:

.. code-block:: bash

    python tracker.py

We still don't have the TemperatureTracker object, neither the insert function, this is why our testes failed.
TemperatureTracker is a container, it must keep a track of all temperatures added. It indicates that we need a collection to
save all our records. Since we don't need to save or retrieve it using keys, we use a list.

.. code-block:: python

    class TemperatureTracker(object):

        def __init__(self):
            self.temperatures = []

``TemperatureTracker`` is now our container. It is responsible to validate and add the temperature to the ``temperatures`` attribute.
Also it will tell us the ``min``, ``max`` and ``mean`` values.

Let's define the ``insert`` function now:

.. code-block:: python

    class TemperatureTracker(object):

        def __init__(self):
            self.temperatures = []

        def insert(self, temperature: int) -> None:
            """Insert a new temperature on the tracker.
            It is added in the end the collection, keeping
            the order from the most recent to the oldest temperature."""
            # Record the temperature
            self.temperatures.append(temperature)

We can run our tests again and check if our test is passing, even if our test does not assert for specific results.
Sometimes it is hard to test functions that mutate some data. Did you ever find yourself testing if the last object inserted
into the database was there by querying it? Since we are dealing with lists, we can make our container to look like a list by
overriding the `__getitem__ <https://docs.python.org/3.6/reference/datamodel.html#object.__getitem__>`_ object method.
It is necessary because we can access the temperatures like accessing list elements:

.. code-block:: python

    class TemperatureTracker(object):

        def __init__(self):
            self.temperatures = []

        def __getitem__(self, index: int) -> int:
            """Return the element in the given index.
            This function overrides the list indexing protocol.
            Example:
                >>> temperature_tracker = TemperatureTracker()
                >>> temperature_tracker.insert(15)
                >>> temperature_tracker[0]
                >>> 15
            """
            return self.temperatures[index]

    # Instantiate our TemperatureTracker object
    temperature_tracker = TemperatureTracker()
    temperature_tracker.insert(22)
    # Get last temperature was added
    temperature_tracker[-1]

Then we get back to our test and add specific asserts to check if the temperature added can be retrieved.

.. code-block:: python

    self.assertEqual(temperature_tracker[-1], 22)

It is working!

There are some constraints we must obey, right? Temperature must be integer and the value must be between 0 and 100.
Let's add code to validate the temperature being inserted.

.. code-block:: python

    class InvalidTemperature(Exception):
        """Raise when an invalid temperature is
        added to the tracker."""
        pass

    class TemperatureTracker(object):

        def __init__(self):
            self.temperatures = []

        def insert(self, temperature: int) -> None:
            """Insert a new temperature on the tracker.
            It is added in the end the collection, keeping
            the order from the most recent to the oldest temperature."""
            # Check temperature value
            self.validate_temperature(temperature)
            # Record the temperature
            self.temperatures.append(temperature)

        def validate_temperature(self, temperature: int) -> None:
            """Check if the temperature is a valid value."""
            if (temperature < 0 or temperature > 100) or not isinstance(temperature, int):
                raise InvalidTemperature(
                    'Temperature must be an integer between 0 and 100')

    class TestTemperatureTracker(unittest.TestCase):

        def test_insert(self):
            temperature_tracker = TemperatureTracker()
            temperature_tracker.insert(22)
            self.assertEqual(temperature_tracker[-1], 22)

        def test_insert_with_invalid_temperature(self):
            temperature_tracker = TemperatureTracker()
            # Insert a value that is too low...
            with self.assertRaises(InvalidTemperature):
                temperature_tracker.insert(-3)

            # Insert a value that is too high...
            with self.assertRaises(InvalidTemperature):
                temperature_tracker.insert(101)

            # Insert a non-integer value...
            with self.assertRaises(InvalidTemperature):
                temperature_tracker.insert(3.0)

    if __name__ == '__main__':
        unittest.main()


Here I decoupled the validation function from the insert method because:

- Easier to test
- Easier to understand
- Can be reused when needed

We have our ``insert`` method tested and working.

``get_max``, ``get_min`` and ``get_mean`` are simpler than the ``insert`` function. We can use the built-in ``max`` and
``min`` functions to get it working. For the ``get_mean`` case we use the mean calculation below:

.. code-block:: python

    def get_mean(self) -> float:
        """Return the mean temperature tracked."""
        return sum(self.temperatures) / len(self.temperatures)

Python 3 returns a float when dividing two integer values. For Python 2 one of the values must be float 
or we can use the `pep0238 <https://www.python.org/dev/peps/pep-0238/>`_ to return the true division 
in the whole module it is being imported.

As already mentioned, this first version of the code is on Github under the tag v0.1

``Tags`` point to a specific commit in history. You can checkout to them:

.. code-block:: bash

    git fetch --tags    
    git checkout v0.1

I omitted some pieces of code here but you can always check the repository to navigate the code yourself.

Refactoring
-----------

Now it is time to refactoring our code. It is not that bad but our ``get_max``, ``get_min`` functions calls can get
expensive when dealing with large lists. Calling ``max`` on a list with 10 elements and 10.000 elements is very different. 
``max`` is O(n) which means the implementation must check every element of the list to know the maximum value.


Let's read the other functions:

.. code-block:: python

    def get_max(self):
        """Return the maximum temperature tracked."""
        return max(self.temperatures)

    def get_min(self):
        """Return the minimum temperature tracked."""
        return min(self.temperatures)

They recalculate these values everytime we call the functions. What if we save the ``max`` and ``min`` values
when inserting the temperature?

.. code-block:: python
    
    temperature_tracker = TemperatureTracker()
    temperature_tracker.insert(1) # 1 is the maximum value now
    temperature_tracker.insert(3) # 3 is the maximum vaue now
    temperature_tracker.insert(2) # 3 is still the maximum value

Let's refactor the ``insert`` function:

.. code-block:: python

    class TemperatureTracker(object):

        def __init__(self):
            self.temperatures = []
            self.max_temperature = None
            self.min_temperature = None

        def insert(self, temperature: int) -> None:
            """Insert a new temperature on the tracker.
            It is added in the end the collection, keeping
            the order from the most recent to the oldest temperature."""
            # Check temperature value
            self.validate_temperature(temperature)
            # Record the temperature
            self.temperatures.append(temperature)
            # Set maximum temperature
            self.set_max(temperature)
            # Set minimum temperature
            self.set_min(temperature)

        def set_max(self, temperature):
            if not self.max_temperature or temperature > self.max_temperature:
                self.max_temperature = temperature
            return self.max_temperature

        def set_min(self, temperature):
            if not self.min_temperature or temperature < self.min_temperature:
                self.min_temperature = temperature
            return self.min_temperature

We added two new functions: ``set_max`` and ``set_min``. They behave like a cache, a way to save a result value to save machine processing.

After running the tests, we can see that all them passed. This happens because we already tested our code, and refactoring only changed **how**
we calculate the values, **we did not introduce any new feature**.

All the refactored code can be read after checking out the tag v0.2:

.. code-block:: bash

    git fetch --tags    
    git checkout v0.2

That is all! This code has space for more improvements. If you have anything to comment, please, go ahead. 
I am open to discuss every point of this article. Share with others if you found it useful. 

Bye!
