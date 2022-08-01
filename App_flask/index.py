<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Fraud Web Application</title>
    <meta charset="utf-8">
        <meta name="author" content="RahulKumarSingh">
        <meta name="viewport" content="width=device-width, initial-scale=1.0,maximum-scale=1,user-scalable=yes">
    <link rel="stylesheet" type="text/css" rel="noopener" target="_blank" href="static/AppStyle.css">


</head>
<body>

    <div class="model_desc">
    <h2> Model Description </h2><br>
    <p>This web application is Fraud transaction prediction system. The aim of this project is to predict that the transaction is Fraud or Not based on their values and transaction type.</p>
    <p>After inputting the corresponding data, a predicted output is displayed.<br>The Step is maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).<br>The Org is balance of origin account before transaction and after transaction.<br> Dest is Destination account balance before and after transaction.<br>Type is the type of transaction customer has done like CASH OUT, PAYMENT, CASH IN, DEBIT and TRANSFER.
    </p>

</div>

<div class="data_part">
    <div class="model_desc2">
        <h2>Model Description</h2><br>
        <p>This web application is Fraud transaction prediction system. The aim of this project is to predict that the transaction is Fraud or Not based on their values and transaction type.</p>
    <p>After inputting the corresponding data, a predicted output is displayed.<br><br> The Step is maps a unit of time in the real world. In this case 1 step is 1 hour of time. Total steps 744 (30 days simulation).<br><br>The Org is balance of origin account before transaction and after transaction.<br><br> Dest is Destination account balance before and after transaction.<br><br>Type is the type of transaction customer has done like CASH OUT, PAYMENT, CASH IN, DEBIT and TRANSFER.
    </p>

    </div>


    <h1>FRAUD PREDICTION</h1>

    <form action="{{url_for('predict')}}" method="post">
            <input class="Input" type="number" name="step" min="0" max='744' step="any" placeholder="Enter step less than 755" required/>
        <input class="Input" type="number" name="amount" min="0" step="any" placeholder="Enter amount" required/>
        <br><br>
        <input class="Input" type="number" name="oldbalanceOrg" min="0" step="any" placeholder="Enter oldbalanceOrg" required/>
        <input class="Input" type="number" name="newbalanceOrig" min="0" step="any" placeholder="Enter newbalanceOrig" required/>
        <br><br>
        <input class="Input" type="number" name="oldbalanceDest" min="0" step="any" placeholder="Enter oldbalanceDest" required/>
        <input class="Input" type="number" name="newbalanceDest" min="0" step="any" placeholder="Enter newbalanceDest" required/>
        <br><br>
        <select name="comp_select3" class="Input">
              {% for o in data %}
              <option value="{{ o.typeid }}">{{ o.typeid }}</option>
              {% endfor %}
            </select><br><br>
        <button type="submit" class="pred-btn"> Predict </button>

</form>
    <h3> {{prediction_text}} </h3>

</div>



</body>
</html>