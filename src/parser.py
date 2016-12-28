import dns.resolver
import dns.query
import dns.zone

def fetch_records(query_hostname, record_type) :
    record_array = []

    try:
        for record in dns.resolver.query(query_hostname, record_type) :
            record_array.append(str(record))

        return record_array

    except dns.resolver.NoAnswer:
        return ['no records']


