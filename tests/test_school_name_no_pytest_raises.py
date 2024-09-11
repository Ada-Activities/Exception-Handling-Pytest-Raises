from school_name import claim_unreserved_code_school_name

def test_invalid_name_no_pytest():
    # Implement the equivalent of this test logic but DO NOT import or otherwise access pytest:

    # with pytest.raises(ValueError):
    #     claim_unreserved_code_school_name("Ada Developers Academy")

    # Think about what the test actually does and think about how to write them ourselves.


    # Assume no error will occur
    got_error = False

    try:
        # Call the function in a try block so we can watch for the error
        claim_unreserved_code_school_name("Ada Developers Academy")
    except ValueError:
        # We saw the error so we'll change the value of `got_error` to reflect this 
        got_error = True

    # Make sure we got the expected error
    assert got_error

    # Isn't the version that uses pytest.raises clearer?