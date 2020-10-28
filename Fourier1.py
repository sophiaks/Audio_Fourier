import sounddevice as sd
import winsound

num = int(input("Escolha um número de 0 a 9:  "))

bitrate = 16000
length = 3

dict_frequencies = {}
dict_frequencies[0] = [941, 1336]
dict_frequencies[1] = [697, 1209]
dict_frequencies[2] = [697, 1336]
dict_frequencies[3] = [697, 1477]
dict_frequencies[4] = [770, 1209]
dict_frequencies[5] = [770, 1336]
dict_frequencies[6] = [770, 1477]
dict_frequencies[7] = [859, 1209]
dict_frequencies[8] = [859, 1336]
dict_frequencies[9] = [859, 1477]



winsound.Beep(dict_frequencies[num][0], 1000)
winsound.Beep(dict_frequencies[num][1], 1000)

