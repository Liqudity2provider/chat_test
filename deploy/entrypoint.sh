#!/bin/bash

set -e

uvicorn chat_test.main:app --host 0.0.0.0 --port 8000