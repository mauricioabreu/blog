Learning Crystal - Part I
#########################

:date: 2016-05-15 16:27
:tags: crystal, tdd
:slug: learning-crystal-part-I

These days I was reading about the Ruby programming language. I got excited of course. It looks pretty cool!

After some readings I found an article talking about a language called `Crystal`_. I got very surprised by the goals the community behind the language is seeking: from a syntax similar to Ruby to efficient compiled native code.

In this post I will walk through the language features using the TDD process.

Let's start with the testing tool. `Spec`_ is built-in and is inspired by `RSpec`_.

Structure of the testing environment
------------------------------------

First create a folder to hold your project. Give it the name `tdd-with-crystal` for example. Now create two new folders: `src` and `spec`.
`src` is where our feature code will be located. `spec` is where ours tests will stay.

To start easy, we are going to write a math library which has very basic functions like: addition, subtraction, multiplication and division. It looks pretty dummy right? And it is the objective.

Inside the spec folder, create a file and name it `math_spec.cr`. All spec files need to have the `_spec` suffix.

Writing our first tests
-----------------------

One of the basic principles of TDD is to write the test first. Okay, let's write our test suite for our math library.

math_spec.cr:

.. code-block:: ruby

    require "spec"
    require "../src/math.cr"

    describe Math do
      describe "addition" do
        it "adds two numbers" do
          addition(1, 1).should eq 2
        end
      end
    end

A spec file starts with the `require` directive. It imports packages. Either built-ins or your own code. Since the `src` folder is one level up, we can use relative import making use of dot notation.

The following lines are part of the Spec DSL. `describe` can be a class or a string and is used to group similar tests. In our example, `Math` could be anything else but to be more clear we give it a proper name. `it` is used to tell the reason why the test exists. `it` has the same goal of a Python test name like `test_addition_with_two_numbers`. Inside the `it` context we call the function and match our expectations. `should` is like the `assert`, dividing the calling function of the expected result. `eq` works like the `==`. Spec has a lot different matchers just like Python unittest has lots of different `assert` statements.

Now we have a test we need to run it. You can either run `crystal spec` in the same level of the `spec` folder or run `crystal math_spec.cr`. Here is the output:

.. code-block:: shell

    Error in ./spec/math_spec.cr:7: undefined method 'addition'

            addition(1, 1).should eq 3

Ops! It looks like we don't have the `addition` implementation yet.

Okay, it is time to code our math package.

Create a file inside the `src` folder and name it math.cr.
Here is the initial code of our math package:

.. code-block:: ruby

    def addition(number1 : Int, number2 : Int)
      2
    end

Here we are defining a function. If you know Python, `def` is very familiar to you. It either defines a function or a method.
Following the TDD guidelines, we are starting with a hardcoded value.

In Crystal it optional to define the type of the arguments being passed in. It means we could rewrite our `addition` function this way:

.. code-block:: ruby

    def addition(number1, number2)
      2
    end

Also it is optional to use the `return` statement. If `return` is missing it is assumed that the last line of the function's body is the value being returned.

Yey! We have the our real code now. Let's run the test suite again. Here is the output:

.. code-block:: shell

    .

    Finished in 0.17 milliseconds
    1 examples, 0 failures, 0 errors, 0 pending

Wow! Our test is passing. But wait...we don't have a real implementation, just a hardcoded return. Change the `addition` function body to something real: 

.. code-block:: ruby

    def addition(number1 : Int, number2 : Int)
      number1 + number2
    end

Voilá! Our code is working fine and it will work for other values too.

I hope you have learned something here. Leave a comment if you find it useful or if you disagree with anything. 

.. _Crystal: http://crystal-lang.org/
.. _Spec: http://crystal-lang.org/api/Spec.html
.. _RSpec: http://rspec.info/
