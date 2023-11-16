import chardet

with open('rockyou.txt', 'rb') as file:
    lines = [line for line in file]
    print(f'last encoding is {chardet.detect(lines[-1])}')
    # for index, line in enumerate(lines):
    #     print(f'checking encoding of {line} of {len(line)}')
    #     print(f'encoding = {chardet.detect(line)}')





# from chardet.universaldetector import UniversalDetector
# file = open('rockyou.txt')
# detector = UniversalDetector()
# for line in file:
#     detector.feed(line)
#     if detector.done:
#         break
# detector.close()
# print(detector.result)
