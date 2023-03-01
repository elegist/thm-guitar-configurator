let addToCartButtons = document.querySelectorAll(".update-cart");

addToCartButtons.forEach((button) => {
    button.addEventListener("click", () => {
        let productId = button.dataset.product;
        let action = button.dataset.action;

        if (USER === "AnonymousUser") {
            console.log("Not logged in");
        } else {
            updateCart(productId, action);
        }
    });
});

const updateCart = (productId, action) => {
    let url = "/update_cart/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrftoken,
        },
        body: JSON.stringify({ productId: productId, action: action }),
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            location.reload();
        });
};
