# from confluent_kafka import Producer
# config = {
#     'bootstrap.servers': 'localhost:9092',  # Adresa Kafka poslužitelja
# }
# producer = Producer(**config)
# def delivery_report(err, msg):
#     if err is not None:
#         print('Message delivery failed:', err)
#     else:
#         print('Message delivered to', msg.topic(), msg.partition())
#
#
