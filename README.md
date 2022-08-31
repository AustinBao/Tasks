# Tasks
Basic Projects

# TRACKTABLE
#### Video Demo:  <URL https://www.youtube.com/watch?v=Z5SRzd6Tb5A>
#### Description:
I came up with the idea of Tracktable during the last few days of summer when schools tend to release time tables in preparation for school to inevitably begin. And the most popular way of sending your time table info was by sending screen shots. It seemed almost comical to send multiple screen shots to multiple people as its such a huge waste of time and not to mention the easy slip ups that might occur. So, I decided to solve this problem with the skills I gained throughout this course and present it as my final project!

To start things off, I decided to use FLASK again since I have grown more comfortable to it after "finance". However, in my app.py this time, I have the following functions: home, instructions, register, login, logout, add, table, and summary.

Home and instructions were just there simply to render a html template I had made.

Register begins to become more complex. I start off by setting variables to each input in the form for future use. Next, we check every parameter's validity. Examples include how grade >= 10 and grade =< 12 and the email must match a very specific formating to be accepted. If any of these fail, we run "apology" which is a direct copy from "finance". Once we have checked through every input, we first hash the password and then we insert into our table called "users".

Login checks the validity of the input just like register. If all checks pass, then the user is free to log in to the site. Notice that we also use session here to save our current user's id.

Add took me the longest to code which means it was also the part where I learned the most. We start off by creating a list called items that has every single user's grade, program, and name in it, making it possible for me to display it in my HTML file. This is what makes up the list that you are greeted with when you click on add. When the request method is POST, we proceed to get the username from the input which we again check the validity of. Afterwards, we SELECT all the info, from the users table, about the current, logged in user to use REPLACE later. REPLACE is used to replace the old row's friends columb with a new value "new". New just contains our username from the input I mentioned above. Now we know that our current user is friends with the username from the form.

Table starts off by assigning the variable "day" to the select form in the HTML file and checking the correctness of the input above. If it's clear, we assign variables to each input field in order to get each period's class. Again, we check the correctness of each period. This leads us to the next part where we simply just REPLACE into our "day" table (will decide which table we switch into since one table of mine is called dayOne and the other is called dayTwo) and fill it with the classes from each period above. Finally, render the table HTML file.

Summary is the final function for my website. This is where the actual details about whether or not you and your friend have any matching classes is. We start by getting the current user's username and also the current user's friend's username. Now that you have your friends username, it can be used to get the id of said username which will let us sift through the time tables. Now, we look through each table using the id to get our friend's table and we also use the current user's id to fet the current user's time table. Next, since my table includes the name of the owner of a time table, I user insert() to insert the name of the current user and friend into their respective lists. Then, we check what classes the user and their friend have in common through the use of indexs and a for loop. Since each list is ordered in period 1 to period 4, we can simply loop and look at each dictionary at the same time to check if any classes are equal to each other. Finally, render the respective HTML file.

With app.py out of the way, I want to explain extra.py. I simply copied over the code from finance since I wanted my website to behave along the same way where apologies popped up whenever false inputs were issued, and login required to be present in all functions that required logging in.

Finally, every HTML file in template had its respective function in app.py with identical labels. Each are straight forward and easy to understand with the help of Jinja.

With this, I have explained my entire website from the functions which run the brains of the website, to the HTML and CSS which display each letter and image. I've gained a lot from this experience and was a wonderful way to cap off the summer and jump straight into the school year! I will be starting grade 11 and looking forward to what comes next.


This was Cs50.
