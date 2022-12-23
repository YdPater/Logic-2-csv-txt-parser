from argparse import ArgumentParser


def generate_strings(INFILE, valid_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!`~?/\|><,.=-_+", string_length = 3):
    recording = False
    counter = 0
    words = []

    with open(INFILE, "r") as infile: 
        word = []
        for line in infile:
            if "Read" in line:
                _, _, _, data, *_ = line.split(",")
                if data in valid_chars:
                    recording = True
                    counter += 1
                    word.append(data)
                else:
                    if recording and counter >= string_length:                        
                        words.append(word)
                    word = []
                    recording = False
                    counter = 0
    return words
                

if __name__ == "__main__":
    parser = ArgumentParser(description="Generate strings from logic 2 csv output (I2C)")
    parser.add_argument("PROTOCOL", type=str, help="Supported protocols: i2c")
    parser.add_argument("FILE", type=str, help="Specify input file")
    parser.add_argument("--charset", type=str, help="Specify charset for string detection.", default="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789)(*&^%$#@!`~?/\|><,.=-_+")
    parser.add_argument("-sl", "--string-length", help="Specify the minimum string length.", type=int, default=3)
    args = parser.parse_args()
    
    words = generate_strings(args.FILE, args.charset, args.string_length)
    for w in words:
        print("".join(w))  
            
