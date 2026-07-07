#!/usr/bin/env python3
import random
import typing


def gen_event() -> typing.Generator:
    players = ["alice",
               "bob",
               "charlie",
               "dylan"]
    actions = ["run",
               "move",
               "sleep",
               "grab",
               "release",
               "swim",
               "eat",
               "climb",
               "use"]
    while True:
        temp = (random.choice(players), random.choice(actions))
        yield temp


def consume_event(events: list) -> typing.Generator:
    while len(events) > 0:
        i = random.randint(0, len(events)-1)
        event = events.pop(i)
        yield event


g = gen_event()
for i in range(1000):
    event = next(g)
    print(f"Event {i}: player {event[0]} did actoin {event[1]}")
events = []
g = gen_event()
for i in range(10):
    event = next(g)
    events.append(event)
print(f"Built list of 10 events : {events}")
consume_event(events)
event = []
g = consume_event(events)
for i in range(10):
    event = next(g)
    print(f"Got event from list: {event}")
    print(f"Remains in list: {events}")
