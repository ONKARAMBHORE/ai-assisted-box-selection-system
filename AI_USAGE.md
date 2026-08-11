# AI Usage

## 1. AI Tool Used

I used ChatGPT while developing this assignment.

I mainly used ChatGPT to understand the assignment requirements, understand
Django and Django REST Framework concepts, solve errors and get help while
implementing different parts of the project.

I did not use AI only to copy the complete project. I used it mostly when I
was not understanding something or getting an error.

---

## 2. How I Used AI

I used ChatGPT for different parts of the project, like:

- Understanding the assignment requirements
- Understanding the project structure
- Setting up Django project and apps
- Creating Django models
- Creating serializers
- Creating ViewSets and routers
- Creating Product, Box and Order APIs
- Understanding the box recommendation logic
- Writing test cases
- Finding and fixing errors

Some prompts I used were:

- Explain this assignment in simple words.
- Tell me how to implement this project step by step.
- Give me the database models for this project.
- Complete Product and Box APIs.
- Explain Order API in simple way.
- Explain box recommendation logic.
- Give test cases for this project.
- Why I am getting this error?
- Explain this code because I am not understanding it.

I also asked small questions many times when I did not understand a
particular line of code.

---

## 3. What I Used From AI

I used the suggestions from ChatGPT mainly for:

- Django models
- Django REST Framework serializers
- ViewSets
- Routers
- Product API
- Box API
- Order API
- Box recommendation logic
- Test cases
- Debugging errors

I tried to understand the code before using it in my project.

I also changed some code when I felt that it was not required for this
assignment.

---

## 4. Changes I Made

I did not use every suggestion exactly as given by AI.

I changed some parts according to my project requirement and kept the
project simple.

I did not add extra features like:

- Advanced authentication
- Complex permission system
- Background tasks
- Redis or Celery
- Complex optimization algorithm
- Full 3D bin packing system

I focused on the features which were required in the assignment.

---

## 5. Errors I Faced

During development I faced some errors and used ChatGPT to understand
and fix them.

### Django Model Error

I first used `max_digit` instead of `max_digits` in DecimalField.

Django showed an error because the correct parameter is `max_digits`.

I corrected it and checked the project again.

### Box Model Not Showing in Admin

My Box model was not showing in Django Admin.

I checked the project and found that `apps.boxes` was missing from
`INSTALLED_APPS`.

I added it and then the Box model was showing in Admin.

### Queryset Error

I wrote:

`Product.objects.all.order_by("id")`

instead of:

`Product.objects.all().order_by("id")`

I was getting an error because `all` is a function and I forgot to use
`()`.

I corrected it.

### Router URL Error

In Box URLs I wrote:

`urlpatterns = router.url`

The correct code was:

`urlpatterns = router.urls`

I corrected this error after checking the error message.

### Failed Test Case

One test case was failing because the product weight was 10 kg and the
large box maximum weight was 20 kg.

So the large box was actually suitable and the recommendation logic was
working correctly.

I changed the test data so the product weight was more than the maximum
weight of available boxes and then tested it again.

---

## 6. Verification

After completing the project, I checked the implementation by:

- Running `python manage.py check`
- Running migrations
- Testing APIs using Postman
- Checking Product, Box and Order data in Django Admin
- Testing the box recommendation API
- Testing when no suitable box is available
- Running `python manage.py test`

I fixed the errors found during testing and ran the tests again.

The final test cases passed successfully.

---

## 7. My Understanding

While using AI, I tried to understand the code instead of only copying it.

ChatGPT helped me understand Django REST Framework concepts like
serializers, ViewSets, routers, nested serializers and API testing.

I also learned how to read Django error messages and find the problem
in the code.

AI was used as a learning and debugging help during the assignment.