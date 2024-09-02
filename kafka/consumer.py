# from confluent_kafka import Consumer, KafkaError
#
# config = {
#     'bootstrap.servers': 'localhost:9092',
#     'group.id': 'match_events',  # Identifikator grupe potrošača
#     'auto.offset.reset': 'earliest'
# }
#
# consumer = Consumer(**config)
# consumer.subscribe(['match_events'])
#
# def recieve_message():
#     try:
#         while True:
#             msg = consumer.poll(1.0)  # čekajte poruku do 1 sekunde
#
#             if msg is None:
#                 continue
#             if msg.error():
#                 if msg.error().code() == KafkaError._PARTITION_EOF:
#                     # Kraj particije
#                     continue
#                 else:
#                     print(msg.error())
#                     break
#             print(msg.value().decode('utf-8'))
#     finally:
#         consumer.close()
