# Board Game Project
This is a teamwork of my course. It is a Django based web application, which allow users to share and lend board games their owned.

# Demo
Here is the [Demo](http://34.145.67.134:8000/) site.

It deploys with Gunicorn, Supervisor and nginx.

# Feature
1. 5 models: Profile, Category, BoardGame, Comment, LoanRecord.
2. All visitors(registered or not) can view a list of all board games, and comments as well.
3. Only registered users can add board games and publish comments.
4. Each of every board game has a title, subtitle, published year, players, playing time period, age limit, complexity rate, and description.
5. Only registered users can modify the info of their shared games.
6. Only registered users can remove(delete) the shared games when it does not borrowed by another user. 
7. Only registered users can publish comments for all the games.
8. Only registered users can borrow and return board games shared by another user. It does not allow borrowing their own games.
9. No users can borrow more than 3 games simultaneously. It will be clearly informed by showing a warning message when the user tries to borrow the 4th game. 
10. Profile model is OneToOne of Django User model.

# Requirement
-	the web site is implemented for an accepted subject, (yes)
-	the implemented web site functions, (yes)
-	MVT architecture is obeyed, (yes)
-	there must be more than 1 model, (yes, 5 models)
-	users (board gamers) can view a list of all available board games entities of one kind, (yes)
-	a user (a board gamer) can add an entity (a board game), (yes)
-	a user can do something for an entity (a board gamer can borrow a board game). (yes)
-	the web site and its source code are presented online to the instructor in agreed time (yes, here it is)

<hr />

- user accounts have been set up (yes)
- no gamer can borrow than 3 games simultaneously (yes)
- a gamer is clearly informed the reason he can’t borrow the 4h game simultaneously  (yes)
- login and logout functionality has been implemented (yes)
- sign-up functionality has been implemented, (yes)
- restricted access has been implemented, (yes)
- information security is considered, at least partly, (yes)
- Django admin site is functioning for the application and the superuser is created, (yes)
- the web site looks good and is styled (well, it depends)

# Some example
### User profile
1. browse all the shared games, the details of borrowing history of every shared game, and remove the available (not borrowed) games.
2. return the borrowed games.

### Single game page
1. the owner can edit or remove the game.
2. all users can publish comment, and edit their comment.

### Category page
1. show all the games under the category (Board Games model is ManyToMany of Category model)
2. category can be modify (add, edit or remove) ONLY by admin.

### Lend Status
- show the currently borrowing status of the game, no history. History is only available for the owner.
