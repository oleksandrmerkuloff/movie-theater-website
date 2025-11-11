document.addEventListener('DOMContentLoaded', function () {
    const seatSelector = '.seat:not(.booked):not(.empty)';
    const seats = document.querySelectorAll(seatSelector);
    const cartList = document.querySelector('.cart-list');
    const totalPriceEl = document.getElementById('total-price');
    const emptyCartMsg = document.querySelector('.empty-cart');
    const payButton = document.querySelector('.btn-pay');
    const clearButton = document.querySelector('.btn-clear');

    let cart = JSON.parse(sessionStorage.getItem('ticket_cart') || '[]');

    function restoreSelection() {
        cart.forEach(item => {
            const seat = document.querySelector(`[data-seat-id="${item.seat_id}"]`);
            if (seat && !seat.classList.contains('booked')) {
                seat.classList.add('selected');
            }
        });
        updateCartDisplay();
    }

    function updateCartDisplay() {
        if (!cartList || !totalPriceEl) return;

        cartList.innerHTML = '';

        if (cart.length === 0) {
            totalPriceEl.textContent = '0 UAH';
            if (emptyCartMsg) emptyCartMsg.style.display = 'block';
            if (payButton) payButton.disabled = true;
            if (clearButton) clearButton.style.display = 'none';
            return;
        }

        const fragment = document.createDocumentFragment();
        let total = 0;

        cart.forEach(item => {
            const li = document.createElement('li');
            li.className = 'cart-item';
            li.innerHTML = `
                <span class="seat-label">R${item.row}-S${item.seat}</span>
                <span class="seat-price">${item.price} UAH</span>
            `;
            fragment.appendChild(li);
            total += item.price;
        });

        cartList.appendChild(fragment);
        totalPriceEl.textContent = `${total} UAH`;

        if (emptyCartMsg) emptyCartMsg.style.display = 'none';
        if (payButton) payButton.disabled = false;
        if (clearButton) clearButton.style.display = 'block';
    }

    if (payButton) {
        payButton.addEventListener('click', function () {
            const input = document.getElementById('ticket_cart_input');
            if (input) {
                input.value = JSON.stringify(cart);
            }
        });
    }

    if (clearButton) {
        clearButton.addEventListener('click', function () {
            setTimeout(() => {
                cart = [];
                sessionStorage.removeItem('ticket_cart');
                updateCartDisplay();
            }, 100);
        });
    }

    seats.forEach(seat => {
        seat.addEventListener('click', function () {
            const seatId = this.dataset.seatId;
            const row = parseInt(this.dataset.row);
            const seatNum = parseInt(this.dataset.seat);
            const price = parseFloat(this.dataset.price);

            if (isNaN(row) || isNaN(seatNum) || isNaN(price)) return;

            const item = { seat_id: seatId, row, seat: seatNum, price };
            const index = cart.findIndex(i => i.seat_id === seatId);

            if (index > -1) {
                cart.splice(index, 1);
                this.classList.remove('selected');
            } else {
                cart.push(item);
                this.classList.add('selected');
            }

            sessionStorage.setItem('ticket_cart', JSON.stringify(cart));

            updateCartDisplay();
        });
    });

    restoreSelection();
});
