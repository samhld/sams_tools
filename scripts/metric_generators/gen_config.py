
settings = {'gen_type': 'http_producer', #gen_type can be any of `kafka_producer`, `http_client`, `udp_client`
            'host': 'localhost',
            'port': 5000,
            'batch_size': 100,
            'interval': 2}  # how often the client flushes metrics (in seconds)c