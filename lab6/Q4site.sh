#!/bin/bash
curl http://127.0.0.1:2223/Q4[000-999] > Q4attack.log
vim Q4attack.log -c '/Q4=[^T]'