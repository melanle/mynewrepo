from flask import Flask

app=Flask(__name__)
#decorator
@app.route('/')
def welcome():
    return 'Welcome'


if __name__=="__main__":
    app.run(debug=True)
