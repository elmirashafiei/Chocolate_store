function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

const searchField = document.querySelector("#searchField");

searchField.addEventListener("keyup", (e) => {
  const searchValue = e.target.value;

  console.log('searchValue', searchValue)

  fetch("/products/search_products/", {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    credentials: "same-origin",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
      "Accept": "application/json",
      'Content-Type': 'application/json'
    },

    body: JSON.stringify({ "searchText": searchValue })

  })
    .then(res => res.json())
    .then(data => {
      let container = document.getElementById('products_container');
      let result = "";
      if (data.length) {
        result += data.map(prod => getProductTemplate(prod));
        result = result.substring(0, result.length - 2);
      } else {
        result = "There isn't any result for the keyword that you are searching.";
      }

      container.innerHTML = result;

    });


})


const getProductTemplate = (prod) => `
                    <div class="col-4">
                                <li><strong>
                                  ${prod.title} (price: ${prod.price} $)
                                  </strong>
                                  <a class="product-title" href="/product/detail/${prod.id}">
                                    <img  src="/media/${prod.thumbnail}" alt="Products!" style="max-width:100%;max-height:100%;
                                    div.desc {
                                      padding: 15px;
                                      text-align: center;} ">
                                  </a>
                                </li>
                              </div>
                    `;