$(document).ready(function(){
    $('.center').slick({
    centerMode: true,
    // centerPadding: '100px',
    slidesToShow: 3,
    responsive: [
        {
        breakpoint: 768,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 3
        }
        },
        {
        breakpoint: 480,
        settings: {
            arrows: false,
            centerMode: true,
            centerPadding: '40px',
            slidesToShow: 1
        }
        }
    ]
    });




    var api_key = '7b98ae9af6fe4cc6b9a33b00e08db54d';
    var api_url = '';
    var imageUrl = "https://spoonacular.com/recipeImages/";
    $('#category').on('change', function() {
        var value = $(this).val();
        //console.log(value);

        $.ajax({
            url: 'https://api.spoonacular.com/recipes/search?diet='+value+'&apiKey='+api_key+'',
            contentType: "application/json",
            dataType: 'json',
            success: function(obj){
                //console.log(obj.baseUri);
                $("#title-results").html(value);
                //console.log(obj.results[0]);
                $.each( obj.results, function( index, cat ){
                    //console.log(cat, index)
                    $("#results .results").empty();
                    
                     $( "#results .results" ).after(
                        '<a href="' + cat.sourceUrl + '"> \n ' +
                        '<div class="link-preview"> \n ' +
                            '<div class="preview-image" style="background-image:url('+imageUrl+cat.image+');display: block; width: 100%; height: 200px; position: relative; background-repeat: no-repeat; background-size: contain;"></div> \n ' +
                            '<div style="width:70%;" class="link-info"> \n ' +
                            '<h4>' + cat.title +'</h4> \n ' +
                            '<p>' + cat.servings +'</p> \n ' +
                            '</div><br> \n ' +
                            '<a href="' + cat.sourceUrl + '" class="url-info"><i class="far fa-link"></i>' + cat.sourceUrl + '</a> \n ' +
                            '</div></a>'
                        );
                });
               
        }
    })
    });





});