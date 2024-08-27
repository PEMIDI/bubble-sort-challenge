# TODO : 152.10.3.5, 0.0.42, 36, 152.11, 0.0.42.1




# 0 < n <= 50

versions = ['152.10.3.5', '0.0.42', '36', '152.11', '0.0.42.1']


k = len(versions)

for i in range(k):

    for j in range(k-i):

        for item in
        if versions[j].split('.') > versions[j+1].split('.'):
            versions[j], versions[j+1] = versions[j+1], versions[j]













