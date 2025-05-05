from fastapi import FastAPI
import subprocess

app = FastAPI()

def getThermal():
    with open('/sys/class/thermal/thermal_zone0/temp') as f:
        return [int(s) for s in f][0] / 1000

def getGitHub():
    return

@app.get('/api/main')
async def home():
    return {'temp': getThermal()}
