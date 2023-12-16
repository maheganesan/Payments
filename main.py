from flask import Flask, render_template, request
import stripe

app = Flask(__name__)

stripe.api_key = "sk_test_51OMYjYSE9NePJBUOMu2MFqCQwvZVbqaCrC5YcSZhzfn4rKoOF1C4IukO7op5pK7A4qyQue4yMu0U61Vor9xSUR1j00g5qXgT72"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/charge', methods=['POST'])
def charge():
    amount = 100

    customer = stripe.Customer.create(
        email=request.form['stripeEmail'],
        source=request.form['stripeToken']
    )

    charge = stripe.Charge.create(
        customer=customer.id,
        amount=amount,
        currency='INR',
        description='Flask Stripe Payment'
    )

    return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
