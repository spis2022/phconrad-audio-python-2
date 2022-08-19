import wave, struct, math, random



def make_wave_file(filename):
    sampleRate = 44100.0 # hertz
    obj = wave.open(filename,'w')
    obj.setnchannels(1) # mono
    obj.setsampwidth(2)
    obj.setframerate(sampleRate)
    for i in range(99999):
       value = random.randint(-32767, 32767)
       data = struct.pack('<h', value)
       obj.writeframesraw( data )
    obj.close()