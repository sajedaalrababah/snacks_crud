# Django CRUD and Forms

## Class-28

---

### Overview
#### Add full CRUD functionality to your bag of tricks by building a Django project that allows Creating, Reading, Updating and Deleting.

<br>
<br>

### Feature Tasks and Requirements
- Create snacks_crud_project Django project

<br>

- Create snacks app

<br>

- Create Snack model
    - title field
    - purchaser field
    - description field
    - Register model with admin

<br>

- Create SnackListView that extends appropriate generic view
    - associated url path is an empty string

<br>

- Create SnackDetailView that extends appropriate generic view
    - associated url path is <int:pk>/

<br>

- Create SnackCreateView that extends appropriate generic view
    - associated url path is create/

<br>

- Create SnackUpdateView that extends appropriate generic view
    - associated url path is <int:pk>/update/

<br>

- Create SnackDeleteView that extends appropriate generic view
    - associated url path is <int:pk>/delete/

<br>

- Add urls to support all views, with appropriate names

<br>

- Add templates to support all views

<br>

- Add navigation links in approp

<br>

- Make all necessary changes to project level files for project to run
    - In other words, make it work

<br>
<br>

### Implementation Notes
#### A lot of functionality is being added here. But it should still follow the “Django way.” So when in doubt refer back to demo.

<br>

### User Acceptance Tests
- Test all Views
- Test Model
    - string representation
    - all fields
- When in doubt on what to test refer to demo

<br>
<br>

### Configuration

#### Create a virtual environment inside snacks_crud.

<br>

---
<br>

