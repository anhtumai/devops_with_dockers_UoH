try:
    if True:
        raise ValueError("DCM")
except Exception as e:
    if type(e) == ValueError:
        print("Lozz")
