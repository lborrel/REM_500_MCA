# Extraction and plotting of the data taken from the REM 500 Neutron Survey Meter

# Authors: Leo Borrel, Sophie Middleton
# Date: 2022-05-20


import matplotlib.pyplot as plt
import csv

time = []
counts = []

with open('data/count_data.txt') as data_file:
    for line in data_file:
        if len(line) == 16:
            value = int(line[0:6],16)
            date = line[7:15]
            time.append(int(date[6:8]) + 60*int(date[3:5]) + 3600*int(date[0:2]))
            counts.append(value)

# Export data to csv
csv_file = open('data/count_data.csv', 'w')
header = ['time', 'counts']

rows = zip(time, counts)

with open('data/count_data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(header)
    for row in rows:
        writer.writerow(row)


# plots

plt.figure()
plt.plot(time, counts)

plt.xlabel('time [s]')
plt.ylabel('Counts')



# Plot of the data from each channel

channel = []

with open('data/channel_data.txt') as channel_file:
    for line in channel_file:
        channel.append(int(line[0:5]))

QF = []

with open('data/QF.txt') as QF_file:
    for line in QF_file:
        QF.append(float(line[0:-1]))

rad = 0
for i in range(5,255):
    rad += 100 * i * channel[i] / 20

rem = 0
for i in range(5,255):
    rem += 100 * i * channel[i] * QF[i] / 20

# divide by runtime
rad = rad / time[-1]
rem = rem / time[-1]

print('rad: ', rad, ' urad/h')
print('rem: ', rem, ' urem/h')

# plot

plt.figure()
plt.bar(range(256),channel)

plt.xlabel('channel #')
plt.ylabel('count')



plt.show()

