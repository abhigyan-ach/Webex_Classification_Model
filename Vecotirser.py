
import pandas as pd

# clear file
with open("/content/zoom/MyDrive/webex-consolidated.csv", "w") as f:
  f.write("Feature Description,Month\n")

# associate month num with file name
data_switch = {
  1 : 'jan-',
  2 : 'feb-',
  3 : 'mar-',
  4 : 'apr-',
  5 : 'may-',
  6 : 'jun-',
  7 : 'jul-',
  8 : 'aug-',
  9 : 'sep-',
  10 : 'oct-',
  11 : 'nov-',
  12 : ''
}

for month in range(1,13,1):
  # october is empty
  if month == 10:
    continue
  # read individual month csv
  data = pd.read_csv(
      f"/content/zoom/MyDrive/zoom-data/{data_switch[month]}Webex-features-2022.csv",
      encoding="ISO-8859-1"
      )
  # add column with month represented as an int
  data["Month"] = [month for _ in range(data["Feature Description"].size)]
  # write only feature and month to consolidated csv
  data.to_csv(
      "/content/zoom/MyDrive/zoom-consolidated.csv",
      columns=["Feature Description", "Month"], 
      index=False,
      header=False,
      mode='a'
  )
