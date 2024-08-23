function calculateDollarValue(inputId) {
    const dollarValueTemp = parseFloat(inputId.slice(1, inputId.length));
    return Number.isNaN(dollarValueTemp) ? 0 : dollarValueTemp;
  }
  
  function calculateGrandTotal(allNumeric) {
    let grandTotal = 0;
    for (const element of allNumeric) {
      const inputId = element.attributes.id.value;
      const dollarValue = calculateDollarValue(inputId);
      const inputValue = Number.isNaN(element.valueAsNumber) ? 0 : element.valueAsNumber;
      updateLabel(inputValue, element, inputId);
      grandTotal = parseFloat((grandTotal + (dollarValue * inputValue)).toFixed(2));
    }
    return grandTotal;
  }
  
  function updateElements(grandTotal) {
    const totalElement = document.getElementById("total");
    const dropElement = document.getElementById("drop");
    totalElement.value = grandTotal;
    if (grandTotal > 150) {
      dropElement.value = parseFloat((grandTotal - 150).toFixed(2));
    } else {
      dropElement.value = 0;
    }
  }

  function updateLabel(inputValue, inputElement, inputId) {
    var inputLabel = inputElement.labels[0];
    console.log(inputElement);
    if (inputValue) {
        labelText = `${inputLabel.htmlFor.replace('d', '$')} x ${inputValue} = $${calculateDollarValue(inputId) * inputValue}`;
        inputLabel.innerHTML = labelText;
    }
    else {
        inputLabel.innerHTML = inputLabel.htmlFor.replace('d', '$');
    }
  }
  
  function calculateAllValue() {
    const allNumeric = document.querySelectorAll('input[type="number"]');
    const grandTotal = calculateGrandTotal(allNumeric);
    updateElements(grandTotal);
  }