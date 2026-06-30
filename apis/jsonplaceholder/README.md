# JSONPlaceholder Client Exercise

API docs: https://jsonplaceholder.typicode.com/

JSONPlaceholder is a fake REST API that is useful for practicing client structure, resource modeling, filtering, and error handling without authentication.

## Client acceptance criteria

Build a Python client that can:

- fetch posts, comments, albums, photos, todos, and users
- fetch individual resources by ID
- support query parameters such as `userId` or `postId`
- model predictable error behavior for missing resources and non-2xx responses
- expose async methods for IO-bound operations
- include tests that mock HTTP responses instead of relying only on live API calls

## API features to exercise

- REST resource paths
- filtering with query parameters
- response validation
- client method naming and resource modeling
- optional pagination-like helpers, even though this API mostly returns bounded lists
