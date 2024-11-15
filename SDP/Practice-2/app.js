const searchtext = document.getElementById("searchText").value;

const allProduct = () => {
  console.log(searchtext);
  fetch(`https://www.themealdb.com/api/json/v1/1/search.php?s=${searchtext}`)
    .then((res) => res.json())
    .then((data) => {
      displayProduct(data);
    });
};

const displayProduct = (products) => {
  const productContainer = document.getElementById("product-container");
  products.meals.forEach((product) => {
    const div = document.createElement("div");
    div.classList.add("card");
    div.innerHTML = `
      <img class="meal-img" src="${product.strMealThumb}" />
      <h5>${product.strMeal}</h5>
      <p>${product.strInstructions.slice(0, 30)}<p/>
      <button type="button"
        class="btn btn-info"
        data-bs-toggle="modal"
        data-bs-target="#exampleModal" onclick="singleProduct(${
          product.idMeal
        })">Details</button>
      `;
    productContainer.appendChild(div);
  });
  // console.log(products.meals);
};

const singleProduct = (id) => {
  fetch(`https://www.themealdb.com/api/json/v1/1/lookup.php?i=${id}`)
    .then((res) => res.json())
    .then((data) => {
      displaySingleProduct(data.meals);
    });
};

const displaySingleProduct = (product) => {
  const modalContainer = document.getElementById("modal-container");

  const div = document.createElement("div");
  console.log(product[0]);

  div.innerHTML = `
      <div class="modal fade"
        id="exampleModal"
        tabindex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true"
      >
        <div class="modal-dialog">
          <div class="modal-content">
            <div class="modal-header">
              <h1 class="modal-title fs-5" id="exampleModalLabel">
              ${product[0].strMeal}
              </h1>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <div class="modal-body text-center">
              <img width="250px" src="${product[0].strMealThumb}" />
              <p>${product[0].strInstructions.slice(0, 100)}</p>
            </div>
            <div class="modal-footer">
              
            </div>
          </div>
        </div>
      </div>
    </div>
  `;
  modalContainer.appendChild(div);
};

const searchBtn = document.getElementById("buttonSearch");
// allProduct();
