import sys

if __name__ == '__main__':
    #python .py {filename} {item} {settlement}
    file_name = sys.argv[1]
    item = sys.argv[2]
    settlement = sys.argv[3]
    print file_name, item, settlement

    _sum = 0
    _count = 0
    with open(file_name, 'r') as data:
        for line in data:
            row = [str(item).strip() for item in line.strip().split(',')]
            if len(row) < 3: 
                continue
            if row[1] == item and row[2] == settlement:
                #print '\t'.join(row)
                try:
                    _sum += int(row[5])
                    _count += 1
                except ValueError as e:
                    print '[ERROR]', e

    print _sum, _count
