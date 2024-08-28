```python
versions = ['152.10.3.5', '0.0.42', '36', '152.11', '0.0.42.1']

versions_list_length = len(versions)

for i in range(versions_list_length):
    for j in range(versions_list_length - i - 1):
        element_one = versions[j].split('.')
        element_two = versions[j + 1].split('.')

        for index in range(len(element_one)):
            element_one[index] = int(element_one[index])
        for index in range(len(element_two)):
            element_two[index] = int(element_two[index])

        if element_one > element_two:
            versions[j], versions[j + 1] = versions[j + 1], versions[j]

print(versions)

```