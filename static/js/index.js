var dropElement = document.getElementById("drop");
var totalElement = document.getElementById("total");
var allNumeric = document.querySelectorAll('input[type="number"]');;

function calculate_all_value() {
    // allNumeric = 
    var total = 0;
    for (var element of allNumeric) {

        var id_ = element.attributes.id.value;
    
        var dollarValueTemp = parseFloat(parseFloat(id_.slice(1, id_.length)).toFixed(2));
        console.log("Type of dollarValueTemp: ", dollarValueTemp, typeof(dollarValueTemp));
    
        var dollarValue = isNaN(dollarValueTemp) ? 0 : dollarValueTemp;
        console.log("Type of dollarValue: ", dollarValue, typeof(dollarValue));
    
        var inputValue = isNaN(element.valueAsNumber) ? 0 : element.valueAsNumber;
    
        total = parseFloat(parseFloat(total + (dollarValue * inputValue)).toFixed(2));
        console.log({
                    id_: id_,
                    dollarValue: dollarValue,
                    inputValue: inputValue,
                    total: total
                });
    
        totalElement.value = total;
        if (total > 150) {
            dropElement.value = parseFloat((total - 150).toFixed(2));
        }
        else{
            dropElement.value = 0.00;
        }
    }
    // var total = 0;
    // for (var element of allNumeric) {
        
    //     var id_ = element.attributes.id.value;
    //     var denomination_value = id_.slice(1, id_.length);
        
        
    //     final_value = isNaN(parseFloat(element.value).toFixed(2)) ? 0 : parseFloat(denomination_value).toFixed(2) * parseFloat(element.value).toFixed(2);
    //     total = total + final_value;
    //     total =  parseFloat(total).toFixed(2)
    //     console.log({
    //         id_: id_,
    //         denomination_value: denomination_value,
    //         final_value: final_value,
    //         total: total
    //     });

    //     totalElement.value = total;
    //     var dropAmount = total - 150;
    //     if (dropAmount < 0) {
    //         dropElement.value = 0;
    //     }
    //     else {
    //         dropElement.value = parseFloat(dropAmount).toFixed(2);
    //     }
    // }

}

for (var element of allNumeric) {
    // element.addEventListener('change', calculate_drop_value);
    element.addEventListener('input', calculate_all_value);
}