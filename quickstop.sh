ps aux | grep java | grep druid  | awk '{print $2}' | xargs kill -9
