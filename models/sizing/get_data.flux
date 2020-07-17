import "experimental"

cpu = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "cpu" and (r._field == "usage_system" or r._field == "usage_user"))
  |> filter(fn: (r) => r.host =~ /data/)
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> rename(columns: {usage_user: "cpu_usage_user", usage_system: "cpu_usage_system"})
  |> group(columns: ["host"])
  |> drop(columns: ["_measurement","_start","_stop","cpu"])

mem = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "mem" and (r._field == "used" or r._field == "available"))
  |> filter(fn: (r) => r.host =~ /data/)
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> rename(columns: {used: "mem_used", available: "mem_available"})
  |> drop(columns: ["_measurement","_start","_stop"])
  |> group(columns: ["host"])

// pointReqs query needs to be fixed so derivative can happen prior to group
// derivative is creating empty tables because some (randomly?) tables have only one record<-- my interpretation from Flux team
pointReqs = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "influxdb_write")
  |> filter(fn: (r) => r._field == "pointReq")
  |> filter(fn: (r) => r.host =~ /data/ and r.host !~ /data-1/)
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> experimental.group(columns: ["cluster_id","host"], mode: "extend")
  |> derivative(unit: 1m, nonNegative: true, columns: ["pointReq"], timeColumn: "_time")
  |> rename(columns: {pointReq: "point_req_per_min"})
  |> drop(columns: ["_measurement","_start","_stop","url"])

system = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "system" and (r._field == "load1" or r._field == "load15" or r._field == "load5" or r._field == "n_cpus"))
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> drop(columns: ["_measurement"])

// needs a sum per disk name per host -- unable to so far because differing row counts per table which will skew sum
diskio = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "diskio" and (r._field == "io_time" or r._field == "iops_in_progress" or r._field == "read_bytes" or r._field == "reads" or r._field == "write_bytes" or r._field == "write_time" or r._field == "writes" or r._field == "read_time"))
  |> experimental.group(columns: ["host", "name"], mode: "extend")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")

queries = from(bucket: "telegraf/two_weeks")
  |> range(start: -1m)
  |> filter(fn: (r) => r._measurement == "influxdb_queryExecutor" and (r._field == "queriesExecuted"))
  |> derivative(unit: 1s, nonNegative: true, columns: ["_value"], timeColumn: "_time")
  |> experimental.group(columns: ["host"], mode: "extend")
  |> pivot(rowKey:["_time"], columnKey: ["_field"], valueColumn: "_value")
  |> drop(columns: ["_measurement","url"])

 cpu_mem = join(tables: {d1: cpu, d2: mem}, on: ["_time","cluster_id","host"])
 points_cpu_mem = join(tables: {d1: pointReqs, d2: cpu_mem}, on: ["_time","cluster_id","host"])
 sys_points_cpy_mem = join(tables: {d1: points_cpu_mem, d2: system}, on: ["_time","cluster_id","host"])
 join(tables: {d1: sys_points_cpu_mem, d2: diskio}, on: ["_time","cluster_id","host"])