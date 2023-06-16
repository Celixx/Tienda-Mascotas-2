$(document).ready(function(){
    $.get('https://fakestoreapi.com/products',
        function(data){
            $('#grid').empty();
            $.each(data, function(i, item) {
                
                var elemento = `
                    <div class="col-sm-12 col-md-4 col-lg-3">
                        <a style="height: 650px;" class="overflow-hidden p-3 shadow nav-link" href="royalCanin.html">
                            <div>
                                <img src="${item.image}" class="img-fluid" style="height: 200px;" alt="Imagen producto">
                                <p class="p-3"> $${item.price} </p>
                                <p class="h5 fw-bold"> ${item.title} </p>
                            </div>
                            <p class="p-3"> ${item.description} </p>
                        </a>
                    </div>
                `;

                $('#grid').append(elemento);
            });
        }
    )
});