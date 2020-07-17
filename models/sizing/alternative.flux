

diskio = from(bucket: "telegraf/two_weeks")
  |> range(start: -5m, stop: -4m)
  |> filter(fn: (r) => r._measurement == "diskio" and (r._field == "reads" or r._field == "writes" or r._field == "write_bytes" or r._field == "read_bytes"))
  |> filter(fn: (r) => r.host =~ /data/ and r.host =~ /data/)
  |> group(columns: ["_time","_value","name"], mode: "except")
  |> difference(nonNegative: true)
  |> sum()
  |> duplicate(column: "_stop", as: "_time")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> drop(columns: ["_measurement","_start","_stop","name"])
  |> rename(columns: {read_bytes: "read_bytes_per_min", reads: "reads_per_min", write_bytes: "write_bytes_per_min", writes: "writes_per_min"})


