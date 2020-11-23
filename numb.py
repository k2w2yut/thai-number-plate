import math

count = 0
bad_pairs = [
    '03', '30', '10', '01', '12', '21', '33', '07', '70', '13', '31', '37', '73', '38', '83',
    '13', '31', '73', '37', '38', '83', '33',
    '10', '01', '02', '20', '03', '30', '13', '31', '33', '06', '60', '67', '76',
    '11', '91', '19',
    '35', '53', '36', '63', '39', '93', '17', '71', '77', '76', '67'
]
good_pairs = [
    '15', '51', '55', '49', '94', '95', '59', '99',
    '22', '23', '32', '24', '42', '26', '62', '29', '92', '36', '63',
    '15', '51', '35', '53', '45', '54', '89', '98', '99',
    '24', '42', '36', '63', '66', '28', '82',
]
bad_for_day = {
    'sun'  : [3,6],
    'mon'  : [1,5],
    'tue'  : [1,2],
    'wedd' : [3,8],
    'wedn' : [4,5],
    'thu'  : [7],
    'fri'  : [7,8]
}
birthday = 'wedn'
for n in range(0,10000):
    a = str(n).zfill(4)

    q = int(a[0])
    w = int(a[1])
    e = int(a[2])
    r = int(a[3])

    keep = True
    for b in bad_for_day[birthday]:
        if str(b) in a:
            keep = False
    if not keep:
        continue

    if q + w + e + r == 13:
        continue
    if (q == 1 and r == 1) or (w == 1 and e == 1):
        continue
    
    skip = False
    for p in bad_pairs:
        if p in a:
            skip = True
            break
    if skip:
        continue

    keep = False
    for p in good_pairs:
        if p in a:
            keep = True
            break
    if not keep:
        continue

    if (q + w) % 10 != 9:
        continue
    if (e + r) % 10 != 9:
        continue

    count = count + 1
    print(a)
print('Remaining: ', count)
