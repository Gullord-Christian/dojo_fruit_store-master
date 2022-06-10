from flask import Flask, render_template, request, redirect
app = Flask (__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_count = request.form['strawberry']
    raspberry_count = request.form['raspberry']
    apple_count = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    count = int(strawberry_count) + int(raspberry_count) + int(apple_count)
    print(f"Charging {first_name} {last_name} for {count} fruit")
    return render_template("checkout.html", first_name = first_name, strawberry_count = strawberry_count, raspberry_count = raspberry_count, apple_count = apple_count)


@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    