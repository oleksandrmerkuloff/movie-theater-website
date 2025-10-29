document.addEventListener("DOMContentLoaded", function() {
    const cart = {}; // { id: {name, price, qty} }
    const cartItemsContainer = document.getElementById("cart-items");
    const cartTotal = document.getElementById("cart-total");

    function updateCartDisplay() {
        cartItemsContainer.innerHTML = "";
        let total = 0;

        Object.values(cart).forEach(item => {
            total += item.price * item.qty;

            const div = document.createElement("div");
            div.classList.add("cart-item");
            div.innerHTML = `
                <span>${item.name} × ${item.qty}</span>
                <span>₴${(item.price * item.qty).toFixed(2)}</span>
            `;
            cartItemsContainer.appendChild(div);
        });

        cartTotal.textContent = `₴${total.toFixed(2)}`;
    }

    document.querySelectorAll(".product-card").forEach(card => {
        const id = card.dataset.id;
        const name = card.dataset.name;
        const price = parseFloat(card.dataset.price);
        const qtyDisplay = card.querySelector(".quantity");

        card.querySelector(".plus").addEventListener("click", () => {
            cart[id] = cart[id] || { name, price, qty: 0 };
            cart[id].qty++;
            qtyDisplay.textContent = cart[id].qty;
            updateCartDisplay();
        });

        card.querySelector(".minus").addEventListener("click", () => {
            if (cart[id] && cart[id].qty > 0) {
                cart[id].qty--;
                qtyDisplay.textContent = cart[id].qty;
                if (cart[id].qty === 0) delete cart[id];
                updateCartDisplay();
            }
        });
    });

    document.getElementById("confirm-cart").addEventListener("click", () => {
        if (Object.keys(cart).length === 0) {
            alert("Your cart is empty!");
            return;
        }
        console.log("Cart confirmed:", cart);

        // Send to Django backend
        fetch(CREATE_CART_URL, {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": getCookie("csrftoken"),
            },
            body: JSON.stringify({"items": cart, 'total': cartTotal.textContent}),
        })
        .then(res => res.json())
        .then(data => {
            if (data.redirect_url) {
                window.location.href = data.redirect_url;
            }
            // alert("Order confirmed!");
            console.log(data);
        });
    });
});

// Helper: CSRF for Django
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let cookie of cookies) {
            cookie = cookie.trim();
            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}