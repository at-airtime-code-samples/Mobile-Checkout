const credentials = {
  apiKey: "62e778b1e5abf6b46a5444e83d424b1337308a5f7b8726408a37217278113fec",
  username: "sandbox"
};

const AfricasTalking = require('africastalking')(credentials);

const payments = AfricasTalking.PAYMENTS;

const initiateMobileCheckout = async () => {
  const options = {
    //Set the product name
    productName: "DUKA",
    phoneNumber: "+254727545805",
    currencyCode: "KES",
    amount: 100,
    metadata: {
      foo: "bar",
      bar: "foo"
    }
  };

  try{
    const result = await payments.mobileCheckout(options);
    console.log(result);
  } catch (err){
    console.log(err);
  }
};

initiateMobileCheckout();
