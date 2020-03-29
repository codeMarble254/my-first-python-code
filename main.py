from flask import Flask, render_template, request

app=Flask("__name__")

@app.route("/")
def displayEntry():
    return render_template("landing.html")

@app.route("/home", methods = ["POST"])
def evaluate():
    if request.method == "POST":
        sentence = request.form["enterSentence"]
        count = 0
        output={'a':0,'b':0, 'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
        for char in sentence:
            output.setdefault(char, 0)
            count+=1
            output[char] += 1
        return render_template("results.html", output=output, count=count)
    else:
        return render_template("landing.html")

if __name__ == "__main__":
    app.run(debug=True)
