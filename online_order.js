let cartTable;

// regular named function
function makeCartRow(item, price, quantity) {
    const row = document.createElement("tr");
    // td is table data
    const itemData = document.createElement("td");
    itemData.innerText = item;
    row.appendChild(itemData);
    const priceData = document.createElement("td");
    priceData.innerText = price;
    row.appendChild(priceData);
    const quantitydata = document.createElement("td");
    quantitydata.innerText = quantity;
    row.appendChild(quantitydata)
    return row;
}

let exampleArray = [{ item: "soup", price: 3 },
    { item: "salad", price: 3 },
    { item: "sandwich", price: 5 }
]

const rowFromItem = function(value) {
    cartTable.appendChild(makeCartRow(value.element.name, '$' + value.element.price, value.quantity));
}

// anonymous function as a variable
const updateCart = async function(array) {
    itemMap = new Map();
    array.forEach(element => {
        if (!Array.from(itemMap.keys()).includes(element.name)) {
            itemMap.set(element.name, {element, quantity: 1 });
            console.dir(itemMap);
        } else {
            itemMap[element.name].quantity++;
            console.log(itemMap[element.name].quantity);
        }
    });
    cartTable = document.getElementById("cart-content"); // step 1: get parent element
    console.log("called updateCart");
    console.dir(cartTable);
    cartTable.innerHTML = "";
    const headerRow = document.createElement("tr"); // step 2: create new element to be child
    const itemHeader = document.createElement("th"); // also step 2 at the next level down
    const amountHeader = document.createElement("th");
    itemHeader.innerText = "Item"; // step 3: create content for new element
    amountHeader.innerText = "Amount";
    headerRow.appendChild(itemHeader); // step 4: append child (lower level)
    headerRow.appendChild(amountHeader);
    cartTable.appendChild(headerRow); // also step 4 (higher level)
    if (!array) {
        array = [];
    }
    itemMap.forEach(rowFromItem);
    const totalRow = document.createElement("tr"); // step 2 new element
    const totalHeader = document.createElement("th");
    const totalAmount = document.createElement("th");
    let sum = 0;
    array.forEach(function(item) {
        sum += item.price;
    })
    totalAmount.innerText = '$' + sum;
    totalHeader.innerText = "Total: ";
    totalRow.appendChild(totalHeader);
    totalRow.appendChild(totalAmount);
    cartTable.appendChild(totalRow);
}
