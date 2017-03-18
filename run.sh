date=$(date -v -1d +%Y%m%d)
echo $date
year=${date:0:4}
month=${date:4:2}
day=${date:6:2}

echo $year $month $day
mkdir -p data
zipFile="data/$date.zip"
csvFile="data/$date.csv"
curl http://www.taifex.com.tw/DailyDownload/DailyDownloadCSV/Daily_${year}_${month}_${day}.zip -o $zipFile && unzip -p $zipFile > $csvFile
rm $zipFile

python summary.py $csvFile 'TX' ${year}${month}

