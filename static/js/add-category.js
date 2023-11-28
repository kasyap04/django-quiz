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