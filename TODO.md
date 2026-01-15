# TODO Plan

## Step 1: Add Earthquake model to server/models.py

- [x] Create Earthquake class inheriting from db.Model and SerializerMixin
- [x] Define columns: id (Integer, primary key), magnitude (Float), location (String), year (Integer)

## Step 2: Add routes to server/app.py

- [x] Add GET /earthquakes/<id> route
- [x] Add GET /earthquakes/magnitude/<magnitude> route

## Step 3: Run tests to verify

- [ ] Run pytest to confirm all tests pass
