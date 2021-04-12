var d;
$(function () {
  $('#product-search').on('keyup', function() {
    var value = $(this).val().toLowerCase();
    $('.js-products-table .js-product-item').filter(function() {
      $(this).toggle(
        $(this).children('.js-product-name').text().toLowerCase().indexOf(value) > -1
      );
    });
  });

  $('.js-add-product').on('click', function() {
    var item = $(this).closest('.js-product-item');
    var itemId = item.data('id');
    var purchasePrice = item.data('purchase-price');
    var name = item.find('.js-product-name').text();
    var salePrice = item.find('.js-product-price').val();
    var quantity = item.find('.js-product-quantity').val();
    addProduct(itemId, purchasePrice, name, salePrice, quantity);
  });

  $('.js-remove-product').on('click', function() {
    var item = $(this).closest('.js-sale-product');
    item.remove()
  });

  $('.js-create-sale').on('click', function() {
    var saleProducts = $('.js-sale-product');
    if (saleProducts.length <= 0){
        alert('No se puede crear una venta sin productos.');
        return null;
    }

    var productsData = [];

    $.each(saleProducts, function(index, product) {
      var itemId = $(product).find('.js-product-id').text();
      var purchasePrice = $(product).find('.js-product-purchase-price').text();

      var name = $(product).find('.js-product-name').text();
      var salePrice = $(product).find('.js-product-sale-price').text();
      var quantity = $(product).find('.js-product-quantity').text();

      productsData.push({
        id: itemId,
        name: name,
        quantity: quantity,
        purchase_price: purchasePrice,
        sale_price: salePrice
      })
    });


    $.ajax({
      url: $(this).data('url'),
      type: 'post',
      data: JSON.stringify(productsData),
      contentType: 'application/json',
      success: alert('Venta registrada :-)')
    });
    // $.post(, , function(response) {
    //   if (response.ok) {
    //
    //   }
    //   else {
    //     alert('Ocurrió un problema al registrar la venta');
    //     console.log(response);
    //   }
    // });

  });
});


function addProduct(itemId, purchasePrice, name, salePrice, quantity) {
  var newProduct = $('.js-hide-product').clone(true);
  newProduct.removeClass('js-hide-product');
  newProduct.addClass('js-sale-product');

  // This two fields are hidden
  newProduct.find('.js-product-id').text(itemId);
  newProduct.find('.js-product-purchase-price').text(purchasePrice);

  newProduct.find('.js-product-name').text(name);
  newProduct.find('.js-product-sale-price').text(salePrice);
  newProduct.find('.js-product-quantity').text(quantity);
  var saleProducts = $('.js-sale-product:last').length;
  if (saleProducts){
    $('.js-sale-product:last').after(newProduct);
  } else {
    $('.js-hide-product').after(newProduct);
  }
}
