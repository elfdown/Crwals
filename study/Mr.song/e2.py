#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pickle

d=dict(name="bob",age=20,score=88)
with open("dump.txt","wb") as f:
    pickle.dump(d,f)
