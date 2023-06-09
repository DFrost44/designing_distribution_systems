import consul
import random

consul_client = consul.Consul(host='localhost', port=8500)  

def register_service(service_name, service_port,tags):
    service_definition = {
        "address": '172.17.0.1',
        "name": service_name,
        "tags": tags,
        "port": service_port,
        "service_id": f"{service_name}-{service_port}",
    }
    consul_client.agent.service.register(**service_definition)


def get_services_with_tag(tag):
    _, nodes = consul_client.catalog.services()
    filtered_services = [service_name for service_name, service_tags in nodes.items() if tag in service_tags]
    return filtered_services

def get_services_by_name(service_name):
    client = consul.Consul()
    _, services = client.catalog.service(service_name)
    return services


def random_choose_service(service_name):
    filtered = get_services_by_name(service_name)
    rnd_name = random.choice(filtered)
      
    node = rnd_name
    return f'http://{node["ServiceAddress"]}:{node["ServicePort"]}/'


def add_hazelcast_data(data):
    key = f"hazelcast/address{data}" 
    value = f"172.17.0.{data}:5701"
    consul_client.kv.put(key, value)
    key = f"hazelcast/map_name" 
    value = f"User_Messages"
    consul_client.kv.put(key, value)

def add_mq_data():
    key = f"mq/address" 
    value = f"172.17.0.3"
    consul_client.kv.put(key, value)
    key = f"mq/name" 
    value = f"MQ"
    consul_client.kv.put(key, value)

def get_key(key):
    _, data = consul_client.kv.get(key)
    if data is not None:
        return data['Value'].decode("utf-8")
    return None

