saveCategory = () => {
    let category = document.getElementById("category-name").value.trim() ;

    if(category){
        $.ajax({
            type: "POST",
            url: "",
            data : {
                'category' : category
            },
            success: (response) => {
                location.reload() ;
                
                // if(response.status){
                //     alert(response.msg) ;
                // } else {
                //     if(response.msg == 'login'){
                //         location.reload()
                //     }
                // }
            },
            error : () => {
                alert("Can't add category") ;
            }
        }) ;
    } else 
    alert("Please enter category name") ;
}


closeEditCategory = () => {
    $(".category-right").animate({
        width: "0",
        padding : "0"
    }, 200, () => {
        $(".category-right").hide() ;
    }) ;
    
}


openEditCategory = (catId, catName) => {
    $(".category-right").show() ;
    $(".category-right").animate({
        width: "50%",
        padding : "0 10px"
    }) ;

    document.getElementById('editname').value = catName ;
    $("#editname").attr("data-id", catId) ;
}

editCategory = () => {
    let catName = document.getElementById('editname').value.trim() ;
    let catId = $("#editname").attr("data-id") ;

    if(catName && catId){
        $.ajax({
            type: "POST",
            url: "edit-category",
            data : {
                name : catName,
                id   : catId
            },
            success: (response) => {
                location.reload() ;
            },
            error : () => {
                alert("Can't add category") ;
            }
        }) ;
    }

}