
from library.file.directory import directory
from library.file.readfile import readfile
from library.string.searchstring import searchstring
from library.data.tree import tree

if __name__ == '__main__':

    print('START')
    flist = directory()
    flist.setpath('./files')
    print(flist.getfile())
    print(flist.getfile_ext_filter('.txt'))
    fileslist = flist.getfile_ext_filter('.txt')
    fh = readfile()
    str_mgr = searchstring()

    data_store = {}
    counter = 0;

    for file in fileslist:
        counter = counter + 1

        value_store = {}


        #open file
        fh.open('./files', file)

        row_pmdcoeff = fh.getline_startwith('PMD Coefficient:')[0]
        value_pmdcoeff = str_mgr.search_numbers(row_pmdcoeff)
        value_store['PMD_COEFF']=value_pmdcoeff

        row_pmddelay = fh.getline_startwith('PMD Delay:')[0]
        value_pmddelay = str_mgr.search_numbers(row_pmddelay)
        value_store['PMD_DELAY']=value_pmddelay

        row_date = fh.getline(23)
        row_date = row_date.strip()
        str_split = row_date.split(' ')
        value_store['DATE']=str_split[0]
        value_store['TIME']=str_split[1]

        data_store[counter]=value_store

    print(data_store)

    resultf = open("result.txt","a")
    resultf.write('DATE,TIME,PMD DELAY, PMD COEFFICIENT \n')

    for key, value in data_store.items():
        resultf.write(value.get("DATE"))
        resultf.write(',')
        resultf.write(value.get("TIME"))
        resultf.write(',')
        resultf.write(value.get('PMD_DELAY'))
        resultf.write(',')
        resultf.write(value.get('PMD_COEFF'))
        resultf.write('\n')

    resultf.close()
    print ('FINISHED')