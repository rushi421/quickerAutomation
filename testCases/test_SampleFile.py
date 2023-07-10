import pytest

@pytest.mark.parametrize("username, password", [("bhavani","bhavani@123"), ("naresh", "naresh@123"),("rushi","rushi@123")])
def test_sample1(username,password):
    print(username+"+"+password)