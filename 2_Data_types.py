import pandas as pd 


# Define the data in a dictionary
data = {
    "Type": ["Text", "Numeric", "float", "complex", "Sequence", "tuple", "range", 
             "Mapping", "Set", "frozenset", "Boolean", "Binary", "bytearray", 
             "memoryview", "None"],
    "Python Type": ["str", "int", "float", "complex", "list", "tuple", "range", 
                    "dict", "set", "frozenset", "bool", "bytes", "bytearray", 
                    "memoryview", "NoneType"],
    "Example": ["\"Data Nerd!\"", "42", "3.14159", "1 + 2j", "[1, 2, 3]", "(1, 2, 3)", 
                "range(10)", "{\"key\": \"value\"}", "{1, 2, 3}", "frozenset([1, 2, 3])", 
                "True or False", "b\"Data\"", "bytearray(5)", "memoryview(b\"Data\")", "None"]
}

# Create the DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)

#output should look like this 
#         Type Python Type               Example
#0         Text         str          "Data Nerd!"
#1      Numeric         int                    42
#2        float       float               3.14159
#3      complex     complex                1 + 2j
#4     Sequence        list             [1, 2, 3]
#5        tuple       tuple             (1, 2, 3)
#6        range       range             range(10)
#7      Mapping        dict      {"key": "value"}
#8          Set         set             {1, 2, 3}
#9    frozenset   frozenset  frozenset([1, 2, 3])
#10     Boolean        bool         True or False
#11      Binary       bytes               b"Data"
#12   bytearray   bytearray          bytearray(5)
#13  memoryview  memoryview   memoryview(b"Data")
#14        None    NoneType                  None