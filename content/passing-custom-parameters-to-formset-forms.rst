Passing custom parameters to Django formset forms
#################################################

:date: 2016-04-01 19:45
:tags: django
:slug: passing-custom-parameters-to-django-formset-forms
:status: draft

An usual question on sites like StackOverflow is: how do I pass a custom parameter to a formset form?

You will end up finding lots of ways to do it. But the most used (at least the more reasonable answer) uses some hard to understand constructions.

Let's say we have an app with two models: Author and Book. 

The problem
-----------

I want to make it possible for the users of my product to add new books on my site. But the price can only be added or updated by superusers (you could use the permissions Django framework here).

Okay! It seems to be an easy task, right? No, it is not.

Django versions lower than 1.9 do not provide an easy waye to do it. This is why I am writing this post and created a repository with a project to demonstrate how it actually works. You can `read the code here <https://github.com/mauricioabreu/formset_custom_arguments>`_. 

The solution
------------

This is one of the best solutions I have ever encountered.

.. code-block:: python

    BookFormset = inlineformset_factory(
        models.Author,
        models.Book,
        form=forms.BookForm,
        extra=1,
        can_delete=False,
    )
    
    BookFormset.form = staticmethod(
        curry(
            forms.BookForm,
            user=request.user
        )
    )


Why does it work?
-----------------

The first part of the code creates a formset relating two models and uses a custom form.

An author can have many books and one book is related to only one author.

More info about how to handle formsets you can find `here <https://docs.djangoproject.com/en/1.8/topics/forms/formsets/>`_.

The second part is where the trick happens. In general, the code is injecting a new form to the formset form in runtime, using the help of `curry`.

`curry` is very similar to the functools.partial function. It takes a function with pre-defined arguments and returns a new function.

So why does it work? It works because the Django internal form construction does something like this: 

.. code-block:: python

    return type(form)(class_name, (form,), form_class_attrs)

After passing a function as a form object, it will call our curryed function, creating a new form with our custom parameters.

A different approach
--------------------

Carl Meyer, Django core developer, has a different style of doing this. See `this answer <http://stackoverflow.com/a/624013>`_ at StackOverflow. It works in a very similar way, but like he says, it does not affect the formset like we are doing here. Anyways, I don't think it will affect the form. You will rarely end up having a business rule attached only to the formset context.
