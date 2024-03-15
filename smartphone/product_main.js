const data = [{
    id: 1,
    img: 'https://cdn.tgdd.vn/Products/Images/42/235838/Galaxy-S22-Ultra-Burgundy-600x600.jpg',
    product: 'Samsung Galaxy S22 Ultra 5G',
    price: '25.990.000₫'
}, {
    id: 2,
    img: 'https://cdn.tgdd.vn/Products/Images/42/153856/iphone-xi-den-600x600.jpg',
    product: 'iPhone 11',
    price: '11.490.000₫'
}, {
    id: 3,
    img: 'https://cdn.tgdd.vn/Products/Images/42/271717/oppo-reno7-z-5g-thumb-1-1-600x600.jpg',
    product: 'OPPO Reno7 series',
    price: '9.990.000₫'
}, {
    id: 4,
    img: 'https://cdn.tgdd.vn/Products/Images/42/261888/realme-c35-thumb-new-600x600.jpg',
    product: 'Realme C35',
    price: '3.990.000₫'
}, {
    id: 5,
    img: 'https://cdn.tgdd.vn/Products/Images/42/269831/Xiaomi-redmi-note-11-black-600x600.jpeg',
    product: 'Xiaomi Redmi Note 11',
    price: '4.190.000₫'
}, {
    id: 6,
    img: 'https://cdn.tgdd.vn/Products/Images/42/262402/Samsung-Galaxy-A13-cam-thumb-600x600.jpg',
    product: 'Samsung Galaxy A13',
    price: '4.190.000₫'
}, {
    id: 7,
    img: 'https://cdn.tgdd.vn/Products/Images/42/230529/TimerThumb/250262.jpg',
    product: 'iPhone 13 Pro Max',
    price: '29.290.000₫'
}, {
    id: 8,
    img: 'https://cdn.tgdd.vn/Products/Images/42/262650/samsung-galaxy-a23-cam-thumb-600x600.jpg',
    product: 'Samsung Galaxy A23',
    price: '5.090.000₫'
}, {
    id: 9,
    img: 'https://cdn.tgdd.vn/Products/Images/42/272668/xiaomi-redmi-note-11s-5g-lam-hong-thumb-600x600.jpg',
    product: 'Xiaomi Redmi Note 11S series',
    price: '6.280.000₫'
}, {
    id: 10,
    img: 'https://cdn.tgdd.vn/Products/Images/42/249720/Vivo-y15s-2021-xanh-den-660x600.jpg',
    product: 'Vivo Y15 series',
    price: '3.490.000₫'
}, {
    id: 11,
    img: 'https://cdn.tgdd.vn/Products/Images/42/249944/oppo-a55-4g-thumb-new-600x600.jpg',
    product: 'OPPO A55',
    price: '4.490.000₫'
}, {
    id: 12,
    img: 'https://cdn.tgdd.vn/Products/Images/42/250625/samsung-galaxy-z-fold4-120822-014401-600x600.jpg',
    product: 'Samsung Galaxy Z Fold4',
    price: '40.990.000₫'
}, {
    id: 13,
    img: 'https://cdn.tgdd.vn/Products/Images/42/226935/samsung-galaxy-z-fold-3-silver-1-600x600.jpg',
    product: 'Samsung Galaxy Z Fold3 5G',
    price: '31.990.000₫'
}, {
    id: 14,
    img: 'https://cdn.tgdd.vn/Products/Images/42/250622/oppo-find-x5-pro-den-thumb-600x600.jpg',
    product: 'OPPO Find X5 Pro 5G',
    price: '32.990.000₫'
}, {
    id: 15,
    img: 'https://cdn.tgdd.vn/Products/Images/42/230521/TimerThumb/230521.jpg',
    product: 'iPhone 13 Pro',
    price: '26.790.000₫'
}, {
    id: 16,
    img: 'https://cdn.tgdd.vn/Products/Images/42/258047/samsung-galaxy-z-flip4-5g-128gb-thumb-600x600.jpg',
    product: 'Samsung Galaxy Z Flip4',
    price: '23.990.000₫'
}, {
    id: 17,
    img: 'https://cdn.tgdd.vn/Products/Images/42/242439/Galaxy-S22-Plus-White-600x600.jpg',
    product: 'Samsung Galaxy S22+ 5G',
    price: '20.990.000₫'
}, {
    id: 18,
    img: 'https://cdn.tgdd.vn/Products/Images/42/223602/TimerThumb/iPhone-13-1.jpg',
    product: 'iPhone 13',
    price: '20.990.000₫'
}, {
    id: 19,
    img: 'https://cdn.tgdd.vn/Products/Images/42/253138/vivo-x80-xanh-thumb-600x600.jpg',
    product: 'Vivo X80',
    price: '19.990.000₫'
}, {
    id: 20,
    img: 'https://cdn.tgdd.vn/Products/Images/42/236780/TimerThumb/236780.jpg',
    product: 'iPhone 13 mini',
    price: '18.790.000₫'
}, ]

const productList = document.getElementById('productList')

for (let i = 0; i < data.length; i++) {
    productList.innerHTML += `
    <div class="product">
        <img src="${data[i].img}" alt="">
        <p>${data[i].product}</p>
        <h1>${data[i].price}</h1>
    </div>
    `
}

const params = window.location.search
const id = new URLSearchParams(params).get('id')
console.log(id)

for (let i = 0; i < data.length; i++) {
    if (data[i].id == id) {
        console.log(data[i])
    }
}