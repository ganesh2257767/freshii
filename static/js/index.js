allNumeric = document.querySelectorAll('input[type="number"]');
lockerElement = document.getElementById("locker");

function calculate_locker_value(event) {
    // var total = parseFloat(lockerElement.value);
    var total = 0;
    for (var element of allNumeric) {
        
        var id_ = element.attributes.id.value;
        var denomination = id_[0];
        var denomination_value = id_.slice(1, id_.length);
        if (denomination == "c") {
            var factor = 0.01;
        }
        else {
            var factor = 1;
        };
        
        final_value = parseInt(denomination_value) * factor * parseInt(element.value);
        total = total + final_value;
        // console.log({
        //     id_: id_,
        //     denomination: denomination,
        //     denomination_value: denomination_value,
        //     factor: factor,
        //     final_value: final_value,
        //     total: parseFloat(total).toFixed(2)
        // });
        lockerAmount = total - 150;
        if (lockerAmount < 0) {
            lockerElement.value = 0;
        }
        else {
            lockerElement.value = parseFloat(lockerAmount).toFixed(2);
        }
    }
}

for (var element of allNumeric) {
    element.addEventListener('change', calculate_locker_value);
}