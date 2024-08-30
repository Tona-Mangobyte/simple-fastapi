from fastapi import FastAPI, Body, Header

app = FastAPI()

@app.get("/")
def greet():
    return "Hello World!"

@app.get("/hello/{who}")
def hello(who: str):
    return f"Hello, {who}?"

@app.get("/greet")
def greet(who: str):
    return f"Greet, {who}!"

@app.post("/greet")
def greet_post(who: str = Body(...)):
    return f"Greet, {who}!"

@app.post("/agent")
def get_agent(user_agent:str = Header()):
    return user_agent

@app.get("/happy")
def happy(status_code=200):
    return ":)"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("hello:app", reload=True)
