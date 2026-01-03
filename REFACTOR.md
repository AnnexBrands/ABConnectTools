# Routes Refactor

## Goal
Update all endpoints to lookup Route from ABConnect/api/routes instead of storing the path as a string in the endpoint.

This maintains an explicit request and response model lookup in a central config.

Post Routes Refactor, for each route
* example is created
* fixture is stored in tests/fixtures/{ModelName.by_alias=True}.json
* tests/api/test_{tag}::test_endpoint.py asserts that the 

## Tracking progress

Create a table in REFACTOR_PROGRESS.md checking off the following has happened.

A subagent should also work on a single Route in sequence.
* Hooman intervention required ( you set ❗, I set ✅)
* Endpoint implementation uses the route and has params 
* A simple example allows us to save a fixture (see examples/api/contacts.py for a demo)
* A fixture allows us to inspect server data (see tests/fixtures/ContactDetails.json with conftest.py fixture)
* A pytest allows us to assert that running the endpoint returns the model instance, (dict means model validate failed)
* A pytest allows us to capture that the fixture can still pass model validate

## Creating an example file

Use examples/api/contacts.py as an example. An example should be as brief as possible. Define params, call api.

Create a simple example in examples/api/[tag].py **important** examples always use api = ABConnectAPI(env='staging', username='instaquote')

If parameters are required, flag for hooman.
If method is DELETE, PATCH, PUT - flag for hooman.
Write but do not run examples and pytests awaiting hooman.

## Creating a fixture file

Any example should result in in not exists, save fixture.
Any extant fixture should be loaded in conftest ( write but return early if we know fixture name but file not found )

## Creating a pytest file

generally endpoint > example > test should be matching file names. some (e.g. helpers) will probably consolidate and simplify, like we will test forms.get_bol() but not get_form_shipments, and overtime we will probably just use convenience funcs in alias tasks and not might not expose examples for timelines, but you can implement timelines files for now.

## Update REFACTOR_PROGRESS.md

Create a commit and pull request
Perform a review - if we are changing anything outside of the minimal enpoint implementation and the explicit items in REFACTOR.md, flag for HITL.